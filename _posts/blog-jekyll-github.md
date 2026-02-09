---
layout: post
title: "Jekyll - genialny silnik dla bloga"
date: RRRR-MM-DD
published: false
categories: 
  - "projects"
  - "self-hosting-eng"
  - "tutorials"

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
image: "/images/jekyll.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/TYTUŁ-eng/)
[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/TYTUŁ/)

Spis treści / Table of contents:
* TOC
{:toc}

Niniejszy wpis łączy się częściowo z [postem dotyczącym migracji mojego bloga z Wordpress na silnik Jekyll i infrastrukturę GitHub Pages](https://blog.tomaszdunia.pl/migracja-bloga/). Opisałem w nim dlaczego to zrobiłem, a teraz przyszła pora na pochyleniem się nad tym **jak to zrobiłem**. Tak jak już pisałem wcześniej, jest to bardzo proste i wierzę, że naprawdę każdy sobie z tym poradzi, bez względu na poziom zaawansowania technicznego. Na aktualny stan mojej wiedzy nie znam łatwiejszego sposobu na uruchomienie swojego osobistego bloga i to w dodatku całkowicie za darmo. Dlatego jeżeli nosisz się z myślą o utworzeniu swojego skromnego kącika w Internecie to zapinaj pasy, bo zabieram Cię w krótką podróż po świecie **GitHub Pages**, **Jekyll**, **Markdown** i **statycznych stron HTML**.

## Przygotowanie środowiska GitHub
1. Jeżeli jeszcze nie posiadasz konta na GitHub to [**załóż je**](https://github.com/signup) i **zaloguj się**.
2. Przejdź na [stronę do **tworzenia nowego repozytorium**](https://github.com/new).
3. W sekcji **General** w polu **Repository name** wpisz: ``` <twój_login_github>.github.io ```, gdzie *<twój_login_github>* to musi być faktycznie nazwa użytkownika Twojego konta na GitHub. W moim przypadku było to dokładnie ``` to3k.github.io ```. W polu **Description** wpisz jakiś krótki opis tego projektu, nie jest to zbytnio istotne, więc możesz wpisać coś w stylu ``` Repozytorium mojego prywatnego bloga ```.
4. Sekcji **Configuration** wypełniamy następująco:
    - **Choose visibility** - *Public*
    - **Add README** - *ON* (zaznacz tę opcję)
    - **Add .gitignore** - *No .gitignore*
    - **Add license** - *No license*, według mnie nie ma potrzeby na tym etapie tego konfigurować, aczkolwiek sam polecam dla bloga licencję Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach 4.0 Międzynarodowe (CC BY-NC-SA 4.0), więc zajmiemy się tym później
5. Na koniec potwierdzamy zielonym przyciskiem **Create repository**.

## Uruchomienie Jekyll
Podstawową zaletą robienia tego z wykorzystaniem GitHub Pages jest to, że wszystko praktycznie robi się samo, a jedyne co trzeba wiedzieć to to, które opcje należy włączyć w ustawieniach.
1. Przechodzimy do nowo utworzonego repozytorium i z paska menu w górnej części strony wybieramy **Settings**.
2. Po lewej sekcja **Code and automation** i następnie zakładka **Pages**.
3. Tu musimy skontrolować czy w sekcji **Build and deployment** mamy wszystko prawidłowo skonfigurowane, tj.:
    - **Source** - *Deploy from a branch*
    - **Branch** - *main* i folder */root*, jeżeli było inaczej to zmieniamy i potwierdzamy przyciskiem **Save**
4. Wracamy do głównego widoku repozytorium (zakładka **Code**).
5. Teraz stworzymy plik konfiguracyjny Jekyll. W tym celu korzysatmy z przycisku **Add file** i **Create new file**.
6. Otworzy się kreator nowego pliku. W polu **Name your file...** wpisujemy ``` _config.yml ```. W treści pliku wklej:
``` 
# --- GŁÓWNE USTAWIENIA ---
title: Tomasz Dunia - Blog # Wpisz tutaj swój tytuł bloga
description: Mój prywatny blog # Wpisz tutaj swój opis bloga
url: "https://to3k.github.io" # Zmień tutaj mój login na swój
baseurl: "" 
favicon: favicon.png

# --- MOTYW ---
remote_theme: riggraz/no-style-please # Domyślnie Jekyll używa motywu minima, ale nie podobał mi się on, więc od razu zmieniłem go na ten i tak też polecam zrobić

# --- USTAWIENIA LINKÓW ---
permalink: /:title/ # Takie permalinki są zgodne ze standardem Wordpress, co później ułatwi ewentualną migrację istniejącego bloga z WP

# --- WTYCZKI ---
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-remote-theme
  - jekyll-sitemap

# --- DANE AUTORA ---
author:
  name: Tomasz Dunia # Wypełni wedle uznania
  url: https://tomaszdunia.pl # Wypełni wedle uznania

# --- USTAWIENIA MARKDOWN ---
markdown: kramdown
kramdown:
  input: GFM
  syntax_highlighter: rouge
``` 
7. Plik w takiej formie zapisujemy w repozytorium przy użyciu zielonego przycisku **Commit changes...** znajdującym się w prawym górnym roku i ponownie **Commit changes...** w oknie, które wyskoczy. Dobrą praktyką na GitHub jest przy każdym Commit wpisywać w pole **Commit message** krótki opis tego co zrobiliśmy, co później będzie widoczne w historii zmian. Wystarczy wpisać nawet ``` Utworzenie pliku _config.yml ```.
8. Teraz pora na plik strony głównej. Nasz blog będzie utrzymany w duchu maksymalnej prostoty, więc na ten moment będzie się składał tylko z wytłuszczonego tytułu i spisu treści, w którym wylistujemy wszystkie posty, które utworzymy dopiero w kolejnych krokach. 
```
---
layout: default
title: Tomasz Dunia - Blog # Wpis tutaj swój tytuł
---

<div id="all-posts">
  <h3>Spis treści / Table of contents:</h3>
  <ul style="list-style: none; padding-left: 0;">
    {% for post in site.posts %}
      <li style="margin-bottom: 8px;">
        <span style="color: #666; font-family: monospace; margin-right: 10px;">{{ post.date | date: "%d-%m-%Y" }}</span>
        &raquo;
        <a href="{{ post.url | relative_url }}" style="font-weight: bold;">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
</div>
```