---
title: "Home Assistant - domowy serwer smart home"
date: 2025-02-01
categories: 
  - "poradniki"
  - "self-hosting"
  - "smarthome"
tags: 
  - "amd"
  - "arm"
  - "balenaether"
  - "github"
  - "haos"
  - "homeassistant"
  - "khadas"
  - "odroid"
  - "opensource"
  - "port8123"
  - "raspberrypi"
  - "selfhosted"
  - "shelly"
  - "smarthome"
  - "tinker"
image: "/images/homeassistantlogo.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/home-assistant-eng/)

W [poprzednim wpisie pokazałem jak od zera zrobić smart oświetlenie w swoim domu w oparciu o produkty firmy _Shelly_](https://blog.tomaszdunia.pl/shelly-smart-oswietlenie/). W moim przypadku był to pierwszy krok w tworzeniu systemu „inteligentnego” domu, w którym mam plan zintegrować znacznie więcej rozwiązań pozwalający na automatyzację różnych aspektów. Jednakże, aby to wszystko miało sens potrzebny jest **mózg systemu, czyli serwer, który będzie pozwalał na zarządzanie **tymi wszystkimi smart urządzeniami** z jednego miejsca**. Na rynku jest wiele rozwiązań tego typu, ale dla mnie wybór był oczywisty. Postawiłem na oprogramowanie o nazwie **_Home Assistant_**. Dlaczego? Oto moje argumenty:

1. jest to oprogramowanie **otwartoźródłowe** (open source),

3. może działać w zupełności **offline** (no może pomijając aktualizację) i zarządzać urządzeniami odciętymi od Internetu, tj. bez konieczności narażania swojej sieci domowej poprzez wpuszczanie urządzeń, które łączą się z podejrzanymi domenami zewnętrznymi,

5. jest **darmowe**,

7. do tego bardzo **popularne**, więc nie ma problemu ze znalezieniem poradników dotyczących dosłownie wszystkiego,

9. na dodatek działa praktycznie **na każdym urządzeniu**,

11. i co więcej współpracuje z naprawdę **ogromną bazą urządzeń**, które wspierają _HA_ natywnie lub poprzez **dodatki pisane przez entuzjastów**,

13. nie zamyka nas w żadnym ekosystemie, co sprawia, że **nie jesteśmy uwiązani do urządzeń jednej marki**.

Czego chcieć więcej? 🤷‍♂️

## Sprzęt

Tak jak napisałem wyżej, _Home Assistant_ może zostać uruchomiony na naprawdę wielu różnych urządzeniach. Może to być **stary komputer PC**, **kontener _Dockera_** czy ten **maszyna wirtualna** uruchomiona na jakimś większym serwerze lub po prostu minikomputer pokroju _**Raspberry Pi**_ czy _**Odroid**_. Ja postanowiłem swój serwer domowy uruchomić na płytce _**Odroid C4**_, bo akurat taką już wcześniej zakupiłem i okazało się, że na ten moment jest to rekomendowany hardware. Na pewno nie jest to przyszłościowe rozwiązanie, bo wraz z czasem **będą zwiększały się wymagania systemu _HA_** jak i moja **domowa sieć urządzeń smart będzie się rozrastać** i wymagać większej mocy obliczeniowej do sprawnego zarządzania nią. Natomiast uważam, **że na początek w zupełności wystarczy**, a z czasem sprawię sobie jakiś mocniejszy serwer. **Przeniesienie konfiguracji z jednego urządzenia na drugie to dosłownie kilka kliknięć**, więc mogę to zrobić w każdym momencie.

Niech nie będzie żadnym wyznacznikiem to, że wybrałem akurat _Odroid C4_, bo może to być równie dobrze _Raspberry Pi 4_ lub _5_. Myślę jednak, że powinno się brać pod uwagę tylko wersje z 4GB RAM (lub więcej).

Nie możemy też zapomnieć o odpowiednim nośniku w postaci karty _microSD_. Istotne, aby **wybrać kartę z oznaczeniem _AC2_**, bo jest to rozwiązanie dedykowane do zapisu i odczytu dużej ilości małych plików i przechowywania aplikacji.

## Instalacja

Osobiście uważam, że tak istotna rzecz jak **domowy serwer smart home powinien być zupełnie niezależnym systemem działającym na urządzeniu dedykowanym** tylko do tego. Dlatego właśnie taki wariant będę omawiał. Jeżeli komuś to nie odpowiada i chciałby uruchomić _HA_ np. na maszynie wirtualnej jakiegoś większego serwera to wierzę, że posiadając taki serwer jest na tyle zaawansowanym użytkownikiem, że da sobie radę z instalacją _HA_ bez mojego poradnika.

Polecam rozpocząć od odwiedzenia strony [home-assistant.io/installation](https://www.home-assistant.io/installation/), na której można zorientować się jakie są możliwości.

Wszystkie obrazy systemu _Home Assistant OS_ są dostępne na _GitHub_ pod adresem [github.com/home-assistant/operating-system/releases](https://github.com/home-assistant/operating-system/releases). Od razu uczulę, aby **pominąć wszystkie wersje otagowane _Pre-release_ i znaleźć tą podpisaną _Latest_**. Dla ułatwienia podam [specjalny link, który od razu powinien przenieść do najnowszej wersji](https://github.com/home-assistant/operating-system/releases/latest). Gdy namierzymy już najnowszą wersję _HAOS_ to musimy znaleźć **obraz odpowiedni dla naszego urządzenia**. Na moment pisania tego wpisu [najnowsza wersja _HAOS_ to 14.1](https://github.com/home-assistant/operating-system/releases/tag/14.1). Wybieram zatem do pobrania plik o nazwie:

```
haos_odroid-c4-14.1.img.xz     276 MB     Dec 19, 2024
```

Jeżeli masz inny sprzęt niż ja to **nie przejmuj się i na spokojnie przejrzyj listę dostępnych obrazów**. Jak widzisz są tam dedykowane obrazy w wielu różnych wariantach:

- **generic aarch64** - ogólny obraz dla urządzeń opartych o architekturę _ARM_, które nie mają dedykowanego obrazu,

- **generic x86** - ogólny obraz dla urządzeń opartych o architekturę _AMD_, które nie mają dedykowanego obrazu,

- **green** - dla posiadaczy gotowego urządzenia _Home Assistant Green_, który można kupić od twórców _HA_,

- **khadas** - dla posiadaczy płytek _Khadas VIM3_,

- **odroid** - dla posiadaczy płytek _Odroid C2, C4, M1, M1S, N2 i XU4_,

- **ova** - obraz dedykowany do uruchamiania jako maszyna wirtualna,

- **rpi** - dla posiadaczy płytek _Raspberry Pi 3, 4 i 5_,

- **tinker** - dla posiadaczy płytek _Tinker_ (_ASUS_),

- **yellow** - dla posiadaczy gotowego urządzenia _Home Assistant Yellow_, który można kupić od twórców _HA_.

Bez względu na to co wybierzemy interesuje nas plik z rozszerzeniem ".img.xz". Jest to **archiwum, które należy rozpakować** np. przy pomocy programu _[7-zip](https://www.7-zip.org/)_.

Mając już obraz i kartę pamięci przyszedł czas na **stworzenie bootowalnego nośnika**. Jak zwykle zarekomenduję użycie do tego narzędzia [_balenaEther_](https://etcher.balena.io/). Cały proces jest szalenie prosty i zdaje się, że już go kiedyś opisywałem na tym blogu. Niemniej jednak dla przypomnienia, na szybko:

1. _Flash from file_ - wybieramy ściągnięty obraz,

3. _Select target_ - wybieramy kartę SD,

5. _Flash!_ - przycisk, który uruchamia proces.

Cały proces podzielony jest na dwa etapy:

1. _Flashing_ - część właściwa tworzenia bootowalnego nośnika,

3. _Validating_ - sprawdzenie jego integralności i ogólnej poprawności wykonania procesu.

![](/images/balenaether1.png)
    
![](/images/balenaether2.png)
    
![](/images/balenaether3.png)
    
![](/images/balenaether4.png)
    

Karta gotowa! Można ją wypiąć z czytnika i wsunąć do odpowiedniego portu w urządzeniu docelowym, które już za moment stanie się naszym domowym serwerem smart home. Gdy urządzenie jest gotowe podpinamy je do kabla sieciowego i zasilania.

## Pierwsze uruchomienie

Zaczynamy od odpalenia przeglądarki i wpisania w pasek adresu [http://homeassistant.local:8123](http://homeassistant.local:8123) lub ewentualnie możemy skorzystać z adresu:

```
http://X.X.X.X:8123
```

gdzie _X.X.X.X_ to adres naszego nowego serwera w sieci lokalnej. Jak widzisz **_Home Assistant_ pracuje na wystawionym porcie _8123_**, zapamiętajmy to, bo później się to przyda. Ekran, który nas przywita powinien wyglądać mniej więcej tak:

![](/images/ha0.png)

Jest to pierwszy krok w procesie konfiguracji nowej instancji _HA_, w którym pobierany jest _Home Assistant Core_. Niestety **długość trwania tego etapu zależy od specyfikacji naszego sprzętu i przede wszystkim jak szybki mamy Internet**, bo do pobrania jest przynajmniej jakieś 700 MB. Gdy zostanie już zakończony to ukaże się strona powitalna, na której możemy zdecydować czy chcemy utworzyć system od zera, czy też może mamy kopię zapasową, z której chcielibyśmy go przywrócić. My dopiero zaczynamy przygodę z _HA_, więc wybieramy _Create my smart home_.

![](/images/ha1.png)

Zaczynamy oczywiście od utworzenia konta administratora. Musimy poddać nazwę, login i dwa razy hasło. Gdy wszystko się zgadza potwierdzamy przyciskiem _Create account_.

![](/images/ha3.png)

W następnym kroku zostaniemy poproszeni o wskazanie lokalizacji swojego domu. Możesz się zastanawia "ale po co?", dlatego spieszę z wyjaśnieniem, że jest to istotna informacja w kontekście:

- **prognozy pogody**, którą można sobie wyświetlić na stronie głównym panelu sterowania,

- **godziny świtu i zmierzchu**, co jest przydatne np. przy sterowaniu oświetleniem zewnętrznym,

- **miliona innych automatyzacji**, które można stworzyć np. w oparciu o warunek pokroju "gdy jestem poza domem" itp.

W tym kroku ustawiamy także system jednostek jaki chcemy używać (metryczny) i walutę. Zaraz zaraz, walutę...? Tak, chodzi o to, że _HA_ ma funkcje, które przeliczają nam np. zużycie prądu i inne tego typu dane na realne kwoty.

![](/images/ha4.png)

Na koniec jeszcze prośba o udostępnienie danych diagnostycznych. Oczywiście nie ma obowiązku zgadzania się na przekazywanie czegokolwiek.

![](/images/ha5.png)

Podstawowa konfiguracja zakończona. W ostatnim oknie jakie zostanie nam wyświetlona _Home Assistant_ wylistuje nam kompatybilne urządzenia, które odnalazł w sieci i może się z nimi zintegrować. Oczywiście jeżeli takie w ogóle w danym momencie istnieją w sieci. Na tym etapie nie ma potrzeby się tym zajmować, bo można to zrobić na spokojnie później, więc naciskamy przycisk _Finish_.

![](/images/ha6.png)

## Podstawowa konfiguracja

_Home Assistant_ ma naprawdę sporo funkcji, więc omówienie wszystkich w ramach jednego wpisu jest raczej niemożliwe. Z uwagi na to skupię się tylko na dwóch rzeczach - **aktualizacjach** i **dodawaniu nowych urządzeń**. Pozostałe funkcje będą przeze mnie omawiane przy okazji kolejnych wpisów, w których na pewno wielokrotnie będę wracał do _HA_.

**Aktualizacje**

_Home Assistant OS_ **sam ogarnia sobie czy istnieją nowe aktualizacje** czy nie i informuje nas o tym. Mowa tutaj nie tylko o aktualizacjach samego systemu, ale także poszczególnych urządzeń o ile ta funkcja jest dla nich obsługiwana. Jeżeli _HAOS_ wykryje, że jest nowa aktualizacja to informacja o tym pojawi się w dwóch miejscach. Pierwsze miejsce to sam szczyt _Ustawień_, gdzie wyświetlona zostanie lista komponentów, które można zaktualizować. Drugie miejsce jest nieco głębiej, bo aby się tam dostać trzeba pokonać następującą ścieżkę - _Ustawienia -> System -> Aktualizacje_.

![](/images/haakt1.png)
    
![](/images/haakt2.png)
    
![](/images/haakt3.png)
    
![](/images/haakt4.png)
    

Jeżeli chodzi o sam proces aktualizacji to w zasadzie konieczne jest tylko naciśnięcie przycisku _Aktualizuj_ i odrobina cierpliwości. Oczywiście to ile tej cierpliwości musi być zależy od mocy sprzętu i prędkości połączenia internetowego.

![](/images/haakt5.png)
    
![](/images/haakt6.png)
    

**Dodawanie nowych urządzeń**

_Home Assistant_ co jakiś czas skanuje sieć lokalną w poszukiwaniu nowych urządzeń. Gdy wykryje takowe to wysyła _Powiadomienie_, w którym daje skrót do dodania go do swojego systemu smart home.

![](/images/hanowe01.png)
    
![](/images/hanowe02.png)
    

Niestety nie zawsze to działa lub nie działa od razu po połączeniu nowego urządzenia, więc pokażę jak to zrobić od początku zgodnie ze sztuką, tj. w taki sposób, który zadziała zawsze. Przechodzimy do listy wszystkich urządzeń podłączonych do naszego _Home Assistant_. Dostępna jest ona w _Ustawienia -> Urządzenia oraz usługi -> zakładka (na górze) Urządzenia_. W prawym dolnym rogu znajduje się przycisk _Dodaj urządzenie_. Pojawi nam się okienko, w którym musimy wyszukać nowe urządzenie po nazwie marki. W prezentowanym przypadku wyszukuję frazę "shelly".

![](/images/hanowe1.png)
    
![](/images/hanowe2.png)
    
![](/images/hanowe3.png)
    
![](/images/hanowe4.png)
    

Od tego momentu są dwie możliwości. Jeżeli _HA_ da radę sam odkryć nowe urządzenie to od razu pojawi się propozycja, którą wystarczy jedynie wybrać z listy i potwierdzić swój wybór.

![](/images/hanowe5.png)
    
![](/images/hanowe6.png)
    

Jeżeli _HA_ jednak nie wykryje nowego urządzenia to zostaniemy poproszeni o wskazanie jego adresu IP i portu, pod którym znajduje się interfejs do jego zarządzania. Po podaniu tych danych naciskamy przycisk _Zatwierdź_.

![](/images/hanowe7.png)

Jeżeli wszystko przebiegło pomyślnie to dostaniemy potwierdzenie, że utworzono konfigurację dla nowego urządzenia. Ostatni krok to wskazanie do jakiego obszaru ma ono zostać przypisane. Obszary są w pełni definiowane przez użytkownika. Niektórzy dzielą cały system na pokoje, czyli np. na obszary salon, kuchnia, sypialnia itd. Ja podszedłem do tematu trochę inaczej i dla mnie wszystkie moduły przekaźnikowe _Shelly_ są w obszarze _Oświetlenie_, bo chcę nimi zarządzać jako jedną grupą. Kończymy cały proces naciśnięciem przycisku _Zakończ_.

![](/images/hanowe8.png)

Gotowe! Nowe urządzenie dodane.

![](/images/hanowe9.png)

## Podsumowanie

Jak pewnie już udało Ci się zauważyć _Home Assistant_ to naprawdę potężne narzędzie. Do tego ma wiele zalet, z których najważniejszą dla mnie jesy nakierowanie na prywatność i bezpieczeństwo danych użytkownika. Nie ma drugiego takiego produktu na rynku, a przynajmniej ja nic nie wiem o istnieniu takiego.
