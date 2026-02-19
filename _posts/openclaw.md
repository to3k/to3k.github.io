---
layout: post
title: "OpenClaw - personalny asystent AI"
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
