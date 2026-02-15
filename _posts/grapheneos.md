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

Jednak w pewnym momencie odkryłem [Plenti](https://plenti.app), firmę która wynajmuje naprawdę szeroki wachlarz różnych urządzeń w całkiem rozsądnych cenach. Od niechcenia wrzuciłem w wyszukiwarkę na tej stronie frazę "samsung fold" i okazało się, że Samsunga Galaxy Z Fold 6 można wypożyczyć już za jedyne 250-300 zł miesięcznie. To była całkiem interesująca opcja, gdyż byłem szalenie ciekawy jak żyje się ze składanym telefonem, który po rozłożeniu staje się ekwiwalentem tabletu. Do tego w życiu nie odważyłbym się kupić tego typu urządzenia, bo po pierwsze ich cena to kosmos, a po drugie mam poważne wątpliwości co do długowieczności łamanego wyświetlacza. Sprawdziłem warunki wynajmu od Plenti i nic nie wzbudziło podejrzeń. Wynajem wydawał się naprawdę spoko opcją, więc zdecydowałem się na wzięcie Folda 6 na pół roku. W ten oto sposób wyłamałem się z sadu i uchyliłem ponownie wrota do mojego serduszka rozwiązaniom bez logo jabłuszka. O całym procesie napisałem nawet wpis - [Zdradziłem #TeamApple na rzecz złamasa](https://blog.tomaszdunia.pl/zdradzilem-teamapple/). Dążę do tego, że w ten oto sposób Android wrócił dla mnie na salony i chyba na nowo się z nim polubiłem.

Moja przygoda z Samsungiem skończyła się po zaplanowanych 6 miesiącach. Z Fold 6 to dobry telefon, a możliwość rozłożenia go do wymiaru tabletu to niesamowita funkcja. Jednakże doskwierało mi w jego przypadku to, że:

1. po złożeniu był strasznie gruby,
2. nie dało się go używać w etui, bo wszystkie etui albo nie pasowały albo zsuwały się z tej części, która ma ekrany po obu stronach,
3. jako golas był bardzo kanciasty, a wręcz ostry, co powodowało u mnie dyskomfort,
4. płacenie 300 zł za wynajem to dobre krótkoterminowe rozwiązanie, żeby wziąć coś w celu sprawdzenia, ale nie na dłuższą metę.

Wszystkie powyższe punkty sprawiły, że zrezygnowałem z przedłużenia wynajmu i zacząłem się zastanawiać co dalej. Co ciekawe z Androidem polubiłem się na tyle, że niekoniecznie miałem ochotę wracać do iOS. Mniej wiecej w tym okresie na mój czytnik RSS trafił artykuł [Twórcy najbezpieczniejszej wersji Androida boją się Francji. Zakaz podróży dla całego zespołu](https://ithardware.pl/aktualnosci/grapheneos_ucieka_francja_kraj_niebezpieczny_prywatnosc_open_source-46855.html) (wydaje mi się, że to był właśnie ten, ale nie jestem tak do końca pewien, nie jest to zbytnio istotne). Prawił on o tym, że Francja chce się dobrać do systemu [**GrapheneOS**](https://grapheneos.org/) i w ten sposób przeprowadzić bardzo poważny atak na prywatność jego użytkowników. Pomyślałem wtedy "Hej! Europejskie państwo chce wymusić wprowadzenie backdoora do systemu, bo jest on zbyt dobrze zabezpieczony, aby inwigilować jego użytkowników. Albo jest to sztuczne rozdmuchiwanie tematu, albo w tym systemie faktycznie jest coś wyjątkowego!". W tym momencie zapłonął we mnie trochę już zapomniany gen nerda. Postanowiłem porzucić nie tylko iOS, ale także mainstreamowego Androida i spróbować całkowicie alternatywnego systemu.

## Czym jest GrapheneOS

GrapheneOS to niefabryczny, otwartoźródłowy system operacyjny, który powstał z myślą o zapewnieniu użytkownikom najwyższego poziomu prywatności i bezpieczeństwa. Bazuje on na projekcie Android Open Source Project (AOSP), jednak znacząco różni się od standardowych wersji oprogramowania spotykanych w smartfonach. Jego twórcy całkowicie wyeliminowali integrację z usługami Google na poziomie systemowym, co pozwala na uniknięcie śledzenia i gromadzenia danych przez korporacje, jednocześnie oferując nowoczesne i stabilne środowisko pracy.

System wyróżnia się zaawansowanym "utwardzaniem" (hardeningiem) jądra oraz kluczowych komponentów, co minimalizuje podatność na ataki hakerskie i exploity. Unikalną cechą GrapheneOS jest możliwość uruchomienia Usług Google Play w odizolowanym środowisku (sandbox), dzięki czemu użytkownik może korzystać z popularnych aplikacji bez przyznawania im szerokich uprawnień systemowych. Obecnie projekt skupia się na wsparciu dla telefonów z serii Google Pixel, wykorzystując ich dedykowane układy zabezpieczające Titan M do pełnej ochrony danych.

## Dedykowane urządzenia

Gdy kiedyś czytałem o GrapheneOS to na liście kompatybilnych urządzeń można było znaleźć pozycje od kilku różnych producentów. Teraz są to jedynie urządzenia Google Pixel. Nie oznacza to, że tego systemu nie uruchomisz np. na Samsungu, ale twórcy po prostu nie gwarantują jego poprawnego działania. Nota bene całkiem zabawne jest to, że system uwolniony od usług Google powinno się uruchomić właśnie na urządzeniach od Google. Jeżeli ktoś ma ochotę doczytać dlaczego to akurat Pixele są najlepsze dla GrapheneOS to polecam sprawdzić następujące słowa kluczowe - Verified Boot, Titan M, IOMMU, MTE.

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

_pogrubiłem te pozycje, które są nie tylko wspierane, ale też rekomendowane_

### Mój wybór smartfona
Na etapie wyboru urządzenia, na którym przetestuję GrapheneOS, nie miałem jeszcze pewności czy takie rozwiązanie w ogóle się dla mnie sprawdzi i czy wytrzymam z nim w dłuższej perspektywie. Toteż nierozsądnym byłoby wykładać sporą sumę pieniędzy. Z uwagi na to chyba jedynym sensownym wyborem był **Google Pixel 9a**. Było to parę miesięcy temu, gdy od premiery rodziny modeli 10 nie minęło jeszcze na tyle dużo czasu, aby trafiły one na listę urządzeń z pełnym wsparciem. Na tamten moment to Pixel 9a był najświeższym urządzeniem na liście i do tego był bardzo atrakcyjny cenowo, gdyż kupiłem go za ok. 1600 PLN.

Z perspektywy czasu dalej uważam to za dobry wybór i na pewno **polecam taką ściężkę każdemu** kto właśnie musi podjąć decyzję na jakim sprzęcie rozpocznie przygodę z GrapheneOS. Jedyne co mi trochę doskwiera w Pixelu 9a to jakość zdjęć jakie wykonuje. Przesiadłem się na niego mając wcześniej wyśmienite pod tym względem iPhone 15 Pro i Samsunga Galaxy Z Fold 6, więc nie można się dziwić, że jestem trochę zawiedziony, bo byłem po prostu przyzwyczajony do zupełnie innego poziomu aparatów. Teraz też wiem już, że GrapheneOS zostanie ze mną na dłużej, więc możliwe, że wiedząc wtedy to co wiem teraz, zdecydowałbym się na jakiś droższy sprzęt. Jednakże nie jest to dla mnie teraz istotne, bo na razie nie planuję przesiadki na inny sprzęt, a do momentu gdy się to zmieni na pewno zmieni się też sytuacja na rynku i lista dostępnych opcji. Poza tym jestem pozytywnie zaskoczony czasem pracy na baterii i ogólną wydajnością tego telefonu.

## Instalacja

### Potrzebujemy

1. Odpowiedni **smartfon** - w moim przypadku to Google Pixel 9a
2. **Kabel** do podłączenia telefonu do komputera, nie może to być byle jaki kabel tylko taki, który służy nie tylko do ładowania, ale także do transmisji danych
3. **Komputer z przeglądarką opartą na Chromium** (np. Google Chrome, Brave, Microsoft Edge), niestety muszę tutaj polecić Windows 10/11, bo nie trzeba się wtedy bawić z żadnymi sterownikami, jest to najprostsza opcja

### Przygotowanie telefonu

1. Jeżeli jest nowy to wyciągamy go z pudełka i **włączamy**. Jeżeli był wcześniej używany to **przywracamy go do ustawień fabrycznych** (Ustawienia -> System -> Opcje resetowania -> Wykasuj wszystkie dane (przywróć ustawienia fabryczne) -> Wykasuj wszystkie dane). Myślę, że to oczywista oczywistość, ale i tak to napiszę - przywrócenie ustawień fabrycznych skutkuje usunięciem wszystkich danych użytkownika z urządzenia, więc jeżeli masz na nim coś istotnego to należy zrobić tego kopię.
2. Musimy **przejść przez podstawową konfigurację** aż do momentu zobaczenia pulpitu. Robimy absolutne minimum czyli:
    - Na ekranie powitalnym możesz zmienić język na polski, ale nie ma takiej konieczności
    - Pomijamy konfigurację usług GSM (karta SIM)
    - Nie łączymy się z Wi-Fi, więc ten krok też pomijamy
    - Ustawienia daty i godziny powinny się zgadzać
    - Wyłączamy wszystkie Google Services (lokalizacja, skanowanie, wysyłanie danych diagnostycznych) i akceptujemy
    - Warunki gwarancji tu nie musimy nic robić, więc tylko przycisk Dalej
    - Akceptujemy Legal Terms
    - Ustawiamy jakiś łątwy PIN np. 12345
    - Nie ma potrzeby tracić czas na konfigurację biometrii, więc uprzejmie dziękujemy i rezygnujemy z odcisku palca i skanu twarzy
    - Chwila oczekiwania
    - Pomijamy samouczek
    - Swipe do góry i gotowe, jesteśmy na pulpicie
3. W pierwszej kolejności musimy się upewnić, że nasz **telefon jest zaktualizowany**. W tym celu idziemy do Ustawienia -> System -> Aktualizacja systemu. Jeżeli jest taka potrzeba to aktualizujemy.
4. Następnie przechodzimy do Ustawienia -> Informacje o telefonie -> znajdujemy pole Numer kompilacji i klikamy na to 7 razy aż zobaczymy komunikat **Jesteś teraz programistą**. W międzyczasie telefon poprosi o podanie PINu, który ustawiliśmy podczas konfigurowania telefonu.
5. Cofamy się i teraz wchodzimy do Ustawienia -> System -> Opcje programistyczne -> włączamy opcję **Zdjęcie blokady OEM**. Telefon znowu poprosi o PIN. Po jego podaniu musimy jeszcze potwierdzić, że na pewno chcemy zdjąć blokadę.

### Odblokowanie bootloadera

1. Proces odblokowania bootloadera rozpoczynamy od **wyłączenia telefonu**.
2. Gdy ekran całkiem zgaśnie **naciskamy jednocześnie i trzymamy przyciski zasilania (power) i zmniejszenia głośności (volume down)** aż do momentu, gdy pojawi nam się tekstowy interfejs **Fastboot Mode**. Jeżeli telefon uruchomi nam się normalnie to znaczy, że któryś z wcześniejszych kroków wykonaliśmy nieprawidłowo.
3. Podłączamy **telefon do komputera**.
4. Przechodzimy do komputera i wchodzimy w przeglądarce (opartej na silniku Chromium) na stronę pod adresem **[https://grapheneos.org/install/web](https://grapheneos.org/install/web)**.
5. Przechodzimy do sekcji [Unlocking the bootloader](https://grapheneos.org/install/web#unlocking-the-bootloader) i naciskamy przycisk **Unlock bootloader**.
6. W przeglądarce wyskoczy okienko z listą urządzeń do wyboru. Powinna na nim być w zasadzie tylko jedna opcja i to właśnie powinien być nasz Pixel. **Wybieramy go i naciskamy przycisk Połącz** (Connect).
7. Zajdą zmiany na wyświetlaczu telefonu. Pojawi się tam komunikat i prośba o potwierdzenie tego, że chcemy faktycznie odblokować bootloader. W tym celu musimy nacisnąć któryś przycisk głośności, tak aby zamiast **Do not unlock the bootlader** pojawiło się **Unlock the bootlader**. W tym momencie możemy potwierdzić poprzez naciśnięcie przycisku zasilania (power).
8. Jeżeli wszystko się udało to pośród danych wyświetlonych w Fastboot Mode powinniśmy widzieć **Device state: unlocked** (na czerwono).

### Pobieranie i wgrywanie obrazu systemu

1. Na stronie internetowej GrapheneOS przewijamy na dół do sekcji [Obtaining factory images](https://grapheneos.org/install/web#obtaining-factory-images) i naciskamy przycisk **Download release**. Jeżeli telefon jest dalej podłączony do komputera to strona sama zadecyduje, który obraz systemu należy pobrać.
2. Czekamy aż pobieranie zostanie zakończone. Oczywistym jest, że czas do tego potrzebny zależy wprost proporcjonalnie od prędkości połączenia internetowego.
3. Gdy pobieranie zostanie zakończone możemy przejść do sekcji [Flashing factory images](https://grapheneos.org/install/web#flashing-factory-images) poniżej i naciskamy **Flash release**.
4. Spluń teraz przez lewe ramie, wstrzymaj oddech i pod żadnym pozorem nie odpinaj telefonu od komputera Najlepiej w ogóle nie dotykaj obu urządzeń.
5. Gdy proces zostanie zakończony telefon zrestartuje się sam i wróci do interfejsu Fastboot Mode. W przeglądarce będziemy widzieli komunikat **Flashed ...**.

### Ponowne blokowanie bootloadera

Zablokowanie bootloadera jest kluczowe, ponieważ umożliwia pełne działanie funkcji Verified Boot (zweryfikowanego rozruchu). Uniemożliwia to również korzystanie z trybu fastboot do wgrywania (flashowania), formatowania lub wymazywania partycji. Verified Boot wykrywa wszelkie modyfikacje partycji systemu operacyjnego i blokuje odczyt jakichkolwiek zmienionych lub uszkodzonych danych. W przypadku wykrycia zmian system wykorzystuje dane korekcji błędów, aby spróbować odzyskać pierwotne dane, które są następnie ponownie weryfikowane – dzięki temu mechanizm system jest odporny na przypadkowe (niezłośliwe) uszkodzenia plików.

Jednakże przed ponownym zabezpieczeniem bootloadera zalecam sprawdzić czy system wgrał nam się prawidłowo i wszystko działa jak należy, bo jeżeli tak nie jest to blokując bootloader możemy sobie uceglić (całkowicie zablokować, a wręcz uszkodzić) telefon. Dlatego:

1. Będąc w Fastboot Mode, gdy widzimy komunikat **Start** to naciskamy przycisk zasilania (power), co spowoduje normalne uruchomienie systemu. Jeżeli na wysokości przycisku zasilania nie widzimy **Start** to musimy naciskać przyciski głośności i odszukać tę opcję.
2. Gdy telefon się uruchomi to możemy od razu wykonać podstawową konfigurację. Bootloader nam nie ucieknie.
3. To standardowa procedura, więc przejdziemy przez nią tylko hasłowo:
    - ekran powitalny,
    - wybieramy język,
    - wybieramy strefę czasową i tym samym ustawiamy datę i czas,
    - łaczymy się do Wi-Fi,
    - jeżeli masz taką możliwość to możesz od razu skonfigurować kartę SIM, ale możesz to też odłożyć na później,
    - polecam wyłączyć usługę lokalizacji, bo lepiej to później skonfigurować na spokojnie przydzielając uprawniania tylko aplikacjom, które naprawdę tego potrzebują,
    - zabezpieczenie telefonu poprzez odcisk palca, ja osobiście jestem zwolennikiem tego rozwiązania, więc rekomenduję używanie go, GrapheneOS nie obsługuje (jeszcze) odblokowywania skanem twarzym, więc odcisk palca i standardowe hasło to jedyne metody jakie mamy do wyboru (oczywiście odblokowanie wzorem odrzucam na starcie jako forma blokady ekranu, której nie można nawet z czystym sumiieniem nazwać jakimkolwiek zabezpieczeniem),
    - zakładam, że jeżeli czytasz ten wpis to jesteś grafenowym świeżakiem i nie masz żadnej kopii zapasowej do przywrócenia, więc ten krok po prostu pomijamy,
    - przycisk **Start** i jesteśmy na pulpicie.
4. Jeżeli wszystko działa prawidłowo to teraz śmiało możesz wyłączyć telefon i włączyć go trzymając przycisk zasilania (power) i zmniejszania głośności (volume down), tak jak to robiliśmy wcześniej.
5. Lądujemy znow w Fastboot Mode. Zakładam, że telefon był cały czas podłączony do komputera (jeżeli nie to podłącz go ponownie). Wracamy do przeglądarki na komputerze. Odnajdujemy sekcję [Locking the bootloader](https://grapheneos.org/install/web#locking-the-bootloader) i naciskamy przycisk **Lock bootloader**.
6. Znowu jest wymagane potwierdzenie tej operacji na telefonie. Wygląda to analogicznie jak przy odblokowywaniu z tym, że tym razem używając przycisków głośności musimy sprawić, aby aktywna była opcja **Lock the bootloader** i potwierdzić to przyciskiem zasilania (power).
7. Efektem powinna być zmiana **Device state** na **locked** (na zielono).

### Przywrócenie blokady OEM

Ostatnim krokiem przed tym jak zaczniemy się bawić nowym systemem jest ponowne nałożenie blokady OEM.

1. Tak jak przy zdejmowaniu blokady przechodzimy do Ustawienia -> Informacje o telefonie -> znajdujemy pole Numer kompilacji i klikamy na to 7 razy aż zobaczymy komunikat **Jesteś teraz programistą**. W międzyczasie telefon poprosi o podanie PINu, który ustawiliśmy podczas konfigurowania telefonu.
2. Cofamy się i teraz wchodzimy do Ustawienia -> System -> Opcje programistyczne -> wyłączamy opcję **Zdjęcie blokady OEM**. Telefon poprosi nas o restart w celu zmiany tego ustawienia, ale na ten moment anulujemy to żądanie, bo chcemy jeszcze wyłączyć całkowicie Opcje programisty, co robi się odznaczając ptaszek przy pierwszej opcji na samej górze **Używaj opcji programisty**.
3. Teraz możemy już zrestartować urządzenie.

## Moja wizja używania GrapheneOS

Teraz tak naprawdę zaczyna się prawdziwa zabawa. Ile osób tyle usłysz opinii na temat tego co powinno się robić, a czego nie w temacie hardeningu GrapheneOS. Jedni są bardzo konserwatywni, a inni podchodzą do tematu nieco bardziej liberalnie. Mi wydaje się, że nie ma jednej słusznej drogi i każdy powinien liznąć temat, poszperać, posprawdzać i zdecydować co mu odpowiada. Szybko przekonasz się, że GrapheneOS to tak naprawdę jeden wielki kompromis pomiędzy wygodą, a prywatnością. Ta sama zasada dotyczy wszystkiego co przynależy do świata cyfrowego.

Nie zamierzam tym wpisem promować jakiejś najmojszej metody używania GrapheneOS. Przedstawię jedynie jak ja używam tego systemu. W ten sposób może uda mi się komuś podpowiedzieć jakiś ciekawy trick jakiego nie znał, a z drugiej strony może trafi się jakiś ekspert, który po przeczytaniu moich wypocin podpowie mi coś ciekawego lub wskaże mi co robię źle / mógłbym robić lepiej.












## Wsparcie projektu

Na koniec chciałbym zachęcić do wsparcia projektu GrapheneOS. Deweloperzy stojący za nim wykonują naprawdę dobrą robotę i w mojej ocenie zasługują na rzucenie w nich odrobiną pieniędzy. Informację gdzie i jak można to zrobić znajdują się [tutaj](https://grapheneos.org/donate).