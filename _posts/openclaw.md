---
layout: post
title: "OpenClaw - Personalny Asystent AI"
published: false
categories: 
  - "poradniki"
  - "projekty"
  - "self-hosting"
tags: 
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
  - "TAG"
image: "/images/openclaw.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/TYTUŁ-eng/)

Spis treści:
* TOC
{:toc}

## Wstęp

Większość z nas przywykła do interfejsów takich jak ChatGPT czy Gemini — to genialne „mózgi w słoiku”. Potrafią pisać, analizować i doradzać, ale rzadko kiedy mogą faktycznie zrobić "coś" poza oknem przeglądarki. **OpenClaw** zmienia tę dynamikę, przesuwając granicę od pasywnych chatbotów do autonomicznych agentów.

### Czym jest OpenClaw?

OpenClaw to **otwartoźródłowy** asystent AI, którego głównym zadaniem jest działanie proaktywne. W przeciwieństwie do standardowych czatów, które czekają na pytanie, OpenClaw posiada tzw. **heartbeat** (z ang. tętno) – potrafi sam monitorować zadania, przypominać o terminach czy reagować na zmiany cyfrowym otoczeniu swojego pana (użytkownika) bez jego bezpośredniej ingerencji w danej chwili.

### Krótka historia i viralowy sukces

Projekt narodził się pod koniec 2025 roku jako dzieło **Petera Steinbergera**. Zanim zyskał finalną (czy aby na pewno...?) nazwę, przeszedł przez kilka etapów ewolucji. Znany był wcześniej jako *WhatsApp Relay*, *Clawdbot* czy *Moltbot*. Stał się viralem na przełomie 2025 i 2026 roku dzięki swojej prostocie – zamiast kolejnej aplikacji, korzystasz z niego tam, gdzie już jesteś: na **Signal**, **Telegram** czy **Discord** (i nie tylko). O potencjale projektu najlepiej świadczy fakt, że w lutym 2026 roku twórca OpenClaw został zwerbowany do zespołu OpenAI, choć sam projekt pozostaje dostępny dla społeczności. Ja osobiście mam (pewnie naiwną) nadzieję, że nie zaora to tego projektu.

### Kluczowe różnice: Agent vs Chatbot

Podstawowa różnica to **dostęp do systemu na poziomie podobnym do fizycznego użytkownika**. Standardowe czaty działają w bezpiecznej piaskownicy na serwerach korporacji. Ba, niektóre LLM nie mają nawet dostępu do Internetu w czasie rzeczywistym. OpenClaw działa tam, gdzie go postawisz, np. na własnym serwerze VPS i co najważniejsze może mieć pełen dostęp do zasobów tego serwera. Chodzi mi tutaj o to, że przykładowo może on korzystać z przeglądarki i normalnie logować się na serwisy wykorzystując dostarczone mu dane do uwierzytelnienia.

| Cecha | Standardowy Chatbot (ChatGPT/Gemini) | OpenClaw |
| :--- | :--- | :--- |
| **Interakcja** | Reaktywna (czeka na prompt) | Proaktywna (sam inicjuje kontakt) |
| **Środowisko** | Zamknięte, chmurowe | Lokalne/VPS, pełny dostęp do plików |
| **Możliwości** | Generowanie treści, analiza | Wykonywanie realnych zadań |
| **Prywatność** | Dane na serwerach dostawcy | Pełna kontrola nad logami i pamięcią |
| **Interfejs** | Dedykowana aplikacja/web | Komunikatory (Telegram, Signal itp.) |

### Co potrafi OpenClaw?

Dzięki wykorzystaniu **Model Context Protocol (MCP)**, OpenClaw ma dostęp do setek **umiejętności**, które nazywane są **skill'ami**. Tworzone są one jak znane w programowaniu biblioteki - społecznościowo. Przykładami takich skill'i są:

- **Zarządzanie kalendarzem i e-mailami** w sposób autonomiczny.
- **Pobieranie dane z systemów zewnętrznych** (np. KSeF hehe) i przetwarzać je dalej.
- **Samodzielnie pisanie skryptów**, instalowanie ich na serwerze i uruchamianie.
- **Kupowanie** biletów do kina.
- **Zarządzanie Twoim kontem** na Tinderze (było o tym głośno w kontekście OpenClaw właśnie).

### Po co to komu?

No wiadomo, takim **nerdom** jak my. Poza tym, kto nie chciałby mieć **swojego przydupasa**, który zrobi (prawie) wszystko o co zostanie poproszony, a do tego jest chodzącą encyklopedią, bo przeczytał 90% Internetu. Taki asystent może być wirtualnym członkiem zespołu deweloperskiego i pisać kod na poziomie seniora, ale możesz także do niego napisać na Telegramie "typie, zorganizuj mi wyjazd do Warszawy", a on zarezerwuje Ci bilety na pociąg, sprawdzi pogodę i powie jak masz się ubrać, ustawi przypomnienia i powiadomi wszystkich ziomków ze stolicy, że w następny piątek będziesz w promieniu 10km od nich gotowy na strzelenie piwka.

### Z tego wpisu dowiesz się

Za chwilę przeczytasz coś w rodzaju **Proof of Concept**, w którym pokażę jak możliwie najtaniej uruchomić działającego bota OpenClaw. Chodzi o pokazanie **jak to zrobić** i sprawdzenie **czy to działa**, a nie uruchomienie zoptymalizowanego środowiska idealnego do jakiegoś konkretnego zadania. OpenClaw jest na tyle wszechstronnym narzędziem, że ma praktycznie **nieskończoną liczbę różnych zastosowań**. To co może zrobić ograniczane jest w zasadzie tylko wyobraźnią operatora. Dlatego ja pokażę mniej więcej co to jest, jak to uruchomić i ewentualnie jak można później rozwinąć to środowisko, a to do czego i jak to narzędzie zostanie wykorzystane pozostawię już Tobie, drogi Czytelniku.

Reasumując, w tym wpisie:
- przeprowadzę Cię za rączkę przez proces **wynajmu serwera** VPS, którego cena to zaledwie **5 dolarów miesięcznie** (!),
- następnie odpowiednio **skonfigurujemy razem ten serwer**,
- pozyskamy **darmowy dostęp do API** Gemini z Google AI Studio,
- uruchomimy **kontener Dockera z botem** w środku,
- przeprowadzimy **podstawową konfigurację**,
- **sprawdzimy czy działa**,
- rozważymy opcje **rozbudowy środowiska**.

### Z tego wpisu NIE dowiesz się

Chcę od razu na wstępie wyłożyć karty na stół i powiedzieć co nie będzie zawarte w ramach tego wpisu, żeby potem ktoś mi nie powiedział, że przeczytał 50 tysięcy znaków i tylko zmarnował czas, bo nie znalazł tego co szukał.

A zatem... nie pokażę tutaj szczegółowej konfiguracji ani żadnego konkretnego zastosowania takiego asystenta, bo po pierwsze każdy ma inne potrzeby, po drugie sam nie jestem jeszcze pewien czy wiem do czego go użyję, a po trzecie ten wpisy i bez tego będzie niebezpiecznie długi. Zostawmy sobie wątki do poruszenia w przyszłych wpisach, bo jeżeli naprawdę polubię się z OpenClaw, a widzę spore szanse, to nie omieszkam sowicie opisać każdego aspektu tej koegzystencji.

### Zapinaj pasy...

... bo lecimy z tematem! Przygotuj picie, przekąski i jeżeli nie masz certyfikatu z kursu szybkiego czytania to rozważ również zaopatrzenie się w nocnik, bo nie będzie to krótki wpis. Obiecuję od tego momentu być w miarę skupiony na merytoryce, bez zbędnego p... :)

## Serwer VPS - ciało asystenta

