---
layout: post
title: "OpenRouter - wszystkie modele AI w jednym miejscu"
published: true
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
image: "/images/openrouter.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/openrouter-eng/)

Spis treści:
* TOC
{:toc}

## Wstęp

Niniejszy wpis jest kontynuacją - **[OpenClaw - Personalny Asystent AI](https://blog.tomaszdunia.pl/openclaw/)**, w którym opisałem jak rozpocząć swoją przygodę z **OpenClaw**. Przypomnijmy sobie, że do testów wykorzystałem **darmowe API Gemini** w ramach planu **Free Tier** w **Google AI Studio**. Już w ramach wniosków z tego poprzedniego wpisu doszedłem do tego, że ten model jest wystarczający, żeby sprawdzić ogólny koncept i czy OpenClaw w ogóle działa, ale jasnym było, że jest to **najsłabszy punkt środowiska**, który trzeba zmodyfikować. Tą modyfikacją jest **podpięcie płatnego API** jednego z wiodących obecnie modeli. Wiele osób poleca w Internecie używanie OpenClaw z **Claude Sonnet** od **Anthropic**. Inni mówią, że to zbyt drogie rozwiązanie i lepiej postawić na nieco tańsze **Gemini 3 Pro** od **Google**. Są też kolejne obozy, które sugerują **wyższość bardziej niszowych modeli ze względu na ich współczynnik ceny do jakości**. Problemy tutaj widzę takie:
1. **każdy model jest wyspecjalizowany w czym innym**, model A może być lepszy w kodowaniu, a model B w generowaniu obrazów,
2. **nie ma jednego lidera**, choć często jeden spośród znanych modeli wychodzi w nowej wersji i odstaje od reszty, ale za chwilę pozostali przeganiają, a gonienie króliczka trwa dalej tylko zmienia się króliczek,
3. **przepłacanie za proste zadania** - nie zawsze potrzebujesz tego wykoksanego modelu, bo płacenie za tokeny Claude Opus przydzielonego do sprawdzenia pogody na dziś i określenia czy potrzebujesz parasola to tak jak wynajęcie prawnika do przynoszenia Ci pod drzwi korespondencji ze skrzynki pocztowej, albo strzelanie z armaty do muchy.

Czy rozumiesz o co mi chodzi? **Nie ma jednego zoptymalizowanego jednocześnie wydajnościowo i kosztowo wyjścia** (modelu). Nie sposób zdecydować się na jeden model, bo jeżeli postawimy na coś bardziej zaawansowanego to będziemy za to słono płacić, a jak z kolei podejdziemy do sprawy optymalizując koszty to nie będziemy zadowoleni z rezultatu pracy przygłupiego taniego modelu. Gdyby tylko dało się mieć ciastko i zjeść ciastko, to znaczy mieć jedno narzędzie skupiające w ramach swojej usługi wiele modeli pomiędzy którymi będzie można płynnie przeskakiwać w zależności od aktualnej potrzeby... 🤔

No i w tym momencie na białym rumaku wjeżdzą **[OpenRouter](https://openrouter.ai/)**. Wbrew temu co myślisz niniejszy materiał NIE jest sponsorowany! :)

## Czy jest OpenRouter

**OpenRouter** to **scentralizowana platforma** pełniąca rolę uniwersalnego interfejsu (API) dla **niemal wszystkich dostępnych na rynku modeli** językowych sztucznej inteligencji. **Zamiast zakładać osobne konta** programistyczne u dostawców takich jak OpenAI, Google, Anthropic czy Mistral, rejestrujesz się tylko w jednym miejscu i generujesz **jeden uniwersalny klucz dostępowy**. Dzięki temu możesz **swobodnie przełączać się pomiędzy flagowymi silnikami** – takimi jak GPT-4o, Claude 3.7 Sonnet czy Gemini Pro – podmieniając wyłącznie ID modelu w konfiguracji swojej aplikacji lub asystenta.

Rozliczenia na platformie działają w wygodnym **modelu pre-paid** ze współdzielonym portfelem. Wpłacasz pojedynczy depozyt (np. 10 dolarów), a system na bieżąco pobiera ułamki centów za faktycznie zużyte tokeny, **niezależnie od tego, z usług jakiej firmy aktualnie korzystasz**. Co niezwykle istotne, rozwiązanie to nie posiada ukrytych haczyków finansowych. **Ceny za tokeny są dokładnie takie same, jak przy zakupie dostępu bezpośrednio u ich twórców**, ponieważ platforma zarabia na własnych, hurtowych zniżkach B2B, a nie na marżach dla użytkowników końcowych.

Kolejnym potężnym atutem tego rozwiązania jest niezawodność oraz wolność od barier terytorialnych. OpenRouter daje natychmiastowy dostęp do najnowszych modeli, które często **z powodu regulacji prawnych są początkowo blokowane dla użytkowników z Europy**. Ujednolicone API platformy idealnie wpisuje się również w konfigurację łańcuchów modeli zapasowych (Fallbacks). Jeśli serwery głównego dostawcy ulegną awarii lub narzucą limit zapytań (Rate Limit), system może w ułamku sekundy i **bez przerywania pracy przekierować Twoje polecenie do zapasowego silnika** od innej firmy.

## Rejestracja

1. Wejdź na stronę **[https://openrouter.ai/](https://openrouter.ai/)** i naciśnij przycisk **Sign Up** znajdujący się w prawym górnym rogu.
2. Podaj login oraz hasło i zaakceptuj regulamin. Potwierdź przyciskiem **Continue**.
3. Przejdź do swojego klienta pocztowego i odbierz maila potwierdzającego.
4. Po udanym zalogowaniu się znajdź ikonę trzech poziomych kresech w prawym górnym rogu strony. Najechanie na nią rozwinie menu, z którego wybieramy **Settings**. Z menu po prawej wybieramy **Settings -> Account**, następnie w wierszu **User** naciskamy przycisk **Manage**. Przechodzimy do zakładki **Security** i w wierszu **Two-step verification** naciskamy **+ Add two-step verification**. Polecam skorzystać z tej dodatkowej warstwy zabezpieczającej konto jeszcze zanim wpłacimy na nie jakiekolwiek pieniądze. Polecam do tego jak zawsze aplikację **[Ente Auth](https://github.com/ente-io/ente)**.

## Doładowanie konta

1. Wracamy do **Settings** i tym razem przechodzimy do **[Credits](https://openrouter.ai/settings/credits)**. To tutaj będziemy zarządzać swoimi finansami.
2. W sekcji **Buy Credits** naciskamy fioletowy przycisk **Add Credits**.
3. Wyskoczy okienko w którym podajemy swoje `imię i nazwisko`, `kraj` i `adres`. Potwierdzamy przyciskiem **Update Address**.
4. W oknie `Add a Payment Method` zacznij od zaznaczenia na dole **Use one-time payment methods**.
5. Okno zmieni się w `Purchase Credits`. W ten sposób zamiast dodawać metodę płatności na stałe dokonamy tylko jednorazowego zakupu kredytów. To znacznie bezpieczniejsze rozwiązanie, bo usuwa możliwość wyczyszczenia sobie karty debetowej lub zadłużenia się na karcie kredytowej po uszy.
6. Zakup zaczynamy od wpisania w pole **Amount** kwoty za jaką chcemy dokonać zakupu. Wartość ta nie może być mniejsza niż 5 (oraz większa od 25000...). Ja postanowiłem wpłacić $10. Do tego doliczone będzie $0,80 podatku.
7. Teraz możemy juz wybrać **metodę płatności**. Do wyboru mamy:
    - kartę,
    - szybki przelew bankowy (aczkolwiek mi nie udało się znaleźć mojego banku),
    - WeChat Pay,
    - Alipay,
    - Cash App,
    - kryptowaluty,
    - Link
    - Amazon Pay.
8. Ja wybrałem **kartę** i wprowadziłem dane mojej wirtualnej karty w Revolut. W ten sposób nie dość, że jestem zabezpieczony robiąc tylko jednorazową transakcję to jeszcze wirtualna karta jest przedpłacona, czyli posiada tyle pieniędzy ile na nią wcześniej wpłacę.
9. Kwota $10 została natychmiast dodana do mojego konta.

## 