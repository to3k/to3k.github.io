---
layout: post
title: "GrapheneOS"
published: false
categories: 
  - "poradniki"
  - "przemyslenia"
tags: 
  - "grapheneos"
  - "android"
  - "ungoogled"
  - "google"
  - "pixel-9a"
  - "prywatność"
  - "privacy"
  - "foss"
  - "open-source"
image: "/images/grapheneos.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/grapheneos-eng/)

Spis treści:
* TOC
{:toc}

## Wstęp (możesz śmiało pominąć)

Jeszcze rok temu siedziałem naprawdę głęboko w ekosystemie Apple. Wydawało się, że nie ma już dla mnie odwrotu od sadu. Telefon, laptop, zegarek, tablet, streaming wideo i muzyki, chmura na pliki, a nawet lokalizator do kluczy. To wszystko od jednego producenta. Do tego współdzielone w rodzinie albumy ze zdjęciami, kalendarze i nawet listy zakupów.

Jednak w pewnym momencie odkryłem [Plenti](https://plenti.app), firmę która wynajmuje naprawdę szeroki wachlarz różnych urządzeń w całkiem rozsądnych cenach. Od niechcenia wrzuciłem w wyszukiwarkę na ich stronie frazę "samsung fold" i okazało się, że Samsung'a Galaxy Z Fold 6 można wypożyczyć już za jedyne 250-300 zł miesięcznie. To była całkiem interesująca opcja, gdyż byłem szalenie ciekawy jak żyje się ze składanym telefonem, który po rozłożeniu staje się ekwiwalentem tabletu. Do tego w życiu nie odważyłbym się kupić tego typu urządzenia, bo po pierwsze ich cena to kosmos, a po drugie mam poważne wątpliwości co do długowieczności łamanego wyświetlacza. Sprawdziłem warunki wynajmu od Plenti i nic nie wzbudziło moich podejrzeń. Wynajem wydawał się naprawdę spoko opcją, więc zdecydowałem się na wzięcie Folda 6 na pół roku. W ten oto sposób wyłamałem się z sadu i uchyliłem ponownie wrota do mojego serduszka rozwiązaniom bez loga jabłuszka. O całym procesie napisałem nawet wpis - [Zdradziłem #TeamApple na rzecz złamasa](https://blog.tomaszdunia.pl/zdradzilem-teamapple/). Dążę do tego, że w ten oto sposób Android wrócił dla mnie na salony i chyba na nowo się z nim polubiłem.

Moja przygoda z Samsung'iem skończyła się po zaplanowanych 6 miesiącach. Galaxy Z Fold 6 to dobry telefon, a możliwość rozłożenia go do rozmiaru tabletu to niesamowita funkcja. Jednakże doskwierało mi w jego przypadku to, że:

1. po złożeniu był strasznie gruby,
2. nie dało się go używać w etui, bo wszystkie pokrowce albo nie pasowały albo zsuwały się z tej części, która ma ekrany po obu stronach,
3. jako golas był bardzo kanciasty, a wręcz ostry, co powodowało u mnie dyskomfort, trzymanie go było po prostu nieprzyjemne,
4. płacenie 300 zł za wynajem to dobre krótkoterminowe rozwiązanie, żeby wziąć coś w celu sprawdzenia, ale nie na dłuższą metę.

Wszystkie powyższe punkty sprawiły, że zrezygnowałem z przedłużenia wynajmu i zacząłem się zastanawiać co dalej. Co ciekawe z Androidem polubiłem się na tyle, że niekoniecznie miałem ochotę wracać do iOS. Mniej więcej w tym okresie na mój czytnik RSS trafił artykuł [Twórcy najbezpieczniejszej wersji Androida boją się Francji. Zakaz podróży dla całego zespołu](https://ithardware.pl/aktualnosci/grapheneos_ucieka_francja_kraj_niebezpieczny_prywatnosc_open_source-46855.html) (wydaje mi się, że to był właśnie ten, ale nie jestem tak do końca pewien, nie jest to zbytnio istotne). Prawił on o tym, że Francja chce się dobrać do systemu [**GrapheneOS**](https://grapheneos.org/) i w ten sposób przeprowadzić bardzo poważny atak na prywatność jego użytkowników. Pomyślałem wtedy "Hej! Europejskie państwo **chce wymusić wprowadzenie backdoora do systemu**, bo jest on zbyt dobrze zabezpieczony, aby inwigilować jego użytkowników. Albo jest to sztuczne rozdmuchiwanie tematu, albo **w tym systemie faktycznie jest coś wyjątkowego!**". W tym momencie zapłonął we mnie trochę już zapomniany gen nerda. Postanowiłem porzucić nie tylko iOS, ale także mainstreamowego Androida i spróbować całkowicie alternatywnego systemu.

## Czym jest GrapheneOS

GrapheneOS to niefabryczny, **otwartoźródłowy system operacyjny**, który powstał z myślą o **zapewnieniu użytkownikom najwyższego poziomu prywatności i bezpieczeństwa**. Bazuje on na projekcie Android Open Source Project (AOSP), jednak znacząco różni się od standardowych wersji oprogramowania spotykanych w smartfonach. Jego twórcy całkowicie **wyeliminowali integrację z usługami Google** na poziomie systemowym, co pozwala na uniknięcie śledzenia i gromadzenia danych przez korporacje, jednocześnie oferując nowoczesne i stabilne środowisko pracy.

System wyróżnia się zaawansowanym "utwardzaniem" (hardeningiem) jądra oraz kluczowych komponentów, co minimalizuje podatność na ataki hakerskie i exploity. Unikalną cechą GrapheneOS jest możliwość uruchomienia Usług Google Play w **odizolowanym środowisku** (sandbox), dzięki czemu użytkownik może korzystać z popularnych aplikacji bez przyznawania im szerokich uprawnień systemowych. Obecnie projekt skupia się na wsparciu dla telefonów z serii **Google Pixel**, wykorzystując ich dedykowane układy zabezpieczające Titan M do pełnej ochrony danych.

## Dedykowane urządzenia

Gdy kiedyś czytałem o GrapheneOS to na liście kompatybilnych urządzeń można było znaleźć pozycje od kilku różnych producentów. Teraz są to jedynie urządzenia Google Pixel. Nie oznacza to, że tego systemu nie uruchomisz np. na Samsungu, ale twórcy po prostu nie gwarantują jego poprawnego działania, a z ewentualnym przeportowaniem wersji musisz poradzić sobie we własnym zakresie. Nota bene całkiem zabawne jest to, że **system uwolniony od usług Google powinno się uruchomić właśnie na urządzeniach od Google**. Jeżeli ktoś ma ochotę doczytać dlaczego to akurat Pixele są najlepsze dla GrapheneOS to polecam sprawdzić następujące słowa kluczowe - Verified Boot, Titan M, IOMMU, MTE.

### Lista wspieranych urządzeń (luty 2026)
- **Pixel 10 Pro Fold (rango)**
- **Pixel 10 Pro XL (mustang)**
- **Pixel 10 Pro (blazer)**
- **Pixel 10 (frankel)**
- **Pixel 9a (tegu)**
- **Pixel 9 Pro Fold (comet)**
- **Pixel 9 Pro XL (komodo)**
- **Pixel 9 Pro (caiman)**
- **Pixel 9 (tokay)**
- **Pixel 8a (akita)**
- **Pixel 8 Pro (husky)**
- **Pixel 8 (shiba)**
- Pixel Fold (felix)
- Pixel Tablet (tangorpro)
- Pixel 7a (lynx)
- Pixel 7 Pro (cheetah)
- Pixel 7 (panther)
- Pixel 6a (bluejay)
- Pixel 6 Pro (raven)
- Pixel 6 (oriole)

_pogrubiłem te pozycje, które są nie tylko wspierane, ale też rekomendowane (w momencie pisania tego wpisu, aktualną listę możesz znaleźć [tutaj](https://grapheneos.org/faq#recommended-devices))_

### Mój wybór smartfona
Na etapie wyboru urządzenia, na którym przetestuję GrapheneOS, nie miałem jeszcze pewności czy takie rozwiązanie w ogóle się dla mnie sprawdzi i czy wytrzymam z nim w dłuższej perspektywie. Toteż nierozsądnym byłoby wykładać znaczną sumę pieniędzy. Z uwagi na to chyba jedynym sensownym wyborem był **Google Pixel 9a**. Było to parę miesięcy temu, gdy od premiery rodziny modeli 10 nie minęło jeszcze na tyle dużo czasu, aby trafiły one na listę urządzeń z pełnym wsparciem. Na tamten moment to Pixel 9a był najświeższym urządzeniem na liście (**oferuje aż 7 LAT wsparcia!**) i do tego był bardzo atrakcyjny cenowo, gdyż kupiłem go za ok. **1600 PLN**.

Z perspektywy czasu dalej uważam to za dobry wybór i na pewno **polecam taką ścieżkę każdemu** kto właśnie jest na etapie podejmowania decyzji na jakim sprzęcie rozpocznie przygodę z GrapheneOS. Jedyne co mi trochę doskwiera w Pixelu 9a to jakość zdjęć jakie wykonuje. Przesiadłem się na niego mając wcześniej wyśmienite pod tym względem iPhone'a 15 Pro i Samsung'a Galaxy Z Fold 6, więc nie można się dziwić, że jestem trochę rozpuszczony, bo byłem po prostu przyzwyczajony do zupełnie innego poziomu aparatów. Teraz też wiem już, że **GrapheneOS zostanie ze mną na dłużej**, więc możliwe, że wiedząc wtedy to co wiem teraz, zdecydowałbym się na jakiś droższy sprzęt. Jednakże nie jest to dla mnie teraz istotne, bo na razie nie planuję przesiadki na inny sprzęt, a do momentu gdy się to zmieni na pewno zmieni się też sytuacja na rynku i lista dostępnych opcji. Poza tym jestem **pozytywnie zaskoczony czasem pracy na baterii i ogólną wydajnością tego telefonu**.

## Instalacja GrapheneOS

### Potrzebujemy

1. Odpowiedni **smartfon** - w moim przypadku to Google Pixel 9a.
2. **Kabel** do podłączenia telefonu do komputera, nie może to być byle jaki kabel tylko taki, który służy nie tylko do ładowania, ale także do transmisji danych, najlepiej użyć po prostu kabla, który dostaliśmy razem z telefonem.
3. **Komputer z przeglądarką opartą na Chromium** (np. Google Chrome, Brave, Microsoft Edge, Vivaldi?), niestety muszę tutaj polecić Windows 10/11, bo nie trzeba się wtedy bawić z żadnymi sterownikami, jest to najprostsza opcja.

### Przygotowanie telefonu

1. Jeżeli jest nowy to wyciągamy go z pudełka i **włączamy**. Jeżeli był wcześniej używany to **przywracamy go do ustawień fabrycznych** (Ustawienia -> System -> Opcje resetowania -> Wykasuj wszystkie dane (przywróć ustawienia fabryczne) -> Wykasuj wszystkie dane). Myślę, że to oczywista oczywistość, ale i tak to napiszę - przywrócenie ustawień fabrycznych skutkuje usunięciem wszystkich danych użytkownika z urządzenia, więc jeżeli masz na nim coś istotnego to należy zrobić tego kopię.
2. Musimy **przejść przez podstawową konfigurację** aż do momentu zobaczenia pulpitu. Robimy absolutne minimum czyli:
    - na ekranie powitalnym możesz zmienić język na taki jaki Ci pasuje,
    - pomijamy konfigurację usług GSM (karta SIM),
    - nie łączymy się z Wi-Fi, więc ten krok też pomijamy,
    - ustawienia daty i godziny powinny się zgadzać,
    - wyłączamy wszystkie Google Services (lokalizacja, skanowanie, wysyłanie danych diagnostycznych) i akceptujemy,
    - z warunkami gwarancji nie musimy nic robić, więc tylko przycisk Dalej,
    - akceptujemy Legal Terms,
    - ustawiamy jakiś łatwy PIN np. 12345,
    - nie ma potrzeby tracić czas na konfigurację biometrii, więc uprzejmie dziękujemy i rezygnujemy z odcisku palca i skanu twarzy,
    - chwila oczekiwania,
    - pomijamy samouczek,
    - swipe do góry i gotowe, jesteśmy na pulpicie.
3. W pierwszej kolejności musimy się upewnić, że **oprogramowanie naszego telefonu jest zaktualizowane** do najnowszej dostępnej wersji. W tym celu idziemy do **Ustawienia -> System -> Aktualizacja systemu**. Jeżeli jest taka potrzeba to aktualizujemy.
4. Następnie przechodzimy do **Ustawienia -> Informacje o telefonie -> znajdujemy pole Numer kompilacji** i klikamy na to 7 razy aż zobaczymy komunikat **Jesteś teraz programistą**. W międzyczasie telefon poprosi o podanie PINu, który ustawiliśmy podczas konfigurowania telefonu.
5. Cofamy się i teraz wchodzimy do **Ustawienia -> System -> Opcje programistyczne -> włączamy opcję Zdjęcie blokady OEM**. Telefon znowu poprosi o PIN. Po jego podaniu musimy jeszcze potwierdzić, że na pewno chcemy zdjąć blokadę.

### Odblokowanie bootloadera

1. Proces odblokowania bootloadera rozpoczynamy od **wyłączenia telefonu**.
2. Gdy ekran całkiem zgaśnie **naciskamy jednocześnie i trzymamy przyciski zasilania (power) i zmniejszenia głośności (volume down)** aż do momentu, gdy pojawi nam się tekstowy interfejs **Fastboot Mode**. Jeżeli telefon uruchomi nam się normalnie to znaczy, że któryś z wcześniejszych kroków wykonaliśmy nieprawidłowo.
3. Podłączamy **telefon do komputera**.
4. Przechodzimy do komputera i wchodzimy w przeglądarce (opartej na silniku Chromium) na stronę pod adresem **[https://grapheneos.org/install/web](https://grapheneos.org/install/web)**.
5. Przechodzimy do sekcji [Unlocking the bootloader](https://grapheneos.org/install/web#unlocking-the-bootloader) i naciskamy przycisk **Unlock bootloader**.
6. W przeglądarce wyskoczy okienko z listą urządzeń do wyboru. Powinna na nim być w zasadzie tylko jedna pozycja i to właśnie powinien być nasz Pixel. **Wybieramy go i naciskamy przycisk Połącz** (Connect).
7. Zajdą zmiany na wyświetlaczu telefonu. Pojawi się tam komunikat i prośba o potwierdzenie tego, że chcemy faktycznie odblokować bootloader. W tym celu musimy nacisnąć któryś przycisk głośności, tak aby zamiast **Do not unlock the bootlader** pojawiło się **Unlock the bootlader**. W tym momencie możemy potwierdzić poprzez **naciśnięcie przycisku zasilania** (power).
8. Jeżeli wszystko się udało to pośród danych wyświetlonych w Fastboot Mode powinniśmy widzieć **Device state: unlocked** (na czerwono).

### Pobieranie i wgrywanie obrazu systemu

1. Na stronie internetowej GrapheneOS przewijamy na dół do sekcji [Obtaining factory images](https://grapheneos.org/install/web#obtaining-factory-images) i naciskamy przycisk **Download release**. Jeżeli telefon jest dalej podłączony do komputera to strona sama zadecyduje, który obraz systemu należy pobrać.
2. Czekamy aż pobieranie zostanie zakończone. Oczywistym jest, że czas do tego potrzebny zależy wprost proporcjonalnie od prędkości połączenia internetowego.
3. Gdy pobieranie zostanie zakończone możemy przejść do sekcji [Flashing factory images](https://grapheneos.org/install/web#flashing-factory-images) poniżej i naciskamy **Flash release**.
4. Spluń teraz przez lewe ramię, wstrzymaj oddech i pod żadnym pozorem nie odpinaj telefonu od komputera. Najlepiej w ogóle nie dotykaj obu urządzeń.
5. Gdy proces zostanie zakończony telefon zrestartuje się sam i wróci do interfejsu Fastboot Mode. W przeglądarce będziemy widzieli komunikat **Flashed ...**.

### Ponowne blokowanie bootloadera

Zablokowanie bootloadera jest kluczowe, ponieważ umożliwia pełne działanie funkcji Verified Boot (zweryfikowanego rozruchu). Uniemożliwia to również korzystanie z trybu fastboot do wgrywania (flashowania), formatowania lub wymazywania partycji. Verified Boot wykrywa wszelkie modyfikacje partycji systemu operacyjnego i blokuje odczyt jakichkolwiek zmienionych lub uszkodzonych danych. W przypadku wykrycia zmian system wykorzystuje dane korekcji błędów, aby spróbować odzyskać pierwotne dane, które są następnie ponownie weryfikowane – dzięki temu mechanizm system jest odporny na przypadkowe (niezłośliwe) uszkodzenia plików.

Jednakże przed ponownym zabezpieczeniem bootloadera zalecam sprawdzić czy system wgrał się prawidłowo i wszystko działa jak należy, bo jeżeli tak nie jest to blokując bootloader możemy sobie uceglić (całkowicie zablokować, a wręcz uszkodzić) telefon. Dlatego:

1. Będąc w Fastboot Mode, gdy widzimy komunikat **Start** to naciskamy przycisk zasilania (power), co spowoduje normalne uruchomienie systemu. Jeżeli na wysokości przycisku zasilania nie widzimy **Start** to musimy naciskać przyciski głośności i odszukać tę opcję.
2. Gdy telefon się uruchomi to możemy od razu wykonać podstawową konfigurację. Bootloader nam nie ucieknie.
3. To standardowa procedura, więc przejdziemy przez nią tylko hasłowo:
    - ekran powitalny,
    - wybieramy **język**,
    - wybieramy strefę czasową i tym samym ustawiamy **datę i czas**,
    - łączymy się do **Wi-Fi**,
    - jeżeli masz taką możliwość to możesz od razu skonfigurować **kartę SIM**, ale możesz to też odłożyć na później,
    - polecam wyłączyć **usługę lokalizacji**, bo lepiej to później skonfigurować na spokojnie przydzielając uprawniania tylko aplikacjom, które naprawdę tego potrzebują,
    - zabezpieczenie telefonu poprzez **odcisk palca**, ja osobiście jestem zwolennikiem tego rozwiązania, więc rekomenduję używanie go, GrapheneOS nie obsługuje (jeszcze) odblokowywania skanem twarzy, więc odcisk palca i standardowe hasło to jedyne metody jakie mamy do wyboru (oczywiście odblokowanie wzorem odrzucam na starcie jako forma blokady ekranu, której nie można nawet z czystym sumieniem nazwać jakimkolwiek zabezpieczeniem),
    - zakładam, że jeżeli czytasz ten wpis to jesteś grafenowym świeżakiem i nie masz żadnej **kopii zapasowej** do przywrócenia, więc ten krok po prostu pomijamy,
    - przycisk **Start** i jesteśmy na pulpicie.
4. Jeżeli wszystko działa prawidłowo to teraz śmiało możesz wyłączyć telefon i włączyć go trzymając przycisk zasilania (power) i zmniejszania głośności (volume down), tak jak to robiliśmy wcześniej.
5. Lądujemy znów w Fastboot Mode. Zakładam, że telefon był cały czas podłączony do komputera (jeżeli nie to podłącz go ponownie). Wracamy do przeglądarki na komputerze. Odnajdujemy sekcję [Locking the bootloader](https://grapheneos.org/install/web#locking-the-bootloader) i naciskamy przycisk **Lock bootloader**.
6. Znowu jest wymagane potwierdzenie tej operacji na telefonie. Wygląda to analogicznie jak przy odblokowywaniu z tym, że tym razem używając przycisków głośności musimy sprawić, aby aktywna była opcja **Lock the bootloader** i potwierdzić to przyciskiem zasilania (power).
7. Efektem powinna być zmiana **Device state** na **locked** (na zielono).

### Przywrócenie blokady OEM

Ostatnim krokiem przed przed rozpoczęciem zabawy nowym systemem jest ponowne nałożenie blokady OEM.

1. Tak jak przy zdejmowaniu blokady przechodzimy do **Ustawienia -> Informacje o telefonie -> znajdujemy pole Numer kompilacji** i klikamy na to 7 razy aż zobaczymy komunikat **Jesteś teraz programistą**. W międzyczasie telefon poprosi o podanie PINu, który ustawiliśmy podczas konfigurowania telefonu.
2. Cofamy się i teraz wchodzimy do **Ustawienia -> System -> Opcje programistyczne -> wyłączamy opcję Zdjęcie blokady OEM**. Telefon poprosi nas o restart w celu zmiany tego ustawienia, ale na ten moment anulujemy to żądanie, bo chcemy jeszcze **wyłączyć całkowicie Opcje programisty**, co robi się odznaczając ptaszek przy pierwszej opcji na samej górze **Używaj opcji programisty**.
3. Teraz możemy już **zrestartować urządzenie**.

## Moja wizja używania GrapheneOS

Teraz tak naprawdę zaczyna się prawdziwa zabawa. Ile osób tyle usłyszysz/przeczytasz opinii na temat tego co powinno się robić, a czego nie, w temacie hardeningu GrapheneOS. Jedni są konserwatywni, a inni podchodzą do tematu nieco bardziej liberalnie. Według mnie nie ma jednej słusznej drogi i każdy powinien poszperać, posprawdzać i zdecydować co mu odpowiada i co pasuje do jego profilu bezpieczeństwa. Szybko przekonasz się, że **GrapheneOS to tak naprawdę jeden wielki kompromis pomiędzy wygodą, a prywatnością**. Co prawda ta sama zasada dotyczy wszystkiego co przynależy do świata cyfrowego, ale dopiero w tym przypadku tak naprawdę to dostrzeżesz, bo **GrapheneOS pokaże Ci o jak wielu rzeczach możesz decydować, czego nie możesz zrobić używając konwencjonalnego Androida**.
Nie zamierzam tym wpisem promować jakiejś "najmojszej" metody używania GrapheneOS. Przedstawię jedynie to jak ja używam tego systemu. W ten sposób osobom świeżym w temacie pokażę podstawy, tym którzy są już od jakiegoś czasu użytkownikami może uda mi się podpowiedzieć jakiś ciekawy trick jakiego nie znali, a z trzeciej strony może trafi się jakiś ekspert, który po przeczytaniu moich wypocin podpowie mi coś ciekawego lub wskaże co robię źle / mógłbym robić lepiej, bo na pewno tak jest, gdyż tak na dobrą sprawę moja przygoda z GrapheneOS trwa zaledwie od 3 miesięcy. Od razu ostrzegam, że nie jestem pewien czy będę w stanie zachować jakiś logiczny ciąg myślowy, bo zapewne będę trochę skakał po zagadnieniach. **Temat GrapheneOS jest obszerny** i w dzisiejszym wpisie uda mi się co najwyżej lekko go zaczepić.

### Dodatkowy profil użytkownika

Jedną z pierwszych rzeczy jaką zrobiłem po uruchomieniu świeżo zainstalowanego systemu było utworzenie drugiego profilu użytkownika. Robi się to w **Ustawienia -> System -> Użytkownicy**. W zamyśle ta funkcja jest po to, aby dwie (lub więcej) osoby mogły korzystać z jednego telefonu i każda z nich posiadała osobny profil ze swoimi ustawieniami, aplikacjami itp. Kto normalny tak robi? O ile współdzielenie tabletu domowego mogę sobie wyobrazić, tak współdzielenia telefonu już zupełnie nie. Wydaje się zatem, że jest to martwa funkcja, ale nic bardziej mylnego.

U mnie działa to tak, że na użytkowniku ***Właściciel***, bo tak nazywa się główne konto, które tworzy się automatycznie wraz z systemem, zainstalowałem **Google Play Store** wraz z **Google Play services** i **GmsCompatConfig**. Robi się to poprzez aplikację **App Store** będącą komponentem systemu GrapheneOS. Nie myl tego proszę z applowskim sklepem z aplikacjami, mimo że nazwa jest taka sama. Ze sklepu Play zainstalowałem jedynie następujące aplikacje:

- **mBank** - płacenie BLIKiem zbliżeniowym przez NFC jest możliwe tylko posiadając zainstalowane usługi Google i działa mi tylko na profilu użytkownika z uprawnieniami administratora (Właściciel),
- **Mój T-Mobile** - bez usług Google nie działała mi zupełnie zakładka Magenta Moments.

I to tyle. Jak widzisz ten profil służy mi tylko do aplikacji, które koniecznie wymagają integracji z usługami Google. W praktyce przełączam się na niego tylko wtedy, gdy w sklepie chcę zapłacić zbliżeniowo, co w sumie ostatnio robię rzadko, bo jeżeli jest taka możliwość to płacę używając kody BLIK. Zaraz po przesiadce z Samsung'a aplikacji na tym profilu było więcej, ale po kolei sukcesywnie rezygnowałem z tych, które uzależniały mnie od wielkego G.

To na **drugim profilu**, który załóżmy nazwałem _Tomuś_, trzymam całe swojego cyfrowe życie. Co mi to daje? Chociażby to, że profilu głównego nie da się łatwo usunąć, a ten dodatkowy już tak. Wyobraźmy sobie sytuację, w której muszę na szybko wyczyścić swój telefon, ale tak, aby działały jego podstawowe funkcje, czyli bez całkowitego przywrócenia ustawień fabrycznych. Przykładem może być np. przylot do USA i kontrola urzędu imigracyjnego. Chcą dostęp do mojego telefonu, więc kasuję użytkownika _Tomuś_, przełączam się na użytkownika _Właściciel_ i oddaję im telefon. Dzwoni, wysyła SMSy, ma nawet aplikację bankową, więc teoretycznie nie powinien wzbudzać podejrzeń. Nie ma jednak wszystkich moich kontaktów, przeglądarki z historią odwiedzanych stron, menedżera haseł, kominikatorów z historią czatów. Jest to raczej drastyczny scenariusz, ale jednak nie tak bardzo nieprawdopodobny, bo akcje typu pyranie telefonu przy przylocie do Stanów to coś co zdarza się na porządku dziennym. Poza tym podstawową zasadą bezpieczeństwa jest to, aby **na co dzień nie używać konta z uprawnieniami administratora**. 

### Obtainium

Na GrapheneOS to Obtainium jest moim **podstawowym agregatorem do pozyskiwania plików instalacyjnych .apk i automatyzacji aktualizowania aplikacji**. To taki Google Play Store, ale szanujący prywatność i dla aplikacji o otwartym kodzie źródłowym. Grzechem byłoby korzystać z GrapheneOS i przynajmniej nie spróbować przerzucić się na aplikacje otwarto-źródłowe. Poniżej przedstawiam listę appek, które ja używam. Dodatkowo dorzucam Ci linki do repozytoriów z kodem źródłowym każdej z nich.

#### Lista moich aplikacji otwarto-źródłowych
- [**AntennaPod**](https://github.com/AntennaPod/AntennaPod) - aplikacja do podcastów (jeszcze całkowicie nie przerzuciłem się na nią z Pocket Casts, ale mam to w planach),
- [**Aurora Store**](https://github.com/whyorean/AuroraStore) - jeżeli nie ma innej opcji na pobranie pliku .apk to właśnie ta aplikacja może posłużyć jako alternatywa dla Google Play Store, wspomnę o tym jeszcze później,
- [**Bitwarden**](https://github.com/bitwarden/android) - menedżer haseł,
- [**Brave**]() - przeglądarka internetowa,
- [**Breezy Weather**](https://github.com/breezy-weather/breezy-weather) - pogoda,
- [**Catima**](https://github.com/CatimaLoyalty/Android) - aplikacja do przechowywania kart lojalnościowych (mam w niej kartę Biedronki i Lidla, ale reszta też czeka na dodanie),
- [**Collabora Office**](https://github.com/CollaboraOnline/online) - pakiet biurowy, który otworzy wszystko to co Microsoft Office czy LibreOffice,
- [**DAVx2**](https://github.com/bitfireAT/davx5-ose) - aplikacja do synchronizacji rzeczy przez DAV (kalendarze, kontakty, listy zadań czy pliki w chmurze), potrzebuję jej do synchronizacji kalendarza, który współdzielę z żoną,
- [**Ente Auth**](https://github.com/ente-io/ente) - dwuetapowe uwierzytelnianie, alternatywa dla Google/Microsoft Authenticatior czy Authy, 
- [**FairScan**](https://github.com/pynicolas/FairScan) - skanowanie dokumentów, prosta bez zaawansowanych funkcji,
- [**Feeder**](https://github.com/spacecowboy/Feeder) - czytnik RSS,
- [**Home Assistant**](https://github.com/home-assistant/android) - zarządzanie "inteligentnym" domem,
- [**Klawiatura FUTO**](https://github.com/futo-org/android-keyboard) - gorąco polecam tą klawiaturę i plus do niej pakiet [FUTO Voice Input](https://voiceinput.futo.org/), który generuje tekst z mowy na bazie działającego offline na urządzeniu modelu LLM,
- [**Librera**](https://github.com/foobnix/LibreraReader) - czytnik ebooków,
- [**Obtainium**](https://github.com/ImranR98/Obtainium) - tak, Obtainium może aktualizować samo siebie,
- [**Organic Maps**](https://github.com/organicmaps/organicmaps) - mapy z nawigacją oparte na OpenStreetMap,
- [**Pachli**](https://github.com/pachli/pachli-android) - klient Mastodon,
- [**Signal**](https://github.com/signalapp/Signal-Android) - komunikator,
- [**Simplenote**](https://github.com/Automattic/simplenote-android) - notatki,
- [**Stremio**](https://github.com/stremio) - VOD bazujące na torrent (na pewno wkrótce napiszę o tym wpis),
- [**Thunderbird**](https://github.com/thunderbird/thunderbird-android) - klient poczty e-mail (to tak naprawdę K-9 Mail po rebrandingu).

Aby zrozumieć jak działa i jak używać Obtainium **polecam zapoznać się z [tym poradnikiem wideo](https://odysee.com/@%C5%81%C4%85cze:4/aplikacje_bez_Google...2025_:f)**.

### Aurora Store

Mam kilka aplikacji, które nie są open-source, ale i tak ich potrzebuję. W takim przypadku nie pobieram ich z Google Play Store, a właśnie z **Aurora Store**, o której wspomniałem wyżej.

Aurora Store to otwartoźródłowy klient sklepu Google Play (można to chyba nazwać frontend'em), który **pozwala na pobieranie aplikacji z serwerów Google bez konieczności posiadania usług Google** (GMS) na telefonie.

Internety charakteryzują to rozwiązanie następująco:

- **Prywatność** - nie musisz logować się kontem Google, aby pobierać darmowe aplikacje (można korzystać z wbudowanych kont anonimowych).
- **Bezpieczeństwo** - instalujesz oryginalne pliki .apk prosto z serwerów Google, a nie z niesprawdzonych stron trzecich.
- **Funkcjonalność** - pozwala omijać ograniczenia regionalne oraz instalować aplikacje, które Google Play uznaje za "niekompatybilne" z danym urządzeniem.
- **Open Source** - cały kod aplikacji jest jawny i audytowalny.

Brzmi idealnie, prawda? Trochę tak, ale niestety nie do końca wszystko trzyma się tu kupy. Do Aurora Store mam **dwa główne zarzuty**.

Z tymi anonimowymi kontami to jest tak, że **czasem działają, a czasem nie**, a to za sprawą limitów, które przy normalnym koncie używanym przez jedną osobę są nie do osiągnięcia, natomiast gdy z jednego konta aplikacje pobiera na raz tysiąc osób to zaczyna się to już robić podejrzane, a limity są dość szybko przekraczane. Używanie Aurora Store narusza warunki korzystania z Google Play Store, więc z kolei **gdy użyjemy swojego konta Google to może ono zostać zablokowane** tymczasowo lub trwale zbanowane. Jakąś opcją jest tutaj utworzenie "śmieciowego" konta tylko do tego, ale to odbiera nam część prywatności, bo Google dalej może nas indeksować na podstawie tego co pobraliśmy. Konta anonimowe dają w tym przypadku niemalże pełną anonimowość, bo jesteśmy wtedy kroplą w morzu.

Jeżeli chodzi o bezpieczeństwo to faktycznie w teorii pobieramy pliki .apk ze sprawdzonego źródła, ale **tylko pod warunkiem, że twórcy Aurora Store nie zafundują nam ataku typu [Man in the Middle](https://pl.wikipedia.org/wiki/Atak_man_in_the_middle)**. Decyzja czy ufasz twórcom tej aplikacji należy do Ciebie.

#### Lista aplikacji, których działanie bez GMS zweryfikowałem

Poniżej przedstawiam listę aplikacji, które pobrałem z Aurora Store, sprawdziłem i mogę potwierdzić, że działają bez GMS (Google Mobile Services).

- **Allegro** - zakupy
- **Apple Music** - tak, z tego nie udało mi się zrezygnować porzucając iPhone
- **Apple TV** - jest w pakiecie, ale jakby nie było to zrezygnowałbym z subskrypcji, bo Stremio mi wystarcza
- **Biedronka** - promki na spożywkę
- **Bolt** - taksówki
- **Booksy** - fryzjer
- **BPme** - promki na paliwo
- **CityParkApp** - parkowanie w mieście
- **Decathlon** - pozbyłem się, ale działało
- **DeepL** - translator, czy jest jakaś otwarto-źródłowa alternatywa, która jest równie dobra?
- **Discord** - po ostatnich wydarzeniach chyba się pozbędę, bo w zasadzie nie używam
- **Duolingo** - sówka! wspólna nauka włoskiego to stały punkt dnia dla moich córek
- **DWService** - zdalny pulpit
- **Ekstraliga** (żużel) - jestem psychofanem
- **epark** - parkowanie w mieście
- **Formula 1** - jestem psychofanem
- **Geoportal Mobile** - plany zagospodarowania terenu, appka zbugowana jak cholera, ale działa lepiej niż wersja webowa na telefonie
- **GitHub** - wiem, że jest alternatywa OpenHub, ale crashuje mi po zalogowaniu do GH
- **Appka mojej gminy** - bo muszę wiedzieć kiedy mi zabiorą śmieci :)
- **Jakdojade** - rozkłady jazdy autobusów
- **Lidl Plus** - promki na spożywkę
- **LiveKid** - komunikacja z przedszkolem córki
- **Messanger** - shame on me, ale niestety mam znajomych, którzy bez FB nie wyobrażają sobie życia...
- **OLX** - ogłoszenia lokalne, używam w zasadzie tylko dla powiadomień
- **OpenVPN** - używam jako tunel do sieci domowej
- **park4night** - świetna appka do znajdowania parkingu na wakacjach (nie tylko kamperem)
- **Pepper** - promki cebulowe
- **Perplexity** - przerzuciłem się na Gemini, ale potwierdzam, że działa
- **Synology Photos** - moja domowa galeria zdjęć na NAS
- **Pocket Casts** - podcasty, planuję migrację na AntennaPod
- **Reddit** - w sumie nie wiem po co mi appka, ale działa
- **Reolink** - monitoring domowy
- **SmartLife** - kto ma cokolwiek smart z Chin to wie po co to
- **Tapo** - kamerki domowe
- **Termius** - tutaj też szukam jakiejś alternatywy open-source
- **Tether** - zarządzanie routerami TP-Link
- **TickTick** - listy zadań (to-do), ciężko jest mi znaleźć sensowną alternatywę, która jest multiplatformowa i ma wszystkie potrzebne mi funkcje
- **TV Time** - śledzenie tego jakie seriale i filmy obejrzałem (tu w sumie też mógłbym być zainteresowany znalezieniem alternatywy)
- **Zepp** - dedykowana appka dla smartwatcha Amazfit Balance, którego używam
- **ZeroTier** - używałem zamiast OpenVPN, gdy jeszcze nie miałem światłowodu tylko samą radiówkę

### Pełna kontrola uprawnień aplikacji

GrapheneOS pozwala na pełną kontrolę tego jakie uprawnienia może mieć każda z aplikacji. Dla przykładu w konwencjonalnych forkach systemu Android każda aplikacja domyślnie posiada przyznane uprawnienia **Network** (dostęp do internetu) i **Sensors** (dostęp do wszystkich czujników jak np. akcelerometr).

Czy ktoś kiedyś zastanawiał się **czy wszystkie aplikacje na telefonie potrzebują dostępu do Internetu?** Faktycznie w przeważającej większości przypadków appka mobilna bez dostępu do sieci jest bezużyteczna, ale nie można tego tak generalizować, bo chociażby wspomniany przeze mnie wcześniej **FUTO Voice Input** do zmiany mowy na tekst używa lokalnego LLM, który działa offline na urządzeniu. Po co w takim razie takiej aplikacji dostęp do Internetu? Po nic, więc **takiego uprawnienia nie powinna mieć**. Weźmy teraz takie aplikacje jak FairScan (skanowanie dokumentów), Catima (agregator kart lojalnościowych), Collabora Office (pakiet biurowy) czy Librera (czytnik ebooków). One też **nie potrzebują dostępu do Internetu!**

Sytuacja wygląda jeszcze bardziej kuriozalnie, gdy popatrzy się na to jakie aplikacje tak naprawdę potrzebują dostępu do wszystkich sensorów naszego urządzenia. Jakby tak zastanowić się na spokojnie to dojdziemy do wniosku, że w tym konkretnym przypadku jest zupełnie odwrotnie niż w poprzednim, czyli **praktycznie żadna aplikacja nie potrzebuje tych informacji**. A przypominam, że **domyślnie na Androidzie z usługami Google wszystkie aplikacje mają takie uprawnienia**.

Aby zarządzać uprawnieniami danej aplikacji wystarczy **przytrzymać palcem na jej ikonie**, z wysuniętego menu wybrać **O aplikacji** i odszukać zakładkę **Uprawnienia**. Pojawi nam się lista posegregowana według takich kategorii - **Ma dostęp**, **Zawsze pytaj** i **Nie ma dostępu**. Polecam przejrzeć tą listę dla każdej aplikacji z osobna zaraz po jej zainstalowaniu. To **podstawa hardeningu GrapheneOS**.

Zbiorcze menu, w którym można podejrzeć konkretne uprawnienia i jakie aplikacje mają je przyznane dostępne jest w **Ustawienia -> Bezpieczeństwo i prywatność -> Ustawienia prywatności -> Menedżer uprawień**. Ciekawym miejscem jest też **Panel prywatności** dostępny w tym samym miejscu. Jest to narzędzie, które pokazuje nie tylko uprawnienia aplikacji, ale także to jak często dana aplikacja sięga po przydzielone im uprawnienia.

### Przestrzeń prywatna

W GrapheneOS mamy nie tylko profile użytkowników, ale do tego każdy użytkownik może mieć też coś co się nazywa **Przestrzeń prywatna**. Coś podobnego spotkałem już na Samsung'u, gdzie nazywało się to **Mój sejf**, więc zakładam, że może to być po prostu funkcjonalność Android, która jest różnie implementowana przez każdego z producentów.

Przestrzeń prywatną włącza się w **Ustawienia -> Bezpieczeństwo i prywatność -> Przestrzeń prywatna**. Jest ona taką jakby odseparowaną piaskownicą, która jest częścią środowiska, którego używasz, ale jednocześnie jest od niego odizolowana. Dla mnie jest to miejsce dzięki któremu mam szybki dostęp do aplikacji, które jednak wymagają usług Google. Zapytasz - dlaczego w takim razie aplikację mBank i T-Mobile trzymam na użytkowniku **Właściciel** skoro mógłbym je trzymać tutaj. Otóż z nieznanych mi przyczyn nie jestem w stanie tak skonfigurować mojej przestrzeni prywatnej, aby działało na niej prawidłowo płacenie BLIKiem zbliżeniowym przez NFC. Tak samo z Magenta Moments od T-Mobile, które nie działają prawidłowo pomimo zainstalowanych GMS w przestrzeni prywatnej.

#### Lista aplikacji w mojej przestrzeni prywatnej

- **Dysk Google** - wykorzystuję jako chmura do udostępniania plików klientom
- **Finax** - odkładam na emeryturę w ramach OIPE
- **IKO** - appka banku PKO BP, obligacje skarbowe plus PPK
- **InPost Mobile** - paczkomaty, w przestrzeni prywatnej nie działa mi też lokalizacja (telefon przesyła swojej pozycji do aplikacji), więc używam kodów QR jak jakiś neandertalczyk
- **mBank** - ponownie, bo o ile nie działa mi tutaj płatność zbliżeniowa to inne funkcje aplikacji bankowej normalnie działają
- **mObywatel** - na początku trzymałem tą aplikację w profilu głównym jako pobrana z Aurora Store i wszystko w miarę działało, ale co jakiś czas aplikacja łapała totalną zwiechę i nie odpowiadała, wydaje mi się, że może to być związane z tym, że jednak w tle wysyła jakieś zapytania związane z usługami Google i nie odpowiada dopóki nie nastąpi timeout takiego zapytania, mam to na liście do zbadania
- **mojeIKP** - ostatnio mam coraz więcej problemów ze zdrowiem, ewidentnie już nie jestem taki niezniszczalny, więc taka geriatryczna aplikacja jest mi po prostu niezbędna
- **Mój T-Mobile** - zdublowane tak jak appka mBank, bo działa wszystko poza Magenta Moments
- **Orlen Vitay** - ta aplikacja nie działała mi bez GMS, więc trochę dwója z minusem dla Orlen, bo appka od BP nie ma takiego problemu
- **Revolut** - w zasadzie chyba nie wymaga GMS, ale stwierdziłem, że już wszystkie aplikacje finansowe będę trzymał w przestrzeni prywatnej
- **Santander** - kolejna aplikacja bankowa...
- **Sklep Play** - skądś muszę pobierać te wszystkie appki, robienie tego przez Aurora Store w przestrzeni prywatnej nie miałoby sensu skoro i tak mam tutaj zainstalowany cały pakiet Google
- **XTB** - kolejna aplikacja do inwestowania... działa bez GMS, ale tak jak mówiłem, wszystkie finansowe w jednym miejscu

## Podsumowanie

Uf... znowu to zrobiłem, przepraszam. Właśnie podliczam ilość znaków i wychodzi mi niespełna 35 000... Zapewne tymi następnymi kilkoma zdaniami przekroczę tę barierę. Cóż, znowu długo, ale znowu mięsooo, więc nie sądzę, żeby ktoś miał powody do marudzenia. Tak jak już wspomniałem wcześniej, tylko liznąłem temat GrapheneOS, który jest obszerny i dobrze, bo to świetny system, a największy szacun należy się osobom stojącym za tym projektem. To dzięki nim mamy w ogóle opcję choć częściowego uwolnienia się od Google (Androida) i Apple (iOS). Dlatego gorąco zapraszam do ostatniego rozdziały tego wpisu.

## Wsparcie projektu GrapheneOS

Na koniec chciałbym zachęcić do wsparcia projektu GrapheneOS. Deweloperzy stojący za nim wykonują naprawdę dobrą robotę i w mojej ocenie zasługują na rzucenie w nich odrobiną pieniędzy. Informacje gdzie i jak można to zrobić znajdują się [tutaj](https://grapheneos.org/donate).