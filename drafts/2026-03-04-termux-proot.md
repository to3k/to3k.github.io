---
layout: post
title: "Desktopowy Linux na każdym Androidzie"
published: true
categories: 
  - "poradniki"
tags: 
  - "linux"
  - "android"
  - "termux"
  - "x11"
  - "xfce"
  - "desktop"
  - "gui"
  - "proot"
image: "/images/termux-proot.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/termux-proot-eng/)

Spis treści:
* TOC
{:toc}

## Wstęp

Współczesne smartfony i tablety to potężne maszyny obliczeniowe, które większość czasu marnują na skrolowanie durnych filmików. Tymczasem w kieszeni nosimy moc porównywalną z ultrabookami. Największą barierą nie jest sprzęt, lecz system operacyjny Android, który choć oparty na jądrze Linux, skutecznie izoluje nas od profesjonalnych narzędzi.

Plan na dzisiaj to przełamanie bariery. Pokażę, jak wykorzystując środowisko **Termux**, warstwę **PRoot** oraz serwer grafiki **Termux-X11**, zmienić **dowolne urządzenie** z Androidem na pokładzie w **pełnoprawną stację roboczą z Linuxem**, środowiskiem XFCE. Wszystko to **bez** odblokowywania bootloadera i **bez** utraty gwarancji.

## Architektura rozwiązania: Co dzieje się pod maską?

Zanim przejdziemy do praktyki, trochę teorii. Są trzy filary, na których opiera się ten projekt.

### Termux - terminal, który jest systemem

**Termux** to nie jest zwykła aplikacja terminala. To kompletne **środowisko Linux** działające w przestrzeni użytkownika Androida. Posiada własny **menedżer pakietów** `pkg`, który pozwala na instalację kompilatorów, interpreterów i narzędzi sieciowych. To tutaj dzieje się cała magia.

### PRoot - bezpieczna piaskownica
Standardowo Android nie pozwala na zmianę katalogu głównego na `/` ani na udawanie użytkownika root. **PRoot** to mechanizm, który przechwytuje zapytania systemowe (system calls) i przekierowuje je tak, aby programy zainstalowane wewnątrz kontenera (np. Ubuntu czy Debian) myślały, że działają na prawdziwym, odizolowanym systemie Linux. To pozwala na instalację pakietów i zarządzanie systemem tak, jakbyś miał uprawnienia administratora.

### Termux-X11 - grafika nowej generacji
Tradycyjnie Linux na Androidzie kojarzył się z powolnym VNC. **Termux-X11** zmienia zasady gry. To natywny serwer wyświetlania, który komunikuje się bezpośrednio z systemem Android. Dzięki temu uzyskujemy płynność bliską natywnej, wsparcie dla systemowego schowka, poprawne skalowanie rozdzielczości i – co najważniejsze – możliwość korzystania z akceleracji sprzętowej na procesorach Snapdragon.

## Przygotowanie sprzętowe i programowe

### Wymagania sprzętowe

* **Procesor** - najlepiej Snapdragon (ze względu na wsparcie dla sterowników GPU Turnip). MediaTek i Google Tensor również zadziałają świetnie w zadaniach deweloperskich (renderowanie programowe),
* **RAM** - minimum 8 GB. VS Code i nowoczesna przeglądarka to pożeracze pamięci,
* **Pamięć wewnętrzna** - przynajmniej 10-15 GB wolnej przestrzeni na system i pliki projektów.

### Niezbędne aplikacje

Cały proces zamyka się w zasadzie na instalacji dwóch aplikacji:
1. **Termux** (wersja 0.118 lub nowsza),
2. **Termux-X11**.

Zaleca się, aby **nie pobierać ich z Google Play Store**, gdzie Termux jest dostępny w przestarzałej wersji. Ludzie polecają F-Droid, ale ja konsekwentnie będę polecał **Obtainium** i to właśnie proces instalacji wykorzystujący tego drugiego opiszę poniżej.

## Proces instalacji

