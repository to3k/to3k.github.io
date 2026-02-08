---
title: "Migracja WriteFreely.pl - FTdL + FreeDNS::42"
date: 2023-11-22
categories: 
  - "poradniki"
  - "projekty"
  - "self-hosting"
tags: 
  - "a"
  - "caa"
  - "cloudflare"
  - "dns"
  - "dnschecker"
  - "freedns42"
  - "ftdl"
  - "fundacjatechnologiedlaludzi"
  - "mx"
  - "nask"
  - "oracle"
  - "txt"
  - "vps"
  - "writefreely"
  - "yunohost"
image: "/images/writefreelyFTdL.png"
---

Spis treści:
* TOC
{:toc}

O fakcie uruchomienia przeze mnie [polskiej instancji _WriteFreely_](https://writefreely.pl/) pisałem [tutaj](https://blog.tomaszdunia.pl/writefreely-polska/). W [oddzielnym wpisie](https://blog.tomaszdunia.pl/yunohost-writefreely/) opisałem, w formie poradnika, jak każdy może uruchomić swoją własną instancję wykorzystując do tego serwer z zainstalowanym oprogramowaniem _[Yunohost](https://blog.tomaszdunia.pl/yunohost-oracle/)_. _WriteFreely.pl_ pierwotnie postawiłem na [darmowym _VPS'ie_ od _Oracle_](https://blog.tomaszdunia.pl/oracle-free-tier/), a jako dostawcę usługi (serwer) DNS wybrałem _[Cloudflare](https://www.cloudflare.com/)_. Było to rozwiązanie i tanie i proste, jednakże nie do końca dbające o prywatność zarówno użytkowników, którzy są twórcami na _WriteFreely.pl_ jak i tych, którzy są jedynie czytelnikami. Wszystko to za sprawą tego, że zarówno _Oracle_ jak i _Cloudflare_ to korporacje, a my świadomi ludzie z [_Outernetu_](https://blog.tomaszdunia.pl/category/pl/outernet/) wiemy, że takim firmom nie można ufać i najlepiej ich unikać, oczywiście jeżeli jest taka możliwość i istnieje sensowna alternatywa. Jeszcze do niedawna Cloudflare nie wydawało się takie złe, bo było postrzegane jako coś w rodzaju strażnika w sieci. Jednakże dość szybko okazało się, że przepuszczana przez ich infrastrukturę jest bardzo duża część Internetu, co przestało się mi i wielu osobom podobać ze względu na centralizację, a można by rzec nawet monopol.

Alternatywa dla _VPS'a_ od _Oracle_ przyszła do mnie sama, bo zaraz po uruchomieniu _WriteFreely.pl_ napisali do mnie ludzie z _[Fundacji Technologie dla Ludzi](https://ftdl.pl/)_ z zapytaniem czy nie chciałbym przenieść instancji do ich infrastruktury. Nie musiałem się zastanawiać dwa razy, bo była to wspaniała oferta, za którą z tego miejsca chciałbym podziękować [Piotrowi Sikorze](https://pol.social/@piotrsikora) oraz [Sebastianowi a.k.a. _m0bi13_](https://pol.social/@m0bi13). Darmowy _VPS_ w infrastrukturze zlokalizowanej w Polsce i stworzonej, aby pomagać właśnie takim projektom _pro publico bono_, biorę! Migracja nastąpiła w dniu 30. października 2023 i przebiegła bez większych problemów, o czym poinformowałem [na blogu z ogłoszeniami _parafialnymi_ dotyczącymi instancji _WriteFreely.pl_](https://writefreely.pl/to3k/sukces). Naturalnym następnym krokiem było pozbycie się pośrednika _Cloudflare_ i wymienienie go na coś analogicznego i przy tym niebudzącego obaw dotyczących prywatności i centralizacji. O tym właśnie będzie ten wpis.

## Serwer DNS

Na wstępie wytłumaczmy sobie w telegraficznym skrócie czym jest serwer _DNS_. Podstawową funkcją tej usługi jest przetłumaczenie adresu domenowego, to jest ten zjadliwy dla człowieka, czyli np. _writefreely.pl_, na adres _IP_ serwera, czyli np. _195.117.15.126_, serwującego zawartość, która ma zostać wyświetlona po wpisaniu tego adresu w pasek adresowy przeglądarki.

Nie jestem sieciowcem, więc jeżeli się mylę to proszę poprawcie mnie, ale według mnie krok po kroku wygląda to tak:

1. Użytkownik wpisuje adres **_https://writefreely.pl_** w przeglądarce.

3. Przeglądarka widzi, że jest to **domena krajowa _.pl_**, więc zwraca się do [_**Krajowego Rejestru Domen**_ (w tym przypadku _NASK_)](https://dns.pl) z prośbą o udzielenie informacji na temat tej domeny.

5. [_NASK_ informuje](https://dns.pl/whois?domainName=writefreely.pl), że domena jest zarejestrowana u dostawcy _Abc Hosting Ltd._ ([cba.pl](https://cba.pl)) i odsyła do następujących serwerów _DNS_ - _**alina.ns.cloudflare.com**_ i _**lloyd.ns.cloudflare.com**_.

7. Przeglądarka komunikuje się z pierwszym z podanych serwerów (drugi jest w ramach redundancji, jakby pierwszy nie działał) i pyta - _**Drogi serwerze DNS, daj mi adres IP serwera obsługującego adres https://writefreely.pl**_.

9. W odpowiedzi przeglądarka otrzymuje adres _**195.117.15.126**_.

11. Przeglądarka komunikuje się z serwerem działającym pod adresem _**195.117.15.126**_ i uzyskuje od niego kod strony, która ma zostać wyświetlona.

13. Przeglądarka przetwarza kod w formę czytelną dla człowieka i wyświetla ją.

To wszystko dzieje się w ułamku sekundy, a potocznie nazywamy to czekaniem aż strona internetowa _się załaduje_. W tym wpisie naszym planem jest zmiana serwerów _DNS_ od _Cloudflare_, o których mowa w punkcie 3 powyższej listy.

## FreeDNS::42

Odpowiedniego serwera _DNS_ nie trzeba wcale daleko szukać, bo Twój dostawca domeny na pewno oferuje taką funkcję w ramach wykupionej domeny. Opcje konfiguracji parametrów _DNS_ domeny znajdują się najpewniej w jej ustawieniach w panelu klienta na stronie dostawcy. W zależności kto nim jest ustawienia te będą mniej lub bardziej zaawansowane i tym samym będą pozwalały na mniej lub więcej. W przeważającej ilości przypadków będzie to wystarczające, ale jeżeli jesteś bardziej wymagającym użytkownikiem to może się to dla Ciebie okazać zbyt ograniczone. W takim przypadku na ratunek przychodzą usługi dedykowane dla takich zapaleńców.

_FreeDNS::42_ to darmowy serwer _DNS_, czyli kolejny fajny projekt _pro publico bono_. Może nie jest to usługa posiadająca najpiękniejszy interfejs użytkownika jaki widziałeś/aś w życiu, ale na pewno nie można odmówić jej funkcjonalności, a przecież to właśnie na to w tym przypadku powinniśmy patrzeć. A zatem, znaleźliśmy rozwiązanie darmowe i w pełni funkcjonalne, a co najważniejsze nie budzące wątpliwości, które mieliśmy wobec _Cloudflare_. W takim wypadku zaczynajmy migrację!

## Odczytajmy nastawy w Cloudflare

Na początek ustalmy jakie rekordy mamy w _Cloudflare_. W tym celu po zalogowaniu się przechodzimy do zakładki _DNS_ i wybieramy _Records_. Wyświetlona zostanie lista wszystkich rekordów. W przypadku _WriteFreely_ potrzebne są raczej tylko rekordy typu _A_ i _CAA_, ale pamiętajmy, że reszta z nich jest ustawiona tak jak [wymagał od nas tego _Yunohost_](https://blog.tomaszdunia.pl/yunohost-writefreely/), więc zostawmy już to tak jak jest. Zatem mamy do przeniesienia następujące rekordy:

| **Type** | **Name** | **Content** |
| --- | --- | --- |
| A | \* | 195.117.15.126 |
| A | writefreely.pl | 195.117.15.126 |
| CAA | writefreely.pl | 0 issue "letsencrypt.org" |
| MX | writefreely.pl | writefreely.pl |
| TXT | \_dmarc | "v=DMARC1; p=none" |
| TXT | mail.\_domainkey | "v=DKIM1; h=sha256; k=rsa; p=(...)" |
| TXT | writefreely.pl | "v=spf1 a mx -all" |

## Konfiguracja strefy w FreeDNS::42

Mając już te dane możemy przejść na stronę _[FreeDNS::42](https://freedns.42.pl/)_ i założyć konto. Po zalogowaniu przechodzimy do _Utwórz strefę_ (dostępne w menu na górze). Podajemy dowolną nazwę strefy, jako typ strefy wybieramy _Podstawowe_ i potwierdzamy przyciskiem _Utwórz_.

![](/images/freedns42-1.png)

W ten sposób tworzymy całkowicie pustą strefę, którą należy teraz odpowiednio skonfigurować. W tym celu wybieramy na górze _Modyfikuj strefę_, na liście odnajdujemy tą świeżo utworzoną i wybieramy ją. Aby uzyskać identyczną konfigurację do tej z _Cloudflare_ musimy wypełnić to jak na poniższych zrzutach ekranu.

![](/images/freedns42-2.png)
    
![](/images/freedns42-3.png)
    
![](/images/freedns42-4.png)
    
![](/images/freedns42-5.png)
    

To wszystko potwierdzamy przyciskiem _Utwórz konfigurację strefy_ znajdującym się na samym dole. Po wszystkim powinniśmy zobaczyć następujące potwierdzenie:

```
Bieżąca strefa: writefreely.pl
Dodawanie rekordu MX writefreely.pl.... OK
Dodawanie rekordu A *... OK
Dodawanie rekordu A @... OK
Dodaję rekord CAA @.... OK
Dodaję rekord TXT @.... OK
Dodaję rekord TXT mail._domainkey.... OK
Dodaję rekord TXT _dmarc.... OK
Nowy numer seryjny: (...)
Twoja strefa pomyślnie przeszła nasze wewnętrzne testy konfiguracji. Powinna być aktywna w ciągu kwadransa.Otrzymasz list informujący Cię o jej aktywowaniu.
Oto wygenerowana konfiguracja:

$TTL 86400 ; Domyślny TTL
writefreely.pl.    	IN SOA   fns1.42.pl. freedns-admin+213320.42.pl (
                   	         1699963109 ; numer seryjny
                   	         86400      ; Częstość odświeżania (refresh)
                   	         10800      ; Częstość powtórek (retry)
                   	         604800     ; Czas wygaśnięcia (expire)
                   	         10800      ; Negatywne buforowanie TTL
                   	)

$ORIGIN writefreely.pl.
                   	IN NS    fns1.42.pl.
                   	IN NS    fns2.42.pl.
@                  	IN MX    10 writefreely.pl. 

*                  	IN A     195.117.15.126 
@                  	IN A     195.117.15.126 

@                  	IN CAA   0 issue "letsencrypt.org"

@                  	IN TXT   "v=spf1 a mx -all"
mail._domainkey    	IN TXT   "v=DKIM1; h=sha256; k=rsa; p=(...)"
_dmarc             	IN TXT   "v=DMARC1; p=none"
```

## Zmiana DNS u dostawcy domeny

Ostatni krok jaki pozostało nam wykonać to zalogować się do panelu klienta u naszego dostawcy domeny, wejść do ustawień tej konkretnej domeny i zmienić dla niej serwery DNS na następujące:

- fns1.42.pl

- fns2.42.pl

![](/images/freedns42-7.png)

Takie ustawienie sprawi, że domena poprzez _NASK_ będzie odsyłała do _FreeDNS::42_, które dalej będzie już kierowało ruch zgodnie z ustawionymi rekordami.

## Koniec?

To nie do końca jest koniec tematu. Z _DNSami_ jest niestety tak, że zmiany w nich wprowadzane nie są natychmiastowe. Lubię to zjawisko nazywać _propagacją_, choć już niejednokrotnie byłem poprawiany przez mądrzejszych ode mnie, że nie jest to odpowiednie określenie. Mimo to dalej wydaje mi się, że jest to najtrafniejsze słowo jakiego mogę użyćw tej sytuacji. Chodzi o to, że sieć serwerów nazw to naprawdę obszerna pajęczyna komputerów, które nieustannie wymieniają się informacjami i nie posiadają centralnego nadzorcy, który pilnowałby, aby wszystkie informacje na wszystkich serwerach były jednakowe i aktualne. Dowolna zmiana w konfiguracji _DNS_ jest tak naprawdę rozgłaszana i rozprzestrzenia się coraz bardziej od serwera do serwera. To właśnie nazywam _propagacją_. Do tego serwery nie aktualizują swoich danych przy każdym zapytaniu do nich skierowanym, bo byłaby to wydajnościowa tragedia. W zamian za to korzystają ze swojej pamięci podręcznej (_cache_), tj. jeżeli tylko mają o danej domenie jakieś informacje, które są względnie aktualne to po prostu je serwują bez sprawdzania czy aby na pewno nie były zmienione sekundy temu. Dążę do tego, że zmiany, których dokonaliśmy w poprzednich akapitach mogą się _propagować_ nawet do 24 godzin i jest to normalne. Postęp tego procesu można monitorować takimi narzędziami jak [_DNS Checker_](https://dnschecker.org/#NS/writefreely.pl). Na poniższym zrzucie ekranu można zaobserwować idealne potwierdzenie tego co napisałem wyżej, czyli to, że część testowych _NSów_ odsyła jeszcze do starych _DNSów_ (_Cloudflare_), a pozostałe serwują już aktualne. Z uwagi na to istotne jest, aby jeszcze przez jakiś czas pozostawić starą konfigurację w _Cloudflare_, dzięki czemu unikniemy tego, że dla pewnych osób strona mogłaby być niedostępna.

![](/images/freedns42-9.png)

W przypadku zmiany serwera _DNS_ propagacja nie jest tak wielkim problemem, bo po prostu wystarczy przez pewien czas pozostawić jednakową konfigurację na dwóch usługach pośredniczących. Większy problem jest, gdy przesiadamy się z jednego serwera na drugi posiadający inny adres _IP_. Wtedy zachowanie ciągłości działania przenoszonej usługi jest niemalże niemożliwe, bo jest ona przenoszona na drugi serwer, a niektóre serwery _DNS_ jeszcze przez pewien czas będą odsyłać do starego, na którym już tej usługi nie ma. Nie jest to przypadek omawiany w tym wpisie, ale myślę, że warto o tym wspomnieć, żeby wyczerpać temat.
