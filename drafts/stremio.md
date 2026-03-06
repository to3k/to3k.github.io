---
layout: post
title: "Stremio"
published: true
categories: 
  - "filmy-i-seriale"
  - "poradniki"
  - "przemyslenia"
tags: 
  - "stremio"
  - "read-debrid"
  - "comet"
  - "mediafusion"
  - "torrentio"
  - "netflix"
  - "hbo"
  - "disney"
  - "skyshowtime"
  - "apple-tv"
  - "amazon-prime"
  - "streaming"
  - "tv"
  - "series"
  - "movies"
  - "seriale"
  - "filmy"
image: "/images/stremio.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/TYTUŁ-eng/)

Spis treści:
* TOC
{:toc}

## Wstęp

Stremio to dla mnie jedno z największych **odkryć końcówki 2025 roku**. Choć początkowo podchodziłem do tematu sceptycznie, platforma ta całkowicie zmieniła sposób, w jaki konsumujemy media w domu. Najtrudniejszą częścią całego procesu było przekonanie żony do **porzucenia znanych i wygodnych aplikacji**. Gdy jednak zobaczyła, jak to działa w praktyce i że wszystko mamy w jednym miejscu, decyzja mogła być tylko jedna: **zrezygnowaliśmy z subskrypcji** wszystkich platform streamingowych, które do tej pory opłacaliśmy. Finał jest taki, że teraz to moja żona częściej korzysta ze Stremio niż ja.

Jeśli zastanawiasz się, jak uwolnić się od rosnących kosztów VOD bez utraty wygody, to właśnie o tym będzie ten wpis.

## Czym jest Stremio

Stremio to **darmowa aplikacja** typu media center (z ang. centrum multimedialne), która służy jako hub dla treści wideo. Sam w sobie program jest jedynie odtwarzaczem z pustą biblioteką. Dopiero po zainstalowaniu odpowiednich rozszerzeń (dodatków) zamienia się w potężne **narzędzie agregujące filmy, seriale, telewizję na żywo czy podcasty** z różnych źródeł w jednym, niezwykle czytelnym i nowoczesnym interfejsie.

## Różnice względem klasycznych serwisów VOD

Klasyczne serwisy (jak Netflix, HBO, Disney+ itd.) posiadają własne serwery i zamknięte biblioteki, do których dostęp wymaga opłacania **miesięcznego abonamentu**. Stremio nie posiada własnych treści. Działa jak **wyszukiwarka i odtwarzacz** – Ty decydujesz, z jakich źródeł (dzięki dodatkom) aplikacja ma pobierać (lub streamować - odtwarzać w locie) media. Zamiast skakać po pięciu różnych aplikacjach w poszukiwaniu konkretnego filmu, wpisujesz tytuł w Stremio i od razu widzisz dostępne źródła. Gwarantuję Ci, że nie uda Ci się wskazać mi jakiegoś materiału, który jest dostępny na dowolnym serwisie streamingowym, a nie znajdę go na Stremio.

## Różnice względem Kodi, Plex i Jellyfin

To najczęstsze pytanie, jakie otrzymywałem na Mastodonie pod postami o Stremio. Różnice są fundamentalne:
- **Plex / Jellyfin** - To oprogramowanie dla osób, które już posiadają własne pliki wideo na dysku. Wymagają postawienia własnego serwera (np. na NAS), który będzie te pliki transkodował i udostępniał urządzeniom końcowym (telewizor, tablet, smartfon czy laptop).
- **Kodi** - To kombajn o ogromnych możliwościach, ale ciężki, trudny w konfiguracji i często wolny na słabszych urządzeniach (np. tanich przystawkach TV). Konfiguracja dodatków w Kodi jest lokalna – jeśli zmienisz urządzenie, musisz ustawiać wszystko od nowa.
- **Stremio** - To takie Kodi, ale lekkie i banalnie proste. Dodatki instaluje się na koncie w chmurze, a nie na urządzeniu. Instalujesz dodatek na komputerze, a po zalogowaniu na telewizorze wszystko już tam jest i działa. Stremio nie wymaga też trzymania plików na własnych dyskach – opiera się na streamingu.

