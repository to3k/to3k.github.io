---
title: "Nie tylko iOS i Android... Ubuntu Touch! (na Google Pixel 3a XL)"
date: 2023-05-17
categories: 
  - "poradniki"
tags: 
  - "adb"
  - "android"
  - "bonito"
  - "bootloader"
  - "chrome"
  - "chromium"
  - "customrom"
  - "debugowanieusb"
  - "fastboot"
  - "flash"
  - "google"
  - "googlepixel3a"
  - "googlepixel3axl"
  - "googleusbdriver"
  - "ios"
  - "linux"
  - "macos"
  - "microsoftedge"
  - "microsoftvisualcplusplus"
  - "minimaladbandfastboot"
  - "oemunlocking"
  - "sargo"
  - "ubports"
  - "ubuntutouch"
  - "usbdebugging"
  - "windows"
  - "xdadevelopers"
image: "/images/ubuntutouch.webp"
description: "Nie ma co ukrywać, że na rynku systemów dla urządzeń mobilnych (smartfonów) mamy bardzo ograniczony wybór, bo możemy w zasadzie wybrać spośród dwóch..."
---

Spis treści:
* TOC
{:toc}

Nie ma co ukrywać, że na rynku systemów dla urządzeń mobilnych (smartfonów) mamy bardzo ograniczony wybór, bo możemy w zasadzie wybrać spośród dwóch systemów - _iOS_ od _Apple_ lub _Android_ od _Google_ (pofragmentowany na nakładki od poszczególnych producentów). To wersja dla zwykłych śmiertelników, bo istnieje jeszcze **przeogromny świat _Custom ROMów_, czyli wariacji systemu _Android_ tworzonych przez entuzjastów**. Dla chętnych, którzy chcą zgłębić temat polecam _[Forum XDA Developers](https://forum.xda-developers.com/)_, które od lat króluje w zakresie tej tematyki. Ja jednak chciałbym w tym wpisie pokazać coś wyróżniającego się z tłumu, a mianowicie **mobilną wersję _Ubuntu_, którą zainstaluję na smartfonie _Google Pixel 3a XL_**, który już teraz jest dość leciwym sprzętem, bo jego oficjalna premiera była w maju 2019 roku. Specjalnie na potrzeby tego wpisu **zakupiłem egzemplarz za 500 zł**.

## Zakup odpowiedniego smartfona

[Lista urządzeń wspierających _Ubuntu Touch_](https://devices.ubuntu-touch.io/) w momencie pisania tego wpisu składa się z 55 pozycji, więc nie jest tak krótka jakby się mogło wydawać. Tak jak napisałem we wstępie ja postawiłem na _Pixela 3a XL_. I to właśnie dla tego modelu oraz dla jego mniejszej wersji _Pixel 3a_ (bez _XL_ w nazwie) będę opisywał całą procedurę.

Jeżeli chodzi o zakup to **istotne jest, aby był to model posiadający możliwość odblokowania _bootloadera_** (czyli takiego telefonowego programu rozruchowego). Nie wszystkie _Pixele_ mają taką możliwość i nie da się tego ustalić np. po numerze seryjnym. Niestety trzeba to sprawdzić indywidualnie dla każdego telefonu. W przypadku zakupu online musimy o to poprosić sprzedawcę, a przy zakupie bezpośrednim zrobić to samemu po uzyskaniu zezwolenia sprzedawcy.

Jak to sprawdzić? Będę to opisywał dla angielskiej wersji językowej systemu, bo tak będzie mi najłatwiej. Wszystkie wskazane nazwy mają zapewne swoje odpowiedniki po polsku, ale jakby ktoś miał problem z ich znalezieniem to proponuję zmienić język systemu na angielski. Wracając do meritum… Należy wejść do ustawień telefonu, następnie _About phone_, odnaleźć na samym dole _Build number_ i naciskać to tak długo aż wyświetli się napis _You are now a developer!_. W taki sposób odblokowuje się dodatkowe (ukryte dla standardowego użytkownika) ustawienia dla deweloperów.

![](/images/deweloper1.webp)

![](/images/deweloper2.webp)

Teraz wracamy do głównego okna ustawień i przechodzimy do _System_ i dalej _Developer options_, które właśnie odblokowaliśmy. Potrzebujemy tutaj włączyć dwie opcje:

1. **_OEM unlocking_** (_Allow the bootloader to be unlocked_) - tak jak mówi podpowiedź, jest to opcja, która umożliwia odblokowanie _bootloadera_ tego urządzenia,

3. **_USB debugging_** (_Debug mode when USB is connected_) - tryb debugowania urządzenia poprzez USB, a po ludzku jest to opcja umożliwiająca manipulowanie w urządzeniu poprzez USB, tj. przez komputer, do którego później podłączymy _Pixela_ i wgramy w ten sposób nowy system oraz wszystkie potrzebne do tego składniki.

**Telefony, które mają zablokowaną możliwość odblokowania _bootloadera_ będą miały tą pierwszą opcję (_OEM unlocking_) wyszarzoną, tj. niedostępną**. Po tym właśnie można rozpoznać telefon, którego nie należy kupować.

W przypadku wyskoczenia komunikatu dotyczącego tego czy zezwalamy na debugowanie USB (_Allow USB debugging?_) zaznaczamy opcję _Always allow from this computer_ (z ang. _Zawsze pozwalaj z tego komputera_) i klikamy _Allow_ (z ang. _Zezwól_).

![](/images/allowusbdebug2.webp)

Przed rozpoczęciem dalszych czynności proponuję zrobić dwie rzeczy:

1. zrestartować telefon,

3. naładować go do pełna.

W trakcie ładowania weźmiemy się za odpowiednie przygotowanie komputera.

## Przygotowanie komputera do odblokowania bootloadera

Przed rozpoczęciem procesu odblokowywania _bootloadera_ i _flashowania_ (wgrywania) nowego systemu musimy przygotować komputer przy pomocy którego będziemy robić te czynności. Ja postawiłem na mój laptop do zadań specjalnych (pancerny _Getac S410_) działający na _Windowsie_, jednakże nic nie stoi na przeszkodzie, aby zrobić to samo na komputerze z _Linuxem_, a nawet _macOS_. Po prostu niektóre kroki mogą się delikatnie różnic, ale ogólnie chodzi o to samo i uzyska się ten sam efekt. Dobrze jest też zaopatrzyć się w sprawdzony i przede wszystkim działający kabel USB, który pozwala na transfer danych, a nie tylko na ładowanie (tak, są takie na rynku jakby ktoś nie miał styczności). Do tego tak ryzykowane działania jak wgrywanie systemu do innego urządzenia zaleca się robić na laptopie. Dlaczego? To proste. W przypadku zaniku prądu laptop przeskoczy na zasilanie bateryjne zamiast je utracić i uceglić nam telefon.

Na komputerze z Windows musimy w zasadzie wykonać cztery czynności:

1. zainstalować (jeżeli nie mamy) _Microsoft Visual C++_, które można [pobrać ze strony _Microsoftu_](https://www.microsoft.com/en-us/download/details.aspx?id=52685) (to wersja 2015, ale gdzieś przeczytałem, że zaleca się też instalację 2012 dostępnej [tutaj](https://www.microsoft.com/en-us/download/details.aspx?id=30679)),

3. zainstalować _Minimal ADB and Fastboot_, do którego zawsze aktualny link znajduje się w [tym wątku na forum _XDA Developers_](https://forum.xda-developers.com/t/tool-minimal-adb-and-fastboot-2-9-18.2317790/),

5. zainstalować instalator od _UBports_, który jest dostępny pod [tym linkiem](https://devices.ubuntu-touch.io/device/sargo#installerDownload),

7. zainstalować sterownik _Google USB Driver_ dostępny pod [tym linkiem](https://developer.android.com/studio/run/win-usb).

O ile krok 1-3 nie powinny dla nikogo stanowić problemu tak chciałbym się pochylić na moment nad czynnością wskazaną w punkcie 4. Pod podanym linkiem dostępna jest paczka .ZIP (archiwum), która należy rozpakować w dowolnym miejscu. Następnie trzeba podłączyć telefon do komputera, na telefonie otworzyć _Centrum powiadomień_ (ruch palcem od górnej krawędzi urządzenia w dół), znaleźć opcję _Charging this device via USB_ (_Tap for more options_) i nacisnąć na nią. To ustawienia _USB Preferences_, które pozwalają zmienić to w jaki sposób telefon ma komunikować się z komputerem. Domyślnie zaznaczoną opcją jest pozwolenie jedynie na ładowanie telefonu bez wymiany danych (_No data transfer_) my jednak chcemy zmienić to na (_Use USB for_) _File transfer / Android Auto_. W ten sposób pozwalamy na transfer danych pomiędzy obydwoma urządzeniami, a telefon pojawi się na naszym komputerze jako dysk zewnętrzny.

![](/images/usbprefs1.webp)

![](/images/usbprefs2.webp)

Na komputerze przechodzimy do _Menu Start_ i następnie _Menedżer urządzeń_ (_Device Manager_). Zostanie wyświetlona lista wszystkich urządzeń znajdujących się w naszym komputerze lub do niego podłączonych. Jeżeli nie instalowaliśmy wcześniej sterownika _Google USB Driver_ to na tej liście powinniśmy mieć jedną pozycję, której ikona będzie miała znak żółtego trójkąta z wykrzyknikiem i być podpisana _Android_, _Pixel 3a_ lub coś w tym stylu. Gdy to zobaczysz na pewno będziesz wiedział/a o co chodzi. Gwoli doprecyzowania będzie to prawdopodobnie w sekcji _Inne urządzenia_ (_Other devices_). Klikamy prawym przyciskiem myszy na to urządzenie i z menu kontekstowego wybieramy _Aktualizuj sterownik_ (_Update driver_). Zostanie odpalone okno, w którym wybieramy drugą opcję, czyli _Przeglądaj mój komputer w poszukiwaniu sterowników_ (_Browse my computer for drivers_). Następnie wybieramy _Pozwól mi wybrać z listy dostępnych sterowników na moim komputerze_ (_Let me pick from a list of available drivers on my computer_), przycisk _Dalej_ (_Next_) i gdy już jesteśmy w oknie proszącym _Wybierz sterownik, który chcesz zainstalować dla tego sprzętu_ (_Select the device driver you want to install for this hardware_) korzystamy z przycisku _Z dysku..._ (_Have Disk..._). Wyskoczy kolejne okienko, w którym musimy odnaleźć przycisk _Przeglądaj..._ (_Browse..._), naciskamy go i wskazujemy plik _android\_winsub.inf_, który znajduje się z pobranej i wypakowanej paczce _Google USB Driver_. Dalej już tylko przeklikujemy _Otwórz_ (_Open_), _OK_, _Dalej_ (_Next_), _Tak_ (_Yes_), _Instaluj_ (_Install_) i po pomyślnej instalacji kończymy przyciskiem _Zamknij_ (_Close_). Po tym wszystkim urządzenie, które wcześniej miało żółty trójkąt z wykrzyknikiem już nie powinno go mieć i zostać rozpoznane jako normalne urządzenie z zainstalowanymi poprawnymi sterownikami.

Jeżeli ktoś potrzebuje wizualnego przewodnika po powyższych czynnościach to polecam [filmik tego Pana (chyba) Hindusa](https://yewtu.be/watch?v=ajdcWIY-5yo).

## Odblokowanie bootloadera

_Pixela_ zostawiamy dalej podłączonego do komputera. Na komputerze uruchamiamy wcześniej zainstalowany program _Minimal ADB and Fastboot_, co powinno skutkować otworzeniem okna wiersza poleceń (windowsowy terminal). Zaczynamy od sprawdzenia czy nasz telefon jest prawidłowo podłączony, skonfigurowany i widoczny dla narzędzia do odblokowania _bootloadera_:

```bash
adb devices
```

Przy pierwszym wpisaniu tego polecenia pod _List of devices attached_ może nam zostać wyświetlony komunikat z identyfikatorem urządzenia (numer seryjny) i obok niego frazą _unauthorized_, co oznacza, że musimy jeszcze raz wyrazić na telefonie zgodę na debugowanie przez USB. Wykonujemy powyższe polecenie jeszcze raz i tym razem powinniśmy już zobaczyć frazę _device_ obok identyfikatora urządzenia. To potwierdza, że wszystko do tego momentu wykonaliśmy prawidłowo.

Następnym poleceniem wywołamy przejście telefonu w tryb _Bootloadera_:

```bash
adb reboot bootloader
```

Na telefonie powinno się pojawić coś podobnego do widocznego na poniższym zdjęciu:

![](/images/IMG_1809.webp)

Jak widać weszliśmy do _Bootloadera_, ale _Device state_ widnieje jako _locked_. Naszym celem jest zmiana tego stanu na _unlocked_. Wracamy do wiersza poleceń na komputerze i tym razem wpisujemy:

```bash
fastboot flashing unlock
```

Przechodzimy na telefon, gdzie musimy potwierdzić, że _bootloader_ ma zostać odblokowany. W tym celu naciskamy jednokrotnie dowolny z przycisków głośności (w tym trybie służą one do przełączania opcji, które chcemy wybrać), tak aby wybrana została opcja _Unlock the bootloader_, i potwierdzamy wybór przyciskiem _Power_.

![](/images/IMG_1811-scaled.webp)

Po krótkiej chwili wrócimy z powrotem do głównego menu _bootloadera_, gdzie powinniśmy już zobaczyć _Device state: unlocked_. Sukces! _Bootloader_ odblokowany, urządzenie stoi przed nami otworem.

![](/images/IMG_1812.webp)

Na koniec dobrze jest jeszcze prawidłowo zakończyć działanie narzędzia _Minimal ADB and Fastboot_ wydając polecenie:

```bash
adb kill-server
```

i następnie zamknąć okno wiersza poleceń.

## Przywrócenie wymaganej wersji systemu Android

W [dokumentacji _UBports_](https://devices.ubuntu-touch.io/device/sargo/) można przeczytać, że w celu wgrania _Ubuntu Touch_ konieczne jest cofnięcie wersji systemu operacyjnego _Android_, działającego na naszym urządzeniu, do konkretnego wydania. W momencie pisania tego poradnika jest to wydanie o oznaczeniu _PQ3B.190801.002_. Piszę o tym, gdyż nie wiem ile czasu minęło od napisania tego poradnika do momentu kiedy z niego korzystasz i możliwe jest, że nowsze wersje _Ubuntu Touch_ będą wymagały innej wersji _Androida_ do instalacji. Dlatego zawsze polecam wejść [tutaj](https://devices.ubuntu-touch.io/device/sargo/) i sprawdzić tę informację na chwilę przed podjęciem dalszych działań. Istotne są też tak zwane code name'y (z ang. nazwy kodowe), które dla każdego modelu _Pixela_ są inne:

- dla _Google Pixela 3a_ jest to **_SARGO_**,

- dla _Google Pixela 3a XL_ jest to **_BONITO_**.

Jest to istotne później, a znajomość tych nazw pozwoli uniknąć pomylenia obrazów systemów i wzięcia obrazu dla niewłaściwego modelu, co w zasadzie może w najgorszym wypadku uceglić całkowicie telefon. Ja będę operował na _Bonito_, bo mam _Pixela 3a XL_, ale te same kroki można wykonać dla _Pixela 3a_ korzystając z obrazu podpisanego _Sargo_.

_Flashowanie_ (wgrywanie) systemu na urządzenia _Pixel_ dokonuje się przy użyciu przeglądarki _Chrome_. Cóż… Telefon od _Google_, więc zrobili tak, aby ich przeglądarka była niezbędna. Sprytne, prawda? Może i tak, ale my jesteśmy bardziej przebiegli, bo może niewiele osób wie, ale tak naprawdę nie potrzeba konkretnie przeglądarki _Chrome_, a dowolną działającą na silniku _Chromium_, czyli możemy równie dobrze użyć przeglądarki _Microsoft Edge_! Do tego użyjemy jej, aby zrobić krok do pozbycia się z telefonu systemu od _Google_, więc totalnie ucieramy nosa tejże korporacji 😉

Odpalamy przeglądarkę _Microsoft Edge_, wchodzimy na stronę [https://developers.google.com/android/images?hl=pl#bonito](https://developers.google.com/android/images?hl=pl#bonito), zjeżdżamy na sam dół, gdzie widnieje niebieski przycisk _Potwierdzam_ przy _Znam i akceptuję powyższe warunki korzystania z usługi_, naciskamy go. Zostaniemy przeniesieni do listy obrazów fabrycznych dla smartfonów _Nexus_ oraz _Pixel_. Tak jak wcześniej już wspomniałem znajdujemy na niej wydanie o oznaczeniu _PQ3B.190801.002_, uważając przy tym, aby był to obraz dedykowany do naszego urządzenia.

![](/images/googleflash1-1024x473.webp)

Po odnalezieniu odpowiedniego obrazu naciskamy obok _W formacie Flash_ (dziwne tłumaczenie na polski, bo w wersji angielskiej jest to po prostu _Flash_). Zostaniemy przeniesieni do webowego narzędzia do wgrywania systemów _Android_. Tym razem nie będę opisywał dokładnie przebiegu procesu, bo to co należy po kolei zrobić widać idealnie na poniższych zrzutach ekranu.

![](/images/aft1.webp)
    
![](/images/aft2.webp)
    
![](/images/aft3.webp)
    
![](/images/aft4.webp)
    
![](/images/aft5.webp)
    
![](/images/aft6.webp)
    
![](/images/aft7.webp)
    
![](/images/aft8.webp)
    
![](/images/aft9.webp)
    
![](/images/aft10.webp)
    
![](/images/aft11.webp)
    
![](/images/aft12.webp)
    
![](/images/aft13-1024x549.webp)
    

Efektem będzie przywrócenie systemu _Android 9_ na naszego _Pixela_. Telefon został także wyczyszczony, więc ponownie trzeba na nim zrobić podstawową konfigurację, gdzie proponuję pominąć większość opcji i po prostu korzystać z przycisku _Skip_. Nie ma nawet sensu konfiguracji Wi-Fi, bo za chwilę telefon zostanie znowu wyczyszczony po wgraniu systemu docelowego (_Ubuntu Touch_). Jedyne co jest istotne po podstawowym skonfigurowaniu systemu to wejść do ustawień, znowu odblokować opcje deweloperskie i sprawdzić czy debugowanie USB jest włączone. Jeżeli nie jest to oczywiście je włączamy i zgadzamy się na debugowanie USB z naszego laptopa (tak jak opisałem wcześniej).

## Flashowanie Ubuntu Touch

_Ubuntu Touch_ wgramy wcześniej zainstalowanym instalatorem _UBports_. Tak jak wcześniej cały proces pokazałem na zrzutach ekranu poniżej.

![](/images/ubp1.webp)
    
![](/images/ubp2.webp)
    
![](/images/ubp3.webp)
    
![](/images/ubp4.webp)
    
![](/images/ubp5.webp)
    
![](/images/ubp6.webp)
    
![](/images/ubp7.webp)
    
![](/images/ubp8.webp)
    
![](/images/ubp9.webp)
    
![](/images/ubp10.webp)
    

## Ubuntu Touch - pierwsze wrażenia

![](/images/IMG_1816-scaled.webp)

![](/images/IMG_1817-scaled.webp)

![](/images/IMG_1818-scaled.webp)

Inicjatywa jaką jest projekt _Ubuntu Touch_ jest bardzo, ale to bardzo, istotna, warta szacunku i godna wsparcia. Jest to ewidentnie próba dania ludziom wolności w zakresie wyboru systemu operacyjnego, który nie będzie ich szpiegował na każdym kroku. Do tego jest otwarty i kompletnie darmowy. System jest całkiem nieźle dopasowany do urządzeń wielkości na jakich ma być uruchomiony i widać, że autorzy w pierwszej kolejności postawili na to, aby działały wszystkie podstawowe funkcjonalności telefonu. Mam tutaj działające takie podstawy jak Wi-Fi, czy transmisja danych komórkowych, ale także takie szczegóły jak czytnik linii papilarnych.

![](/images/ubuntutouchpixel.webp)

Jednakże wyżej wymienione podstawy to nie wszystko. To co najgorzej boli, gdy używa się _Ubuntu Touch_, to absolutny brak aplikacji. Niestety w "sklepie" z aplikacjami jest dramatycznie mało pozycji, co widać na poniższych zrzutach ekranu. Pobawiłem się w aptekarza i policzyłem wszystkie z nich - na moment pisania tego wpisu są to 184 pozycje...

![](/images/ubuntustore1.webp)

![](/images/ubuntustore2.webp)

Czy _Ubuntu Touch_ zainstalowane na smartfonie _Google Pixel 3a XL_ może być urządzeniem do codziennego użytku? W mojej ocenie niestety nie. Jednak jest to na pewno bardzo ciekawy temat i każdemu polecam sprawdzić "z czym to się je". Marzę, aby ten projekt został doprowadzony znacznie dalej niż to gdzie znajduje się teraz. Na pewno będę go dalej obserwował.
