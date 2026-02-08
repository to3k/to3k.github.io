---
title: "Terminal z Proxmox - ambitny serwer domowy"
date: 2023-03-25
categories: 
  - "poradniki"
  - "self-hosting"
tags: 
  - "allegro"
  - "cpu"
  - "dellwyse"
  - "fujitsu"
  - "intelnuc"
  - "maszynawirtualna"
  - "minipc"
  - "opensource"
  - "proxmox"
  - "ram"
  - "raspberrypi"
  - "selfhosted"
  - "terminal"
  - "virtualmachine"
  - "vm"
image: "/images/proxmox1.png"
---

[🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/terminal-proxmox-eng/)

Spis treści:
* TOC
{:toc}

Omówiłem już jak dość prosto i stosunkowo niskim kosztem ogarnąć sobie serwer domowy bazując na platformach _Raspberry Pi_ i podobnych. Istnieją jednak również inne, nieco bardziej ambitne, rozwiązania. Przykładem może być serwer domowy zbudowany w oparciu o urządzenia, które ze względu na swoją specyfikę lubię nazywać _terminalami_. Takie urządzenia to np. [_Intel NUC_](https://www.intel.pl/content/www/pl/pl/products/details/nuc.html). Oczywiście taki _NUC_ w sensownej konfiguracji będzie dość sporo kosztował, szczególnie w odniesieniu do _RPi_. **Jednak jest wyjście, aby nie zrujnować swojego portfela!** Jest nim zakup sprzętu poleasingowego, powystawowego lub po prostu używanego. Jest wiele firm, które oferują sprzęt tego typu z drugiej ręki, dając przy tym gwarancję nawet na 6 miesięcy. Sporo ciekawych ofert można znaleźć chociażby na _Allegro_.

## Terminal vs Raspberry Pi

Postanowiłem obrazowo przedstawić _zady_ i _walety_ _terminali_ względem opisywanego wcześniej _Raspberry Pi_.

### Zalety

- Mocniejsze procesory

- Procesory w architekturze x86 (a nie tylko ARM)

- Procesor montowany w normalnym socket'cie, np. LGA 1150, a nie wlutowany na płycie głównej, co pozwala na jego wymianę

- Więcej RAMu (rozsądne cenowo są rozwiązania nawet z 16GB)

- Zwarta bryła ze zintegrowanym chłodzeniem i przestrzenią na dyski

- Można bardziej zaawansowana wirtualizacja

### Wady

- Cena, szczególnie za sensowną specyfikację

- Trzeba raczej celować w sprzęt używany, żeby nie zbankrutować

- Większe zużycie energii

- Kultura pracy - chłodzenie aktywne (wentylator)

- Większy rozmiary

Jak widać to rozwiązanie ma swoje zalety, ale ma też wady. Jednak jeżeli ktoś na poważnie chce wejść w self-hosting to myślę, że i tak skończy się to na zakupie _terminala_.

## Sensowne parametry

Ze względu na stosunek ceny do jakości, bardzo dużą popularnością cieszy się _Dell Wyse 5070_. Jeżeli stawiamy na optymalizację budżetu to zdecydowanie polecam pochylić się nad tą opcją. Jednakże według mnie 8GB RAMu to zbyt mało. Jakbym miał określić moje **minimalne parametry**, od których zaczynamy mówić o naprawdę fajnym sprzęcie, to będą to:

- **4 rdzeniowy** procesor w architekturze x86,

- **16GB** RAM,

- dysk **SSD** **512GB**,

- port Ethernet (RJ45) w standardzie **1 Gbps**.

To takie minimum, które pozwoli uruchomić całkiem niezłe 4 maszyny wirtualne (oczywiście to tylko przykład, bo zasoby można dzielić wedle uznania), z których każda dostanie po jednym dedykowanym rdzeniu i 4GB RAMu. Będzie to podobne doznanie do posiadania czterech Raspberry Pi 4B, a cena wcale nie będzie tak bardzo odjechana, co za chwilę pokażę.

## Na własnym przykładzie

Jako przykład najlepiej mi będzie przytoczyć to co sam nabyłem jakiś czas temu. Swój _terminal_ kupiłem jako powystawowy na _Allegro_. Jakby ktoś był zainteresowany to dla ułatwienia przygotowałem [link do _Allegro_](https://allegro.pl/kategoria/komputery-stacjonarne-486?order=d&monitor=brak&liczba-rdzeni-procesora=4&liczba-rdzeni-procesora=6&liczba-rdzeni-procesora=8&liczba-rdzeni-procesora=32&wielkosc-pamieci-ram=16%20GB&wielkosc-pamieci-ram=24%20GB&wielkosc-pamieci-ram=32%20GB&wielkosc-pamieci-ram=64%20GB&typ-dysku-twardego=SSD&typ-dysku-twardego=SSD%20\(M.2\)&typ-dysku-twardego=brak%20dysku&offerTypeBuyNow=1&price_to=1000) z odpowiednio wybranymi filtrami wyszukiwania, który może stanowić dobrą bazę do rozpoczęcia poszukiwań. Znajdują się tam też komputery znacznie większego formatu (wielkości normalnego PC) niż rozwiązania, o których rozmawiamy, bo spełniają one wymagania sprzętowe określone w filtrach wyszukiwania, a nie da się ich odfiltrować w żadne sposób pod kątem rozmiaru czy nawet typu, więc niestety tą część roboty musisz, drogi Czytelniku, wykonać sam. Na marginesie, nie jest to link w żaden sposób afiliacyjny, więc **nie mam żadnych benefitów** z tego, że go tutaj wkleiłem.

Wracając do tematu, _terminal_ jaki kupiłem to **_Fujitsu Q920_** wyposażony w **4-rdzeniowy procesor** Intel i5-4590T, a więc leciwa ale dalej szanowana 4-ta generacja, o taktowaniu 2.0GHz (max. 3.0 GHz) i **16GB pamięci RAM** (to było chyba dla mnie najważniejsze). Zapłaciłem za niego w granicach **630 zł**, ale było to jakiś czas temu, więc ceny obecnie mogą być nieco innego, jednak rząd wielkości powinien zostać taki sam, a jest to już pewnego rodzaju cenna informacja. Musiałem do niego dokupić jeszcze **dysk SSD** w standardzie rozmiarowym 2.5" i **pojemności 512GB** (stwierdziłem, że tyle mi wystarczy). Tutaj warto podkreślić, że postanowiłem nieco dopłacić do dysku typu _SLC_, który charakteryzuje się większą wytrzymałością, dlatego jest dedykowanym rozwiązaniem do zastosowań serwerowych. _SLC_ wiąże się też z nieco wyższą kwotą, ale obecne ceny pamięci są tak niskie, że spokojnie z takim dyskiem zmieściłem się w **200 zł.**

## Instalacja Proxmox

W mojej ocenie **najlepszym co można zainstalować** jako system operacyjny dla takiego _terminala_ jest **_Proxmox_**. Jest to **bezpłatne** środowisko do wirtualizacji o **otwartym kodzie źródłowym**, działające w oparciu o system _Debian_. W [jednym z poprzednich wpisów](https://blog.tomaszdunia.pl/docker/) pisałem o _Dockerze_. _Proxmox_ to taki bardziej zaawansowany _Docker_, który pozwala stawiać nie tyle kontenery (podsystemy) z usługami, co całe pełnoprawne systemy operacyjne. To bardziej jak uruchamianie wielu płytek _Raspberry Pi_ w jednym _terminalu_. _Proxmox_ ma też swoje wymagania, na które trzeba zwrócić uwagę przy zakupie _terminala_, główne z nich to:

- 64 bitowa architektura procesora,

- wsparcie dla wirtualizacji (w przypadku procesorów Intela - Intel-VT, a dla AMD - AMD-V)

Instalacja jest banalnie prosta i analogiczna do tej, którą opisałem [we wpisie o konfiguracji serwera domowego](https://blog.tomaszdunia.pl/serwer-domowy) opartego o platformy _Raspberry Pi_ i podobne. W skrócie, pobieramy obraz _Proxmox_ ze [strony twórców](https://www.proxmox.com/en/downloads/category/iso-images-pve) i wgrywamy na pendrive przy pomocy programu [_balenaEther_](https://www.balena.io/etcher), tworząc tym samym _bootowalne USB_, które następnie wpinamy do _terminala_ i uruchamiamy go. Tutaj sytuacja wygląda trochę inaczej, bo nie możemy wykonać tzw. _headless setup_ tak jak to robiliśmy w przypadku _RPi_. Niezbędne nam będą przynajmniej monitor i klawiatura. Instalacja _Proxmox_ jest dość prosta, ale w skrócie hasłowo przejdę przez cały proces.

1. **Ekran powitalny**, na którym wybieramy oczywiście _Install Proxmox VE._

3. Akceptacja **licencji**.

5. Wybór **dysku**, na który ma zostać zainstalowany.

7. Wybór lokalizacji (państwo/miasto) i **strefy czasowej**.

9. Ustawienie **hasła administratora** oraz adresu e-mail, na który będą przychodziły wszystkie istotne komunikaty związane z naszym serwerem.

11. **Ustawienia sieciowe** - tutaj dla każdego będzie to wyglądało inaczej. Najpierw wybieramy _kartę sieciową_ jaka ma być wykorzystana (istotne, jeżeli nasz serwer posiada więcej niż jedną kartę, nie muszę chyba mówić, że zalecane jest podłączenie serwera poprzez LAN bezpośrednio do naszego routera i wybranie karty sieciowej odpowiadającej interfejsowi kablowemu, a nie karty odpowiedzialnej za komunikację bezprzewodową). Następnie dość istotne jest ustawienie odpowiedniego _Hostname_, który będzie identyfikatorem naszego serwera w sieci lokalnej. Później już należy tylko skontrolować czy automatycznie podany _adres IP w sieci lokalnej_, _brama dostępowa_ (_gateway_) i _serwer DNS_, obsługujący nasz ruch sieciowy, zostały wskazane prawidłowo. _Proxmox_ zawsze próbuje sam ustalić wartości domyślne, które w razie potrzeby należy skorygować.

13. **Ekran podsumowujący** wszystko co ustawiliśmy. Warto sprawdzić wszystko jeszcze raz i jeżeli jest OK to **rozpocząć instalację**.

15. Trzeba się niestety uzbroić w **cierpliwość**, bo proces nie jest błyskawiczny. Dużo też zależy od mocy naszego urządzenia i chociażby szybkości dysku.

17. Po zakończeniu instalacji (jeżeli nie odznaczyliśmy tej opcji to) urządzenie powinno się samo **zrestartować**.

19. Prawidłowo uruchomiony serwer powinien wyświetlić na monitorze następujący komunikat:

> Welcome to the Proxmox Virtual Environment. Please use your web browser to configure this server - connect to:
> 
> https://\[adres ip serwera\]:8006/

Zgodnie z treścią komunikatu wystarczy przepisać podany adres i na innym komputerze wejść do panelu zarządzania środowiskiem _Proxmox_. W tym momencie można też odłączyć monitor i klawiaturę od serwera, bo nie będą one już potrzebne. Dodatkowo nie trzeba się martwić o ostrzeżenia przeglądarki, które zostaną prawdopodobnie wyświetlone po wejściu na podany adres. Chodzi o to, że używamy połączenia _HTTPS_, a nasz serwer nie posiada _certyfikatu SSL_, więc przeglądarka zgłosi, że coś jest nie tak i ostrzeże nas o tym ogromnym komunikatem. Panel zarządzania naszym serwerem będzie dostępny jedynie z poziomu sieci lokalnej, więc nie ma potrzeby bawienia się w jakiekolwiek certyfikaty, a wszelkie komunikaty tego typu należy przeklikać przyciskami o treści _znam ryzyko i chcę je zignorować_ lub coś w tym stylu.

## Ciąg dalszy nastąpi...

Niestety ten wpis zaczął się robić niewygodnie długi, a ja chciałbym przekazać jeszcze sporo informacji, więc na tym etapie zatrzymuję się i zapraszam do [kolejnego wpisu](https://blog.tomaszdunia.pl/proxmox-vm/), w którym opiszę **jak uruchomić pierwszą maszynę wirtualną** w świeżo zainstalowanym środowisku _Proxmox_.
