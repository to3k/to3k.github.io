---
title: "YunoHost - kopia zapasowa"
date: 2023-05-10
categories: 
  - "poradniki"
  - "self-hosting"
tags: 
  - "archivist"
  - "automatyzacja"
  - "backup"
  - "borgbackup"
  - "cron"
  - "crontab"
  - "kluczessh"
  - "kopiazapasowa"
  - "linux"
  - "nano"
  - "opensource"
  - "restic"
  - "scp"
  - "selfhosted"
  - "ssh"
  - "sshkeys"
  - "vps"
  - "yunohost"
  - "zadaniacron"
image: "/images/yunohostbackup.png"
description: "W poprzednich wpisach opisałem jak zainstalować środowisko YunoHost oraz jak uruchomić na nim pierwszą aplikacji - instancję WriteFreely. Następnym..."
---

Spis treści:
* TOC
{:toc}

W poprzednich wpisach opisałem [jak zainstalować środowisko _YunoHost_](https://blog.tomaszdunia.pl/yunohost-oracle/) oraz [jak uruchomić na nim pierwszą aplikacji - _instancję WriteFreely_](https://blog.tomaszdunia.pl/yunohost-writefreely/). Następnym naturalnym krokiem jaki wykonałby każdy rozsądny admin jest stworzenie systemu, który po pierwsze będzie tworzył kopie zapasowe uruchomionej infrastruktury, a po drugie zabezpieczy te kopie na wypadek, gdyby serwer, na którym jest to wszystko uruchomione, nagle stwierdził, że to dobry moment na sprawienie problemów.

Na początek dla ułatwienia zdefiniujmy sobie robocze nazewnictwo dla dwóch maszyn, których będę używał w tym wpisie:

- **_serwer z YunoHost_** - maszyna, na której zainstalowany jest _YunoHost_ i której kopię zapasową będziemy robić,

- **_serwer do backup'ów_** - dowolna inna maszyna z Linuxem, może to być komputer, serwer domowy lub VPS, na którym będziemy przechowywać stworzone kopie zapasowe.

## Zadania do wykonania na serwerze z YunoHost

Zacznijmy od połączenia się przez _SSH_ do serwera z _YunoHost_. Teraz stworzymy zadanie cykliczne, które w sposób zautomatyzowany będzie wykonywało dwie kopie dziennie. Jedna z nich będzie powstała o 5:00, a druga o 15:00. Zadanie tworzenia kopii zapasowej musi być wykonywane z uprawnieniami root, więc w pierwszej kolejności musimy przełączyć się właśnie na roota.

```bash
sudo su
```

Zostaniemy poproszeni o podanie hasła do naszego konta administratora _YunoHost_. Otwieramy tablicę zadań Cron, a raczej tworzymy ją, bo jeżeli wcześniej nie była używana to domyślnie nie istnieje:

```bash
crontab -e
```

Pojawi się krótki konfigurator, w którym musimy określić jakiego edytora tekstu chcemy użyć. Dla mnie domyślnym jest _nano_, więc wybieram opcję _1\. /bin/nano_, czyli wciskam _1_ i _ENTER_. Zostanie otwarta nasza tablica, na której początku będzie dość długi komentarz. Możemy całkowicie usunąć ten tekst lub po prostu go pominąć i przejść na koniec pliku. Tablica crontab działa tak, że jedno zadanie to jedna linijka, która składa się z formuły definiującej interwał (częstotliwość) uruchamiania oraz polecenia, programu lub ścieżki do skryptu, które mają zostać wykonane. Notacja formuły interwału składa się z pięciu części, kolejno – minuta, godzina, dzień miesiąca, miesiąc, dzień tygodnia. Bardzo pomocna tutaj jest strona [Crontab Guru](https://crontab.guru/). Dla naszego zadania polecenie w tablicy zadań Cron powinno wyglądać tak:

```bash
0 5,15 * * * yunohost backup create
```

Taka notacja oznacza, że polecenie _yunohost backup create_ (wbudowane w _YunoHost_ gotowe polecenie do wywołania tworzenia kopii zapasowej) będzie wykonywane w minucie 0, godzin 5 i 15, każdego dnia, każdego miesiąca, bez względu jaki to dzień tygodnia. Tablicę zamykamy tak samo jak zawsze wychodzimy z edytora tekstowego _nano_ (_ctrl+x_, _y_, _ENTER_).

Super istotne jest, aby na obu serwerach mieć zsynchronizowane strefy czasowe, dlatego dla pewności ustawmy strefę odpowiednią dla Polski:

```bash
timedatectl set-timezone Europe/Warsaw
```

Dodatkowo, po każdej zmianie w tablicy zadań Cron należy pamiętać, aby przebudować proces i tym samym wprowadzić zmiany w życie:

```bash
service cron reload
```

Na serwerze z _YunoHost_ pozostaje nam jeszcze włączyć logowanie przy użyciu kluczy _SSH_, bo bez tego ciężko będzie nam połączyć się z poziomu serwera do _backup'ów_. Jak to zrobić opisałem [tutaj](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja/#kluczessh).

To wszystko co mamy tutaj do zrobienia. Pora przejść na maszynę, która będzie naszą przestrzenią do przechowywania stworzonych kopii zapasowych.

## Zadania do wykonania na serwerze do backup'ów

Teraz przełączamy się na serwer do _backup'ów_. W pierwszej kolejności ustawmy również i tutaj strefę czasową odpowiednią dla Polski:

```bash
timedatectl set-timezone Europe/Warsaw
```

Skonfigurujmy teraz połączenie przez _SSH_ do serwera z _YunoHost_. W tym celu w folderze _/home/$USER/.ssh/_ stwórzmy plik _yunohost_ i wkleić do niego prywatny klucz _SSH_ do serwera z _YunoHost_:

```bash
nano /home/$USER/.ssh/yunohost
```

Plik zapisujemy i wychodzimy z niego. Nadajmy mu odpowiednie uprawnienia:

```bash
chmod 600 /home/$USER/.ssh/yunohost
```

Dodajmy ten klucz prywatny do naszego "pęku" kluczy:

```bash
ssh-add /home/$USER/.ssh/yunohost
```

Od tego momentu powinniśmy być w stanie z poziomu serwera do _backup'ów_ połączyć się przez _SSH_ do serwera z _YunoHost_, więc sprawdźmy to używając poniższego polecenia sformatowanego odpowiednio do swoich potrzeb:

ssh <nazwa\_admina>@<ip\_serwera\_z\_yunohost>

Jeżeli wszystko zrobiliśmy prawidłowo to nie powinniśmy zostać poproszeni o hasło i bez problemu uzyskać dostęp do powłoki serwera z _YunoHost_. Przerwijmy połączenie _SSH_ i wróćmy z powrotem na serwer do _backup'ów_ używając polecenia:

```bash
exit
```

Do pobierania kopii zapasowych z serwera z _YunoHost_ i przerzucania ich na serwer do _backup'ów_ użyjemy narzędzia _scp_, którego rozwinięcie nazwy to _Secure Copy_ (z ang. bezpieczne kopiowanie). Pozwala ono na proste i bezpieczne przenoszenie danych pomiędzy serwerami. Składnia _scp_ dla naszego zastosowania jest następująca:

> scp <nazwa\_admina>@<ip\_serwera\_z\_yunohost>:<co\_skopiować> <gdzie\_skopiować>

Znamy już mechanizm pozyskiwania plików z jednego serwera na drugi. Teraz trzeba zastanowić się nad strategią jak zamierzamy to robić. Przypomnijmy sobie, że na serwerze z _YunoHost_ mamy uruchomione zadanie tworzenia kopii zapasowej każdego dnia o godzinie 5:00 i 15:00. Tworzenie kopii zajmuje raczej mniej niż minutę, ale wraz ze wzrostem naszego środowiska _YunoHost_ ten czas może ulec wydłużeniu, a więc dla bezpieczeństwa przyjmijmy, że kopię zapasową będziemy pobierać godzinę po jej wykonaniu, czyli o 6:00 i 16:00.

Należy teraz zrozumieć jak _YunoHost_ zarządza kopiami zapasowymi. Do tworzenia kopii z poziomu terminala twórcy udostępnili gotowe polecenie:

```bash
yunohost backup create
```

Polecenie to musi zostać wykonane przez uprawnieniami administratora, a więc albo bezpośrednio z poziomu użytkownika _root_ albo poprzedzone frazą _sudo_. Taka składnia polecenia sprawi, że zostaną użyte domyślne ustawienia tego narzędzia, a więc zostanie stworzona kopia wszystkiego (konfiguracja systemu, dane użytkowników, aplikacje...), która zostanie zapisana w folderze:

```bash
/home/yunohost.backup/archives/
```

Nazwa pod jaką zostanie zapisana dana kopia ma następujący format:

> `<rok><miesiąc><dzień>-<godzina><minuta><sekunda>.tar`

Zatem jeżeli kopia powstanie _8 lipca 2023 o godzinie 12:34:56_ to będzie miała ona nazwę _20230708-123456.tar_. Dlaczego skupiam się na tym tak bardzo? Jest to istotne w kontekście tego jak będziemy określać, który plik ma zostać pobrany, a więc która kopia jest najnowszą i powinna zostać pozyskana, aby zająć miejsce obok już wcześniej pobranych kopii na serwer do _backup'ów_. Zauważ, że robiąc dwie kopie dziennie będę każdego dnia miał dwa pliki, których część nazwy przed myślnikiem będzie taka sama, bo to data. W takim razie można je rozróżnić tylko po drugiej części nazwy (tej po myślniku), czyli na podstawie godziny utworzenia. Zauważ, że celowo robię dwie kopie, z których pierwsza jest z 5:00, a więc po myślniku w nazwie będzie miała _0_ (_zero_), a druga jest z 15:00, a więc po myślniku w nazwie będzie miała _1_ (_jedynkę_). W ten sposób kopia o nazwie _20230708-0\*_ jest kopią poranną zrobioną _8 lipca 2023_, a kopia o nazwie _20230708-1\*_ jest kopią popołudniową. Użycie znaku _\*_ w _bash'u_ oznacza, że pozostała część nazwy może być dowolna.

Skoro mamy już wszystko zaplanowane to w takim razie przystąpmy do działania. Zacznijmy od utworzenia na serwerze do _backup'ów_ miejsca (folderu), w którym będziemy przechowywać pobrane kopie zapasowe.

```bash
mkdir /home/$USER/yunohost_backups
```

Teraz otwórzmy (lub utwórzmy jeżeli jeszcze nie istnieje) tablicę zadań Cron na tym serwerze:

```bash
crontab -e
```

Na końcu otwartego pliku tekstowego wstawmy takie dwie linijki:

```bash
0 6 * * * scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-0* /home/$USER/yunohost_backups/
0 16 * * * scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-1* /home/$USER/yunohost_backups/
```

Pamiętaj tylko, aby frazę _admin_ zamienić na nazwę swojego administratora _YunoHost_, a frazę _AAA.BBB.CCC.DDD_ na adres serwera z _YunoHost_. Plik zapisujemy i wychodzimy z niego. Powyższe dwie linijki wykonują prawie to samo tylko odpalają się o dwóch różnych porach (codziennie o 6:00 i 16:00). W przypadku obu następuje połączenie przez _scp_ z serwerem z _YunoHost_, znalezienie pliku, którego nazwa zaczyna się od dzisiejszej daty, następnie myślnika i w przypadku pierwszej linijki (odpalenie o 6:00) dalej mamy _0\*_ (zero i dowolne inne znaki), a w przypadku drugiej linijki (odpalenie o 16:00) dalej mamy _1\*_ (jedynka i dowolne inne znaki). Na końcu każdej z linijek jest jeszcze wskazanie ścieżki do folderu z kopiami zapasowymi na serwerze do _backup'ów_.

Tak samo jak wcześniej musimy po modyfikacji zadań Cron przeładować tą usługę:

```bash
service cron reload
```

## Jak zwykle czasem coś nie działa...

W moim przypadku jako serwer do _backup’ów_ wybrałem _Mikrusa_ i natrafiłem na ciekawy problem. Po jakimś czasie _Mikrus_ całkowicie zapomina mój klucz prywatny do serwera z _YunoHost_. I żeby tego było mało to jeszcze, gdy chciałem dodać go ponownie poleceniem _ssh-add_ to otrzymywałem komunikat:

```bash
Could not open a connection to your authentication agent.
```

To znany problem, gdy próbuje się użyć _ssh-add_, gdy _ssh-agent_ nie działa jako proces. Wychodzi na to, że proces _ssh-agent_ jest z jakiegoś powodu ubijany po pewnym czasie przez mój serwer… Czy jest to problem nie do rozwiązania? Ależ skąd! Trzeba jednak nieco zmodyfikować przedstawione przeze mnie działania.

W pierwszej kolejności muszę napisać dwa skrypty, które zastąpią mi te dwa zadania z tablicy zadań Crona. Te skrypty będą:

1. uruchamiały _ssh-agent'a_,

3. dodawały mój klucz prywatny do serwera z _Yunohost_ do pęku kluczy,

5. wykonywały polecenie kopiujące plik z kopią zapasową przy użyciu _scp_ tak jak to było wcześniej.

Najpierw tworzymy pierwszy skrypt, który będzie cyklicznie uruchamiany o 6:00:

```bash
nano /home/$USER/yunohost_backup1.sh
```

Wklejmy do niego następującą treść (pamiętaj oczywiście, aby zmodyfikować odpowiednio pod siebie frazy _admin_ i _AAA.BBB.CCC.DDD_):

```bash
#!/bin/bash
eval "$(ssh-agent)"
ssh-add /home/$USER/.ssh/yunohost
scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-0* /home/$USER/yunohost_backups/
```

Następnie tworzymy drugi skrypt:

```bash
nano /home/$USER/yunohost_backup2.sh
```

Wklejmy do niego następującą treść (pamiętaj oczywiście, aby zmodyfikować odpowiednio pod siebie frazy _admin_ i _AAA.BBB.CCC.DDD_):

```bash
#!/bin/bash
eval "$(ssh-agent)"
ssh-add /home/$USER/.ssh/yunohost
scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-1* /home/$USER/yunohost_backups/
```

Teraz musimy uczynić oba skrypty _wykonywalnymi_ (nadać im uprawnienia do wykonywania się):

```bash
sudo chmod +x /home/$USER/yunohost_backup1.sh /home/$USER/yunohost_backup2.sh
```

Na koniec musimy zmodyfikować jeszcze tablicę zadań Cron:

```bash
crontab -e
```

Zamiast wcześniej ustawionych dwóch linijek wklejamy takie:

```bash
0 6 * * * /home/$USER/yunohost_backup1.sh
0 16 * * * /home/$USER/yunohost_backup2.sh
```

Tak zmodyfikowany sposób działania rozwiązuje problem z _ssh-agent'em_.

## Alternatywne rozwiązania

Trzeba przyznać, że przedstawione przeze mnie rozwiązanie na pewno nie należy do najbardziej wykwintnych. Pokazuje ono jednak, że istnieje wiele sposobów jakimi można dojść do tego samego efektu. Jeżeli ktoś szuka innego sposobu to _YunoHost_ w swojej dokumentacji wspomina o trzech aplikacjach, z których można skorzystać: [BorgBackup](https://yunohost.org/en/backup/borgbackup), [Restic](https://yunohost.org/en/backup/restic) i [Archivist](https://yunohost.org/en/backup/archivist). Próbowałem skorzystać z tej ostatniej, ale zdaje się, że aktualnie jest ona uszkodzona i po prostu nie działa... Międzyinnymi dlatego postanowiłem wszystko ustawić od początku do końca po swojemu, bez polegania na aplikacjach zewnętrznych. Polecam jednak zapoznać się z dokumentacją _YunoHost_ i samemu zdecydować, która opcja dla Ciebie, drogi Czytelniku, wydaje się najlepsza.
