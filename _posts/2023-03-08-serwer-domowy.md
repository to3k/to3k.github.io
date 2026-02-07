---
title: "Serwer domowy niskim kosztem"
date: 2023-03-08
categories: 
  - "ipad-only"
  - "poradniki"
  - "self-hosting"
tags: 
  - "arm"
  - "debian"
  - "ipadonly"
  - "linux"
  - "odroid"
  - "ovh"
  - "raspberrypi"
  - "ssh"
  - "termius"
  - "ubuntu"
  - "vps"
image: "/images/ssh.png"
---

[🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/serwer-domowy-eng/)

W tym wpisie opiszę jak stworzyć domowy serwer, który będzie idealnym pomocnikiem (wsparciem, czy może też uzupełnieniem) dla _iPada_. Nie jest to do końca zgodne z ideologią _#iPadOnly_, bo zakłada używanie nie tylko samego tableta, ale potraktujcie to jak relację pomiędzy Batmanem i Alfredem 😉

Ten wpis powstał w oparciu o mojego drugiego bloga - [odroid.pl](https://odroid.pl/blog/), który jest poradnikiem dla początkujących i ewentualnie średnio-zaawansowanych, który bardzo mocno skupia się na tematyce self-hosted, a konkretnie traktuje o tym jak stosunkowo niskim kosztem stworzyć swój mały serwer domowy, na którym można uruchomić kilka(naście) bardzo przydatnych narzędzi i usług. Mimo niedomknięcia jeszcze wszystkich tematów, które zaplanowałem opisać, na odroid.pl nie publikowałem już jakiś czas. Niemniej jednak wiedza tam zawarta jest cały czas aktualna i może być dla niektórych przydatna. Będę część z tych materiałów używał tutaj i do nich nawiązywał, a także planuję tutaj dokończyć tematy, których tam opisać mi się nie udało. Wiedza, którą w formie pigułki zawrę w tym wpisie jest bardziej rozwinięta na [odroid.pl](https://odroid.pl/blog/), więc jeżeli którekolwiek z poniższych zagadnień będzie niejasne to polecam odwiedzić także drugiego blog.

## Potrzebny sprzęt

Zaczynamy od zaopatrzenia się w sprzęt:

1. **Raspberry Pi lub równoważna alternatywa** - tutaj polecam płytki o specyfikacji podobnej do RPi 4B w wersji z 4GB RAMu, ODROID C4 lub mocniejsze (grunt to 4 rdzeniowy procesor i nie mniej niż 4 GB RAMu),

3. **Obudowa** - nie będzie tutaj za wielkiego wyboru, bo każda płytka ma 2-3 dedykowane obudowy, więc po prostu wybierzcie najtańszą,

5. **Chłodzenie** - przeważnie jest w zestawie z samą płytką lub obudową do niej, nie pchajcie się w chłodzenie inne niż pasywne (radiator aluminiowy), bo po pierwsze nie przewiduję aż takiego obciążenia, po drugie nawet pod obciążeniem te płytki nie grzeją się ekstremalnie, a po trzecie chłodzenie pasywne to komfort akustyczny nieosiągalny nawet przy wentylatorze najwyższej klasy,

7. **Zasilacz** - zwróć uwagę na typ złącza, napięcie zasilania i maksymalny prąd jaki potrzebuje płytka, do którego przy wyborze zasilacza należy dodać przynajmniej 1A, aby mieć zapas zasilania dla ewentualnych peryferiów (np. dyski zewnętrzne), które będziemy chcieli podpiąć w przyszłości,

9. **Karta microSDXC** - pojemność 64GB na start wystarczy w zupełności, decyzję o zakupie większej pozostawiam już do oceny indywidualnej,

11. **Kabel RJ-45 (Ethernet)** - jeżeli nie macie to będzie potrzebny do wpięcia serwera bezpośrednio w router domowy.

Zestaw o powyższej specyfikacji **nie powinien kosztować więcej niż 500 zł** i to tylko ze względu na szalejące w ostatnim czasie ceny. Normalnie Raspberry Pi można było kupić sporo taniej niż obecnie. Więcej na temat doboru sprzętu możecie przeczytać [tutaj](https://odroid.pl/blog/odroid-c4-zakup/).

## Czy to się w ogóle opłaca?

Policzmy czy posiadanie w domu serwera opartego o platformę RPi opłaca się bardziej niż wykupienie sobie VPSa (Virtual Private Server - czyli maszyny, która działa w serwerowni poza naszym domem).

Dla porównania weźmy najpopularniejszego w Polsce dostawcę tego typu rozwiązań - [OVH](https://www.ovhcloud.com/pl/vps/), gdzie za porównywalny do Raspberry Pi 4B serwer, z dwoma wirtualnymi rdzeniami (vCore), 4GB RAMu i dyskiem 80GB, przyszłoby nam płacić ok. **70 zł brutto miesięcznie**. Nie dajcie sobie zamydlić oczu cenami podanymi na stronie, bo po pierwsze to podane 45 zł to kwota netto, a po drugie obowiązująca tylko przez pierwszy miesiąc.

Jak to wygląda dla RPi? W tym przypadku ponosimy wyższy koszt początkowy, ale rozbijmy sobie to na miesiące i zobaczmy jak szybko nam się zwróci. Najpierw jednak należy uwzględnić koszt prądu, bo w tym przypadku urządzenie jest w naszym domu i wymaga zasilania, za które oczywiście płacimy. Dla łatwego rachunku i żeby uciąć wszelkie dyskusje weźmy przypadek najgorszy, w którym serwer będzie chodził cały czas na maksymalnej mocy. Producent malinki dla modelu 4B zaleca zastosowanie zasilacza o napięciu 5V i maksymalnym prądzie 3A, co w najgorszym przypadku daje nam moc na poziomie (5V x 3A =) 15W, a więc na godzinę będziemy zużywać 15 Wh. Przeliczmy to na kilowatogodziny, które są używane jako standardowa jednostka na rachunkach za prąd i pomnóżmy to razy 24 godziny, aby ustalić ile prądu pójdzie nam na dobę - (0.015 kWh x 24 h =) 0.36 kWh. Spojrzałem na moje historyczne rachunki za prąd i z uwzględnieniem wszystkich dodatkowych kosztów (typu przesył itp.) średnio za kilowatogodzinę płacę jakieś 0.81 zł i to już po tych legendarnych podwyżkach cen prądu, bo wcześniej było to nie więcej niż 60 groszy... Kontynuując kalkulację weźmy teraz zużycie dobowe razy średnia cena i razy 30 dni, co da nam **miesięczny koszt** - (0.36 kWh x 0.81 zł x 30 dni =) **8.75 zł**.

Reasumując, VPS miesięcznie jest ok. 8 razy droższy, tj. każdego miesiąca VPS wychodzi o ponad 60 zł drożej niż koszt prądu do zasilania serwera działającego lokalnie. Uwzględniając teraz cenę początkową podzespołów, na poziomie 500 zł, można łatwo policzyć, że zwrot następuje już po 8 miesiącach, a później zysk jest już wykładniczy.

## Wgrywamy system

Ja jestem zwolennikiem systemu Ubuntu, ale każdy może wybrać jaki preferuje. Na RPi jest mnóstwo dedykowanych obrazów systemów dla praktycznie każdej dystrybucji, a jak jest dla RPi to będzie działać też na alternatywach jak ODROID. Jedyne na co trzeba zwrócić uwagę to fakt, że te płytki działają w oparciu o architekturę ARM i trzeba na to zwrócić uwagę wybierając wersję systemu.

Załóżmy, że wybraliśmy już system, więc trzeba go wgrać na kartę microSD, do tego celu przeważnie używam programu o nazwie [balenaEther](https://www.balena.io/etcher), bo jest on dostępny na każdy system. Jest banalnie prosty w użyciu, więc nie będę szczegółowo opisywał procesu wgrywania systemu na kartę, bo odbywa się poprzez naciśnięcie dosłownie 3 przycisków (wybór obrazu, wybór nośnika, flash'uj… gotowe!).

Więcej szczegółów o tym znajdziecie [tutaj](https://odroid.pl/blog/odroid-instalacja-ubuntu/).

## Nawiązujemy połączenie SSH

Konfigurację możemy przeprowadzić na dwa sposoby: podpinając monitor i klawiaturę lub tzw. **headless setup poprzez połączenie _SSH_**. Do tego drugiego potrzebujemy drugiego komputera (hosta), ale za to nie potrzebujemy żadnych peryferiów.

Do nawiązania połączenia _SSH_ w pierwszej kolejności musimy ustalić adres nowo uruchomionego serwera w naszej sieci lokalnej. Dokładny opis jak to zrobić, dla początkujących, znajdziecie [tutaj](https://odroid.pl/blog/odroid-ssh/). Następnie będziemy potrzebować login i hasło domyślnego użytkownika. Informacje te są zawarte w dokumentacji dystrybucji, której obraz pobraliście. Przykładowo może to być:

- _root_:_(brak hasła)_ - standard dla Debiana

- _pi_:_raspberry_ - dla Raspberry Pi

- _odroid_:_odroid_ - dla ODROIDa

Z uwagi na _#iPadOnly_ hostem w moim przypadku jest oczywiście _iPad_, a swoimi serwerami zarządzam z poziomu aplikacji _[Termius](https://apps.apple.com/pl/app/termius-terminal-ssh-client/id549039908)_, w której wystarczy jedynie utworzyć nowy tunel i wprowadzić powyżej zebrane informacje. Jeżeli ktoś nie chce używać _Termiusa_ to może to samo osiągnąć korzystając z dowolnego terminala i komendy:

```bash
ssh pi@192.168.1.69
```

Gdzie _pi_ i _192.168.1.69_ należy zastąpić adekwatnymi dla swojego przypadku danymi.

## Ciąg dalszy nastąpi…

Serwer kupiony, system zainstalowany i udało się z nim nawiązać połączenie, a więc wszystko działa jak należy. W [następnym wpisie](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja/) zajmiemy się podstawową konfiguracją, czyli fundamentalnymi działaniami, które należy wykonać na każdym świeżo postawionym serwerze.