### Krok 1 - Konfiguracja Androida
Android 12 i nowsze posiadają mechanizm, który zabija procesy zużywające dużo zasobów w tle. Musimy go ograniczyć:
1. Przejdź do **Ustawienia -> Informacje o telefonie**, na samym dole znajdziesz **Numer kompilacji**, klikaj to pole (7 razy), aż zobaczysz komunikat **Jesteś teraz programistą**.
2. Przejdź do **Ustawienia -> System -> Opcje programisty**, odszukaj sekcję **Aplikacje**, następnie konkretnie opcję **Wyłącz ograniczenia procesów podrzędnych aplikacji** (ang. _Disable child process restrictions_) i włącz ją. 

### Krok 2 - Instalacja Termux i Termux-X11

1. Jeżeli jeszcze nie posiadasz **Obtainium** to wejdź na [oficjalną stronę](https://obtainium.imranr.dev/), pobierz **plik instalacyjny APK** i zainstaluj na swoim telefonie. Może być tak, że będzie konieczne wyrażenie zgody na instalację aplikacji ze źródeł trzecich (nieznanych). Dodatkowo w GrapheneOS trzeba jeszcze nadać uprawnienia konkretnej aplikacji (w tym przypadku przeglądarce) na instalację innych aplikacji. Protip: po instalacji Obtainium polecam odebrać to uprawnienie przeglądarce.
2. Uruchamiamy świeżo zainstalowane Obtainium.
3. Na dole znajduje się przycisk **+Dodaj apkę**.
4. W pole **Adres URL źródła aplikacji** wklej adres [repozytorium](https://github.com/termux/termux-app) `https://github.com/termux/termux-app`, naciśnij przycisk **Dodaj**.
5. Aplikacja Obtainium powinna sama znaleźć odpowiedni plik APK dla Twojego telefonu. Wystarczy tylko na dole kliknąć **Instaluj**.
6. W ten sposób zainstalowaliśmy **Termux**. Dla **Termux-X11** sprawa wygląda analogicznie tylko jako adres repozytorium wklejamy [repozytorium](https://github.com/termux/termux-x11) `https://github.com/termux/termux-x11`.

### Krok 3 - Konfiguracja środowiska

1. Otwieramy aplikację **Termux**. Wygląda ona jak standardowy terminal tylko, że uruchomiony na telefonie.
2. Zaczynamy od udzielenia jej **uprawnień do pamięci** telefonu:

    ```bash
    termux-setup-storage
    ```

3. W oknie, które wyskoczy **zgadzamy się na dostęp**.
4. **Zaktualizujmy** pakiety:

    ```bash
    pkg update && pkg upgrade -y
    ```

5. **Instalujemy** `git`:

    ```bash
    pkg install git -y
    ```

6. Pozyskamy teraz **gotowy skrypt instalacyjny** z GitHuba gościa o nicku [orailnoor](https://github.com/orailnoor):

    ```bash
    git clone https://github.com/orailnoor/termux-linux-setup
    ```

7. **Wejdźmy** do pobranego repozytorium:

    ```bash
    cd termux-linux-setup/
    ```

8. W środku oprócz pliku `README.md` jest skrypt `termux-linux-setup.sh`, któremu musimy **nadać uprawnienia do wykonywania się**:

    ```bash
    chmod +x termux-linux-setup.sh
    ```

9. **Odpalmy** go:

    ```bash
    ./termux-linux-setup.sh
    ```

10. Odpalony skrypt w pierwszej kolejności spróbuje identyfikować na jakim telefonie został odpalony. Tak jak wpisałem wcześniej rekomendowane jest posiadanie telefonu z procesorem Snapdragon, a konkretnie z GPU Adreno. Jednakże ma to istotne znaczenie tylko w przypadku, gdybyśmy chcieli odpalić na naszym telefonie gry, a mnie takie rzeczy nie interesują. **Do VS Code i podstawowej pracy na środowisku graficznym nie musi to wcale być ta konkretna rodzina procesorów wspierająca akcelerację sprzętową**.
11. Powiedziawszy to, musimy wybrać środowisko graficzne (ang. _Desktop Environment_), którego chcemy używać. Ja rekomenduje wybranie **XFCE**, ale każdy może dokonać wyboru według własnych preferencji. Zatem, aby dla przykładu wybrać `XFCE` musimy wprowadzić z klawiatury cyfrę **1** i potwierdzić **ENTERem**.
12. To jest ten moment, w którym musimy uzbroić się w **cierpliwość**, bo jest to zasadniczy etap pracy skryptu. Gdy zostanie zakończony otrzymamy duży komunikat `INSTALLATION COMPLETE!`, a na jego końcu znajdzie się najważniejsza dla nas informacja, tj. **dwie komendy**, z których pierwsza uruchamia środowisko, a druga zatrzymuje jego pracę:

    ```bash
    TO START THE DESKTOP: ./start-linux.sh
    TO STOP THE DESKTOP: ./stop-linux.sh
    ```

### Krok 4 - uruchomienie środowiska graficznego

1. Zgodnie z podpowiedzią z ostatniego punktu poprzedniego kroku **wpisujemy w Termux komendę**:

    ```bash
    ./start-linux.sh
    ```
2. Teraz możemy zminimalizować aplikację Termux i przejść do **Termux-X11**.
3. Po dosłownie chwili oczekiwania powinien **ukazać nam się pulpit** pięknego interfejsu XFCE!

Na końcu tego wpisu załączam kilka **zrzutów ekranu**, które pokazują jak to wygląda **na moim Pixelu 9a**. Może i nie wygląda to imponująco, ale warto zauważyć, że jest to ekran o przekątnej zaledwie 6.3". Mimo tego myślę, że zmiana kilku ustawień z odpowiednim skalowaniem na czele zmieniłaby sytuację diametralnie, a to co się liczy to jak płynnie działa to środowisko. Preinstalowany Firefox lata na tym bez problemu nawet z kilkoma kartami, do tego widziałem, że ludzie instalują i używają bez problemu takie programy jak GIMP, VS Code i inne. Jak dla mnie WOW!

Co ciekawe Termux-X11 to zwykła aplikacja, więc można się **płynnie przełączać pomiędzy nią i wszystkimi innymi aplikacjami** jakie ma się na telefonie.

## Podsumowanie

Wiele osób zapyta - `no dobra, ale po co to komu...?`. Dla mnie w pierwszej kolejności jest to ***Proof of Concept*** i ciekawe rozwiązanie. Po drugie, jestem w stanie wyobrazić sobie całkiem sporą liczbę scenariuszy, w których mam przy sobie tylko smartfon i konieczne jest nagłe wykonanie jakiegoś zadania, które najlepiej, lub wręcz tylko i wyłącznie, można zrobić na środowisku desktopowym. Po trzecie, monitor oraz klawiaturę i myszkę na Bluetooth to wszystko co jest potrzebne do stworzenia w miarę komfortowego stanowiska pracy z całym swoim środowiskiem, które masz w kieszeni - na swoim smartfonie.

Po krótkich testach zacząłem się zastanawiać naprawdę poważnie nad sprawieniem sobie jakiegoś w miarę taniego i wytrzymałego (typu rugged) tabletu z dużą baterią i ekranem o przekątnej ok. 10". Poszperałem nawet już trochę w Internecie i moją uwagę przykuł **Ulefone Armor Pad 4 Ultra**. Brzmi egzotycznie, ale według licznych opinii to całkiem ciekawy sprzęt, a można go wyrwać już za jakieś 1300 PLN (wliczając już cło). Oczywiście z Chin.

![](/images/termux1.png)

![](/images/termux2.png)

![](/images/termux3.png)

![](/images/termux4.png)

## Wideo

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 6px; margin-bottom: 20px;">
  <iframe src="https://www.youtube.com/embed/PyDQmfeRXQc" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>