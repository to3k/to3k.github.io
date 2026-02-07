---
title: "Darmowa chmura ~200GB na Twoje pliki"
date: 2024-10-06
categories: 
  - "poradniki"
  - "self-hosting"
tags: 
  - "cloudflare"
  - "docker"
  - "dockerhub"
  - "dockerio"
  - "freetier"
  - "freedns42"
  - "https"
  - "iptables"
  - "letsencrypt"
  - "linux"
  - "mariadb"
  - "mysql"
  - "nextcloud"
  - "nginxproxymanager"
  - "opensource"
  - "oracle"
  - "portainer"
  - "putty"
  - "selfhosted"
  - "ssh"
  - "ssl"
  - "termius"
  - "ubuntu"
  - "ufw"
  - "vps"
coverImage: "/images/Darmowa-chmura-200GB.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/darmowa-chmura-200gb-eng/)

Mój wpis o [darmowym serwerze _VPS_ od _Oracle_](https://blog.tomaszdunia.pl/oracle-free-tier/) jest prawdziwym **hitem tego bloga**. Patrząc na statystyki ma więcej odsłon niż wszystkie inne wpisy razem wzięte. Nic w tym dziwnego, gdyż chyba każdy lubi czasem trochę przycebulić i **dostać coś fajnego za darmo**. Oczywiście będą tutaj głosy mówiące, że jak coś jest za darmo to towarem jesteśmy tak naprawdę my, a może raczej nasze dane. Pewnie tak, ale przyznam szczerze, że ja osobiście nie zastanawiałem się dwa razy decydując się na skorzystanie z tej **ciekawej promocji _Oracle_**, w której można otrzymać tak naprawdę **trzy serwery** - jeden z **4-rdzeniowym procesorem o 24GB RAMu** oparty o architekturę _ARM_, oraz **dwa o znacznie słabszej mocy procesora (1/8 OCPU) i tylko 1GB RAM** oparte na architekturze _AMD_. Ten pierwszy to **prawdziwa kobyła, na której można zrobić naprawdę wiele kozackich rzeczy**, a dwa pozostałe to takie satelity, które **świetnie sprawdzają się jako poligony treningowe lub dla mniejszych projektów**. Co ciekawe w zeszłym tygodniu orałem moją całą infrastrukturę _Oracle_ i stawiałem od zupełnego zera, co dało mi możliwość sprawdzenia czy opisany przeze mnie sposób dalej działa i muszę z przyjemnością powiedzieć, że tak. Zatem oficjalnie odpowiadam na wiele zadanych mi w ostatnich miesiącach pytań - **tak, serwery w ramach _Always Free Tier_ są dalej normalnie dostępne, a mój [poradnik](https://blog.tomaszdunia.pl/oracle-free-tier/) aktualny**.

## Co ciekawego zrobimy dzisiaj?

W dzisiejszym wpisie na tym darmowym _VPS_ od _Oracle_ **postawimy prywatną chmurę na pliki, na której będziemy mogli przechowywać do blisko 200 GB danych**. Zrobimy to poprzez uruchomienie kontenera _Docker_, w którego środku będzie _Nextcloud_, a zrobimy to przy użyciu _Portainer_. Do tego podepniemy do niego własną domenę, do czego wykorzystamy _NGINX Proxy Manager_, który będzie uruchomiony jako oddzielny kontener, oraz _Cloudflare_ (choć dla chętnych, a raczej niechętnych do _CF_, opiszę również jak to zrobić przez _FreeDNS::24_). Oczywiście zadbamy także o szyfrowanie komunikacji, czyli _SSL/HTTPS_, co zrealizujemy również przez _NGINX Proxy Manager_ używając certyfikatu _Let's Encrypt_.

## Spis treści

1. [Pozyskanie darmowego serwera VPS od Oracle](#oracle)

3. [Wstępna konfiguracja serwera](#conf)

5. [Zapora sieciowa](#firewall)

7. [Docker i Portainer](#portainer)

9. [Podpięcie domeny przez Cloudflare](#cloudflare)

11. [Alternatywne rozwiązanie z FreeDNS::42 zamiast Cloudflare](#freedns42)

13. [NGINX Proxy Manager](#nginx)

15. [Nextcloud i MariaDB](#nextcloud)

17. [Zamykanie portów (aktualizacja 07-10-2024)](#cleanup)

## Pozyskanie darmowego serwera VPS od Oracle

Jeżeli nie masz jeszcze takiego serwera to cały proces opisałem naprawdę bardzo szczegółowo w [oddzielnym wpisie](https://blog.tomaszdunia.pl/oracle-free-tier/). Na potrzeby tego poradnika proponuję utworzyć sobie instancję o następujących parametrach:

- domena - **_EU-Frankfurt-1_** (ja ostatnio nie miałem problemów z uzyskaniem _VPS_ dokładnie z domeny **_AD2_**),

- Shape (typ maszyny) - zakładka _Virtual Machine_ i dalej _Ampere_, gdzie wybieramy konkretnie **_VM.Standard.A1.Flex_**,

- Image (obraz systemu) - **_Ubuntu 22.04_**, które zaktualizujemy do _24.04 LTS_ podczas początkowej konfiguracji, bo z niewiadomych mi przyczyn _Oracle_ podaje, że _24.04 LTS_ nie działa z tym typem maszyny na _ARM_ (co jest nieprawdą i udowodnię to) i po prostu nie pozwala od razu zacząć od tego systemu,

- CPU - **4 rdzenie**,

- RAM - **24GB**, na potrzeby _Nextcloud_ nie potrzebujemy aż tyle, ale nie ograniczajmy się i bierzmy maksymalną ilość, którą dają, bo w przyszłości pozwoli nam to na uruchomienie również innych rzeczy,

- **publiczny adres _IPv4_** - pamiętaj, aby przypisać go do maszyny już podczas jej tworzenia co uprości cały proces, rozważ także przypisanie adresu _IPv6_, bo może Ci się przydać w przyszłości,

- **klucze SSH** - _Oracle_ nie da Ci bez tego ruszyć dalej, co jest dobrą praktyką, więc po prostu zrób nowy klucz i go zapisz lub skorzystać ze swojego i podaj go _Oracle_,

- pojemność dysku - (określa się to w sekcji _Boot volume_ po zaznaczeniu _Specify a custom boot volume size_) - za darmo możemy dostać **maksymalnie 200GB do podziału na wszystkie maszyny**, możesz przypisać wszystko do tej maszyny _ARM_ albo podzielić to jakoś, tak aby również dla tych dwóch _AMD_ coś zostało,

- szyfrowanie komunikacji pomiędzy instancją i magazynem - zaznacz opcję _**Use in-transit encryption**_.

## Wstępna konfiguracja serwera

Zaczynamy standardowo o połączenia się z wcześniej utworzoną instancją. Ja przeważnie używam do tego celu aplikacji [_Termius_](https://termius.com/), ale możesz też użyć _[PuTTY](https://www.putty.org/)_ lub dowolnego innego sposobu pozwalającego na nawiązanie komunikacji _SSH_. To jak łączyć się z serwerami poprzez _SSH_ opisałem w [tym wpisie](https://blog.tomaszdunia.pl/serwer-domowy/#ssh). Natomiast w [tym wpisie](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja/#kluczessh) to jak używać kluczy _SSH_. Nie będę tego wszystkie powtarzał jeszcze raz. Skupimy się tutaj jedynie na tym co dla konkretnego przypadku jest nieoczywiste. Do połączenia przez _SSH_ potrzebujemy w zasadzie czterech rzeczy:

1. Adresu _IP_ serwera

3. Nazwy użytkownika, na którego się zalogujemy

5. Publicznego klucza _SSH_

7. Prywatnego klucza _SSH_

Pierwsza dwa uzyskamy poprzez wejście do centrum zarządzania instancjami _Oracle_. Po poprawnym jej utworzeniu powinniśmy w tym miejscu widzieć ją na liście naszych instancji, więc wejdźmy do jej właściwości \[1\].

![](/images/oracle40.png)

Szukane przez nas informacje (adres IP serwera \[2\] i nazwa użytkownika \[3\]) znajdują się w zakładce _Instance information_ w sekcji _Instance access_ po prawej stronie.

![](/images/oracle41.png)

Wymagane do uwierzytelniania klucze _SSH_ pobraliśmy już na dysk podczas tworzenia instancji. Mamy już wszystko, więc teraz trzeba tylko to wszystko wrzucić do _Termius'a_ (lub użyć innego programu) i połączyć się z naszym nowiusieńkim _VPSem_.

Teraz przeprowadzimy **podstawową konfigurację serwera**. Zaczniemy oczywiście od aktualizacji pakietów. Po jej zakończonej można rozważyć restart serwera.

```bash
sudo apt update
sudo apt upgrade -y
sudo reboot now
```

Z oczywistych przyczyn zostaniem rozłączeni z serwerem, poczekajmy chwilę na jego ponowne uruchomienie i wznówmy połączenie _SSH_. Teraz przystąpimy to aktualizacji systemu Ubuntu z wersji 22.04 do 24.04 LTS.

```bash
sudo do-release-upgrade
```

Cały proces jest intuicyjny, więc nie będę go szczegółowo opisywał w tym miejscu. Może kiedyś zrobię o tym oddzielny wpis, jeżeli faktycznie okaże się, że w narodzie jest taka potrzeba. Jeżeli potrzebujesz potwierdzenia, że aktualizacja przebiegła pomyślnie to możesz użyć komendy:

```bash
lsb_release -a
```

Wynik działania polecenia powinien wyglądać mniej więcej tak:

```bash
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.1 LTS
Release:        24.04
Codename:       noble
```

W ramach podstawowej konfiguracji zawsze sprawdzam jeszcze ustawienia autoryzacji poprzez _SSH_, bo przeważnie nie jest to ustawione tak jak lubię. Dlatego wchodzimy do edytora tekstu i zmieniamy zapisy w pliku _sshd\_config_.

```bash
sudo nano /etc/ssh/sshd_config
```

Musimy w nim znaleźć odpowiednie wiersze i zmienić ich wartość na te poniżej. Uwaga, wskazane linie mogą nie tylko nie być jedna pod drugą, ale także występować w innej kolejności.

```bash
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
PasswordAuthentication no
```

## Zapora sieciowa

Ja korzystając z _Oracle_ używam tak naprawdę **trzypoziomowej zapory**. Pierwszym poziomem jest **zapora w samej infrastrukturze _Oracle_**. Druga to _**iptables**_ na serwerze, a trzecia to pakiet _**ufw**_, który doinstalowuję zawsze we własnym zakresie. Skonfigurujmy je jedna po drugiej.

To jak otwierać porty w infrastrukturze _Oracle_ opisałem w [tym wpisie](https://blog.tomaszdunia.pl/oracle-free-tier/#porty). W turbo skrócie robi się to wchodząc w _Virtual Cloud Networks_ (pamiętam, aby najpierw wybrać odpowiedni _Compartment_) -> na liście znajdujemy naszą sieć i wchodzimy do jej właściwości -> z menu _Resources_ po lewej wybieramy _Security Lists_ -> na liście powinna być tylko jedna nazwana _Default Security List for..._. Interesują nas w tym miejscu _Ingress Rules_ i korzystając z przycisku _Add Ingress Rules_ dodajemy reguły otwierające **porty 80, 443, 81, 444, 9443**. Robimy to wypełniając formularz dla każdego z portów analogicznie do poniższego, w którym zademonstrowałem jak zrobić to dla portu 80.

![](/images/obraz-300x215.png)

W ten sposób otworzyliśmy następujące porty:

- **80** - standardowy _HTTP_ dla _NGINX Proxy Manager_,

- **443** - standardowy _HTTPS_ dla _NGINX Proxy Manager_,

- **81** - port _HTTP_ dla panelu administracyjnego _NGINX Proxy Manager_,

- **444** - port _HTTPS_ dla _Nextcloud_,

- **9443** - port _HTTPS_ dla _Portainer_.

To wszystko co należy zrobić po stronie _Oracle_. Kolejnym krokiem jest aktualizacja _iptables_ na serwerze. Jest to taka wewnętrzna tablica z regułami sieciowymi, która określa jaki ruch z i do serwera jest dozwolony, a jaki nie. Przechodzimy na serwer i korzystamy z następujących komend:

```bash
sudo su
nano /etc/iptables/rules.v4
```

W ten sposób otworzy nam się edytor tekstu. Odszukujemy wiersz:

```bash
(...)
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
(...)
```

Zaraz po nim dodajemy nowe wiersze o następującej treści:

```bash
-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 81 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 444 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 9443 -j ACCEPT
```

Plik _rules.v4_ zapisujemy i zamykamy poprzez użycie "control + x", "y" i ENTER. Zostało nam jeszcze skonfigurowanie ostatniej bramy, czyli aplikacji _ufw_.

```bash
sudo apt install ufw
sudo ufw disable
sudo ufw reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 81
sudo ufw allow 444
sudo ufw allow 9443
sudo ufw enable
sudo ufw status verbose
```

Finalny wynik powinien wyglądać tak:

```bash
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
-- ------ ----
22                         ALLOW IN    Anywhere                  
80                         ALLOW IN    Anywhere                  
443                        ALLOW IN    Anywhere                  
444                        ALLOW IN    Anywhere                  
81                         ALLOW IN    Anywhere                  
9443                       ALLOW IN    Anywhere                  
22 (v6)                    ALLOW IN    Anywhere (v6)             
80 (v6)                    ALLOW IN    Anywhere (v6)             
443 (v6)                   ALLOW IN    Anywhere (v6)             
444 (v6)                   ALLOW IN    Anywhere (v6)             
81 (v6)                    ALLOW IN    Anywhere (v6)             
9443 (v6)                  ALLOW IN    Anywhere (v6) 
```

Dla pewności należy jeszcze upewnijmy się, że usługa _ufw_ będzie uruchamiana wraz ze startem systemu (np. po restarcie). Ta opcja powinna się włączyć sama, ale zawsze dobrze sprawdzić to we własnym zakresie. Wchodzimy do pliku konfiguracyjnego _ufw_:

```bash
sudo nano /etc/ufw/ufw.conf
```

Interesuje nas tutaj, aby zmienna _ENABLED_ była ustawiona na _yes_:

```bash
# Set to yes to start on boot. If setting this remotely, be sure to add a rule 
# to allow your remote connection before starting ufw. Eg: 'ufw allow 22/tcp' 
ENABLED=yes
```

Teraz pozostaje już tylko zrestartować maszynę.

```bash
sudo reboot now
```

## Docker i Portainer

Opisałem to szczegółowo w [oddzielnym wpisie](https://blog.tomaszdunia.pl/portainer/), więc tutaj przejdę tylko na szybko w ramach przypomnienia.

```bash
sudo apt install docker.io -y
sudo groupadd docker
sudo usermod -aG docker $USER
```

Docker zainstalowany, więc przechodzimy do stworzenia wolumenu na dane _Portainer'a_.

```docker
docker volume create portainer_data
```

Następnym krokiem jest już utworzenie odpowiednio skonfigurowanego kontenera.

```docker
docker run -d \
-p 9443:9443 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
--name Portainer \
--restart unless-stopped \
portainer/portainer-ce:latest
```

_Portainer_ został uruchomiony na porcie 9443, więc teraz musimy odszukać jeszcze raz adres serwera, który wykorzystywaliśmy do połączenia _SSH_, wejść do przeglądarki i w pasek adresu wpisać:

> https://<ip\_vpsa\_oracle>:9443

Naszym oczom ukaże się bardzo prosty instalator, w którym wystarczy ustawić jedynie login i hasło dla administratora. Na następnej stronie wybieramy przycisk _Get Started_ jako, że chcemy, aby _Portainer_ używał środowiska znajdującego się na maszynie lokalnej, na której jest uruchomiony. Finalnie zostaniemy przeniesieni do listy dostępnych środowisk, na której będzie jedynie jedno o nazwie _local_ (z ang. lokalne). Aby rozpocząć zarządzanie tym środowiskiem należy po prawej stronie nacisnąć niebieski przycisk _Live connect_. Poskutkuje to tym, że po lewej stronie zamiast _Environment: None selected_ pojawią się nam zakładki z opcjami do zarządzania.

![](/images/portainer1.png)
    
![](/images/portainer2.png)
    
![](/images/portainer3.png)
    

## Podpięcie domeny przez Cloudflare

1. Logujemy się na [Cloudflare.com](https://cloudflare.com) i naciskamy przycisk _Add a domain_.

3. Wpisujemy adres posiadanej przez nas domeny, w moim przypadku jest to przykładowe _exampleforblog.com_. Wybieramy _Manually enter DNS records_, bo chcemy zaczynać od czystej karty bez zbędnego zgadywania _CF_ jakie rekordy chcemy mieć. Potwierdzamy przyciskiem _Continue_.

5. Na następnej stronie przewijamy na dół, bo plan (oczywiście jedyny słuszny, czyli darmowy), który nas interesuje jest na samym końcu.

7. Wybieramy plan _Free_ i potwierdzamy przyciskiem _Continue_.

9. Na kolejnej stronie przewijamy niżej do informacji, które nas interesują.

11. W pierwszej kolejności _CF_ prosi nas o wyłączenie funkcji _DNSSEC_ u naszego dostawcy domen. Nie wszyscy dostawcy włączają to z automatu, ale przykładowo takie _OVH_ chyba właśnie tak robi, więc uznałem, że warto o tym wspomnieć.

13. Na tej samej stronie, ale niżej, _CF_ listuje nam dwa adresy _DNS_, do których mamy skierować cały ruch z posiadanej przez nas domeny. Robi się to na stronie dostawcy domeny.

15. Z menu po lewej wybieramy zakładkę _DNS_ i następnie _Records_. Zaczynamy dodawanie rekordów przyciskiem _Add record_.

17. W _Type_ zostawiamy _A_ (tak jak jest domyślnie). W pole _Name_ wpisujemy _portainer_. W _IPv4 address_ podajemy adres naszego serwera _VPS_ od _Oracle_, goły adres bez żadnych portów, czyli np. _101.102.103.104_ (oczywiście zmyśliłem ten adres, więc tutaj wpisz swój). Chcemy, aby ruch był przepuszczany przez _CF_, więc zostawiamy ustawienie _Proxied_. _TTL_ nie da się zmienić, więc zostaje _Auto_. W polu _Comment_ na dole możemy wpisać dowolny komentarz, który pozwoli nam w przyszłości zorientować się o co chodzi i skąd wziął się ten rekord. Napisz po prostu swoimi słowami to co chcesz i do czego będziesz używać tego rekordu. Na koniec pozostaje tylko potwierdzić przyciskiem _Save_.

19. Pierwszy rekord dodany, ale na potrzeby tego poradnika będziemy potrzebować w sumie trzech, więc dodajemy kolejne korzystając ponownie z przycisku _Add record_.

21. W ten sposób dodajemy jeszcze analogicznie rekordy dla _Name_ - _cloud_ i _nginx_. To co zrobiliśmy teraz to utworzyliśmy trzy subdomeny dla domeny macierzystej. Są to odpowiednio _portainer.exampleforblog.com_, _cloud.exampleforblog.com_ i _nginx.exampleforblog.com_.

23. Wracamy do menu po lewej i tym razem wybieramy zakładkę _SSL/TLS_, a z niej _Overview_. W sekcji podpisanej _SSL/TLS encryption_ naciskamy przycisk _Configure_.

25. W okienku podpisanym _Custom SSL/TLS_ naciskamy przycisk _Select_.

27. Zmieniamy opcję z _Full_ na _Flexible_ i potwierdzamy wybór przyciskiem _Save_.

29. W ramach tej samej zakładki z menu po lewej wybieramy _Edge Certificates_. Odnajdujemy okienko podpisane _Always Use HTTPS_ i włączamy tą funkcję.

31. Zjeżdżamy niżej, znajdujemy _Automatic HTTPS Rewrites_ i również włączamy tą funkcję.

![](/images/cf1.png)
    
![](/images/cf2.png)
    
![](/images/cf3.png)
    
![](/images/cf4.png)
    
![](/images/cf5.png)
    
![](/images/cf6.png)
    
![](/images/cf7.png)
    
![](/images/cf8a.png)
    
![](/images/cf9.png)
    
![](/images/cf10.png)
    
![](/images/cf10a.png)
    
![](/images/cf11.png)
    
![](/images/cf12.png)
    
![](/images/cf13.png)
    
![](/images/cf14.png)
    
![](/images/cf15.png)
    

Gotowe. Możemy się już wylogować z _Cloudflare_ i przejść do następnego kroku.

## Alternatywne rozwiązanie z FreeDNS::42 zamiast Cloudflare

To samo co w _Cloudflare_ można uzyskać poprzez skorzystanie np. z _[FreeDNS::42](https://freedns.42.pl)_ lub innego narzędzia tego rodzaju.

1. Zaczynamy od zalogowania się do swojego konta na _FreeDNS::42_. Przychodzimy do _Utwórz strefę_.

3. Jako _Nazwa strefy_ podajemy naszą domenę. Jako _Typ strefy_ wybieramy _Podstawowe_. Naciskamy przycisk _Utwórz_.

5. Nowa strefa utworzona, więc przechodzimy do _zakładki modyfikacji_.

7. Przewijamy na dół...

9. ... aż znajdziemy sekcję _Rekordy (NS) serwerów DNS_. Widnieją w niej dwa adresy _fns1.42.pl_ i _fns2.42.pl_. Na te adresy DNS mamy skierować cały ruch z posiadanej przez nas domeny. Robi się to na stronie dostawcy domeny.

11. Na tej samej stronie przewijamy jeszcze trochę aż do sekcji _Rekordy adresów (A)_, gdzie dodajemy trzy rekordy, które w kolumnie _Nazwa_ będą miały wartości kolejno _portainer_, _nginx_ i _cloud_, natomiast w kolumnie _IP_ podajemy trzy razy adres naszego serwera _VPS_ od _Oracle_.

13. Taką konfigurację finalizujemy przyciskiem _Utwórz konfigurację strefy_, który znajduje się na samym dole.

15. Na koniec zostanie nam wyświetlone podsumowanie, na którym możemy sprawdzić czy wszystko się zgadza.

![](/images/fdns1.png)
    
![](/images/fdns2.png)
    
![](/images/fdns3.png)
    
![](/images/fdns4.png)
    
![](/images/fdns5.png)
    
![](/images/fdns6.png)
    
![](/images/fdns7.png)
    
![](/images/fnds8.png)
    

## NGINX Proxy Manager

_NGINX Proxy Manager_ posłuży do odpowiedniego **kierowania ruchem trafiającym do naszego serwera za pośrednictwem domeny**, którą dodaliśmy przed chwilą w _Cloudflare_/_FreeDNS::42_. Chodzi o to, żeby np. ruch z subdomeny _portainer.exampleforblog.com_ trafił dokładnie na port 9443, czyli tam gdzie uruchomiony jest panel administratora _Portainer'a_. _NGINX Proxy Manager_ to dużym uproszczeniu **taki drogowskaz**.

Uruchomienie kontenera z _NGINX Proxy Manager'em_ rozpoczynamy od zalogowania się do panelu administratora _Portainer_. W sekcji _Environments_ wybieramy _local_ i naciskamy przycisk _Live connect_. Z menu po lewej wybieramy _Stacks_. Naciskamy przycisk _Add stack_. W polu _Name_ wpisujemy _nginx\_proxy\_manager_. W sekcji _Build method_ zostawiamy domyślne _Web editor_. W obszar tekstowy _Web editor_ wklejamy ten gotowy kod:

```docker
version: '3.8'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80' # Public HTTP Port
      - '443:443' # Public HTTPS Port
      - '81:81' # Admin Web Port
    volumes:
      - /var/lib/docker/volumes/nginx_proxy_manager/data:/data
      - /var/lib/docker/volumes/nginx_proxy_manager/letsencrypt:/etc/letsencrypt
```

Pokrótce go skomentuję. Korzystamy z obrazu _[jc21/nginx-proxy-manager](https://hub.docker.com/r/jc21/nginx-proxy-manager)_, który zostanie pobrany z _Docker Hub_. Kontener będzie automatycznie restartowany po każdym zatrzymaniu, chyba że sami ręcznie go zatrzymamy. Będzie używać portów 80 (HTTP), 443 (HTTPS) i 81. Pod tym ostatnim dostępny będzie panel administratora. To właśnie na niego wskażemy subdomeną _nginx.exampleforblog.com_. Tworzymy dwa wolumeny, którymi wyciągniemy z kontenera foldery _/data_ (dane dot. konfiguracji) i _/etc/letsencrypt_, czyli miejsce, w którym zapisane będą certyfikaty _SSL_.

Po wklejeniu tego kodu niewiele więcej musimy robić, bo wystarczy tylko utworzyć tak skonfigurowany kontener korzystając z przycisku _Deploy the stack_ znajdującego się w sekcji _Actions_ na samym dole. Robienie tego z poziomu _Stacks_ ma tą zaletę, że za jednym razem załatwiamy wszystko, czyli tworzymy kontener oraz wolumeny potrzebne do jego działania.

Przejdźmy teraz do panelu administratora _NGINX Proxy Manager'a_. Wchodzi się tam przez przeglądarkę wpisując w pasek adresu:

> https://<ip\_vpsa\_oracle>:81

Przywita nas od razu formularz logowania. Ale jaki jest login i hasło? Na pomoc przychodzi nam dokumentacja, w której podane jest, że kontener tworzony jest z domyślnymi poświadczeniami, które po pierwszym logowaniu jesteśmy zmuszeni zmienić. Są to:

```
Email:    admin@example.com
Password: changeme
```

Logujemy się przy ich pomocy i od razu tworzymy nowego administratora na podstawie już wprowadzonych przez siebie danych. Przechodzimy do zakładki _Hosts_, która znajduje się na pasku na górze, i wybieramy _Proxy Hosts_. Korzystając z przycisku _Add Proxy Host_ dodajemy pierwszego. W pole _Domain Names_ wpisujemy _portainer.exampleforblog.com_ (oczywiście _exampleforblog.com_ zamień na swoją domenę). W _Scheme_ wybieramy _https_. W _Forward Hostname / IP_ wpisujemy **lokalny** adres IP swojego serwera. Aby go poznać potrzebujemy zainstalować _net-tools_:

```bash
sudo apt install net-tools
```

I użyć polecenia:

```bash
ifconfig
```

Poszukiwany adres będzie znajdował się w sekcji _enp0s6_. Tak wygląda wycinek z wyniku działania komendy _ifconfig_.

```bash
enp0s6: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9000
        inet 10.0.0.195  netmask 255.255.255.0  broadcast 10.0.0.255
        inet6 ...  prefixlen 128  scopeid 0x0<global>
        inet6 ...  prefixlen 64  scopeid 0x20<link>
        ether 02:00:17:06:21:40  txqueuelen 1000  (Ethernet)
        RX packets 335922  bytes 763693420 (763.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 301753  bytes 418933520 (418.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Adres, którego szukamy to w moim przypadku _10.0.0.195_ (u Ciebie prawie na pewno będzie inny). Pozostaje nam jeszcze wpisać _9443_ w polu _Forward Port_. Prawidłowo wypełniony formularz w moim wypadku wygląda tak:

![](/images/obraz-3-273x300.png)

Ale to nie koniec, bo musimy jeszcze przeskoczyć z zakładki _Details_ do _SSL_, gdzie z menu rozwijanego podpisanego _SSL Certificate_ wybieramy _Request a new SSL Certificate_. Do tego zaznaczamy opcję _Force SSL_ oraz _I Agree to the Let's Encrypt Terms of Service_.

![](/images/obraz-4-273x300.png)

Teraz możemy już potwierdzić przyciskiem _Save_. Robimy to samo analogicznie jeszcze dwa razy dla dwóch pozostałych subdomen, które utworzyliśmy w _Cloudflare_.

- dla _nginx.exampleforblog.com_ podajemy port _81_

- dla _cloud.exampleforblog.com_ podajemy port _444_

## Nextcloud i MariaDB

Ostatnie co nam pozostało to stworzenie kontenera _Nextcloud_, dla którego bazą danych będzie _MariaDB_ uruchomiona w oddzielnym, ale sprzężonym kontenerze. Zrobimy to w sposób analogiczny do tego jak robiliśmy to w przypadku _NGINX Proxy Manager_, czyli poprzez _Stacks_ w _Portainer_. A zatem wchodzimy w _Stacks_ i naciskamy przycisk _Add stack._ Jako _Name_ podajemy _nextcloud_, a w _Web editor_ wklejamy poniższy gotowy kod:

```docker
version: '2'

services:
  db:
    image: mariadb:latest
    restart: unless-stopped
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW
    volumes:
      - /var/lib/docker/volumes/Nextcloud_Database:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=<hasło_roota_bazy_danych>
      - MYSQL_PASSWORD=<hasło_użytkownika_dla_nextcloud>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud

  app:
    image: lscr.io/linuxserver/nextcloud:latest
    restart: unless-stopped
    ports:
      - 444:443
    links:
      - db
    volumes:
      - /var/lib/docker/volumes/Nextcloud_Application/config:/config
      - /var/lib/docker/volumes/Nextcloud_Application/data:/data
    environment:
      - MYSQL_PASSWORD=<hasło_użytkownika_dla_nextcloud>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_HOST=db
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Warsaw
```

W tym kodzie tworzymy tak naprawdę tandem składający się z dwóch kontenerów. Pierwszy z nich to baza danych. Z kolei drugi to nasza chmura _Nextcloud_. Co ciekawe dla bazy danych nie przypisałem żadnego portu, a mogłem, bo w przyszłości mógłbym chcieć z niej skorzystać. Nie jest to wielki problem, bo w później można to zmodyfikować. Natomiast dla _Nextcloud_ przypisałem port 444, bo 443 jest już zajęty do obsługi _NGINX Proxy Manager'a_, ale to zostało już przez nas załatwione odpowiednim przekierowaniem na etapie konfiguracji _NGINX Proxy Manager'a_. Jeżeli chodzi o obraz _Dockera_ to wykorzystałem _[lscr.io/linuxserver/nextcloud](https://hub.docker.com/r/linuxserver/nextcloud)_, a nie oficjalny obraz, który też jest dostępny na _Docker Hub_. Wszystko rozchodzi się o to, że obraz od _linuxserver_ (chyba) jako pierwszy miał wsparcie dla architektury _ARM_ i po prostu używam go już od dawna. Do tego mam średnie doświadczenia z tym oficjalnym, więc po prostu wolę ten i polecam go. Zauważ, że w kodzie są dwa fragmenty _<hasło\_roota\_bazy\_danych>_ i _<hasło\_użytkownika\_dla\_nextcloud>_, wpisz w ich miejsce wymyślone przez siebie hasła. Tak sparametryzowany _Stack_ tworzymy potwierdzając przyciskiem _Deploy the stack_ i gotowe.

Aby dostać się do naszej świeżo stworzonej chmury nie musimy już bawić się w żadne adresy IP, bo wystarczy, że po prostu wklepiemy w pasek przeglądarki adres _cloud.exampleforblog.com_. Pozostaje nam już tylko utworzenie konta administratora i finalizacja instalacji. Podczas instalacji może wyniknąć konieczność podania jeszcze raz danych dostępowych do bazy danych MariaDB, bo z nieznanych mi powodów co jakiś czas zdarza się, że nie są one prawidłowo zapisane w kontenerze podczas jego tworzenia. Nie jest to wielki problem, bo wystarczy podczas instalacji _Nextcloud_ rozwinąć menu z ustawieniami zaawansowanymi, wybrać _MariaDB_ i wypełnić cztery pola danymi, które podaliśmy podczas tworzenia _Stack'a_ w _Web editor'ze_.

```
MYSQL_PASSWORD=<hasło_użytkownika_dla_nextcloud>
MYSQL_DATABASE=nextcloud
MYSQL_USER=nextcloud
MYSQL_HOST=db
```

O _Nextcloud_ pisałem sporo w dwóch wpisach, więc podlinkuję je tutaj, bo mogą się przydać:

- [Nextcloud – prywatna chmura na pliki](https://blog.tomaszdunia.pl/nextcloud/)

- [Portainer – GUI dla Docker’a](https://blog.tomaszdunia.pl/portainer/)

Na koniec jeszcze jedna rzecz, z którą każdy zapewne będzie miał problem, a jest nią taki komunikat:

![](/images/portainer_nextcloud13.png)

Rozwiązanie tego problemu jest stosunkowo proste, ale znalezienie go już nie do końca, bo trzeba trochę poszukać w dokumentacji. Mogli to zrobić zdecydowanie bardziej intuicyjnie... Na szczęście macie mnie, czyli gościa, który odwalił już całą robotę i za chwile przedstawi gotowe i zwięzłe rozwiązanie. Otwieramy w edytorze tekstowym plik _config.php_, o którym mowa w komunikacie.

```bash
sudo su
nano /var/lib/docker/volumes/Nextcloud_Application/config/www/nextcloud/config/config.php
```

Odnajdujemy w nim sekcję _trusted\_domains_ i wypełniamy ją analogicznie do tego:

```bash
(...)
'trusted_domains' =>
    array (
      0 => 'localhost',
      1 => 'cloud.exampleforblog.com',
  ),
(...)
```

Oczywiście zamiast _cloud.exampleforblog.com_ należy podać swoją subdomenę, którą konfigurowaliśmy wcześniej. Teraz odśwież stronę w przeglądarce, a dostęp będzie już możliwy.

## Zamykanie portów (aktualizacja 07-10-2024)

Na koniec możemy jeszcze pozamykać porty 81, 444 i 9443 na poziomie zapory _Oracle_ i _iptables_. Nie jest to jakieś konieczne zabezpieczenie, ale na pewno można nazwać to dobrą praktyką. Usuwa się je analogicznie tak jak je się dodawało, więc nie będę tego opisywał. Dopowiem jednak, że takie działanie sprawi, że _Portainer_, _NGINX Proxy Manager_ i _Nextcloud_ będą dalej dostępne z zewnątrz, ale jedynie przez odpowiednie subdomeny, które do nich przypisaliśmy w _NGINX Proxy Manager'ze_. Nie będzie natomiast możliwe dostanie się do np. _Portainer'a_ poprzez wpisanie _https://<ip\_vpsa\_oracle>:9443_. Porty muszą jednak zostać otwarte na poziomie _ufw_, bo jak tam je zamkniemy to nawet i przez _NGINX_ nie będzie możliwości dostępu do zasobu z zewnątrz.

## Podsumowanie

Znowu wyszedł mi straszny tasiemiec, ale wierzę, że to lubicie. W tym wpisie zawarty jest **kawał porządnego mięska**. Liczę, że komuś się to przyda. Jeżeli Tobie się przydało to napisz do mnie w dowolny możliwy sposób (komentarz poniżej, [Mastodon](https://infosec.exchange/@to3k) itd.) i **pochwal się swoją nową i co najważniejsze w pełni darmową chmurą**. **Poleć ten sposób znajomym**, niech i oni na tym skorzystają. W przypadku napotkania jakichkolwiek problemów także **śmiało pisz**. Obiecuję, że **postaram się pomóc** najlepiej jak tylko będę mógł. Powodzenia!

Aha i na koniec, zauważ, że tak stworzone środowisko jest w zasadzie **idealną podwaliną do tego, żeby na tym serwerze stawiać różne inne wartościowe usługi**. Myślę, że wrócę do tego tematu jeszcze nie raz w kolejnych wpisach. Jak masz jakiś ciekawy pomysł jak można wykorzystać taką maszynę to chętnie o nim przeczytam!