### Rejestracja w Hetzner

1. W celu utworzenia konta na Hetzner przechodzimy do **[formularza rejestracyjnego](https://accounts.hetzner.com/signUp)**.
2. Podajemy **adres e-mail**, **hasło** (dwa razy), akceptujemy **regulamin** i naciskamy przycisk **Continue**.
3. Na maila zostanie nam wysłany link do aktywacji konta, więc przechodzimy do naszego klienta poczty i odszukujemy go. Ciekawostka - u mnie coś nie zadziałało za pierwszym razem i maila dostałem dopiero za drugim razem (wpisałem oczywiście te same dane).
4. Link z maila przeniesie nas do dalszej części formularza rejestracyjnego. W tym miejscu musimy:
    - wybrać typ konta - **Individual**,
    - Title, czyli tytuł - do wyboru Pan (Mr.) lub Pani (Ms.), ale można po prostu zostawić **None**,
    - First Name - **Imię**,
    - Surname - **Nazwisko**,
    - nacisnąć przycisk **Continue**.
5. Kolejna strona dotycząca danych kontaktowych:
    - Street / House number - **Ulica**,
    - Postal code - **Kod pocztowy**,
    - City - **Miasto** (nie przyjęło mi polskich znaków),
    - Country - **Kraj**,
    - VAT ID - **NIP**, nieobowiązkowe bo dotyczy raczej tylko przedsiębiorców,
    - Phone - **Numer telefonu** (wydaje mi się, że trzeba go poprzedzić _+48_),
    - Mobile phone - **Numer komórkowy** to jakiś mocny przeżytek z czasów telefonów stacjonarnych, dlatego opcjonalne i pozostawiamy puste,
    - naciskamy przycisk **Continue**.
6. Następny krok dotyczy metody rozliczania:
    - wybieramy **walutę** - często jest tak, że warto jest wybrać dolara, bo usługi kosztują np. 5 dolarów lub 5 euro, gdzie nie pamiętam czasów kiedy dolar był droższy od euro, jednakże w tym przypadku Hetzner przelicza kwoty i wychodzi praktycznie to samo, więc wybierz tą co Ci bardziej pasuje, może Twój bank ma jakiś preferencyjny przelicznik dla którejś za walut (?), ja wybrałem dolara
    - mamy trzy metody płatności - **tradycyjny przelew**, **karta kredytowa** i **PayPal**, ja wybrałem kartę kredytową i podałem dane mojej wirtualnej karty prepaid (przedpłacona, czyli ma tyle środków ile na nią wpłacę i nie więcej, co jest bezpieczne) w Revolut, którą mam specjalnie na takie potrzeby
        - Card holder - wpisujemy **imię i nazwisko** widniejące na karcie,
        - Credit card - wybieramy typ karty, czyli **Visa**, **MarsterCard** lub **American Express**,
        - Card number - **numer karty**,
        - Expires Month i Year - **miesiąc i rok do kiedy karta jest ważna**,
        - CVC code - **3-cyfrowy kod CVC zabezpieczający karty**,
        - zdecyduj czy chcesz zapisać dane karty, żeby w przyszłości nie wprowadzać ich ponownie i jeżeli tak to zaznacz opcję _Hetzner Online has my permission to save my credit card data on my account and to use this information to pay open invoices._
    - naciskamy przycisk **Complete**,
    - to spowoduje konieczność potwierdzenia dodania karty, w moim przypadku poprzez aplikację Revolut (dostałem powiadomienie i potwierdziłem).
7. Sukces. Dostajemy potwierdzenie, że pomyślnie przeszliśmy proces rejestracji.
8. JEDNAKŻE, mocno rekomendowane jest dodanie dodatkowego zabezpieczenia 2FA, dlatego polecam kliknąć **Enable 2FA**. Oczywiście nie musisz tego robić, po prostu olać tą rekomendację i przejść dalej.
9. Zostaniemy przeniesieni do ustawień konta, gdzie ponownie naciskamy żółty przycisk **Enable 2FA**.
10. Wyskoczy okno, w którym mamy podać hasło do konta i zaznaczyć okienko poprzez które potwierdzamy, iż rozumiemy, że jeżeli stracimy kod odzyskiwania to Hetzner przyśle nam nowy pocztą i nie zrobi tego w żaden inny sposób. Potwierdzamy to wszystko przyciskiem **Enable 2FA** (ile można...?).
11. Zapisujemy w bezpiecznym miejscu wyświetlony na ekranie **LOGIN** i **KEY**. Możemy je także wydrukować korzystając z przycisku. Po czym naciskamy na dole **Set up authentication**.
12. Wybieramy metodę zabezpieczenia. Jeżeli masz **Yubikey** to użyj go, a jeżeli nie to możesz wybrać **Mobile device**, a do tego potrzebujesz telefonu z odpowiednią aplikacją np. **[Ente Auth](https://github.com/ente-io/ente/)**, którą polecam. Opiszę jak to zrobić właśnie tą drugą metodą.
13. Odpalamy **Ente Auth**, naciskamy **przycisk plusa** aby dodać nowy element i wybieramy **Zeskanuj kod QR**. Udzielamy aplikacji dostęp do aparatu i **skanujemy kod QR** wyświetlony na stronie Hetznera. W tym momencie w aplikacji na telefonie pojawi się nam już nowa pozycja. Wracamy do storny Hetznera i wpisujemy:
    - Desctription - jakiż krótki **opis**, którym nazwiemy nasze urządzenie, możesz wpisać coś ala _Ente Auth Pixel 9a_,
    - Account password - **hasło** do konta Hetzner,
    - New generated OTP - aktualny ** OTP** wyświetlany w aplikacji Ente Auth na telefonie,
    - przycisk **Add**.
14. W tym momencie zostaniemy wylogowani i będziemy musieli zalogować się ponownie. Dlatego podajemy normalnie login i hasło oraz naciskamy oczywiście przycisk **Login**. Teraz to jest ten dodatkowy krok, w którym musimy podać aktualny kod OTP z aplikacji Ente Auth na telefonie. Naciskamy przycisk **Verify**. Po pomyslnym zalogowaniu trafiamy ponownie do ustawień zabezpieczeń konta, gdzie widzimy, że dwuetapowe uwierzytelnienie zostało aktywowane. Nasze konto jest na pewno 100 razy bardziej bezpieczne z tym niż z samym loginem i hasłem.
15. Po czasie Hetzner poprosił mnie mailowo o dodatkową weryfikację tożsamości, bo moje konto wzbudziło jakieś wątpliwości. Musiałem wejść w link podany w mailu (był to link do zakładki **Verification** w ustawieniach konta) i potwierdzić swoją tożsamość dokumentem (dowód osobisty, prawo jazdy, paszport i chyba coś jeszcze do wyboru...) oraz zdjęciem twarzy. Żeby było śmieszniej to automatyczna weryfikacja nie przeszła, bo chyba przytyłem czy coś i nie wyglądam jak na zdjęciu z dowodu, więc musiałem dodatkowo czekać na weryfikację przez człowieka, co trwało na szczęście może tylko z minutę lub maksymalnie dwie.

### Wybór serwera

Zdecydowałem się na Hetzner, bo nie znam firmy, która dostarcza serwery z lepszym **współczynnikiem ceny do jakości**. Mówiąc wprost - za maszyny o całkiem niezłych parametrach Hetzner chce naprawdę małe pieniądze, więc jest to opcja idealna, żeby przetestować jakieś rozwiązanie, nawet przez parę miesięcy.

Zobaczmy jak kształtuje się aktualna oferta Hetzner. Polecam skorzystać z przycisku na górze, który pozwala ustawić język (English), walutę (ja wybrałem USD) i co najważniejsze kraj dla jakiego ma być liczony **VAT**, co pozwoli nam poznać **ceny brutto**, bo domyślnie prezentowane są ceny netto bez podatku.

Teraz możemy przejść do zakładki [**Cloud**](https://www.hetzner.com/cloud/) i zjechać do sekcji **Prices**. To co nas interesuje to serwery z kategorii **Shared Cost-Optimized**, czyli współdzielone, a przez to zoptymalizowane cenowo, a to po prostu ładniejsza nazwa na serwery dla cebulaków. Teraz już chyba nikt nie ma wątpliwości, że to właśnie to czego szukaliśmy. Możemy wybrać spośród dwóch lokalizacji, ale dla mnie **Niemcy** (Germany) są dość oczywistym wyborem ze względu na to, że w mojej ocenie serwerownia, z której się korzysta powinna być zawsze możliwie jak najbliżej, a Finlandia jest niewątpliwie dalej i do tego połączona przez kabel na dnie Bałtyku. Jesteśmy leniuchami i nie chce nam się bawić z problemami z IPv6, więc wybieramy opcję z **IPv4** pomimo tego, że jest o 74 centy droższa.

Aktualna (na luty 2026) **oferta** Hetzner prezentuje się tak:

![Oferta Hetzner](/images/hetznerprices.png)

To co nas interesuje to najtańszy serwer **CX23** z procesorem o **2 wirtualnych rdzeniach** (VCPU)*, **4GB** pamięci RAM i dyskiem SSD o pojemności **40GB**. Taki serwer w momencie pisania tego wpisu kosztuje 5.03 USD **miesięcznie** (!), czyli przeliczając po aktualnym kursie jakieś **18 PLN** z groszami. Trudno się nie zgodzić, że jest to atrakcyjna cena.

### Wynajęcie serwera

1. Aby wynając wybrany serwer przechodzimy do konsoli użytkownika (**Console**), a konkretnie do zakładki **[Projects](https://console.hetzner.com/projects)**.
2. Naciskamy duży przycisk **+ New project**.
3. W pole **Name** wprowadzamy nazwę projektu, ja wpisałem **OpenClaw**.
4. Do tak utworzonego projektu możemy teraz dodać serwer, dlatego w sekcji projektu **OpenClaw** naciskamy przycisk **+ CREATE SERVER**.
5. Zostaniemy przeniesieni do **konfiguratora**, w którym ustawimy parametry serwera. Konfigurator przeprowadzi nas przez wszystkie opcje po kolei:
    - Type - typ serwera, już wcześniej ustaliliśmy, że wybierzemy opcję **Cost-Optimized** (tj. dla cebulaczków), a do tego postawimy na **architekturę x86**, bo zależy nam na maksymalnej kompatybilności kosztem odrobiny większej wydajności, na koniec wybieramy z listy **CX23**,
    - Location - lokalizacja serwera, wybrałbym **Falkenstein**, ale niestety nie był to możliwe ze względu na chwilowo (?) duży popyt, więc wybrałem **Nuremberg**,
    - Image - dobór systemu, ja polecam **Ubuntu 24.04**, bo jak już wcześniej wspomniałem zależy nam na maksymalnej kompatybilności, a Ubuntu jest jak zupa pomidorowa, większość ludzi (w tym przypadku oprogramowania) lubi ją,
    - Networking - wybieramy **Public IPv4**, co jest dodatkowo płatne, ale już o tym rozmawialiśmy, oraz **Public IPv6** co akurat jest w cenie, nie wybieramy natomiast **Private networks**
    - SSH keys - w tej sekcji możemy utworzyć klucz SSH, ale jeżeli tego nie zrobimy to Hetzner wyśle nam po prostu hasło mailem co na ten moment nam odpowiada, bo **kluczami SSH zajmiemy się później podczas konfigurowania serwera**,
    - Volumes - **pomijamy**, bo nasz serwer bazowo ma już 40GB pamięci na dane,
    - Firewalls - **pomijamy** na tym etapie, bo zapory sieciowe tworzy się w innej zakładce projektu,
    - Backups - jeżeli ktoś jest zainteresowany dziennymi kopiami zapasowymi to ta opcja kosztuje dodatkowe 0.86 USD miesięcznie, ja nie potrzebuję, więc **pominąłem tę sekcję**,
    - Placement groups - tutaj można utworzyć klastry serwerów, ale na to jest niepotrzebne, więc **pomijamy**,
    - Labels - jestem zbyt mało zorientowany, żeby wypowiedzieć się na temat tego co to jest, więc **pomijam**,
    - Cloud config - jestem zbyt mało zorientowany, żeby wypowiedzieć się na temat tego co to jest, więc **pomijam**,
    - Name - tutaj nadamy naszemu serwerowi nazwę, ja wpisałem **openclaw-assistant**
6. Konfiguracja powinna wyglądać mniej więcej tak:

![Konfiguracja serwera do zakupu](/images/hetznerserverconfig.png)

7. Z taką konfiguracją możemy przystąpić do zakupu serwera. W tym celu naciskamy czerwony przycisk **Create & Buy now**.
8. Zostaniemy przeniesieni do listy naszych serwerów, gdzie pojawi się nowa (i jedyna) opcja, czyli serwer, który właśnie utworzyliśmy. Na początku będzie się przy nim kręcić kółko co oznacza, że trzeba chwilę poczekać na jego utworzenie. Jednak po chwili na dole wyskoczy zielony komunikat **Server created**, co oznacza, że nasz poligon doświadczalny jest już gotowy.

### Połączenie przez SSH do serwera

Serwer gotowy, więc pora zajrzeć na maila, gdzie powinna już znajdować się wiadomość ze wszystkimi informacjami potrzebnymi do łączenia się do niego. Powinna ona wyglądać mniej więcej tak:

```html
{% raw %}
Your new server

Your server "openclaw-assistant" was created!

You can access your server with the following credentials:
 
IPv4	    ADRES_IPV4/32
IPv6	    ADRES_IPV6/64
User	    root
Password	OCENZUROWANE_HASŁO
	
You will be prompted to change your password on your first login.

To improve security, we recommend that you add an SSH key when creating a server. This way, no root password will be set and this e-mail won't be generated. 
{% endraw %}
```

Z tego maila będziemy dalej potrzebować **ADRES_IPV4** oraz **OCENZUROWANE_HASŁO**. Spróbujmy teraz połączyć się z serwerem.
1. Otwieramy **terminal** i wpisujemy:

```bash
ssh root@ADRES_IPV4
```

2. Powinniśmy zobaczyć taki **komunikat**:

```bash
The authenticity of host 'ADRES_IPV4 (ADRES_IPV4)' can't be established.
ED25519 key fingerprint is SHA256: CENZURA.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

3. Musimy na to odpowiedzieć wpisując **yes** i nacisnąć **ENTER**.
4. Rezultatem będzie komunikat informujący, że adres naszego serwera został dodany do listy znanych hostów i następnym razem zostanie rozpoznany poprzez swój fingerprint (odcisk palca) i nie będzie konieczne potwierdzenie autentyczności.

```bash
Warning: Permanently added 'ADRES_IPV4' (ED25519) to the list of known hosts.
Connection closed by ADRES_IPV4 port 22
```

5. Połączenie zostanie przerwane, więc musimy jeszcze raz skorzystać z **komendy**:

```bash
ssh root@ADRES_IPV4
```

6. Powita nas prośba o podanie hasła, więc wpisujemy **OCENZUROWANE_HASŁO** i potwierdzamy **ENTERem**. Uwaga: jeżeli nie masz doświadczenia z SSH to zdziwić Cię może to, że podczas wpisywania hasła nic się nie dzieje, tj. nie pojawiają się nawet gwiazdki, tak ma być i jest to porządane działanie, wpisz po prostu hasło i nie przejmuj się tym.
7. Jeżeli niczego nie pomyliliśmy to powinniśmy skutecznie nawiązać połączenie i zostać **powitani** czymś w rodzaju:

```bash
You are required to change your password immediately (administrator enforced).
Welcome to Ubuntu 24.04.3 LTS (GNU/Linux 6.8.0-90-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Feb 19 07:43:22 PM UTC 2026

  System load:              0.16              
  Processes:                127
  Usage of /:               4.1% of 37.23GB   
  Users logged in:          0
  Memory usage:             5%                
  IPv4 address for eth0:    ADRES_IPV4
  Swap usage:               0%                
  IPv6 address for eth0:    ADRES_IPV6

Expanded Security Maintenance for Applications is not enabled.

62 updates can be applied immediately.
43 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

Changing password for root.
Current password: 
```

8. Serwer jest tak skonfigurowany, że już podczas pierwszego połączenia **wymusza na nas zmianę hasła dla administratora**. To dobra praktyka, więc posłusznie stosujemy się do sugestii.
    - najpierw pisujemy stare **OCENZUROWANE_HASŁO** i potwierdzamy **ENTERem**,
    - a później wpisujemy dwa razy **NOWE_HASŁO** każdorazowo potwierdzając **ENTERem**.

### Aktualizacja

Podstawową konfigurację zaczniemy od **zaktualizowania pakietów na serwerze**. Wykorzystamy do tego gotowy skrypcik, który już wcześniej przedstawiałem w [jednym z wpisów na tym blogu](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja/#aktualizacja-to-podstawa).

1. Wpisujemy **komendę**:

```bash
nano /usr/local/sbin/aktualizacja.sh
```

2. W edytorze, który się otworzy **wklejamy poniższą treść**:

```bash
{% raw %}
#!/bin/bash
#Skrypt do aktualizacji systemu i pakietow z blog.tomaszdunia.pl
echo 'Krok 1 - update'
sudo apt update
echo 'Krok 2 - upgrade'
sudo apt upgrade -y
echo 'Krok 3 - autoremove'
sudo apt autoremove -y
echo 'Krok 4 - clean'
sudo apt clean
{% endraw %}
```

3. Wychodzimy z pliku kombinacją klawiszy **Control (CTRL) + X**, zostaniemy zapytani czy zapisać plik w takim stanie, wystarczy potwierdzić naciskając **y**, a potem na pytanie pod jaką nazwą zapisać wystarczy potwierdzić, że pod taką pod jaką otworzyliśmy, czyli po prostu **ENTER**.

4. Teraz musimy nadać temu skryptowi uprawnienia do uruchamiania się:

```bash
chmod +x /usr/local/sbin/aktualizacja.sh
```

5. Teraz wystarczy wpisać nazwę pliku jak komendę, aby rozpoczął się automatyczny proces aktualizacji i czyszczenia po niej:

```bash
aktualizacja.sh
```

6. Po zakończonej tak dużej aktualizacji (zakładam, że sporo pakietów będzie nieaktualnych) dobrze jest rozważyć restart serwera:

```bash
reboot
```

7. Oczywiście utracimy połączenie z serwerem, więc będziemy musieli je nawiązać tak jak robiliśmy to wcześniej.

### Tworzenie nowego użytkownika

Podstawą rozsądnego używania serwera VPS jest nie pracowanie na użytkowniku z uprawnieniami root. Dlatego utworzymy teraz zwykłego użytkownika i przydzielimy go do grupy mogącej wykonywać komendy administracyjne. To taki administrator, ale z dodatkową warstwą zabezpieczenia, bo przed wykonaniem komendy administracyjnej będzie musiał wpisać **sudo** i potwierdzić hasłem. To czasem wystarcza, żeby opamiętać się przed zrobieniem czegoś głupiego. Utworzenie takiego konta to standardowa praktyka. Nadamy mu nazwę **manager**.

1. Tworzymy użytkownika o nazwie **manager**:
```bash
adduser manager
```

2. Serwer poinformuje nas, że utworzył nowego użytkownika i grupę, nadał im unikalne identyfikatory i utworzył katalog domowy. Zostaniemy także poproszeni o podanie dwukrotnie **hasła dla nowego użytkownika**.
3. Następnie kreator będzie chciał wyciągnać od nas niepotrzebne dane typu imię i nazwisko, numer pokoju, telefon itp. co nas nie interesuje, więc wszystkie rubryki zostawiamy puste i tylko potwierdzamy **ENTERem**. To wszystko trzeba będzie jeszcze potwierdzić **y**.
4. Użytkownik utworzony, więc trzeba go teraz dodać do grupy administratorów:

```bash
usermod -aG sudo manager
```

### Firewall - zapora sieciowa

Skonfigurujmy **zaporę sieciową**. Dobrą praktyką jest na początek **zablokować cały ruch przychodzący**, **odblokować cały ruch wychodzący** i do tego **otworzyć port 22** (domyślny dla SSH).

1. Zacznijmy od instalacji **ufw** (skrót od Uncomplicated Firewall, z ang. nieskomplikowana zapora sieciowa), to taka nakładka na **iptables**, która trochę umila tworzenie reguł zapory:

```bash
apt install ufw
```

2. Teraz wykonamy parę komend jedna po drugiej. **Wyłączomy** firewall w celu zmiany jego ustawień:

```bash
ufw disable
```

3. **Zresetujemy** (wyczyścimy) wszystkie reguły, żeby zacząć zupełnie od nowa, będzie trzeba to potwierdzić **y**:

```bash
ufw reset
```

4. Zablokujemy cały *ruch **przychodzący***:

```bash
ufw default deny incoming
```

5. Odblokujemy cały ruch **wychodzący**:

```bash
ufw default allow outgoing
```

6. Otworzymy **port 22** dla połączeń SSH:

```bash
ufw allow 22
```

7. **Włączymy** zaporę, trzeba potwierdzić **y**:

```bash
ufw enable
```

8. Teraz nawet jeżeli coś zepsuliśmy to nie utracimy połączenia z serwerem, a co najwyżej nie będziemy mogli się do niego połączyć po przerwaniu połączenia. Dlatego korzystajmy z chwili i sprawdźmy jeszcze drugi raz czy wszystko jest ustawione tak jak tego chcieliśmy:

```bash
ufw status verbose
```

9. Wynik tej komendy powinien być następujący:

```bash
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To          Action      From
--          ------      ----
22          ALLOW IN    Anywhere                  
22 (v6)     ALLOW IN    Anywhere (v6)
```

10. Jeżeli wszystko się zgadza to do znaku to możesz być spokojny.
11. Sprawdźmy jeszcze czy aby na pewno **ufw** będzie uruchamiać się wraz z systemem po każdym restarcie. Zajrzyjmy do pliku:

```bash
nano /etc/ufw/ufw.conf
```

12. Wewnątrz powinniśmy znaleźć następującą treść:
```bash
{% raw %}
# /etc/ufw/ufw.conf
#

# Set to yes to start on boot. If setting this remotely, be sure to add a rule
# to allow your remote connection before starting ufw. Eg: 'ufw allow 22/tcp'
ENABLED=yes

# Please use the 'ufw' command to set the loglevel. Eg: 'ufw logging medium'.
# See 'man ufw' for details.
LOGLEVEL=low
{% endraw %}
```

13. Istotna dla nas jest zmienna **ENABLED**. Jej wartość ma być **yes**, a linijka, w której występuje nie może być zakomentowana (bez \# na początku).
14. Z pliku wychodzimy kombinacją **Control (CTRL) + X**.

### Fail2Ban

To program, który chroni przed atakami typu **brute force**. Jeśli ktoś spróbuje odgadnąć hasło SSH kilka razy z rzędu i mu się nie powiedzie to Fail2Ban automatycznie zablokuje jego adres IP.

1. **Instalujemy** program:
```bash
apt install fail2ban -y
```

2. **Włączamy** go:

```bash
systemctl enable fail2ban --now
```

### Klucze SSH

Nie będę tłumaczył dlaczego stosowanie kluczy SSH to zalecana praktyka. Po prostu pokażę jak to skonfigurować.

1. Zacznijmy jednak od **wylogowania się** z konta root:

```bash
exit
```

2. Teraz połączmy się kontem **docelowym do zarządzania serwerem**, żeby sprawdzić czy wszystko działa prawidłowo:

```bash
ssh manager@ADRES_IPV4
```

3. Pamiętaj, że teraz musisz **wpisać to hasło, które zostało podane przy tworzeniu tego użytkownika**, a nie hasło root'a.
4. Jeżeli udało się połączyć i uwierzytelnić to znaczy, że **wszystko jest OK** i znowu możemy się **rozłączyć** i wrócić do terminala lokalnego:

```bash
exit
```

4. **Utwórzmy teraz parę kluczy SSH** (komenda do wykonania na komputerze lokalnym!):

```bash
ssh-keygen -t ed25519 -C openclaw-assistant
```

5. Skrypt zapyta o ścieżkę i nazwę pliku, w którym ma zostać zapisany klucz, nam **pasuje wartość domyślna**, więc tylko potwierdzamy **ENTERem**:

```bash
Enter file in which to save the key (/root/.ssh/id_ed25519): 
```

6. Następnie poprosi o ustawienie hasła zabezpieczającego klucz, polecam to zrobić, ale niech to będzie coś raczej prostego co będzie nam łatwo zapamiętać, to tylko dodatkowa warstwa zabezpieczenia na wypadek, gdyby nasz komputer z kluczem na dysku trafił w niepowołane ręce odblokowany i z pełnym fizycznym dostępem włamywacza. Dla mnie to scenariusz, w którym utrata kluczy SSH będzie moim najmniejszym problemem, więc przymykam oko na taki wektor ataku. Możesz także nie ustawiać hasła i po prostu pominąć ten krok naciskając dwa razy **ENTER**.

```bash
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
```

7. Wyślijmy teraz świeżo wygenerowane klucze na serwer VPS:

```bash
ssh-copy-id manager@ADRES_IPV4
```

8. Ten jeden ostatni raz zostaniemy poproszeni o podanie hasła użytkownika **manager** przy logowaniu. Klucze wysłane i teraz można już przetestować logowanie bez konieczności podawania hasła:

```bash
ssh manager@ADRES_IPV4
```

9. Teraz wykonamy dwa ważne kroki - wyłączymy logowanie hasłem, czyli od teraz będzie można dostać się na serwer tylko posiadając klucz prywatny SSH, oraz wyłączymy możliwość zalogowania się na konto root. W tym celu edytujemy plik:

```bash
sudo nano /etc/ssh/sshd_config
```

10. Odszukujemy parametry **PermitRootLogin**, **PubkeyAuthentication** i **PasswordAuthentication** (uwaga - nie będą obok siebie), sprawdzamy czy nie są zakomentowane (mają nie miec \# na początku linii) i zmieniamy ich wartości na takie jak poniżej:

```bash
PermitRootLogin no
...
PubkeyAuthentication yes
...
PasswordAuthentication no
```

11. Zapisujemy i opuszczamy plik - **Control (CTRL) + X**, później **y** i **ENTER**.
12. Resetujemy proces **ssh**, żeby wprowadzić zmiany:

```bash
sudo service ssh restart
```

## Model AI - mózg asystenta

Do OpenClaw można podpiąć wiele różnych modeli LLM. Podobno najlepiej działa z **[Claude Sonnet](https://claude.com/pricing#api)** od **Anthropic**, ale jest to płatne rozwiązanie i to w dodatku rozliczane na podstawie użycia (cena za tokeny), co trochę gryzie mi się z ideą robienia tego na próbę, a więc za możliwie jak najmniejszym kosztem. Na ratunek przychodzi tutaj **Google Gemini**, które w ramach **[Google AI Studio](https://aistudio.google.com/)** jest rozwiązaniem **darmowym** do naszego zastosowania. Śmierdzi podejrzanie prawda? Można to sobie tłumaczyć walką Google z konkurencją OpenAI i Anthropic, ale nie ukrywajmy, że tak naprawdę nie ma nic za darmo, bo korzystając z planu **Free Tier** w **Google AI Studio** tak naprawdę płacimy walutą w postaci naszych danych, które zostaną wykorzystane do szkolenia modeli molocha. Oczywiście będą zanonimizowane i tak dalej... Jak to mówią za darmo to i ocet słodki, a my przecież jesteśmy tutaj, żeby sprawdzić jak to w ogóle działa. Poza tym nie wiem jak Wy, ale ja nie planuję w tym eksperymencie tykać żadnych poufnych danych, więc trochę mi to zwisa czy ktokolwiek będzie analizował durnoty, które wrzucę w testowanego asystenta.

Jeżeli OpenClaw okaże się niesamowitym wynalazkiem to później możemy się łatwo przepiąć na Claude lub w ogóle skorzystać z **[OpenRouter](https://openrouter.ai/)**, co pozwoli płynnie przełączać się pomiędzy różnymi modelami.

Warto jeszcze wspomnieć, że darmowy plan od Google posiada oczywiście limity użycia:
- **RPM** (Requests Per Minute) - limit zapytań na minutę,
- **TPM** (Tokens Per Minute) - limit słów/danych (tokenów) na minutę,
- **RPD** (Requests Per Day) - limit zapytań na dobę.

Limity dostępne dla swojego konta można sprawdzić w **[Dashboard -> Rate Limit](https://aistudio.google.com/rate-limit?timeRange=this-month)**. Polecam skupić się na sekcji **Rate limits by model** i posortować tabelę po nazwie modelu, czyli kolumnie **Model**. Jest tam sporo różnych modeli, ale nas interesują w zasadzie tylko te podpisane **Gemini**, czyli te z kategorii **Text-out models**. Na moment pisania tego wpisu limity dla planu **Free tier** wyglądają dla mnie następująco:

| Model | Category | RPM | TPM | RPD |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini 2.5 Flash** | Text-out models | 0 / 5 | 0 / 250K | 0 / 20 |
| **Gemini 2.5 Pro** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Flash** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Flash Exp** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Flash Lite** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Pro Exp** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 3 Flash** | Text-out models | 0 / 5 | 0 / 250K | 0 / 20 |
| **Gemini 2.5 Flash Lite** | Text-out models | 0 / 10 | 0 / 250K | 0 / 20 |
| **Gemini 3 Pro** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 3.1 Pro** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |

Jak widzisz ograniczenia są dość srogie. W darmowym planie mamy dostęp w zasadzie tylko do trzech modeli:
  - **Gemini 2,5 Flash**
  - **Gemini 3 Flash**
  - **Gemini 2.5 Flash Lite**
Do tego jeżeli chodzi o limity to mamy 5-10 zapytań na minutę, 250k tokenów (to akurat każdemu mówi niewiele) i jedynie 20 zapytań na dobę. To dość kiepsko, ale na przetestowanie bota powinno wystarczyć.

### Pozyskanie klucza API z Google AI Studio

1. Wchodzimy na stronę **[Google AI Studio](https://aistudio.google.com/)** i naciskamy przycisk **Get started** w prawym górnym rogu.
2. **Logujemy się** naszym kontem Google.
3. Z menu po lewej na dole wybieramy **[Get API key](https://aistudio.google.com/api-keys)**.
4. Naciskamy przycisk **Create API key** znajdujący się na górze po prawej.
5. W pole **Name your key** wpisujemy nazwę dla klucza, może to być np. **OpenClaw Assistant**. Z listy **Choose an imported project** wybieramy **+ Create project**, nadajemy mu nazwę np. **OpenClaw Project** i naciskamy **Create project**. Następnie naciskamy **Create key**.
6. Na liście kluczy pojawi się pozycja o nazwie, którą wpisaliśmy. Po prawej stronie mamy kilka ikon, a pierwsza od lewej nazywa się **Copy API key** i to właśnie z tego korzystamy.
7. Skopiowany klucz zapisujemy w bezpiecznym miejscu.

## Uruchamiamy kontener Dockera - narodziny asystenta

Pora przejść do działania. OpenClaw ma nawet w dokumentacji [specjalny podrozdział dotyczący uruchamiania usługi w oparciu o Docker na serwerze Hetzner](https://docs.openclaw.ai/install/hetzner). Będziemy się na nim bazować.

### Przygotowanie Docker'a

1. Wracamy do serwera VPS i logujemy się na użytkowniku **manager**:

```bash
ssh manager@ADRES_IPV4
```

2. Instalujemy potrzebne **pakiety** - Docker, Docker Compose i Git:

```bash
sudo apt install -y docker.io docker-compose-v2 git
```

3. Aby zarządzać kontenerami bez konieczności pisania w kółko _sudo_ przed poleceniami dodamy użytkownika **manager** do grupy **docker**:

```bash
sudo usermod -aG docker manager
```

4. Aby nowe uprawnienia zaczęły działać musimy się wylogować komendą **exit** i połączyć ponownie do serwera:

```bash
ssh manager@ADRES_IPV4
```

### Pobranie repozytorium OpenClaw

1. Przed wykonaniem następnego polecenia sprawdź czy w momencie kiedy to czytasz poniższy link jest dalej aktualny. Piszę o tym, bo z projektem OpenClaw było już tak, że 3 czy 4 razy zmieniana była nazwa a raz nawet osobom trzecim udało się przejąć domenę projektu, co jest szalenie niebezpiecznym procederem. Jeżeli masz wątpliwość to zawsze śmiało możesz napisać do mnie bezpośrednio na Mastodon lub w komentarzu do tego wpisu. Gdy już wiemy, że mamy dobry link do repozytorium to pobieramy je na swój serwer:

```bash
git clone https://github.com/openclaw/openclaw.git
```

2. Przechodzimy do pobranego folderu:

```bash
cd openclaw
```

### Konfiguracja środowiska

1. Teraz definiujemy stały katalog. Docker usuwa dane przy restarcie. Aby bot zachował pamięć (loginy, ustawienia itp.), musimy utworzyć odpowiedni folder na serwerze, w którym będą one utrzymywane:

```bash
mkdir -p /home/manager/.openclaw/workspace
```

2. Musimy jeszcze nadać im odpowiednie uprawnienia wewnętrznego użytkownika kontenera (UID 1000):

```bash
chown -R 1000:1000 /home/manager/.openclaw
```

3. Skonfigurujmy środkowisko. W tym celu tworzymy plik **.env**:

```bash
nano .env
```

4. Jako treść pliku wklejamy:

```bash
OPENCLAW_IMAGE=openclaw:latest
OPENCLAW_GATEWAY_TOKEN=TWÓJ_TOKEN
OPENCLAW_GATEWAY_BIND=lan
OPENCLAW_GATEWAY_PORT=18789
OPENCLAW_CONFIG_DIR=/home/manager/.openclaw
OPENCLAW_WORKSPACE_DIR=/home/manager/.openclaw/workspace
GOG_KEYRING_PASSWORD=TWÓJ_KLUCZ
XDG_CONFIG_HOME=/home/node/.openclaw
GEMINI_API_KEY=KLUCZ_API_GEMINI
```

5. Nie zamykamy jeszcze pliku, bo konieczne jest w nim zmodyfikowanie trzech rzeczy:
    - **TWÓJ_TOKEN** - zamiast tego wpisz jakiś skomplikowany ciąg znaków, który zapiszesz również w swoim menedżerze haseł, będzie to **hasło dostępowe do panelu sterowania** (Control UI) bota.
    - **TWÓJ_KLUCZ** - zamiast tego wpisz jakiś skomplikowany ciąg znaków, który zapiszesz również w swoim menedżerze haseł, będzie to **klucz, którym zaszyfrowane zostaną dane w stałym katalogu** (_./.openclaw/workspace_), który utworzyliśmy wcześniej, dzięki temu nawet jeżeli ktoś włamie się na VPS i skopiuje ten folder to nie odczyta poufnych danych tam przechowywanych.
    - **KLUCZ_API_GEMINI** - zamiast tego podaj **klucz API**, który wcześniej skopiowaliśmy z Google AI Studio.
    - **UWAGA** - przy generowaniu tokenu i klucza uważaj, aby w ciągu znaków nie było **$**, bo wykrzaczyło mi to kontener przy jego budowie i straciłem chyba z godzinę poszukując problemu.
6. Teraz już możemy zapisać i zamknąć plik konfiguracyjny środowiska - **Control (CTRL) + X**, później **y** i **ENTER**.
7. Zanim zbudujemy kontener musimy jeszcze zmodyfikować domyślny plik **docker-compose.yml**, bo nasz przypadek różni się nieco od tego założonego jako domyślny w głównym repozytorium.
8. Jednakże przed modyfikacją pliku lepiej jest zrobić jego kopię zapasową, żeby w razie czego można było odnieść się do jego pierwotnej treści:

```bash
cp docker-compose.yml docker-compose-old-backup.yml
```

9. Otwieramy w edytorze plik **docker-compose.yml**:

```bash
nano docker-compose.yml
```

10. Prawidłowa treść powinna być następująca:

```bash
{% raw %}
services:
  openclaw-gateway:
    image: ${OPENCLAW_IMAGE}
    build: .
    restart: unless-stopped
    env_file:
      - .env
    environment:
      - HOME=/home/node
      - NODE_ENV=production
      - TERM=xterm-256color
      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}
      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}
      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}
      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}
      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}
      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    volumes:
      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw
      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace
    ports:
      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.
      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.
      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"
    command:
      [
        "node",
        "dist/index.js",
        "gateway",
        "--bind",
        "${OPENCLAW_GATEWAY_BIND}",
        "--port",
        "${OPENCLAW_GATEWAY_PORT}",
        "--allow-unconfigured",
      ]
{% endraw %}
```

### Uruchomienie kontenera

1. Przyszła pora na zbudowanie kontenera:

```bash
docker compose build
```

2. Teraz pozostaje czekać cierpliwie. W moim przypadku proces trwał 174 sekundy.

3. Jeżeli kontener został zbudowany pomyślnie (zielony komunikat **built**) to możemy spróbować go uruchomić:

```bash
docker compose up -d openclaw-gateway
```

4. Sprawdźmy teraz czy kontener się uruchomił:

```bash
docker ps
```

5. Na liście powinna pojawić się jedna pozycja o nazwie **openclaw-openclaw-gateway-1**, a w kolumnie **Status** powinno być **Up ...** informujące jaki czas temu kontener "wstał".

6. Sprawdźmy jeszcze logi:

```bash
docker compose logs -f openclaw-gateway
```

7. Jeżeli nie ma tam żadnych czerwonych napisów, **WARNING** albo **ERROR** to to znaczy, że wszystko jest ok. Nie wymagam od nikogo rozumienia co tam jest napisane, bo sam na pewno nie rozumiem tego w pełni. Jeżeli masz wątpliwości to możesz mi podesłać treść logów, wrzucić je tutaj w komentarzu lub zapytać o to np. Gemini ( :-) ). Z logów wychodzimy kombinacją przycisków **Control (CTRL) + C**.

## Panel sterowania - przygotowanie interfejsu do komunikacji

Kontener został uruchomiony, więc pora wejść do jego środka i spróbować podjąć pierwszą próbę kontaktu z botem działającym wewnątrz. A konkretnie wejdziemy do panelu, z którego poziomu będziemy zarządzać botem.

### Tunel SSH

1. Ze względów bezpieczeństwa zablokowaliśmy zarówno dostęp do serwera z zewnątrz (poza portem 22, czyli przez SSH) jak i do samego kontenera. Dlatego, aby dostać się do środka stworzonego środowiska potrzebujemy **zestawić tunel SSH**. W tym celu w terminal na komputerze lokalnym (nie na serwerze) wpisujemy:

```bash
ssh -N -L 18789:127.0.0.1:18789 manager@ADRES_IPV4
```

2. Nie zdziw się, bo terminal w momencie potwierdzenia tej komendy będzie zachowywał się jakby się zawiesił. Tak ma być i znaczy to, że **tunel został uruchomiony** i działa. Będzie tak do momentu zatrzymania procesu (Control + C) lub zamknięcia okna terminala.
3. W ten sposób zestawiliśmy port 18789 naszego komputera z portem 18789 serwera VPS w infrastrukturze Hetzner'a. **Pod tym portem wystawiony jest właśnie panel sterowania botem** uruchomionym w kontenerze Docker'a.
4. Uruchamiamy **przeglądarkę na komputerze** lokalnym i w pasek adresu wpisujemy **[http://127.0.0.1:18789](http://127.0.0.1:18789)**.

### Logowanie do panelu

1. Teraz będziemy potrzebować tokenu **TWÓJ_TOKEN**, który podaliśmy w treści pliku **.env** jako wartość dla zmiennej **OPENCLAW_GATEWAY_TOKEN**.
2. Po załadowaniu strony w przeglądarce zostaniemy poproszeni o jego **podanie w celu uwierzytelnienia**. Jeżeli tak się nie stanie i załaduje nam się pozornie nie działajacy panel z komunikatem o błędzie, podobnym do tego wklejonego przeze mnie poniżej, to musimy **zrobić to ręcznie**.
    > disconnected (1008): unauthorized: gateway token missing (open the dashboard URL and paste the token in Control UI settings)
3. W tym celu w menu po lewej znajdujemy sekcję **Control** i wybieramy zakładkę **Overview**. To tutaj w sekcji **Gateway Access** i polu **Gateway Token** musimy podać nasz token.
4. Naciskamy przycisk **Connect** znajdujący się poniżej w tej samej sekcji... i zonk, dalej nie działa, ale tym razem wywala błąd:
    > disconnected (1008): pairing required
5. To wbrew pozorom dobry znak, bo po pierwsze oznacza, że idziemy w dobrym kierunku, a po drugie to, że zabezpieczenia kontenera działają prawidłowo. Twórcy OpenClaw przewidzieli dodatkową warstwę uwierzytelnienia na wypadek, gdybyś wystawił panel sterowania na świat i w dodatku ktoś poznałby Twój token. Tą ostatnią warstwą zabezpieczającą jest konieczność zatwierdzenia każdego nowego próbującego się połaczyć urządzenia z poziomu konsoli serwera.
6. Aby to zrobić musimy wrócić do terminala i ponownie połączyć się z serwerem VPS. Nie zamykajmy przy tym przeglądarki z panelem wyświetlającym błąd 1008.

```bash
ssh manager@ADRES_IPV4
```

7. Przechodzimy do folderu, do którego pobraliśmy repozytorium OpenClaw:

```bash
cd /home/manager/openclaw
```

8. Uruchamiamy komendę, której zadaniem jest listę urządzeń oczekujących na zatwierdzenie:

```bash
docker compose exec openclaw-gateway node dist/index.js devices list
```

9. Odpowiedź u mnie wyglądała tak:

![](/images/openclawauthpending.png)

10. Z otrzymanego wyniku kopiujemy z sekcji **Pending** wartość z kolumny **Request**. W moim przypadku jest to:
    > 0108ae0d-98dc-4fde-9175-c90392a7fdaf
11. To **IDENTYFIKATOR_ŻĄDANIA**, który wpisujemy jako element na końcu poniżej komendy:

```bash
docker compose exec openclaw-gateway node dist/index.js devices approve IDENTYFIKATOR_ŻĄDANIA
```

12. W podpowiedzi powinniśmy otrzymać komunikat zawierający słowo **Approved** (z ang. zatwierdzony).

13. Teraz, gdy wrócimy do przeglądarki na komputerze lokalnym to powinniśmy już zobaczyć prawidłowo działający panel sterowania.

### Ustawienie modelu

1. W menu po lewej znajdujemy sekcję **Agent** znajdźmy zakładkę **Agents** i wejdźmy do niej.
2. To w tym miejscu znajdują się wszystkie najważniejszego ustawienia naszego bota, to znaczy agenta. Na liście dostępnych agentów powinien widnieć jeden o nazwie **main** i to właśnie jego będziemy używać. Można stworzyć ich więcej z poziomu konsoli serwera, ale na razie ten jeden domyślny nam wystarczy.
3. To co nas interesuje w pierwszej kolejności to sprawdzenie czy w polu wyboru **Primary model (default)** mamy Gemini.

![](/images/openclawcontrolui1.png)

4. Zakładam, że niestety nie znajdziesz tam nic tak jak na moim zrzucie ekranu. Dlatego musimy wrócić do terminala połączonego z serwerem VPS. Wpisujemy w niego komendę:

```bash
docker compose exec openclaw-gateway node dist/index.js models set google/gemini-3-flash
```

5. W odpowiedzi powinniśmy otrzymać komunikat:

```bash
🦞 OpenClaw 2026.2.20 (unknown) — I'll refactor your busywork like it owes me money.