## Podstawowa konfiguracja

Aby rozpocząć oglądanie swojego pierwszego odcinka serialu przez Stremio, wystarczy kilka minut.

### Instalacja na różnych urządzeniach (TV, komputer, telefon)

Aplikacja jest **dostępna na większość popularnych platform** (Windows, macOS, Linux, Android, Android TV, wybrane systemy Smart TV). Pobierzesz je stąd: **[Oficjalna strona Stremio - Pobieranie](https://www.stremio.com/downloads)**.

### Wersja przeglądarkowa Stremio Web

Jeśli nie chcesz lub nie możesz zainstalować aplikacji na danym urządzeniu, możesz skorzystać z wersji w przeglądarce pod adresem [web.stremio.com](https://web.stremio.com/).

### Niezbędne dodatki

Na start wystarczą Ci trzy kluczowe rozszerzenia. Instaluje się je zazwyczaj poprzez kliknięcie linku konfiguracyjnego na ich stronach i przekierowanie do aplikacji Stremio:
* **[Comet](https://comet.elfhosted.com/configure) / [MediaFusion](https://mediafusion.elfhosted.com/app)** - główne dodatki wyszukujące źródła wideo (torrenty), nie trzeba się decydować na jeden, bo instalacja dwóch zapewnia redundancję (można jeszcze rozważyć [Torrentio](https://torrentio.org/), ale ostatnio kiepsko ze stabilnością tego dodatku).
* **[OpenSubtitles](https://opensubtitles-v3.strem.io/)** - oficjalny dodatek (zazwyczaj zainstalowany domyślnie), który automatycznie dobiera napisy w wybranym języku.

### Real-Debrid albo VPN

Ze względów prawnych potrzebujesz jednej z dwóch poniższych opcji:
1. **VPN** - ukryje Twój adres IP,
2. **Real-Debrid** - usługa, która robi za pośrednika, tj. pobiera i udostępnia plik w ramach P2P, a nam tylko go streamuje.

Obie z tych opcji opiszę dokładniej w dalszej części wpisu.

## Stremio a legalność

> **UWAGA: Korzystanie ze Stremio w sposób, który opiszę w dalszej części tego wpisu jest balansowaniem na granicy legalności. Jeżeli jest to zgodne z Twoim sumieniem to wiedz, że robisz to na własną odpowiedzialność. Jeżeli nie przebywasz na terenie Polski to dwa razy sprawdź jak wyglądają przepisy w zakresie korzystania z sieci P2P na danym terytorium.**

### Czy używanie Stremio jest legalne?

Samo pobranie i używanie Stremio, jak i oglądanie treści z oficjalnych dodatków (np. klasyki w domenie publicznej), jest w 100% legalne. Problem pojawia się w momencie instalacji **dodatków społecznościowych opartych na torrentach**. W takim przypadku Stremio opiera się na **protokole BitTorrent (P2P)**. Oznacza to, że **oglądając film, jednocześnie go udostępniasz**, co w wielu krajach wiąże się z **surowymi karami finansowymi za naruszenie praw autorskich**. W Polsce nie jest to taki oczywisty temat, ale maksymalnie można go uprościć do - **pobieranie do użytku własnego jest legalne, udostępnianie już nie**. Wydaje mi się, że nie mija się to z prawdą.

### VPN

W przypadku posiadania VPN sprawa jest o tyle łatwa, że dobry VPN (o ile w ogóle można zaufać któremukolwiek z nich) **powinien zamaskować nasz realny adres IP** i w ten sposób uchronić nas od ewentualnych konsekwencji prawnych.

Jeżeli miałbym coś polecić (choć niechętnie) to byłyby to (kolejność nie jest przypadkowa):
- **[Mullvad](https://mullvad.net/pl)**,
- **[ProtonVPN](https://protonvpn.com/)**,
- **[AirVPN](https://airvpn.org/)**.

### Real-Debrid

To znacznie lepsze, tańsze i niejednokrotnie szybsze rozwiązanie niż VPN. **[Real-Debrid](https://real-debrid.com/)** to usługa, która pobiera torrenty na swoje serwery, a następnie przesyła je do Ciebie bezpośrednio, **bezpiecznym, szyfrowanym połączeniem (HTTPS)**.
- Twoje IP nigdzie nie jest widoczne w sieci P2P (**nic nie udostępniasz**).
- Szybkość zależy tylko od Twojego łącza – brak problemów z buforowaniem, nawet przy plikach 4K o wadze 80 GB.

Koszt to około **3-4 euro miesięcznie** (w zależności od długości zobowiązania), a do tego zbiera się jeszcze punkty, które co jakiś czas można wymienić na darmowy okres premium. Zdecydowanie warto. Oczywiście nie jest to jedyne rozwiązanie tego typu, ale tylko to osobiście przetestowałem i mogę polecić z czystym sumieniem.

### Jak pozyskać klucz Real-Debrid (API Token)

Aby połączyć Stremio z kontem Real-Debrid, większość dodatków będzie wymagała podania specjalnego **klucza API**. Jest to Twój prywatny identyfikator, którego **nie powinieneś nikomu udostępniać**. 

Oto kroki jak go zdobyć:
1. **Zaloguj się** na swoje konto na stronie [Real-Debrid](https://real-debrid.com/).
2. Upewnij się, że masz **wykupioną subskrypcję** Premium na platformie Real-Debrid.
3. Po zalogowaniu **przejdź bezpośrednio pod [ten ukryty adres](https://real-debrid.com/apitoken)**. Token jest też dostępny w zakładce **My Devices**.
4. Na stronie zobaczysz długi ciąg znaków w sekcji **API Private Token**. **Skopiuj** go – to właśnie Twój klucz API, który przyda nam się podczas konfiguracji dodatków opisanej w dalszej części wpisu.

## Dodatki

To właśnie one stanowią o sile Stremio.

### Jak działają dodatki

Dodatki w Stremio nie są pobierane na Twój dysk jako fizyczne pliki (jak w Kodi). Działają po stronie zewnętrznych serwerów internetowych. Twoja aplikacja Stremio wysyła do nich zapytanie - np. `Mam film X, jakie masz do niego linki i napisy?`, a dodatek zwraca gotowe wyniki. Dzięki temu aplikacja działa błyskawicznie nawet na najtańszych telewizorach.

### Oficjalne vs społecznościowe

* **Oficjalne** - Tworzone przez twórców Stremio (np. YouTube, OpenSubtitles, Public Domain Movies). Są w pełni legalne i bezpieczne, ale nie dają dostępu do najnowszych kinowych hitów.
* **Społecznościowe (Community Addons)** - Tworzone przez niezależnych deweloperów. To one integrują Stremio z sieciami P2P i serwisami typu Real-Debrid. 

### Instalacja i konfiguracja Comet

Comet to jeden z najnowszych i najszybszych dodatków wyszukujących (alternatywa dla Torrentio), który świetnie współpracuje z Real-Debrid i oferuje bardzo wysoką jakość linków. To obecnie **mój numer jeden** po tym jak kilka wieczorów z rzędu miałem problemy z Torrentio.

1. Wejdź na **[stronę konfiguracyjną dodatku Comet](https://comet.elfhosted.com/configure)**.
2. W polu **Resolution** proponuję wybrać:
    - **4K UHD 2160p**,
    - **QHD - 1440p**,
    - **FHD - 1080p**,
    - **HD - 720p**.
3. W **Max Results Per Resolution** i **Max Size (GB)** zostawmy **0**, co oznacza, że nie chcemy limitu ilości wyników oraz rozmiaru plików. Jeżeli masz średnie połączenie internetowe i wiesz, że streaming filmu 4K nie będzie możliwy to możesz rozważyć ograniczenie parametru _Max Size_ do np. 3 GB.
4. Rozwijamy sekcję **Debrid Services**. Naciskamy przycisk **Add Debrid Service**. Z listy rozwijanej wybieramy **Real-Debrid** (lub innego dostawcę który został wybrany). W pole po prawej wklejamy **API Private Token**, który pozyskaliśmy w poprzednim rozdziale tego wpisu.
5. Rozwińmy sekcję **Language Settings**. W polu **Required Languages** mam wybrane tylko **English** i **Polish**, bo są to jedyne dwa języki, którymi posługuję się biegle i chcę, żeby Comet pokazywał mi tylko seriale/filmy, które posiadają jedną z tych dwóch ścieżek dźwiękowych. Polecam jeszcze zaznaczyć opcję **Remove Unknown Languages**, co odfiltruje materiały, w których metadanych nie określono dostępnych języków. Resztę zostawiam bez zmian względem domyślnego ustawienia.
6. W ostatniej sekcji **Advanced Settings** mam zaznaczone opcje **Show Cached Only** i **Remove Trash**. To pierwsze usuwa z wyników wyszukiwania wszystkie propozycje, które nie zostały jeszcze zacachowane (z ang. załadowane do bufora) przez Real-Debrid. Chodzi o to, że jak znajdziemy wystarczająco niszową produkcję to zamiast odcinka serialu otrzymamy wielki biały napis na czarnym tle mówiący o tym, że ten materiał nie został jeszcze zacachowany przez Real-Debrid, ale jak poczekamy chwilę to za moment będzie on dostępny. Jest to największe kłamstwo w historii kłamstw, bo jeszcze nigdy w moim przypadku tak się nie stało, dlatego po prostu wywalam te materiały, których nie ma w buforze Real-Debrid.
7. Doszliśmy do końca konfiguratora i widzimy na samym dole trzy przyciski:
    - **Install** - przeniesie nas bezpośrednio do aplikacji Stremio odpowiedniej dla naszego urządzenia lub jeżeli takiej nie mamy to otworzy Stremio Web i w ten sposób zainstaluje nam dodatek skonfigurowany zgodnie z tym co wyklikaliśmy powyżej,
    - **Copy Link** - jego naciśnięcie spowoduje skopiowanie do schowka odpowiedniego, długiego linku, który zawiera wszystkie informacje na temat naszej konfiguracji, aby użyć tego linku należy przejść ręcznie do Stremio, zakładka Dodatki, nacisnąć Dodaj dodatek i wkleić ten link w pole do podawania adresu dodatku,
    - **Setup Kodi** - ten przycisk nie ma zastosowania w naszym przypadku.

### Instalacja i konfiguracja MediaFusion

MediaFusion to potężny kombajn, który potrafi dostarczyć filmy, seriale, a także wydarzenia sportowe i telewizję na żywo. Posiada zaawansowane opcje scrapowania, w tym treści z regionalnych trackerów. **Dla mnie to numer dwa**, czyli rezerwa na wypadek potknięcia Comet, co przez cały czas zdarzyło mi się może jeden raz. Konfiguracja jest bardzo podobna do Comet tylko poszczególne opcje są w innych miejscach.

1. Przejdź na **[stronę konfiguratora MediaFusion](https://mediafusion.elfhosted.com/configure)**.
2. W przeciwieństwie do Comet tutaj wszystko jest poukładane w zakładkach. Pierwszą, którą odwiedzamy jest **Provider**. Naciskamy przycisk **Add Streaming Provider**, z listy rozwijanej wybieramy Real-Debrid (lub inny wedle uznania), wpisujemy dowolny **Provider Name**. Teraz mamy dwie opcje - autoryzujemy się poprzez przycisk **Authorize Real-Debrid** i wykonanie krótkiej instrukcji, albo po prostu podajemy **API Private Token** w polu poniżej. Na koniec na dole mamy opcję **Only Show Cached Streams**, czyli tak jak w przypadku Comet włączamy opcję wyświetlania tylko zacachowanych materiałów przez Real-Debrid.
3. Następna zakładka, która nas interesuje to **Preferences**. W sekcji **Resolutions** polecam zostawić tylko: **4K**, **2160p**, **1440p**, **1080p** i **720p**. W **Quality Filter** polecam: **BluRay/UHD**, **WEB/HD** i **DVD/TV/SAT**. W **File Size Filters** możemy ustawić minimalną i maksymalną wielkość pliku (można też zostawić bez limitu) oraz ile ma być wyników na daną rozdzielczość i tutaj nie można podać 0, więc jeżeli nie chcesz mieć limitu to podaj jakąś wysoką liczbę. W **Preferred Languages** ustawiłem **English** i **Polish**. Reszta opcji w tej zakładce jest dla mnie nieistotna.
4. Pozostałe zakładki proponuję zostawić w domyślnej formie lub ewentualnie później w wolnej chwili zajrzeć do nich i może coś podkręcić.
5. Po dojściu do tego momentu szukamy fioletowego przycisku **Generate Install URL**, który znajduje się zarówno na górze jak i na dole konfiguratora. W rezultacie jego naciśnięcia pojawi nam się okienko z wygenerowanym długim linkiem z zakodowanymi wszystkimi naszymi ustawieniami. Wklejamy go w naszym Stremio tak samo jak w przypadku Comet.

### Instalacja i konfiguracja Torrentio

Torrentio to klasyk i chyba najpopularniejszy dodatek tego typu do Stremio, ale wydaje mi się, że jego popularność i przede wszystkim wystrzał popularności Stremio trochę mu zaszkodziły i jego serwery po prostu nie wytrzymały naporu. Liczę na to, że sytuacja się niedługo unormuje, ale póki co mam z tym dodatkiem najgorsze doświadczenia, więc jest **dopiero moim numerem trzy** jako rezerwa rezerwy.

1. Otwórz **[stronę konfiguratora Torrentio](https://torrentio.strem.fun/configure)**.
2. W sekcji **Providers** nie musisz nic zmieniać – domyślnie wyszukuje w najważniejszych miejscach.
3. Z listy rozwijanej **Sorting** polecam wybrać **By quality then seeders**, co posortuje nam wyniki najpierw pod względem jakości, a później tego ilu użytkowników sieci P2P deklaruje możliwość udostępnienia tego materiału.
4. W polu **Max Results per Quality** nie podajemy żadnej liczby, czyli zostawiamy **All results**. tj. nie limitujemy ilości wyników.
5. Na liście **Priority Language** zaznaczyłem tylko **Polish**. O dziwo nie ma tu angielskiego, ale zakładam, że jest wybierany domyślnie.
6. W sekcji **Exclude Resolutions** poprzez zaznaczenie wykluczamy dane rozdzielczości, więc zaznaczamy: **Unknown**, **Cam**, **Screener** i **480p**.
7. Jeżeli uważamy, że nasz internet to pociągnie to w **Video Size Limit** nie określamy limitu rozmiaru plików.
8. Na koniec najważniejsze, czyli **Debrid Provider**. Wybieramy z listy **RealDebrid** (lub inny wedle uznania) i podajemy **API Private Token**.
9. Na samym dole konfiguratora mamy duży fioletowy przycisk **Install**, który przeniesie nas do aplikacji Stremio lub do Stremio Web jeżeli nie mamy aplikacji, i zainstaluje nam dodatek. Natomiast poniżej dużego przycisku znajduje się maly odnośnik **Copy Link**, który wrzuci nam do schowka specjalny link z zakodowaną konfiguracją gotową do ręcznego wklejenia do naszego Stremio.

## Podstawowa obsługa

### Wyszukiwanie seriali i filmów

Wystarczy użyć **paska wyszukiwania** lub przeglądać ekran główny (zakładka "Discover" lub "Board"), który – jeśli zainstalowałeś odpowiednie **dodatki katalogujące** – będzie przypominał klasyczny interfejs jak Netflixa czy innych tego typu platform. Mi jako dodatek katalogujący wystarcza (póki co) domyślny **[Cinemeta](https://v3-cinemeta.strem.io/)**.

### Wybór odpowiedniego źródła / pliku źródłowego z listy

Po wybraniu określonego odcinka serialu wyświetli nam się lista dostępnych opcji. Na tej liście znajdują się wszystkie pozycje jakie zostały zescrapowane (zebrane) **ze wszystkich źródeł**, do których dostęp mają nasze dodatki - Comet, MediaFusion i Torrentio. Są one **posortowane** według dodatku, następnie rozdzielczości, ilości seederów lub rozmiaru itd. **Nie przejmuj się tym zbytnio**. **Po prostu kliknij** pierwszy lepszy jaki wpadnie Ci pod palec, a jeżeli coś będzie z nim nie tak (nie działa, słaba jakość, coś nie tak z dźwiękiem, nie ten język, brak napisów itd.) to po prostu włącz kolejną pozycję z listy.

![Zrzut ekranu Stremio lista seriali](/images/stremio1.png)

![Zrzut ekranu Stremio lista odcinków serialu Picard](/images/stremio2.png)

### Napisy

Stremio **automatycznie próbuje pobrać napisy** z dodatku OpenSubtitles w języku ustawionym w konfiguracji konta. W trakcie odtwarzania możesz kliknąć ikonę napisów i w locie **zmienić źródło, język lub poprawić synchronizację** (opóźnienie), jeśli napisy rozjeżdżają się z obrazem. Z doświadczenia mogę powiedzieć, że rozjazd napisów często wynika z tego, że są one przygotowane dla filmu / odcinka serialu, w którym nie ma sekcji Previously (z ang. w poprzednim odcinku). Natomiast często odcinki mają ten dodatkowy wstęp. Wtedy **wystarczy opóźnić** (ang. delay) napisy o daną ilość sekund, którą trwa ten fragment. W temacie napisów polecam także **zajrzeć do ustawień Stremio**, bo można tam ustawić **preferowany język napisów** (nie trzeba go zmieniać za każdym razem z X na polski), a także np. czarne lekko transparentne **tło** dla białych napisów itd. Wszystko w zależności jak będzie Ci najwygodniej.

### Ścieżki dźwiękowe

Jeśli dany plik posiada wiele ścieżek dźwiękowych (np. oryginalna i polski lektor), obok ikony napisów znajdziesz **ikonę audio**, pozwalającą **płynnie przełączać się między dostępnymi wersjami językowymi**.

### Synchronizacja

Stremio **synchronizuje informację pomiędzy różnymi urządzeniami** podpiętymi pod to samo konto. I nie mówię tutaj jedynie o bibliotece (ostatnio oglądane, zapisane na później) czy oznaczaniu obejrzanych już odcinków seriali / filmów, ale o tym, że oglądanie można zacząć na telefonie, przesiąść się na komputer, a **odtwarzacz automatycznie zacznie dokładnie w momencie, w którym skończyliśmy** na telefonie. Jest to o tyle szokujące, że można wybrać zupełnie inne źródła - np. na telefonie Comet, na komputerze MediaFusion, a Stremio i tak da sobie z tym radę. Ciekawi mnie jak to działa pod maską. **Stremio jest oprogramowaniem otwartoźródłowym**, więc możliwe, że kiedyś w wolnej chwili zajrzę do kodu.

## Śledzenie tego co się obejrzało (Trakt)

Dla osób, które lubią mieć pełną statystykę obejrzanych filmów i seriali, Stremio oferuje **integrację z serwisem [Trakt.tv](https://trakt.tv/)**. Po sparowaniu kont aplikacja **automatycznie odhacza obejrzane odcinki**. Sam osobiście z tego nie korzystam, bo od wieków jest ze mną aplikacja **TV Time**, a ta nie synchronizuje się (chyba) ze Stremio, ale **wiele osób bardzo chwali Trakt**, dlatego uznałem, że wspomnę o tym.

## Oszczędności

Wydaje mi się, że skutecznie pokazałem, że **Stremio to nie tylko oszczędność na miesięcznych opłatach za serwisy streamingowe, ale też wygoda i niezależność**. Mimo to z kronikarskiego obowiązku zobaczmy sobie ile tak naprawdę miesięcznie jesteśmy w stanie zaoszczędzić dzięki używaniu Stremio.

Sprawdziłem oferty wszystkich popularnych platform streamingowych:

| Serwis VOD | Najtańszy pakiet | Najdroższy pakiet) |
| :--- | :--- | :--- |
| ***Netflix*** | 33.00 zł | 67.00 zł |
| ***Max (HBO)*** | 24.92 zł | 41.58 zł |
| ***Disney+*** | 29.16 zł | 49.99 zł |
| ***SkyShowtime*** | 16.67 zł | 33.25 zł |
| ***Apple TV+*** | 34.99 zł | 34.99 zł |
| ***Amazon Prime*** | 5.75 zł | 5.75 zł |
| **SUMA** | **144.49 zł / msc** | **232.56 zł / msc** |

Zanim podsumuję powyższą tabelę chciałbym tylko powiedzieć, że są to **ceny aktualne na 6 marca 2026**. Do tego kwoty mogą wydawać się dziwne, ale to tylko dlatego, że **kombinowałem jak zrobić to najtaniej**, czyli w tabeli widać ceny miesięczne np. dla przypadku wzięcia na usługi na cały rok z góry, bo wtedy przeważnie jest taniej średnio o ok. 16% z tego co udało mi się zauważyć u więszkości dostawców.

Jak widać **miesięcznie zaoszczędzamy minimum 144.49 zł**, ale warto wspomnieć, że jest to kwota jaką należałoby płacić za pakiety najgorszej jakości, czyli przeważnie w **marnej rozdzielczości 720p lub wręcz z reklamami**... **Stremio powinno się porównywać raczej do kwoty 232.56 zł** bo taką jakość oferuje, czyli wszystko na maksa. Realny koszt Stremio to tylko subskrypcja Real-Debrid, która w najgorszym przypadku wynosi 4 euro, czyli ok. **17 zł**.

Pomijam już fakt, że **na Stremio można znaleźć produkcje, których nie sposób znaleźć na żadnej z tych sześciu wiodących platform**. Przykładem takiego serialu jest długo poszukiwany przez moją żonę **Schitt's Creek**, który **nie jest dostępny w ramach żadnego abonamentu** streamingowego w Polsce. Na pewno to nie jedyny taki przypadek.

## Podsumowanie
Stremio w połączeniu z Real-Debrid to rozwiązanie, które raz skonfigurowane, po prostu działa. Nie jest to już zabawa dla entuzjastów, ale **pełnoprawna, stabilna alternatywa dla rozdrobnionego rynku VOD**. Jeśli przerażają Cię **rosnące ceny abonamentów** i fakt, że ulubione **seriale są rozsiane** po pięciu różnych aplikacjach – daj Stremio szansę. Twoja żona (i portfel) prawdopodobnie Ci za to podziękują. Mówię z doświadczenia.

Masz pytania dotyczące konfiguracji? Śmiało uderzaj do mnie na [Mastodonie](https://infosec.exchange/@to3k) lub w sekcji komentarzy poniżej!