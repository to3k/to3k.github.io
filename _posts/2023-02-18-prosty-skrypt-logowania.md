---
title: "PHP+MySQL - Prosty skrypt logowania"
date: 2023-02-18
categories: 
  - "poradniki"
tags: 
  - "bloglab"
  - "ciasteczka"
  - "cookies"
  - "hash"
  - "mysql"
  - "opensource"
  - "password"
  - "passwordhash"
  - "php"
  - "pregmatch"
  - "proofofconcept"
  - "session"
  - "skrypt"
image: "/images/loginscript.webp"
description: "Pomysł na ten wpis wpadł mi do głowy podczas pracy nad moim nowym, małym projektem, który w niedalekiej przyszłości powinien ujrzeć światło dzienne. Finałem..."
---

Spis treści:
* TOC
{:toc}

Pomysł na ten wpis wpadł mi do głowy podczas pracy nad moim nowym, małym projektem, który w niedalekiej przyszłości powinien ujrzeć światło dzienne. Finałem poniższego wywodu będzie **stworzenie prostego skryptu logowania do wykorzystania na dowolnej stronie**. Stworzymy bazę danych MySQL do przechowywania informacji o użytkownikach, skrypt do tworzenia nowych kont i skrypt do logowania, czyli uzyskania dostępu do zawartości chronionej. Będzie to rozwiązanie typu _[Proof of Concept](https://en.wikipedia.org/wiki/Proof_of_concept)_, czyli skupię się na niezbędnym minimum, a dalsze ewentualne dostosowanie do konkretnych potrzeb pozostawię Czytelnikowi.

## Strona demonstracyjna

Specjalnie na potrzeby tego wpisu stworzyłem coś co nazwałem _bloglab1_, czyli **środowisko testowe** do zademonstrowania sposobu działania mechanizmu, który za chwilę opiszę. Dostęp do dema można uzyskać poprzez wejście w [ten link](https://oldblog.tomaszdunia.pl/bloglab/lab1/login.php).

## Baza użytkowników MySQL - lab1\_users\_db.sql

Do przechowywania danych użytkowników potrzebujemy **bazy MySQL**. Jako, że skupiamy się jedynie na podstawach, nazwiemy naszą bazę _lab1\_users\_db_ i będzie się ona składała jedynie z trzech kolumn przechowujących:

- unikatowe **ID** użytkownika, które jednocześnie będzie _kluczem podstawowym_ dla bazy,

- **login** użytkownika,

- **hasło** użytkownika w formie zahaszowanej (z ang. hashed), czyli takiej, która pozwoli jednoznacznie zweryfikować użytkownika znającego prawidłowe hasło, ale jednocześnie takiej, której pozyskanie nie sprawi, że poznamy to hasło.

Temat hasła jest nieco zagmatwany, ale w telegraficznym skrócie mogę wyjaśnić, że z _hashowaniem_ **chodzi o to, żeby będąc administratorem nie mieć dostępu do "jawnej" formy hasła użytkownika, a jednocześnie móc go prawidłowo zweryfikować/uwierzytelnić**. Do tego wykorzystuje się szyfrowanie jednostronne, a może raczej nazwałbym je (teoretycznie) nieodwracalnym, czyli takie, które z pewnego ciągu znaków (hasła w formie jawnej i powiedzmy zrozumiałej dla użytkownika), poprzez odpowiedni algorytm szyfrujący, tworzy _hash_, który z pozoru wygląda jak ciąg kompletnie losowych znaków o stosunkowo sporej długości, którego nie da się z powrotem przekonwertować do formy jawnej, a przynajmniej nie jest to możliwe przy obecnym stanie zaawansowania techniki, tj. mocy obliczeniowej komputerów. Taki _hash_ zapisywany jest w bazie podczas tworzenia danego konta. Późniejsza weryfikacja polega na tym, że użytkownik przy każdym logowaniu podaje hasło, serwer konwertuje je na _hash A_, pobiera z bazy MySQL _hash B_ stworzony podczas zakładania konta i porównuje te dwa ze sobą, Jeżeli są zgodne (_A==B_) to użytkownik zostaje uwierzytelniony.

Teorie mamy za sobą teraz stwórzmy bazę, w której będziemy przechowywać dane użytkowników. Poniższy kod jest gotowym poleceniem tworzącym prawidłowo skonfigurowaną bazę na potrzeby tego poradnika. Taką bazę można stworzyć również ręcznie np. w panelu _phpMyAdmin_.

```sql
CREATE TABLE `lab1_users_db` (
  `id` int(11) NOT NULL,
  `login` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hashed_password` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;
ALTER TABLE `lab1_users_db`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `lab1_users_db`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
```

## Skrypt do rejestracji - signup.php

W tym skrypcie najciekawsze są w zasadzie **dwa fragmenty**:

- **linijki 43-50** - weryfikacja zgodności z wymaganiami podanych przy rejestracji loginu i hasła,

- **linijki 63-69** - tworzenie szyfrowanie podanego przez użytkownika hasła do postaci _hasha_.

Do walidacji poprawności loginu i hasła wykorzystujemy, wspomniane już przeze mnie w [jednym z poprzednich wpisów](https://blog.tomaszdunia.pl/twittodon/), wyrażenia regularne (_regexp_). Najpierw należało zdefiniować jak mają wyglądać loginy i hasła naszych użytkowników. W mojej ocenie rozsądnym podejściem w przypadku loginu jest dopuszczenie ciągu o długości od 3 do 20 znaków, który składać się może z duży i małych liter, cyfr i dwóch znaków specjalnych - _myślnika_ ( - ) oraz _podłogi_ ( \_ ). Natomiast hasło powinno być ciągiem o długości od 8 do 64 znaków i składać się z duży i małych liter, cyfr i nieco większej grupy znaków specjalnych - ! @ # $ % ^ & \*. Dodatkowo w przypadku hasła wymusiłem na użytkowniku użycie przynajmniej jednego znaku z każdej z wymienionych grup. Tak sformułowane wyrażenia regularne wystarczy wrzucić jako argument do funkcji _preg\_match()_, które resztę pracy wykona już za nas. Jeżeli login/hasło będzie zgodne z określonym wyrażeniem regularnym w/w funkcja zwróci wartość _1_ (_true_), natomiast jeżeli coś się nie zgadza to zwróci _0_ (_false_).

Omówmy teraz fragment dotyczący hashowania hasła. Wykorzystujemy do tego funkcję password\_hash(), dla której musimy podać trzy argumenty:

- **hasło do zaszyfrowania** - w naszym przypadku jest to zawartość zmiennej _$password_ pobrana od użytkownika przy pomocy pola tekstowego w formularzu rejestracyjnym,

- **algorytmu szyfrowania** - używamy _PASSWORD\_BCRYPT_, czyli algorytmu _CRYPT\_BLOWFISH_, który jako wynik zawsze zwraca nam ciąg o długości 60 znaków,

- **zestaw opcji (_options_)** - na który składają się dwa parametry: _cost_ określający poziom skomplikowania z jakim ma zostać wykonane szyfrowanie (musi być dobrany do mocy obliczeniowej jednostki szyfrującej), _salt_ (_sól_) jest to ciąg znaków dodawany przed szyfrowaniem w celu utrudnienia ataków słownikowych (rodzaj ataku typu brute force).

```php
<?php
    include("[ścieżka do pliku z danymi do logowania do bazy MySQL]");
	
	header('Content-Type: text/html; charset=utf-8');
	$mysqli = mysqli_connect($host, $user, $pass, $db);
	mysqli_set_charset($mysqli, "utf8");
    // Inicjalizuje nową sesję lub wczytuje już istniejącą
	session_start();
    // Jeżeli w sesji istnieją zmienne z informacją o nazwie użytkownika i zahashowanym haśle to ...
    if(isset($_SESSION['login']) AND isset($_SESSION['hashed_password']))
    {
        // ... sprawdza w bazie czy istnieje rekord zawierający te dwie wartości
		$login = addslashes(strip_tags($_SESSION["login"]));
		$hashed_password = addslashes(strip_tags($_SESSION['hashed_password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."' AND hashed_password = '".$hashed_password."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
		// Jeżeli istnieje to ...
        if(!empty($db_users))
        {
            // ... pomija proces logowania i od razu odsyła do zawartości chronionej
            header("Location: secret.php");
        }
        else
        {
            // Natomiast jeżeli nie ma takiego rekordu to niszczy obecną sesję i odsyła do panelu logowania
            session_unset();
            session_destroy();
            header("Location: login.php");
        }
    }
	
	// Jeżeli wciśnięto przycisk Sign up (co oznacza, że formularz rejestracji został wysłany)
    if(isset($_POST['signup']))
    {
        // Ustawia pustą zmienną alert
        $alert = "";
		// Przeprowadza proces weryfikacji poprawności podanego loginu i hasła
        $login = addslashes(strip_tags($_POST['login']));
		$password = addslashes(strip_tags($_POST['password']));
		// Wymagania dot. loginu - długość 3-20 znaków, duże i małe znaki, cyfry i znaki specjalne "_-"
		$check_login = '/^[A-Za-z0-9_-]{3,20}$/';
		// Wymagania dot. hasła - długość 8-64 znaków, przynajmniej jedna duża i jedna mała litera, przynajmniej jedna cyfra i przynajmniej jeden znak specjalny z listy dozwolonych "!@#$%^&*"
		$check_password = "/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*]).{8,64}$/";
        if(preg_match($check_login, $login))
        {
			if(preg_match($check_password, $password))
			{
				// Jeżeli login i hasło spełniają wymagania to jeszcze sprawdza czy w bazie nie ma już użytkownika o tej nazwie
				$query = "SELECT * FROM lab1_users_db WHERE login = '".$login."'";
				$result = mysqli_query($mysqli, $query);
				$db_users = mysqli_fetch_assoc($result);
				if(!empty($db_users))
				{
					// Jeżeli jest to wyświetla błąd
					$alert = "User with that name already exists!";
				}
				else
				{
					// Jeżeli nie ma jeszcze takiego użytkownika to ...
					// Ustawia opcje algorytmu szyfrującego hasło (tworzenie hasha)
					$options = [
						'cost' => 10,
						'salt' => 'secret_salt'
					];
					// Tworzy hash
					$hashed_password = password_hash($password, PASSWORD_BCRYPT, $options);
					// Wprowadza do bazy nowy rekord
					$add = "INSERT INTO lab1_users_db (login, hashed_password) VALUES ('".$login."', '".$hashed_password."')";
					mysqli_query($mysqli, $add);
					// Odsyła do panelu logowania
					header("Location: login.php");
				}
			}
			else
			{
				// Jeżeli hasło nie spełnia wymagań wyświetla błąd
				$alert = "Invalid password! It needs to be 8-64 length, have at least one lower and upper case letters, number and special character (allowed: !@#$%^&*)";
			}
		}
		else
		{
			// Jeżeli login nie spełnia wymagań wyświetla błąd
			$alert = "Invalid login! It needs to be 3-20 length and contains only allowed characters: a-z, A-Z, 0-9, special chars '_-'";
		}
    }
?>
<!-- Część HTML (formularz) -->
<h1>CREATE ACCOUNT</h1>
<form action="" method="post">
	<p><input type="text" name="login" value="" placeholder="Login..." autocomplete="off"></p>
	<p><input type="password" name="password" value="" placeholder="Password..." autocomplete="off"></p>
	<p><button type="submit" name="signup">Sign up</button></p>
</form>
<p><a href="login.php">Already have account? Log in instead!</a></p>
<?php
	if($alert != "")
	{
		echo "<p>".$alert."</p>";
	}
?>
<p>Made for this blog post: <a href="https://blog.tomaszdunia.pl/prosty-skrypt-logowania/">https://blog.tomaszdunia.pl/prosty-skrypt-logowania/</a></p>
```

## Skrypt do logowania - login.php

Przy okazji tego skryptu chciałbym się pochylić nad tematem czym jest _sesja_ (_session_), która w przypadku tworzonego przeze mnie mechanizmu logowania jest kluczowa. Otóż _sesja_ jest nam potrzebna głównie po to, **żeby użytkownik nie musiał ponownie logować się przy każdym odświeżeniu strony**. W zakresie _sesji_ zachowujemy informację, że ten konkretny osobnik już raz się uwierzytelnił i dopóki przypisana do niego _sesja_ nie wygasła jego tożsamość jest potwierdzona, a więc z czystym sumieniem można serwować mu zawartość chronioną, która jest dla niego przeznaczona. Sesją będziemy zarządzać przy pomocy trzech głównych poleceń:

- **session\_start()** - inicjalizuje nową lub wczytuje już istniejącą _sesję_,

- **session\_unset()** - czyści zmienne danej _sesji_,

- **session\_destroy()** - usuwa wszystkie dane danej _sesji_, czyli w praktyce ją niszczy.

W obrębie sesji możemy definiować i wykorzystywać tzw. **zmienne globalne**, które dostępne są pomiędzy poszczególnymi uruchomieniami skryptów (np. odświeżenie strony). Przechowywane są one w tablicy _$\_SESSION_. Zmienne te przechowywane są po stronie serwera, więc **użytkownik nie ma możliwości manipulować ich zawartością**. Po stronie użytkownika (przeglądarki) przechowywany jest jedynie identyfikator _sesji_, który pozwala na korelację danego użytkownika i _sesji_.

```php
<?php
    include("[ścieżka do pliku z danymi do logowania do bazy MySQL]");
    header('Content-Type: text/html; charset=utf-8');
    $mysqli = mysqli_connect($host, $user, $pass, $db);
	mysqli_set_charset($mysqli, "utf8");
    // Inicjalizuje nową sesję lub wczytuje już istniejącą
	session_start();
    // Jeżeli w sesji istnieją zmienne z informacją o nazwie użytkownika i zahashowanym haśle to ...
    if(isset($_SESSION['login']) AND isset($_SESSION['hashed_password']))
    {
        // ... sprawdza w bazie czy istnieje rekord zawierający te dwie wartości
        $login = addslashes(strip_tags($_SESSION['login']));
        $hashed_password = addslashes(strip_tags($_SESSION['hashed_password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."' AND hashed_password = '".$hashed_password."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
        // Jeżeli istnieje to ...
        if(!empty($db_users))
        {
            // ... pomija proces logowania i od razu odsyła do zawartości chronionej
            header("Location: secret.php");
        }
        else
        {
            // Natomaist jeżeli nie ma takiego rekordu to niszczy obecną sesję i odsyła do panelu logowania
            session_unset();
            session_destroy();
            header("Location: login.php");
        }
    }
    // Jeżeli wciśnięto przycisk Sign in (co oznacza, że formularz logowania został wysłany)
    if(isset($_POST['signin']))
    {
        // Ustawia pustą zmienną alert
        $alert = "";
        // Pobiera z bazy MySQL dane podanego użytkownika
        $login = addslashes(strip_tags($_POST['login']));
        $password = addslashes(strip_tags($_POST['password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
        // Sprawdza czy taki użytkownik w ogóle istnieje
        if(empty($db_users))
        {
            // Jeżeli brak danych zwrotnych z bazy to znaczy, że nie istnieje
            $alert = "There is no such user!";
        }
        else
        {
            // Jeżeli jednak istnieje to weryfikuje zgodność pomiędzy podanym hasłem i hashem hasła pobranym z bazy
            if(password_verify($password, $db_users['hashed_password']))
            {
                // Jeżeli są zgodne to ustawia zmienne sesji i odsyła do zawartości chronionej
                $_SESSION['login'] = $login;
                $_SESSION['hashed_password'] = $db_users['hashed_password'];
                header("Location: secret.php");
            }
            else
            {
                // Jeżeli są niezgodne to wyświetla błąd
                $alert = "Invalid password!";
            }
        }
    }
?>
<!-- Część HTML (formularz) -->
<h1>LOGIN</h1>
<form action="" method="post">
	<p><input type="text" name="login" value="" placeholder="Login..." autocomplete="off"></p>
	<p><input type="password" name="password" value="" placeholder="Password..." autocomplete="off"></p>
	<p><button type="submit" name="signin">Sign in</button></p>
</form>
<p><a href="signup.php">Don't have account? Create it!</a></p>
<?php
	if($alert != "")
	{
		echo "<p>".$alert."</p>";
	}
?>
<p>Made for this blog post: <a href="https://blog.tomaszdunia.pl/prosty-skrypt-logowania/">https://blog.tomaszdunia.pl/prosty-skrypt-logowania/</a></p>
```

## Zawartość chroniona - secret.php

Doszliśmy do naszej mitycznej _wartości chronionej_! W tym skrypcie nie dzieje się nic zbytnio ekscytującego. Na wstępie sprawdzamy czy w sesji znajdują się zmienne, które umożliwiają nam dostęp do konkretnych danych z bazy danych MySQL, jeżeli tak to wyświetlamy je. Natomiast jeżeli cokolwiek poszło nie tak to odsyłamy użytkownika bezpośrednio do panelu logowania, aby uwierzytelnił się w sposób prawidłowy.

```php
<?php
    include("[ścieżka do pliku z danymi do logowania do bazy MySQL]");
    header('Content-Type: text/html; charset=utf-8');
	$mysqli = mysqli_connect($host, $user, $pass, $db);
	mysqli_set_charset($mysqli, "utf8");
	// Inicjalizuje nową sesję lub wczytuje już istniejącą
	session_start();
    
    // Jeżeli w sesji istnieją zmienne z informacją o nazwie użytkownika i zahashowanym haśle to ...
    if(isset($_SESSION['login']) AND isset($_SESSION['hashed_password']))
    {
        // ... sprawdza w bazie czy istnieje rekord zawierający te dwie wartości
        $login = addslashes(strip_tags($_SESSION['login']));
        $hashed_password = addslashes(strip_tags($_SESSION['hashed_password']));
        $query = "SELECT * FROM lab1_users_db WHERE login = '".$login."' AND hashed_password = '".$hashed_password."'";
        $result = mysqli_query($mysqli, $query);
        $db_users = mysqli_fetch_assoc($result);
        // Jeżeli istnieje to ...
        if(!empty($db_users))
        {
            // ... wyświetla zawartość chronioną
            echo "<p>This is secret content page! You can access it only after a successful log in.</p>";
            echo "<p>Your login is: ".$db_users['login']."</p>";
            echo "<p>Your hashed password is: ".$db_users['hashed_password']."</p>";
            echo "<p><a href=\"logout.php\">Log out</a></p>";
        }
        else
        {
            // Natomaist jeżeli nie ma takiego rekordu to niszczy obecną sesję i odsyła do panelu logowania
            session_unset();
            session_destroy();
            header("Location: login.php");
        }
    }
    else
    {
        header("Location: login.php");
    }
?>
<p>Made for this blog post: <a href="https://blog.tomaszdunia.pl/prosty-skrypt-logowania/">https://blog.tomaszdunia.pl/prosty-skrypt-logowania/</a><p>
```

## Skrypt do wylogowania - logout.php

Najkrótszy skrypt w zestawieniu, ale nie najmniej istotny. Umożliwia użytkownikowi potoczne wylogowanie się, a w praktyce wymazanie całej aktualnej _sesji_, co wymusi ponowne logowanie w celu uzyskania dostępu do chronionych danych.

```php
<?php
    // Inicjalizuje nową sesję lub wczytuje już istniejącą
    session_start();
    // Czyści wszystkie zmienne sesji
    session_unset();
    // Usuwa wszystkie dane sesji
    session_destroy();
    // Przekierowuje do panelu logowania
    header("Location: login.php");
?>
```

## Czy ten skrypt używam ciasteczek?

Skoro czytasz ten wpis, drogi Czytelniku, to pewnie widziałeś przynajmniej jeden z moich projektów, a więc pewnie wiesz, że staram się, aby każdy z nich były otwarto-źródłowy, transparentny i w maksymalny możliwy sposób **dbał o prywatność użytkownika**. Podciąga się pod to wykorzystywanie _ciasteczek_ (_cookies_), które są niestety orężem obosiecznym, bo z jednej strony sprawiają, że nasze życie w Internecie jest **wygodne**, chociażby dlatego, że dzięki nim nie musimy przy każdym odświeżeniu strony poświadczać swojej tożsamości (logować się), ale też z drugiej strony są **tragiczne pod kątem prywatności**. Chodzi głównie o to, że nieprawidłowo skonfigurowana przeglądarka internetowa może przekazywać wszystkie _ciasteczka_ zebrane na naszym urządzeniu do stron, które nie są właścicielami tych _ciasteczek_. Na tej podstawie w/w strony **mogą nas skutecznie profilować**, a nawet uzyskiwać istotne dane na temat naszego zachowania w innych miejscach sieci. Przykładem może być tutaj profilowanie i wyświetlanie reklam oddziałujących na nas podprogowo na podstawie tego co czytamy albo kupujemy w sieci.

Dlaczego o tym piszę? Jednym z fundamentów rozwiązania, opisanego przeze mnie w tym wpisie, jest zastosowanie _sesji_ (_session_), która jest pewnego rodzaju pokrewną _ciasteczek_. Oba te rozwiązania służą do przechowywania w tle pewnych informacji o użytkowniku. Główna różnica polega jednak na tym, że _ciasteczka_ przechowują te informacje **na urządzeniu** użytkownika (głównie w przeglądarce), a _ses_**_ja_ po stronie serwera**. A więc dane _sesji_ **nie są dostępne** dla stron trzecich tak jak to jest w przypadku _ciasteczek_ opisanym w poprzednim akapicie. Zapytasz - w takim razie w czym jest problem? Otóż do prawidłowego działania _sesji_ konieczne jest jednak przechowanie **jednej danej** na komputerze użytkownika, a jest nią _PHPSESSID_ (PHP Session ID, czyli identyfikator sesji PHP), która jest niezbędna do powiązania danych zapisanych na serwerze z konkretnym użytkownikiem. Teoretycznie to ID również może zostać wykorzystane przez strony trzecie do identyfikacji użytkownika, ale ja w tym przypadku **nie kruszyłbym o to kopii**. Wspomniany identyfikator przestaje istnień w dwóch przypadkach:

- zakończenie sesji przez skrypt, czyli w naszym przypadku są to polecenia zawarte w pliku _logout.php_,

- zamknięcie przeglądarki.

Tak więc ciężko porównać to do _ciasteczek_, które mogą utrzymywać się na naszym urządzeniu przez lata i przez ten czas przechowywać wiele informacji, które nie są niezbędne do prawidłowego działania stron, których dotyczą.

> TL;DR  
> _Sesja_ działa podobnie do _ciasteczek_, ale przechowuje po stronie użytkownika jedynie informacje niezbędne do prawidłowego działania strony i przestaje istnieć po wylogowaniu lub wyłączeniu przeglądarki. Plusem jest dbanie o prywatność użytkownika, a minusem konieczność częstszego logowania niż w przypadku rozwiązania opartego o standardowe _ciasteczka_.