Updated ~/.openclaw/openclaw.json
Default model: google/gemini-3-flash-preview
```

6. Wracamy do panelu sterowania odpalonego w przeglądarce na komputerze i w polu **Primary model (default)** powinno już widnieć **google/gemini-3-flash-preview** (ewentualnie może być konieczność odświeżenia strony).

## Pierwsza rozmowa

Nadeszła ta wiekopomna chwila. Pora sprawdzić czy jesteśmy w stanie wysłać coś do naszego nowego asystenta, a co ważniejsze czy odpisze on do nas z jakimkolwiek sensem.

1. W menu po lewej z sekcji **Chat** wybieramy zakładkę **Chat**.
2. Wyświetli nam się intefejs jak przy standardowym modelu LLM. Na dole mamy pole do wpisywania swojej wiadomości.
3. Napiszmy do niego:

```
Witaj mój nowy Asystencie! Piszę tę wiadomość w ramach testu czy działasz prawidłowo. Czy wiesz jaka jest dzisiaj data?
```

4. DZIAŁA! Odpisał mi dokładnie to:

```
Witaj! Działam jak najbardziej prawidłowo. Dzisiaj jest sobota, 21 lutego 2026 roku.

Skoro test mamy za sobą — co chciałbyś dzisiaj zrobić?
```

## Modele zastępcze

1. Z uwagi na ubogie limity dodamy jeszcze modele zapasowe, czyli **Fallbacks**, które będą wchodzić do gry, gdy model główny, czyli **Primary**, będzie miał kłotopy.
6. Najpierw jako model zapasowy dodamy **Gemini 2.5 Flash**:

```bash
docker compose exec openclaw-gateway node dist/index.js models fallbacks add google/gemini-2.5-flash
```
2. A następnie model **Gemini 2.5 Flash Lite**:

```bash
docker compose exec openclaw-gateway node dist/index.js models fallbacks add google/gemini-2.5-flash-lite
```

3. Kolejność ma znaczenie i w ten sposób łancuch modeli będzie używany tak **Gemini 3 Flash** -> **Gemini 2.5 Flash** -> **Gemini 2.5 Flash Lite**.

Na krótką metę taki pakiet powinien wystarczyć, ale już po napisaniu pierwszego prompta, w którym się przywitałem, widzę, że nie ma możliwości, aby ten darmowy plan na Google AI Studio był wystarczający do napędzienia bota/asystenta, który dostanie jakieś poważniejsze zadanie. Ale o tym jeszcze za chwilę.

## Osobowość asystenta

Tomek nie filozuj, nie filozuj chłopie! Nope, nie powstrzymam się. Osobowość każdego z nas definiowana jest przez bagaż doświadczeń jakie przeżyliśmy w trakcie naszej egzystencji. W przypadku bota OpenClaw ten bagaż doświadczeń, czytaj osobowość, definiowana jest przy pomocy 8 plików, które dostępne są w **Agent -> Agents -> Files**.

### Pliki osobowości
- **Soul.md** (Dusza) - Określa fundamenty zachowania i wartości. Tutaj definiujesz twarde granice oraz to, czy asystent ma być suchy i analityczny, czy może mieć własne zdanie, poczucie humoru i potrafić się z Tobą nie zgodzić.
- **Identity.md** (Tożsamość) - Czyste "dane osobowe" agenta – jego imię, ulubione emoji, awatar i ogólny styl bycia (tzw. vibe).
- **Agents.md** (Instrukcje operacyjne) - Jeżeli miałbym wskazać najważniejszy plik to były to ten. Tłumaczy botowi, jak ma korzystać ze swoich zasobów, kiedy wolno mu się odzywać bez pytania i jak krok po kroku ma analizować problemy.
- **User.md** (Użytkownik) - Plik z informacjami o Tobie. Wpisujesz tu swoje preferencje, kim jesteś, nad jakimi projektami pracujesz i w jakiej formie oczekujesz odpowiedzi. Bot czyta to, by dostosować się do Twojego stylu życia.
- **Memory.md** (Pamięć długotrwała) - Bardzo ważny plik, który bot często aktualizuje sam. Przenosi tu najważniejsze fakty, wnioski i Twoje nawyki z codziennych rozmów (z tzw. pamięci krótkotrwałej), dzięki czemu z upływem miesięcy staje się coraz mądrzejszy i nie zapomina ustalonych wcześniej faktów.
- **Tools.md** (Narzędzia) - Dokumentacja umiejętności bota (skill'i). Definiuje techniczne aspekty tego, do jakich systemów bot ma dostęp (np. czytanie plików lokalnych, przeglądarka internetowa) i jak ma ich używać.
- **Heartbeat.md** (Bicie serca) - Instrukcje dotyczące proaktywności (działań w tle). Steruje tym, kiedy bot ma "budzić się" bez Twojej wyraźnej komendy, np. by cyklicznie zrewidować notatki, sprawdzić powiadomienia lub wysłać Ci podsumowanie dnia.
- **Bootstrap.md** (Rozruch) - Plik używany tylko i wyłącznie przy pierwszym uruchomieniu (tzw. moment przebudzenia). Czasami instruuje bota, by na start zapytał "Kim jestem?". Z reguły po pierwszej konfiguracji traci na znaczeniu.

### Ciekawostka

Te pliki przechowywane są w lokalizacji /home/node/.openclaw/workspace, która jest podpieta do stałego katalogu, zatem są zabezpieczone przed usunięciem/wyczyszczeniem/nadpisaniem, gdy coś niedobrego stanie się z kontenerem.

### Podpowiedź

Powyższe pliki wydają się szalenie istotne w kontekście personalizacji asystenta według swoich potrzeb, jednakże warto pamiętać, że ich zawartość jest wstrzykiwana do każdego jednego prompta wysyłanego do API, a więc od tego jak obszerna jest ich zawartość zależy wprosto proporcjonalnie to jak ciężkie będą zapytania wysyłane do API, a co za tym idzie jak szybko będziemy zużywać limity lub też ile będziemy płacić za tokeny, jeżeli jednak zdecydujemy się przejść na plan płatny. Zalecałbym zatem opisywanie wszystkiego w żółnierskich słowach.

## Narzędzia i umiejętności asystenta

### Tools vs Skills

W systemie OpenClaw często myli się te dwa pojęcia, ale technicznie odpowiadają one za zupełnie inne warstwy działania bota:
- **Tools (Narzędzia)** - To wbudowane, twarde funkcje rdzenia. Są dostarczane domyślnie z systemem i stanowią fundament, dzięki któremu agent w ogóle potrafi wejść w interakcję ze światem i Twoim serwerem.
- **Skills (Umiejętności):** To zewnętrzne, społecznościowe wtyczki (add-ony), które instalujesz dodatkowo. Zawierają one specyficzne instrukcje (zapisane najczęściej w pliku `SKILL.md`) oraz skrypty, które uczą bota wykonywania konkretnych, złożonych zadań przy użyciu jego podstawowych `Narzędzi (Tools)`.

### Narzędzia (Tools)

Narzędzia kontrolujemy w pliku `Tools.md` lub w panelu konfiguracyjnym. Najważniejsze z nich to:
- **Operacje na plikach** - `read` (odczyt) i `write` / `edit` (zapis i edycja)
- **Zarządzanie systemem** - `exec` (wykonywanie komend w terminalu) i `process` (zarządzanie procesami w tle).
- **Internet** - `web_search` (wyszukiwanie) i `web_fetch` (pobieranie treści stron).

### 3. Umiejętności (Skills)

Podczas, gdy `Tool` to np. sprzętowa możliwość używania przeglądarki internetowej, `Skill` to gotowa paczka ucząca bota krok po kroku, jak zalogować się do konkretnej usługi (np. Gmaila czy GitHuba) i wykonać tam zadanie. 

Skill'e pobiera się z publicznego rejestru **[ClawHub](https://clawhub.ai/skills?sort=downloads&nonSuspicious=true)** (działa to jak sklep z aplikacjami). Polecam odwiedzić tą bibliotekę i przejrzeć co tam jest. Zauważ, że wszystkie cokolwiek warte Skill'e posiadają obszerny opis, w którym zajdziemy informację jak go prawidłowo zainstalować swojemu asystentowi oraz jak go używać.

Gdy znajdziemy już interesujący nas skill wystaczy, że skorzystamy z gotowej komendy do jego instalacji. Robimy to z poziomu konsoli serwera VPS. Poniżej przykładowa komenda do instalacji skill'a do obsługi GitHub:

```bash
docker compose exec openclaw-gateway clawhub install github
```

Jednakże zanim zaczniesz doinstalowywać skill'e z ClawHub najpierw zajrzyć jakie domyślne są już zainstalowane, bo w moim przypadku było ich aż 50! Pełna lista znajduje się w **Agent -> Skills -> zwinięte menu Built-in Skills**. W tym samym miejscu zainstalowane skill'e można włączać i wyłączać. Często wystarczy tylko podać swój klucz API do danej usługi i gotowe. Polecam wygenerować specjalny klucz tylko dla asystenta, żeby w razie czego szybko go odłaczyć.

## Kanał komunikacji



## Baw się

To wszystko co przygotowałem w tym wpisie. Tak jak zapowiedziałem nie pokazałem żadnego konkretnego zastosowania, bo nie taki był cel tego wpisu. Teraz czas na pracę domową, czyli uruchomienie wyobraźni. Pomyśl do czego taki asystent mógłby Ci się przydać. Spróbuj to wdrożyć. Zepsuj coś, napraw, znowu zepsuj i znowu napraw, aż osiągniesz swój cel. A jak uda Ci się zrobić coś kozackiego to koniecznie napisz o tym w komentarzu poniżej lub wyślij do mnie dowolnym kanałem.