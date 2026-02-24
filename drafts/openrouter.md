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

### Czyszczenie niepotrzebnych skilli

OpenClaw uruchamia się z domyślnymi skillami, których w moim przypadku było aż 50. Przejrzałem całą tą listę i doszedłem do wniosku, że nie potrzebuję żadnego z nich, a nawet jeżeli będę potrzebował w przyszłości to mogę go szybko doinstalować. Instrukcje obsługi wszystkich włączonych skilli są doklejane do każdego zapytania kierowanego do API, więc jeżeli nie korzystamy z nich to są tylko zbędnym zapychaczem. Listę skilli można sprawdzić w panelu sterowania w **Agent -> Skills** i z tego poziomu można je też wszystkie wyłaczyć. Kliknięcie 50 razy przycisku `Disable` nie jest wygodne, więc proponuję to zrobić z poziomu terminala serwera VPS. W tym celu edytujemy plik `/home/manager/.openclaw/openclaw.json`.

```bash
nano /home/manager/.openclaw/openclaw.json
```

Tuta nie tylko można wyłączyć skille (zmieniając parametr `enabled` na `false`), ale także w ogóle je usunąć, co polecam zrobić, żeby nie robić sobie śmietnika. To czego powinniśmy się pozbyć to fragmentu:

```json
{
  "meta": {
    "lastTouchedVersion": "2026.2.20",
    "lastTouchedAt": "2026-02-24T10:48:06.665Z"
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "google/gemini-3-flash-preview",
        "fallbacks": [
          "google/gemini-2.5-flash",
          "google/gemini-2.5-flash-lite"
        ]
      },
      "models": {
        "google/gemini-3-flash-preview": {},
        "google/gemini-2.5-flash": {},
        "google/gemini-2.5-flash-lite": {}
      },
      "compaction": {
        "mode": "safeguard"
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      },
      "contextTokens": 20000
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
      "botToken": "XXXXXXXXXXXX",
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
      },
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
```

### Ograniczenie pamięci krótkotrwałej

Każda kolejna wiadomość wysłana przez nas generuje wywołanie kolejnego prompta do API (za które płacimy). Każdy taki kolejny **prompt zawiera historię danego czatu**, tj. ileś wiadomości z konwersacji na Telegramie patrząc wstecz. Z przymróżeniem oka można to nazwać **pamięcią krótkotrwałą bota**. Oczywistym jest, że **im większy blok tekstu z historią** wysyłany jest w każdym z promptów tym **więcej zużywanych jest tokenów** i tym **więcej płacimy**. Dlatego wprowadzimy tutaj znacznie **niższy limit** niż pozwala na to załóżmy model Claude Sonnet, dla którego wartość `Context Limit` może maksymalnie wynosić nawet 200 000. Ustawmy **10 razy mniejszą** wartość tego parametru, czyli 20 000.

Jeżeli martwisz się, że zasadniczo ogłupi to asystenta to nie przejmuj się, bo **OpenClaw ma przecież plik `MEMORY.md`**, który jest czymś w rodzaju **pamięci długotrwałej**. Zmniejszenie pojemności pamięci krótkotrwałej będzie powodowało tylko to, że bot będzie **częściej robił podsumowania i w skróconej wersji zapisywał to co jest istotne do pliku** z pamięcią długotrwałą.

Parametr ten definiuje się w pliku `/home/manager/.openclaw/openclaw.json`, zatem otwórzmy go do edycji:

```bash
nano /home/manager/.openclaw/openclaw.json
```

W jego treści musimy znaleźć `agents` dalej `defaults` i na końcu dodajemy `"contextTokens": 15000`. Poniżej wrzucam fragment treści `openclaw.json`, żeby pokazać jak należy to dopisać:

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
      "contextTokens": 20000
    }
  },
  ```

Plik oczywiście zapisujemy i zamykamy - **Control (CTRL) + X**, potem **y** i **ENTER**.

## Uniwersalny klucz API

