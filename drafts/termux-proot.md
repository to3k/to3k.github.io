---
layout: post
title: "Desktopowy Linux na każdym Androidzie"
published: true
categories: 
  - "poradniki"
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
image: "/images/termux-proot.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/termux-proot-eng/)

Spis treści:
* TOC
{:toc}

## Wstęp

Współczesne smartfony i tablety to potężne maszyny obliczeniowe, które większość czasu marnują na skrolowanie durnych filmików. Tymczasem w kieszeni nosimy moc porównywalną z ultrabookami. Największą barierą nie jest sprzęt, lecz system operacyjny Android, który choć oparty na jadrze Linux, skutecznie izoluje nas od profesjonalnych narzędzi.

Plan na dzisiaj to przełamanie bariery. Pokażę, jak wykorzystując środowisko **Termux**, warstwę **PRoot** oraz serwer grafiki **Termux-X11**, zmienić **dowolne urządzenie** z Androidem na pokładzie w **pełnoprawną stację roboczą z Linuxem**, środowiskiem XFCE i VS Code. Wszystko to **bez** odblokowywania bootloadera i **bez** utraty gwarancji.

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
* **Dysk** - przynajmniej 10-15 GB wolnej przestrzeni na system i pliki projektów.

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











### Krok 2 - Przygotowanie Termuxa
Otwórz Termux i przygotuj repozytoria:
```bash
pkg update && pkg upgrade -y
termux-setup-storage
pkg install proot-distro git wget -y
```

### Krok 3: Instalacja dystrybucji i środowiska graficznego
Zainstalujemy Ubuntu, które jest najbardziej przyjazne dla początkujących i posiada najlepsze wsparcie dla VS Code:
```bash
proot-distro install ubuntu
proot-distro login ubuntu
```
Teraz jesteś wewnątrz Ubuntu. Zainstalujmy pulpit XFCE4:
```bash
apt update && apt upgrade -y
apt install xfce4 xfce4-goodies dbus-launch -y
```

---

## 4. Instalacja VS Code: Prawdziwe IDE na tablecie

To najważniejszy punkt dla każdego dewelopera. VS Code na ARM64 działa znakomicie, o ile wiesz, jak go zainstalować.

### Pobieranie paczki
Będąc w terminalu Ubuntu (proot), pobierz wersję `.deb` dla architektury ARM64:
```bash
wget "[https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64](https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64)" -O vscode.deb
```

### Instalacja
```bash
apt install ./vscode.deb -y
```

### Uruchamianie (Pułapka Sandboxa)
Silnik Electron, na którym bazuje VS Code, wymaga piaskownicy (sandbox), która nie jest wspierana w środowisku PRoot. Aby uruchomić edytor, musisz dodać flagę `--no-sandbox`:
```bash
code --no-sandbox
```
**Tip:** Dodaj alias do pliku `~/.bashrc`, aby móc wpisywać po prostu `code`:
`echo "alias code='code --no-sandbox'" >> ~/.bashrc`

---

## 5. Uruchomienie środowiska graficznego

1. Wróć do głównego terminala Termux (wyjdź z Ubuntu wpisując `exit`).
2. Uruchom aplikację **Termux-X11** na telefonie.
3. W Termuxie wpisz komendy startowe (przykładowy schemat):
```bash
proot-distro login ubuntu --shared-tmp -- env DISPLAY=:1 dbus-launch xfce4-session
```
4. Przełącz się na aplikację Termux-X11 – Twoim oczom ukaże się pełny pulpit Linuxa.

---

## 6. Co możesz robić na takim zestawie?

Możliwości są praktycznie identyczne jak na standardowym laptopie z Linuxem:

* **Full-stack Development:** Możesz bez problemu uruchomić Node.js, Pythona, Go czy PHP. VS Code obsługuje wszystkie Twoje ulubione wtyczki.
* **Praca z Git:** Pełna obsługa repozytoriów, kluczy SSH i narzędzi typu GitKraken (w wersji Linux).
* **Desktopowa Przeglądarka:** Instalując Firefoxa lub Chromium przez `apt`, zyskujesz dostęp do pełnych narzędzi deweloperskich (DevTools), których brakuje w mobilnym Chrome.
* **Centrum Deweloperskie:** Po podłączeniu tabletu do monitora przez USB-C (HDMI) oraz sparowaniu klawiatury i myszy, otrzymujesz stację roboczą, która zużywa ułamek energii tradycyjnego PC, a oferuje pełną moc terminala Linux.

## Podsumowanie

Przekształcenie Androida w Linuxowe centrum deweloperskie to nie tylko efektowny pokaz możliwości sprzętu. To realne narzędzie dla osób, które chcą pracować w podróży, na kawie, czy w terenie, mając pod ręką dokładnie to samo środowisko, którego używają na desktopie. Dzięki PRoot i Termux-X11, granica między "zabawką do multimediów" a "narzędziem pracy" została ostatecznie zatarta.