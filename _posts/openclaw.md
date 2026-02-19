---
layout: post
title: "OpenClaw - Personalny Asystent AI"
published: false
categories: 
  - "poradniki"
  - "projekty"
  - "self-hosting"
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
image: "/images/openclaw.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/TYTUŁ-eng/)

Spis treści:
* TOC
{:toc}

## Wstęp

...

## Serwer VPS

### Rejestracja w Hetzner

1. W celu utworzenia konta na Hetzner przechodzimy do **[formularza rejestracyjnego](https://accounts.hetzner.com/signUp)**.
2. Podajemy **adres e-mail**, **hasło** (dwa razy), akceptujemy **regulamin** i naciskamy przycisk **Continue**.
3. Na maila zostanie nam wysłany link do aktywacji konta, więc przechodzimy do naszego klienta poczty i odszukujemy go. Ciekawostka - u mnie coś nie zadziałało za pierwszym razem i maila dostałem dopiero za drugim razem (wpisałem oczywiście te same dane).
4. Link z maila przeniesie nas do dalszej części formularza rejestracyjnego. W tym miejscu musimy:
    - wybrać typ konta - **Individual**,
    - Title, czyli tytuł - do wyboru Pan (Mr.) lub Pani (Ms.), ale można po prostu zostawić **None**,
    - First Name - **Imię**,
    - Surname - **Nazwisko**,
    - nacisnąć przycisk **Continue**.
5. Kolejna strona dotycząca danych kontaktowych:
    - Street / House number - **Ulica**,
    - Postal code - **Kod pocztowy**,
    - City - **Miasto** (nie przyjęło mi polskich znaków),
    - Country - **Kraj**,
    - VAT ID - **NIP**, nieobowiązkowe bo dotyczy raczej tylko przedsiębiorców,
    - Phone - **Numer telefonu** (wydaje mi się, że trzeba go poprzedzić _+48_),
    - Mobile phone - **Numer komórkowy** to jakiś mocny przeżytek z czasów telefonów stacjonarnych, dlatego opcjonalne i pozostawiamy puste,
    - naciskamy przycisk **Continue**.
6. Następny krok dotyczy metody rozliczania:
    - wybieramy **walutę** - często jest tak, że warto jest wybrać dolara, bo usługi kosztują np. 5 dolarów lub 5 euro, gdzie nie pamiętam czasów kiedy dolar był droższy od euro, jednakże w tym przypadku Hetzner przelicza kwoty i wychodzi praktycznie to samo, więc wybierz tą co Ci bardziej pasuje, może Twój bank ma jakiś preferencyjny przelicznik dla którejś za walut (?), ja wybrałem dolara
    - mamy trzy metody płatności - **tradycyjny przelew**, **karta kredytowa** i **PayPal**, ja wybrałem kartę kredytową i podałem dane mojej wirtualnej karty prepaid (przedpłacona, czyli ma tyle środków ile na nią wpłacę i nie więcej, co jest bezpieczne) w Revolut, którą mam specjalnie na takie potrzeby
        - Card holder - wpisujemy **imię i nazwisko** widniejące na karcie,
        - Credit card - wybieramy typ karty, czyli **Visa**, **MarsterCard** lub **American Express**,
        - Card number - **numer karty**,
        - Expires Month i Year - **miesiąc i rok do kiedy karta jest ważna**,
        - CVC code - **3-cyfrowy kod CVC zabezpieczający karty**,
        - zdecyduj czy chcesz zapisać dane karty, żeby w przyszłości nie wprowadzać ich ponownie i jeżeli tak to zaznacz opcję _Hetzner Online has my permission to save my credit card data on my account and to use this information to pay open invoices._
    - naciskamy przycisk **Complete**,
    - to spowoduje konieczność potwierdzenia dodania karty, w moim przypadku poprzez aplikację Revolut (dostałem powiadomienie i potwierdziłem).
7. Sukces. Dostajemy potwierdzenie, że pomyślnie przeszliśmy proces rejestracji.
8. JEDNAKŻE, mocno rekomendowane jest dodanie dodatkowego zabezpieczenia 2FA, dlatego polecam kliknąć **Enable 2FA**. Oczywiście nie musisz tego robić, po prostu olać tą rekomendację i przejść dalej.
9. Zostaniemy przeniesieni do ustawień konta, gdzie ponownie naciskamy żółty przycisk **Enable 2FA**.
10. Wyskoczy okno, w którym mamy podać hasło do konta i zaznaczyć okienko poprzez które potwierdzamy, iż rozumiemy, że jeżeli stracimy kod odzyskiwania to Hetzner przyśle nam nowy pocztą i nie zrobi tego w żaden inny sposób. Potwierdzamy to wszystko przyciskiem **Enable 2FA** (ile można...?).
11. Zapisujemy w bezpiecznym miejscu wyświetlony na ekranie **LOGIN** i **KEY**. Możemy je także wydrukować korzystając z przycisku. Po czym naciskamy na dole **Set up authentication**.
12. Wybieramy metodę zabezpieczenia. Jeżeli masz **Yubikey** to użyj go, a jeżeli nie to możesz wybrać **Mobile device**, a do tego potrzebujesz telefonu z odpowiednią aplikacją np. **[Ente Auth](https://github.com/ente-io/ente/)**, którą polecam. Opiszę jak to zrobić właśnie tą drugą metodą.
13. Odpalamy **Ente Auth**, naciskamy **przycisk plusa** aby dodać nowy element i wybieramy **Zeskanuj kod QR**. Udzielamy aplikacji dostęp do aparatu i **skanujemy kod QR** wyświetlony na stronie Hetznera. W tym momencie w aplikacji na telefonie pojawi się nam już nowa pozycja. Wracamy do storny Hetznera i wpisujemy:
    - Desctription - jakiż krótki **opis**, którym nazwiemy nasze urządzenie, możesz wpisać coś ala _Ente Auth Pixel 9a_,
    - Account password - **hasło** do konta Hetzner,
    - New generated OTP - aktualny ** OTP** wyświetlany w aplikacji Ente Auth na telefonie,
    - przycisk **Add**.
14. W tym momencie zostaniemy wylogowani i będziemy musieli zalogować się ponownie. Dlatego podajemy normalnie login i hasło oraz naciskamy oczywiście przycisk **Login**. Teraz to jest ten dodatkowy krok, w którym musimy podać aktualny kod OTP z aplikacji Ente Auth na telefonie. Naciskamy przycisk **Verify**. Po pomyslnym zalogowaniu trafiamy ponownie do ustawień zabezpieczeń konta, gdzie widzimy, że dwuetapowe uwierzytelnienie zostało aktywowane. Nasze konto jest na pewno 100 razy bardziej bezpieczne z tym niż z samym loginem i hasłem.
15. Po czasie Hetzner poprosił mnie mailowo o dodatkową weryfikację tożsamości, bo moje konto wzbudziło jakieś wątpliwości. Musiałem wejść w link podany w mailu (był to link do zakładki **Verification** w ustawieniach konta) i potwierdzić swoją tożsamość dokumentem (dowód osobisty, prawo jazdy, paszport i chyba coś jeszcze do wyboru...) oraz zdjęciem twarzy. Żeby było śmieszniej to automatyczna weryfikacja nie przeszła, bo chyba przytyłem czy coś i nie wyglądam jak na zdjęciu z dowodu, więc musiałem dodatkowo czekać na weryfikację przez człowieka, co trwało na szczęście może tylko z minutę lub maksymalnie dwie.

### Wybór serwera

Zdecydowałem się na Hetzner, bo nie znam firmy, która dostarcza serwery z lepszym **współczynnikiem ceny do jakości**. Mówiąc wprost - za maszyny o całkiem niezłych parametrach Hetzner chce naprawdę małe pieniądze, więc jest to opcja idealna, żeby przetestować jakieś rozwiązanie, nawet przez parę miesięcy.

Zobaczmy jak kształtuje się aktualna oferta Hetzner. Polecam skorzystać z przycisku na górze, który pozwala ustawić język (English), walutę (ja wybrałem USD) i co najważniejsze kraj dla jakiego ma być liczony **VAT**, co pozwoli nam poznać **ceny brutto**, bo domyślnie prezentowane są ceny netto bez podatku.

Teraz możemy przejść do zakładki [**Cloud**](https://www.hetzner.com/cloud/) i zjechać do sekcji **Prices**. To co nas interesuje to serwery z kategorii **Shared Cost-Optimized**, czyli współdzielone, a przez to zoptymalizowane cenowo, a to po prostu ładniejsza nazwa na serwery dla cebulaków. Teraz już chyba nikt nie ma wątpliwości, że to właśnie to czego szukaliśmy. Możemy wybrać spośród dwóch lokalizacji, ale dla mnie **Niemcy** (Germany) są dość oczywistym wyborem ze względu na to, że w mojej ocenie serwerownia, z której się korzysta powinna być zawsze możliwie jak najbliżej, a Finlandia jest niewątpliwie dalej. Jesteśmy leniuchami i nie chce nam się bawić z problemami z IPv6, więc wybieramy opcję z **IPv4** pomimo tego, że jest o 74 centy droższa.

Aktualna (na luty 2026) **oferta** Hetzner prezentuje się tak:

![Oferta Hetzner](/images/hetznerprices.png)

To co nas interesuje to najtańszy serwer **CX23** z procesorem o **2 wirtualnych rdzeniach** (VCPU)*, **4GB** pamięci RAM i dyskiem SSD o pojemności **40GB**. Taki serwer w momencie pisania tego wpisu kosztuje 5.03 USD **miesięcznie** (!), czyli przeliczając po aktualnym kursie jakieś **18 PLN** z groszami. Trudno się nie zgodzić, że jest to atrakcyjna cena.

### Wynajęcie serwera

1. Aby wynając wybrany serwer przechodzimy do konsoli użytkownika (**Console**), a konkretnie do zakładki **[Projects](https://console.hetzner.com/projects)**.
2. Naciskamy duży przycisk **+ New project**.
3. W pole **Name** wprowadzamy nazwę projektu, ja wpisałem **OpenClaw**.
4. Do tak utworzonego projektu możemy teraz dodać serwer, dlatego w sekcji projektu **OpenClaw** naciskamy przycisk **+ CREATE SERVER**.
5. Zostaniemy przeniesieni do **konfiguratora**, w którym ustawimy parametry serwera. Konfigurator przeprowadzi nas przez wszystkie opcje po kolei:
    - Type - typ serwera, już wcześniej ustaliliśmy, że wybierzemy opcję **Cost-Optimized** (tj. dla cebulaczków), a do tego postawimy na **architekturę x86**, bo zależy nam na maksymalnej kompatybilności kosztem odrobiny większej wydajności, na koniec wybieramy z listy **CX23**,
    - Location - lokalizacja serwera, wybrałbym **Falkenstein**, ale niestety nie był to możliwe ze względu na chwilowo (?) duży popyt, więc wybrałem **Nuremberg**,
    - Image - dobór systemu, ja polecam **Ubuntu 24.04**, bo jak już wcześniej wspomniałem zależy nam na maksymalnej kompatybilności, a Ubuntu jest jak zupa pomidorowa, większość ludzi (w tym przypadku oprogramowania) lubi ją,
    - Networking - wybieramy **Public IPv4**, co jest dodatkowo płatne, ale już o tym rozmawialiśmy, oraz **Public IPv6** co akurat jest w cenie, nie wybieramy natomiast **Private networks**
    - SSH keys - w tej sekcji możemy utworzyć klucz SSH, ale jeżeli tego nie zrobimy to Hetzner wyśle nam po prostu hasło mailem co na ten moment nam odpowiada, bo **kluczami SSH zajmiemy się później podczas konfigurowania serwera**,
    - Volumes - **pomijamy**, bo nasz serwer bazowo ma już 40GB pamięci na dane,
    - Firewalls - **pomijamy** na tym etapie, bo zapory sieciowe tworzy się w innej zakładce projektu,
    - Backups - jeżeli ktoś jest zainteresowany dziennymi kopiami zapasowymi to ta opcja kosztuje dodatkowe 0.86 USD miesięcznie, ja nie potrzebuję, więc **pominąłem tę sekcję**,
    - Placement groups - tutaj można utworzyć klastry serwerów, ale na to jest niepotrzebne, więc **pomijamy**,
    - Labels - jestem zbyt mało zorientowany, żeby wypowiedzieć się na temat tego co to jest, więc **pomijam**,
    - Cloud config - jestem zbyt mało zorientowany, żeby wypowiedzieć się na temat tego co to jest, więc **pomijam**,
    - Name - tutaj nadamy naszemu serwerowi nazwę, ja wpisałem **openclaw-assistant**









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
