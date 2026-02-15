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

Z perspektywy czasu dalej uważam to za dobry wybór i na pewno polecam taką ściężkę każdemu kto właśnie musi podjąć decyzję na jakim sprzęcie rozpocznie przygodę z GrapheneOS. Jedyne co mi trochę doskwiera w Pixelu 9a to jakość zdjęć jakie wykonuje. Przesiadłem się na niego mając wcześniej wyśmienite pod tym względem iPhone 15 Pro i Samsunga Galaxy Z Fold 6, więc nie można się dziwić, że jestem trochę zawiedziony, bo byłem po prostu przyzwyczajony do zupełnie innego poziomu aparatów. Teraz też wiem już, że GrapheneOS zostanie ze mną na dłużej, więc możliwe, że wiedząc wtedy to co wiem teraz, zdecydowałbym się na jakiś droższy sprzęt. Jednakże nie jest to dla mnie teraz istotne, bo na razie nie planuję przesiadki na inny sprzęt, a do momentu gdy się to zmieni na pewno zmieni się też sytuacja na rynku i lista dostępnych opcji. Poza tym jestem pozytywnie zaskoczony czasem pracy na baterii i ogólną wydajnością tego telefonu.

## Instalacja

### Potrzebujemy

1. Odpowiedni **smartfon** - w moim przypadku to Google Pixel 9a
2. **Kabel** do podłączenia telefonu do komputera, nie może to być byle jaki kabel tylko taki, który służy nie tylko do ładowania, ale także do transmisji danych
3. **Komputer z przeglądarką opartą na Chromium** (np. Google Chrome, Brave, Microsoft Edge)

### Przygotowanie telefonu

1. Jeżeli jest nowy to wyciągamy go z pudełka i **włączamy**. Jeżeli był wcześniej używany to **przywracamy go do ustawień fabrycznych** (Ustawienia -> System -> Opcje resetowania -> Wykasuj wszystkie dane (przywróć ustawienia fabryczne) -> Wykasuj wszystkie dane).
2. Musimy przejść przez podstawową konfigurację aż do momentu zobaczenia pulpitu. Robimy absolutne minimum czyli:
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
3. W pierwszej kolejności musimy się upewnić, że nasz telefon jest zaktualizowany. W tym celu idziemy do Ustawienia -> System -> Aktualizacja systemu. Jeżeli jest taka potrzeba to aktualizujemy.
4. Następnie przechodzimy do Ustawienia -> Informacje o telefonie -> znajdujemy pole Numer kompilacji i klikamy na to 7 razy aż zobaczymy komunikat "Jesteś teraz programistą". W międzyczasie telefon poprosi o podanie PINu, który ustawiliśmy podczas konfigurowania telefonu.
5. Cofamy się i teraz wchodzimy do Ustawienia -> System -> Opcje programistyczne -> włączamy opcję Zdjęcie blokady OEM. Telefon znowu poprosi o PIN. Po jego podaniu musimy jeszcze potwierdzić, że na pewno chcemy zdjąć blokadę.










PODTYTUŁ:
## PODTYTUŁ

LINKI:
[TEKST](LINK)

POGRUBIENIE:
**GRUBE**

KURSYWA:
_POCHYLONE_

OBRAZ:
![](/images/OBRAZ.png)

KOD:
```JĘZYK
{% raw %}
TREŚĆ
{% endraw %}
```

LISTA:
- punkt1
- punkt2
- punkt3
1. numer1
2. numer2
3. numer3
