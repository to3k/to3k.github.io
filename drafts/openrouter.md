---
layout: post
title: "OpenClaw + OpenRouter"
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

## Optymalizacja bota

Zanim podepniemy OpenRouter do naszego agenta OpenClaw powinniśmy trochę go zoptymalizować. Teraz w grę wchodzą już **realne pieniądze**, więc jeżeli **nie chcesz płacić za głupoty** to trzeba pozmieniać ustawienia bota tak, aby jak najmniej tych głupot robił.

### Edycja plików osobowości

W [poradniku o OpenClaw](https://blog.tomaszdunia.pl/openclaw/#podpowied%C5%BA) pisałem, że dobrą praktyką jest **ograniczyć się do minimum** w zakresie plików definiujących "osobowość" bota. Te pliki **trafiają do każdego zapytania** wysłanego do API, więc **im bardziej obszerne są tym więcej zapłacimy**. Dlatego zajrzyjmy do nich i wprowadzmy zmiany. Modyfikować je możemy na dwa sposoby:
1. z poziomu terminala na serwerze VPS wchodząc do folderu, w którym się znajdują `cd /home/manager/.openclaw/workspace` i edytując za pomocą edytora `nano` wszystkie z nich po kolei,
2. z poziomu panelu sterowania wchodząc do **Agent -> Agents -> Files**.

Przejdzmy przez wszystkie z nich po kolei.

#### AGENTS.md

Treści tego pliku nie zmieniam i zostawiam domyślną. Możliwe, że w przyszłości wprowadzę tam jakieś zmiany, ale na razie nie widzę takiej potrzeby. W mojej ocenie jest to najważniejszy plik, który stanowi ogólną instrukcję zachowania bota oraz to jak korzystać z pozostałych plików, które wymienię poniżej. Edytując go trzeba uważać, bo można tym niechcący upośledzić bota.

#### SOUL.md

Przypomnę, że jest to plik, który określa jaki bot ma się zachowywać. Treść mojego pliku `SOUL.md` to:

```
- Bezpośredni, techniczny asystent.
- Odpowiadaj maksymalnie konkretnie, bez zbędnej otoczki i powitań
- Unikaj korporacyjnego żargonu i sztucznej uprzejmości
- Jeżeli nie masz pewności co do tego co mówisz powiedz wprost "nie wiem" zamiast zmyślać lub halucynować.
```

#### TOOLS.md

Proponuję zostawić ten plik w pierwotnej formie.

#### IDENTITY.md

Plik, w którym tworzymy tożsamość bota:

```
- Pseudonim: Areczek
- Mój osobisty asystent AI
- Uruchomiony w Docker na VPS od Hetzner
- Komunikacja: Telegram
```

#### USER.md

Tu wrzucamy podstawowe informacje o sobie, które uznamy za użyteczne w kontekście współpracy z botem:

```
- Imię: Tomasz
- Praca: Inżynier, konstruktor, mechatronik, branża autobusy miejskie
- Hobby: blog techniczny (blog.tomaszdunia.pl), self-hosting, smarthome (Home Assistant), open source, strzelectwo sportowe (broń palna)
- Sport: motorowe (żużel, F1)
- Sociale: Mastodon - infosec.exchange/@to3k
- Mieszka: Lublin, Polska
```

#### HEARTBEAT.md

Czyścimy do zera. Tutaj będą trafiać zadania cykliczne i związane z pracą w tle, ale to bot będzie sobie wypełniał sam. Można tutaj ewentualnie zajrzeć co jakiś czas, żeby sprawdzić czy wykonuje w tle (bez naszej wiedzy) jakiś dziwnych tasków.

#### BOOTSTRAP.md

Ten plik przydaje się tylko przy pierwszym uruchomieniu bota. Konfiguracja, którą wykonujemy teraz zastępuje ten pierwszy krok, więc czyścimy ten plik, żeby nam nie zawalał niepotrzebnie promptów.

#### MEMORY.md

U mnie ten plik domyślnie w ogóle nie istniał, dlatego go utworzyłem i pozostawiłem pustym. To miejsce, gdzie bot sam będzie zapisywał rzeczy, które musi zachować w ramach pamięci długotrwałej.

#### Podpowiedź

Powyższe pliki służą do tego, aby za ich pomocą dostosować asystenta do swoich potrzeb. Jak to mówią apetyt rośnie w miarę jedzenia, więc na pewno będziemy chcieli w przyszłości coś podkręcić. Na pewno bedą zmieniać się także nasze wymagania względem asystenta. Dobry pracownik zawsze może być lepszy. Modyfikuj te pliki aż osiągniesz zadowalający Cię efekt. Jednakże pamiętaj o jednym. Niektóre modele LLM cache'ują (zapamiętują) zawartość tych plików. Przykładem takiego modelu jest właśnie Claude od Anthropic. Po pierwszym zapoznaniu się z plikami "osobowości" naszego asystenta model ten zapamięta je i przy następnym zapytaniu API zapłacimy tylko 90% za skorzystanie z tej części pamięci. Jest jednak jeden warunek. Zawartość tych plików nie może uleć zmianie. Każda nawet drobna zmiana spowoduje ponowne cachowanie i tym samym przepada nam zniżka 90%.

### Wyłączenie niepotrzebnych skilli

OpenClaw uruchamia się z domyślnymi skillami, których w moim przypadku było aż 50. Przejrzałem całą tą listę i doszedłem do wniosku, że nie potrzebuję żadnego z nich, a nawet jeżeli będę potrzebował w przyszłości to mogę go szybko włączyć. Instrukcje obsługi wszystkich włączonych skilli są doklejane do każdego zapytania kierowanego do API, więc jeżeli nie korzystamy z nich to są tylko zbędnym zapychaczem. Listę skilli można sprawdzić w panelu sterowania w **Agent -> Skills** i z tego poziomu można je też wszystkie wyłaczyć. Kliknięcie 50 razy przycisku `Disable` nie jest wygodne, więc proponuję to zrobić z poziomu terminala serwera VPS. W tym celu edytujemy plik `/home/manager/.openclaw/openclaw.json`.

```bash
nano /home/manager/.openclaw/openclaw.json
```

Skille znajdują się w sekcji `skills` i dalej `entries`, a wyłącza się je poprzez zmianę wartości parametru`enabled` na `false`. Przykład wyłaczenia skilla 1password:

```json
"skills": {
  "entries": {
    "1password": {
      "enabled": false
    },
    ...
  }
```

### Ograniczenie pamięci krótkotrwałej

Każda kolejna wiadomość wysłana przez nas generuje wywołanie kolejnego prompta do API (za które płacimy). Każdy taki kolejny **prompt zawiera historię danego czatu**, tj. ileś wiadomości z konwersacji na Telegramie patrząc wstecz. Z przymróżeniem oka można to nazwać **pamięcią krótkotrwałą bota**. Oczywistym jest, że **im większy blok tekstu z historią** wysyłany jest w każdym z promptów tym **więcej zużywanych jest tokenów** i tym **więcej płacimy**. Dlatego wprowadzimy tutaj znacznie **niższy limit** niż pozwala na to załóżmy model Claude Sonnet, dla którego wartość `Context Limit` może maksymalnie wynosić nawet 200 000. Ustawmy **4 razy mniejszą** wartość tego parametru, czyli 50 000.

Jeżeli martwisz się, że zasadniczo ogłupi to asystenta to nie przejmuj się, bo **OpenClaw ma przecież plik `MEMORY.md`**, który jest czymś w rodzaju **pamięci długotrwałej**. Zmniejszenie pojemności pamięci krótkotrwałej będzie powodowało tylko to, że bot będzie **częściej robił podsumowania i w skróconej wersji zapisywał to co jest istotne do pliku** z pamięcią długotrwałą.

Parametr ten definiuje się w pliku `/home/manager/.openclaw/openclaw.json`, zatem otwórzmy go do edycji:

```bash
nano /home/manager/.openclaw/openclaw.json
```

W jego treści musimy znaleźć `agents` dalej `defaults` i na końcu dodajemy `"contextTokens": 50000`. Poniżej wrzucam fragment treści `openclaw.json`, żeby pokazać jak należy to dopisać:

```bash
"agents": {
    "defaults": {
      "model": {
        ...
      },
      "models": {
        ...
      },
      "compaction": {
        ...
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      },
      "contextTokens": 50000
    }
  },
  ```

Plik oczywiście zapisujemy i zamykamy - **Control (CTRL) + X**, potem **y** i **ENTER**.

### Restart kontenera

Na koniec zrestartujmy kontener aby załadować nową konfigurację ze wszystkimi wyżej opisanymi zmianami:

```bash
docker compose restart openclaw-gateway
```

Wydaje mi się, że teraz nasz bot jest godzien ładowania w niego pieniędzy. Nie jest wykluczone, że 

## Uniwersalny klucz API

Wracamy na stronę [OpenRouter](https://openrouter.ai/) i pozyskamy w końcu ten legendarny uniwersalny klucz API, dający dostęp do bazy tak wielu różnych modeli od różnych dostawców. 

1. Wejdź do **Settings -> [API Keys](https://openrouter.ai/settings/keys)** i naciśnij fioletowy przycisk **Create**.
2. W okienku, które wyskoczy:
    - w polu `Name` podajemy nazwę naszego klucza, np. **OpenClaw Assistant**,
    - w polu `Credit limit (optional)` możemy podać limit kredytów, jaki chcemy nałożyć na ten klucz, ja wpisałem **5 dolarów**, jeżeli zostawimy puste to lecimy bez limitu (kto bogatemu zabroni...),
    - lista rozwijana `Reset limit every...` łączy się bezpośrednio z poprzednim polem dotyczącym limitów i określa jaki ma być interwał resetowania limitu, ja wybrałem **Daily**, czyli codziennie, bo jestem w stanie przeboleć jak bot zeżre mi $5 w jeden dzień,
    - lista rozwijana `Expiration` pozwala nam określić długość życia tego klucza API, tj. kiedy ma on wygasnąć, ja wybrałem opcję **No expiration**, bo nie mam problemu z tym, że klucz będzie wieczny, gdyż będzie on bezużyteczny, gdy wykorzystane zostanie całe saldo, a przypominam, że zdecydowałem się na model rozliczenia pre-paid zamiast dodawać kartę na sztywno.
3. Potwierdzamy przyciskiem **Create**.
4. W rezultacie otrzymamy komunikat, w którego treści będzie klucz, który należy zapisać w bezpiecznym miejscu:

    ```
    Your new key:
    KLUCZ_API_OPENROUTER

    Please copy it now and write it down somewhere safe. You will not be able to see it again.
    You can use it with OpenAI-compatible apps, or your own code
    ```
5. Otrzymany klucz dodamy teraz do środowiska naszego bota. Otwieramy do edycji plik `/home/manager/openclaw/.env`:

    ```bash
    nano /home/manager/openclaw/.env
    ```
6. Dodajemy na jego końcu linijkę, w której zamiast `KLUCZ_API_OPENROUTER` podajemy klucz API od OpenRouter, który utworzyliśmy w poprzednich krokach:

    ```bash
    OPENROUTER_API_KEY=KLUCZ_API_OPENROUTER
    ```
7. Otwieramy do edycji kolejny plik `/home/manager/openclaw/docker-compose.yml`:

    ```bash
    nano /home/manager/openclaw/docker-compose.yml
    ```
8. Na końcu sekcji `environment` dodajemy linijkę:

    ```bash
    - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
    ```
9. Jeszcze tylko restart kontenera:

    ```bash
    docker compose up -d openclaw-gateway
    ```

## Strategia Multi-Model

OpenRouter to wyborna usługa. Jest genialna w swojej prostocie. Nie okrada swoich użytkowników żadnymi dodatkowymi marżami, a tym samym ma prosty model zarabiania, który poleca na tym, że skupia wielu detalistów, oferuje im te same ceny co poszczególnie producenci, a zarabia na tym, że tak naprawdę kupuje hurtowo, bo wielu detalistów to tak naprawdę już hurtownik, i dzięki temu ma lepsze ceny, co implikuje dochód na bazie różnicy ceny hurtowej i detalicznej.

Jednakże dla nas poza cenami najważniejszą funkcją oferowaną przez OpenRouter jest możliwość żąglowania, tj. płynnego preskakiwania pomiędzy, poszczególnymi modelami. Oczywiście można by było zdecydować się na jeden model np. Claude Sonnet, spiąć go na sztywno ze swoim botem OpenClaw i ewentualnie zastąpić w przyszłości jakimś innym modelem, który wyjdzie i okaże się bardziej wydajny. Lecz byłoby grzech nie wejść bardziej w temat i nie skorzystać z tej elastyczności, którą daje OpenRouter. W tym momencie wchodzi strategia Multi-Model.

Do używania wielu modeli można podejść na wiele sposobów, ale ja przedstawię tylko tą najprostszą i wymagającą najmniej uwagi. Nazwijmy to rozwiązaniem dla leniwych.

### Auto Router

Ktoś kto stoi za OpenRouter ma łeb na karku. Wymyślił mechanizm działający tak:
1. wysyłamy zapytanie do OpenRouter używając klucza API,
2. zapytanie trafia do małego, ultraszybkiego meta-modelu uruchomionego przez OpenRouterl, którego nazwiemy dalej bramkarzem,
3. bramkarz w ułamku sekundy robi podstawową analizę naszego zapytania, której celem jest klasyfikacja intencji (intent classification):
    - **Ocena Złożoności (Complexity Scoring)** - bramkarz skanuje prompt pod kątem trudności. Jeżeli wykryje zadanie wymagające zaawansowanego rozumowania (np. pisanie kodu, analiza architektoniczna, matematyka), nadaje mu wysoką wagę i kieruje do modeli klasy frontier (jak Claude 3.7 Sonnet czy GPT-4o). Jeśli to błahe zadanie (np. rutynowy heartbeat bota, tłumaczenie, prosta klasyfikacja), kieruje je do modeli tanich (jak Llama 3 czy Gemini Flash).
    - **Filtrowanie Kontekstu** (Context Windowing) - system w locie zlicza tokeny (długość wiadomości i wklejonych logów czy historii czatu). Jeśli przesyłasz paczkę danych o wielkości 50 000 tokenów, router automatycznie odrzuca modele, które mają mniejsze okno pamięci, i wybiera ten, który fizycznie poradzi sobie z tą objętością zapytania.
    - **Telemetria na żywo** (Health & Latency Check) - OpenRouter stale monitoruje status serwerów dostawców. Decyzja o routingu uwzględnia to, czy API Anthropic lub OpenAI nie ma w danej sekundzie czkawki (Rate Limits). Jeśli główny, inteligentny model od jednego dostawcy nie odpowiada, router dynamicznie przerzuca żądanie do jego odpowiednika u innej firmy.
4. po dokonaniu klasyfikacji następuje krok **Proxy i Przekazanie** (Forwarding), czyli po podjęciu decyzji algorytm nadpisuje docelowe ID modelu w nagłówkach HTTP i wysyła zapytanie przez swoje zunifikowane API do serwerów wybranego twórcy. Wynik wraca do Ciebie dokładnie tym samym kanałem.

Brzmi obiecująco, prawda? Mnie to przekonuje dlatego w pierwszej kolejności zdecydowałem się na przetestowanie tego wariantu i robię to właśnie teraz. Pewnie po jakimś czasie zaktualizuję ten wpis o moje przemyślenia po testach.

Dobra, ale jak to skonfigurować?
1. Logujemy się na serwer VPS:

    ```bash
    ssh manager@ADRES_IPV4
    ```

2. Otwieramy plik `/home/manager/.openclaw/openclaw.json` w edytorze:

    ```bash
    nano /home/manager/.openclaw/openclaw.json
    ```

3. Jego treść modyfikujemy tak, aby wyglądała następująco:

    ```json
    {
      "meta": {
        "lastTouchedVersion": "2026.2.20",
        "lastTouchedAt": "2026-02-24T10:48:06.665Z"
      },
      "agents": {
        "defaults": {
          "model": {
            "primary": "openrouter/openrouter/auto"
          },
          "heartbeat": {
            "every": "6h",
            "model": "openrouter/google/gemini-3-flash",
            "target": "last"
          },
          "compaction": {
            "mode": "safeguard"
          },
          "maxConcurrent": 4,
          "subagents": {
            "maxConcurrent": 8
          },
          "contextTokens": 50000
        }
      },
      "messages": {
        "ackReactionScope": "group-mentions"
      },
      "commands": {
        "native": "auto",
        "nativeSkills": "auto",
        "restart": true
      },
      "channels": {
        "telegram": {
          "enabled": true,
          "dmPolicy": "pairing",
          "botToken": "TOKEN_TELEGRAM",
          "groupPolicy": "allowlist",
          "streamMode": "partial"
        }
      },
      "skills": {
        "entries": {
          "1password": {
            "enabled": false
          },
          "apple-notes": {
            "enabled": false
          },
          "apple-reminders": {
            "enabled": false
          },
          "bear-notes": {
            "enabled": false
          },
          "blogwatcher": {
            "enabled": false
          },
          "blucli": {
            "enabled": false
          },
          "bluebubbles": {
            "enabled": false
          },
          "camsnap": {
            "enabled": false
          },
          "clawhub": {
            "enabled": false
          },
          "coding-agent": {
            "enabled": false
          },
          "discord": {
            "enabled": false
          },
          "eightctl": {
            "enabled": false
          },
          "gemini": {
            "enabled": false
          },
          "gh-issues": {
            "enabled": false
          },
          "gifgrep": {
            "enabled": false
          },
          "github": {
            "enabled": false
          },
          "gog": {
            "enabled": false
          },
          "goplaces": {
            "enabled": false
          },
          "healthcheck": {
            "enabled": false
          },
          "himalaya": {
            "enabled": false
          },
          "imsg": {
            "enabled": false
          },
          "mcporter": {
            "enabled": false
          },
          "model-usage": {
            "enabled": false
          },
          "nano-banana-pro": {
            "enabled": false
          },
          "nano-pdf": {
            "enabled": false
          },
          "notion": {
            "enabled": false
          },
          "openai-image-gen": {
            "enabled": false
          },
          "openai-whisper": {
            "enabled": false
          },
          "openai-whisper-api": {
            "enabled": false
          },
          "oracle": {
            "enabled": false
          },
          "openhue": {
            "enabled": false
          },
          "obsidian": {
            "enabled": false
          },
          "ordercli": {
            "enabled": false
          },
          "peekaboo": {
            "enabled": false
          },
          "sag": {
            "enabled": false
          },
          "session-logs": {
            "enabled": false
          },
          "sherpa-onnx-tts": {
            "enabled": false
          },
          "skill-creator": {
            "enabled": false
          },
          "slack": {
            "enabled": false
          },
          "songsee": {
            "enabled": false
          },
          "sonoscli": {
            "enabled": false
          },
          "spotify-player": {
            "enabled": false
          },
          "summarize": {
            "enabled": false
          },
          "things-mac": {
            "enabled": false
          },
          "tmux": {
            "enabled": false
          },
          "trello": {
            "enabled": false
          },
          "video-frames": {
            "enabled": false
          }
          "voice-call": {
            "enabled": false
          },
          "wacli": {
            "enabled": false
          },
          "weather": {
            "enabled": false
          }
        }
      },
      "plugins": {
        "entries": {
          "telegram": {
            "enabled": true
          }
        }
      }
    }
    ```

4. Omówmy ten plik linijka po linijce:
    - **`meta`**: Metadane pliku konfiguracyjnego.
      - **`lastTouchedVersion`**: Wersja systemu OpenClaw, która jako ostatnia nadpisała lub zaktualizowała ten plik (2026.2.20).
      - **`lastTouchedAt`**: Dokładna data i czas ostatniej modyfikacji.
    - **`agents.defaults`**: Domyślne ustawienia dla Twojego asystenta.
      - **`model`**: Główny "mózg" bota. Przypisany `auto` z OpenRoutera oznacza, że system sam dobiera optymalny model do każdego zapytania.
      - **`heartbeat`**: Konfiguracja proaktywnego działania w tle.
        - **`every`**: Interwał czasowy (wybudzanie co 6 godzin).
        - **`model`**: Silnik dedykowany do tego zadania (ustawiony szybki i tani Gemini 3 Flash).
        - **`target`**: Określa, do kogo bot ma skierować ewentualną wiadomość wygenerowaną w tle (`last` oznacza ostatnio używany kanał/ostatniego rozmówcę).
      - **`compaction.mode`**: Mechanizm zarządzania pamięcią krótkotrwałą. Tryb `safeguard` kompresuje i streszcza najstarsze wiadomości z czatu, zapobiegając przekroczeniu limitu tokenów.
      - **`maxConcurrent`**: Maksymalna liczba operacji (np. jednoczesne użycie kilku narzędzi), które główny agent może wykonywać równolegle (4).
      - **`subagents.maxConcurrent`**: Maksymalna liczba niezależnych podwykonawców pracujących w tle, których agent może uruchomić do pomocy przy złożonych zadaniach (8).
      - **`contextTokens`**: Twardy limit pamięci czatu (50 000 tokenów) wysyłanej do API przy każdej wiadomości.
    - **`messages`**:
      - **`ackReactionScope`**: Określa, w jakich sytuacjach bot ma potwierdzać przeczytanie wiadomości za pomocą reakcji (np. emoji). Wartość `group-mentions` oznacza, że zrobi to wyłącznie, gdy zostanie bezpośrednio oznaczony (@) w czacie grupowym.
    - **`commands`**: Konfiguracja obsługi komend wpisywanych na czacie (np. na Telegramie z użyciem ukośnika `/`).
      - **`native`**: Automatycznie włącza i obsługuje podstawowe komendy systemowe (np. `/model`).
      - **`nativeSkills`**: Automatycznie rejestruje i obsługuje komendy pochodzące od zainstalowanych skilli.
      - **`restart`**: Zezwala na użycie komendy `/restart` bezpośrednio z poziomu komunikatora w celu zresetowania procesu.
    - **`channels.telegram`**: Konfiguracja interfejsu Telegram.
      - **`enabled`**: Aktywuje komunikację przez ten kanał.
      - **`dmPolicy`**: Zasady dla wiadomości prywatnych. Tryb `pairing` oznacza, że każdy nowy użytkownik musi podać kod autoryzacyjny, aby bot z nim porozmawiał.
      - **`botToken`**: Twoje hasło uwierzytelniające z BotFathera.
      - **`groupPolicy`**: Zasady dla grup. Tryb `allowlist` blokuje bota przed działaniem w nieznanych czatach grupowych, chyba że dodasz je wcześniej do białej listy.
      - **`streamMode`**: Tryb strumieniowania tekstu. Wartość `partial` sprawia, że długie odpowiedzi są aktualizowane w Telegramie partiami, co imituje płynne "pisanie na żywo" bez spamowania API komunikatora przy każdym pojedynczym słowie.
    - **`skills.entries`**: Miejsce, w którym zapisywane są ręcznie zainstalowane umiejętności dodatkowe z ClawHub (aktualnie puste).
    - **`plugins.entries.telegram.enabled`**: Włącza rdzenny moduł (wtyczkę silnika) odpowiedzialny za utrzymanie połączenia z serwerami Telegrama.
5. Jak widzisz jako model główny podpiąłem tutaj `openrouter/openrouter/auto`, ale dodatkowo dla `heartbeat`, czyli operacji cyklicznych w tle przypisałem na sztywno model `openrouter/google/gemini-3-flash`, czyli czyli najszybszy i najtańszy model, ale z najnowszej wersji Gemini. Teoretycznie Auto Router poradził by sobie z doborem odpowiedniego modelu dla heartbeatsów, ale skonfigurowanie tego na sztywno jest tak proste, że szkoda kusić losu. Do tego taki zapis pozwala mi na sztywno określić interwał odpalania działań w tle i na początek zdecydowałem, że będzie to 6 godzin.
6. Teraz zresetujmy kontener, aby utrwalić zmiany:

    ```bash
    docker compose restart openclaw-gateway
    ```

A jak to działa w praktyce? Dość prosto. Zauważyłem, że cały dialog ze mną na Telegramie prowadzony jest na bazie modelu Gemini 2.5 Flash. Jeżeli agent dostanie trudniejsze zadanie to zleca je subagentowi, który wykonuje je na bardziej złożonym modelu. W moim przypadku został wytypowany Claude Opus, za którego niestety zapłaciłem dość słono, bo jest to jeden z najdroższych spośród dostępnych modeli. Trzeba jednak przyznać, że zleciłem agentowi dość złożone zadanie, do którego sama instrukcja była dość długim promptem. Muszę się chyba trochę poduczyć z optymalizacji, bo w taki sposób dość szybko zbankrutuję.

## OpenRouter poza OpenClaw

Z OpenRouter można **korzystać również jak ze zwykłego czatu**. Wystarczy wejść na stronę **[https://openrouter.ai/chat](https://openrouter.ai/chat)**. Jednakże nie jest to tak do końca normalny czat. Jako że OpenRouter jest agregatorem modeli LLM to możemy nie tylko przeskakiwać płynnie pomiędzy modelami i zadawać im kolejne pytania na przemian, ale także możemy na raz zadać to samo pytanie do kilku modeli lub włączyć funkcję Auto Router, które sama dopasuje sobie odpowiedni model i w ten sposób optymalizować koszty oraz jakość wyników.

Polecam także zajrzeć do **[Rankingu modeli](https://openrouter.ai/rankings)**, co jest nieocenionym źródłem informacji na temat tego jakie modele aktualnie trendują, czyli są najchętniej używane. W ten sposób można podłapać jaki model aktualnie jest najskuteczniejszy, ale także który najbardziej się opłaca ze względu na stosunek jakości do ceny.

Z kolei **[baza modeli](https://openrouter.ai/models)** oferuje bardzo rozbudowane i szczegółowe filtry wyszukiwania, co pomaga znaleźć model odpowiedni do wymaganego zastosowania.