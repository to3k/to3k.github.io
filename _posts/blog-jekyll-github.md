---
layout: post
title: "Jekyll - genialny silnik dla bloga"
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
3. W sekcji **General** w polu **Repository name** wpisz: ` <twój_login_github>.github.io `, gdzie *<twój_login_github>* to musi być faktycznie nazwa użytkownika Twojego konta na GitHub. W moim przypadku było to dokładnie ` to3k.github.io `. W polu **Description** wpisz jakiś krótki opis tego projektu, nie jest to zbytnio istotne, więc możesz wpisać coś w stylu ` Repozytorium mojego prywatnego bloga `.
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
5. Teraz stworzymy plik konfiguracyjny Jekyll. W tym celu korzystamy z przycisku **Add file** i **Create new file**.
6. Otworzy się kreator nowego pliku. W polu **Name your file...** wpisujemy ` _config.yml `. W treści pliku wklej:
```yaml
# --- GŁÓWNE USTAWIENIA ---
title: Tytuł bloga # Wpisz tutaj swój tytuł bloga
description: Opis bloga # Wpisz tutaj swój opis bloga
url: "https://to3k.github.io" # Zmień tutaj mój login na swój
baseurl: "" 
favicon: favicon.png # ikonę wrzuć do głównego folderu repozytorium pod tą nazwą (najlepiej rozdzielczość 192x192 albo 512x512)

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
  name: Jan Kowalski # Wypełni wedle uznania
  url: https://pajacyk.pl # Wypełni wedle uznania

# --- USTAWIENIA MARKDOWN ---
markdown: kramdown
kramdown:
  input: GFM
  syntax_highlighter: rouge
``` 
7. Plik w takiej formie zapisujemy w repozytorium przy użyciu zielonego przycisku **Commit changes...** znajdującym się w prawym górnym roku i ponownie **Commit changes...** w oknie, które wyskoczy. Dobrą praktyką na GitHub jest przy każdym Commit wpisywać w pole **Commit message** krótki opis tego co zrobiliśmy, co później będzie widoczne w historii zmian. Wystarczy wpisać nawet ` Utworzenie pliku _config.yml `.
8. Teraz pora na plik strony głównej. Nasz blog będzie utrzymany w duchu minimalizmu, więc na ten moment będzie się składał tylko z wytłuszczonego tytułu i spisu treści, w którym wylistujemy wszystkie posty. 
```html
---
layout: default
title: Strona główna # Wpis tutaj tytuł strony głównej
---

<div id="all-posts">
  <h3>Spis treści:</h3>
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
9. Pora stworzyć pierwszy, testowy wpis. Zgodnie z dokumentacją Jekyll wszystkie pliki, które mają zostać zakwalifikowane jako wpisy i być jako takie wyświetlone na blogu, muszą zostać umieszczone w folderze ` _posts `. Zatem musimy stworzyć taki folder, a na GitHub robi się to po prostu poprzez utworzenie w nim pierwszego pliku. W tym celu znowu korzystamy z przycisku **Add file** i **Create new file**.
10. Otworzy się kreator nowego pliku. W polu Name your file... wpisujemy wpisujemy ` _posts/ `, co spowoduje, że automatycznie zmieni nam się ścieżka, w której utworzymy plik. Dalej wpisujemy już normalnie nazwę posta ` 2026-02-10-hello-world.md `. Tutaj bardzo istotne, aby zrozumieć składnię. Nazwa posta musi zaczynać się od daty w formacie RRRR-MM-DD (rok-miesiąc-dzień), bo w ten sposób Jekyll sortuje wpisy od najnowszych do najstarszych, plus podana w ten sposób data jest wyświetlana wewnątrz posta jako informacja dla odwiedzającego. Po dacie jest myślnik i identyfikator wpisu. Niektórzy błędnie piszą, że musi to być tytuł. Nie o to w tym chodzi. W naszym przypadku identyfikatorem będzie fraza ` hello-world ` co oznacza, że link do wpisu będzie wyglądał tak ` https://<twój_login_github>.github.io/hello-world/ `. Na końcu nazwy pliku musi się oczywiście znaleźć jeszcze rozszerzenie ` .md `. Natomiast w treści pliku wklejamy:
```yaml
--- 
layout: post
title: "Hello World!"
published: true # Przydatne do późniejszego tworzenia draftów wpisów przed ich oficjalną publikacją, po prostu dopóki wpis nie jest gotowy to wpisz tu false, a Jekyll będzie go ignorował
categories: # Tu wrzucasz kategorie, którymi później można sortować wpisy
  - "kategoria1"
  - "kategoria2"
tags: # Tu wrzucasz tagi, którymi później można sortować wpisy
  - "tag1"
  - "tag2"
image: "/images/COVERIMAGE.png" # Odnośnik do grafiki wiodącej wpisu, jeżeli planujesz takowych używać
---

To jest mój pierwszy wpis na nowym blogu z silnikiem Jekyll odpalonym na GitHub Pages.
```
11. Plik w takiej formie zapisujemy w repozytorium przy użyciu zielonego przycisku **Commit changes...** znajdującym się w prawym górnym roku i ponownie **Commit changes...** w oknie, które wyskoczy.
12. To wystarczające minimum, aby uruchomić podstawowy blog. Teraz trzeba dać GitHub parę minut na zbudowanie strony (można to śledzić w zakładce **Actions** naszego repozytorium). Gdy wszystko będzie już gotowe to możemy przejść na stronę pod adresem ` https://<twój_login_github>.github.io ` i obejrzeć rezultat powyższych prac.

## Własna domena
Oczywiście jest możliwość podpięcia bloga pod własną domenę np. ` blog.tomaszdunia.pl `. W tym przypadku jes to raczej subdomena domeny ` tomaszdunia.pl `, ale nie ma to większego znaczenia, bo jest to możliwe zarówno dla domeny najwyższego poziomu jak i subdomen.

### Ustawienia po stronie GitHub
1. Wracamy do repozytorium i z paska menu w górnej części strony wybieramy **Settings**.
2. Po lewej sekcja **Code and automation** i następnie zakładka **Pages**.
3. Znajdujemy sekcję **Custom domain** i w pole tekstowe wpisumeny domenę, którą chcemy podpiąć po bloga i potwierdzamy przyciskiem **Save**.
4. Poniżej powinno się pojawić ` DNS Check in Progress `, co oznacza, że GitHub czeka już na konfigurację od strony dostawcy domeny.
5. Dodatkowo GitHub utworzy nam w repozytorium plik ` CNAME `, nie wyrzucajmy go, tak ma być.
6. Po stronie GitHub to na razie tyle, teraz musimy przejść na stronę dostawcy domeny i zalogować się do panelu do administrowania rekordami DNS domen.

### Ustawienia dla domeny najwyższego poziomu (np. tomaszdunia.pl)
Musisz ustawić następujące rekordy:
- **A** - etykieta *pusta* -> wartość *185.199.108.153*
- **A** - etykieta *pusta* -> wartość *185.199.109.153*
- **A** - etykieta *pusta* -> wartość *185.199.110.153*
- **A** - etykieta *pusta* -> wartość *185.199.111.153*
- **CNAME** - etykieta *www* -> wartość *<twój_login_github>.github.io*

*Uwaga: pamiętaj, że jeżeli były tam wcześniej jakieś rekordy to musisz je wyczyścić.*

### Ustawienia dla subdomeny (np. blog.tomaszdunia.pl)
Jeżeli domena wyższego poziomu należy do Ciebie (` tomaszdunia.pl `) to wchodzisz w ustawienia jej rekordów DNS i ustawiawsz:
- **CNAME** - etykieta *blog* (tutaj wpisujesz ten pierwszy człon subdomeny) -> wartość *<twój_login_github>.github.io*
Natomiast jeżeli masz możliwość zarządzania tylko subdomeną (bo domena nadrzędna jest na przykład zarządzana przez inny podmiot) to wszystko realizujesz z poziomu jej ustawień rekordów DNS i ustawiasz:
- **CNAME** - etykieta *pusta* -> wartość *<twój_login_github>.github.io*

*Uwaga: pamiętaj, że jeżeli były tam wcześniej jakieś rekordy to musisz je wyczyścić.*

### Wracamy do ustawień GitHub
Teraz pozostaje tylko czekać aż DNSy rozprzestrzenią się po sieci. Czasem może to być chwila, a w innym przypadku nawet 24 godziny... O zakończeniu całego procesu będziemy pewni, gdy po wejściu w **Settings** -> sekcja **Code and automation** -> Zakładka **Pages** -> w sekcji **Custom domain** zobaczymy zielony napis ` DNS check successful `. W tym momencie musimy przejść jeszcze odrobinę niżej wy zaznaczyć opcję **Enforce HTTPS** co spowoduje wygenerowanie certyfikatu SSL dla naszej strony. Zarządza tym GitHub, więc absolutnie nie musimy się tym przejmować.

Teraz można już wpisać w pasek adresu przeglądarki podpiętą domenę i cieszyć się blogiem widniejącym pod nowym adresem.

## Menu
Przeważnie blog to nie tylko wpisy. Warto wzbogacić go o dodatkowe strony jak ` O autorze `, ` Polityka prywatności ` czy chociażby ` Wesprzyj / Donate `. Zróbmy sobie zatem takie przykładowe menu, które później każdy będzie mógł dostosować pod siebie.

1. Motyw *No Style Please*, którego używamy dla tego bloga, domyślnie trzyma informacje o strukturze strony w pliku ` /_layouts/default.html `. Aby dodać nasze menu musimy wyciągnąć pierwowzór tego pliku prosto z [repozytorium motywu](https://github.com/riggraz/no-style-please), stworzyć kopię, nadpisać nią oryginał w swoim repozytorium i dorzucić do niego swój fragment kodu.
2. Oszczędzę Ci całego zachodu i poniżej przygotuję gotową zawartość pliku, który musisz utworzyć w folderze ` _layouts/ ` swojego repozytorium pod nazwą ` default.html `:
```html
<!DOCTYPE html>
<html lang="{{ site.lang | default: "pl" }}">
  {% include head.html %}

  <body>
    <div style="max-width: 700px; margin: 0 auto; padding: 20px;">

      <header class="masthead" style="margin-bottom: 40px;">
        <h1 style="margin-bottom: 10px;">
          <a href="{{ "/" | relative_url }}" style="text-decoration: none; color: inherit;">{{ site.title }}</a>
        </h1>
        <nav style="border-bottom: 1px solid #eee; padding-bottom: 10px;">
          <a href="{{ "/about" | relative_url }}">Autor</a> /
          <a href="{{ "/donate" | relative_url }}">Wesprzyj</a> /
          <a href="{{ "/rodo" | relative_url }}">Polityka prywatności</a>
          
        </nav>
      </header>

      <main>
        {{ content }}
      </main>

      <footer style="margin-top: 80px; padding-top: 20px; border-top: 1px dashed #ccc; font-size: 0.8em; color: #666;">
        <p>
          &copy; {{ site.time | date: '%Y' }} {{ site.author.name }}.
          Treść dostępna na licencji <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pl" target="_blank">CC BY-SA 4.0</a>.
        </p>
        <p>
          Blog powstał na podstawie poradnika dostępnego na<a href="https://blog.tomaszdunia.pl/blog-jekyll-github/">blog.tomaszdunia.pl</a>!
        </p>
        <p>Zachęcam również do subskrybowania tego bloga poprzez <a href="/feed.xml">kanał RSS</a>.</p>
      </footer>

    </div>
  </body>
</html>
```
3. Plik w takiej formie zapisujemy w repozytorium przy użyciu zielonego przycisku **Commit changes...** znajdującym się w prawym górnym roku i ponownie **Commit changes...** w oknie, które wyskoczy.
4. Jako bonus w powyższym pliku umieściłem stopkę, w której zawarłem informację o licencji, o tym że blog powstał w oparciu o ten poradnik (możesz śmiało usunąć tą informację lub ją zostawić, będzie mi bardzo miło) oraz dodałem odnośnik do kanału RSS, żeby Twoim przyszłym czytelnikom było łatwiej wrzucić go do swojego ulubionego czytnika.
5. Wracając do temat menu, utworzyłem je tak, aby składało się z odnośników do trzech podstron - ` /about `, ` /donate ` i ` /rodo `. Na tym etapie linki prowadzą donikąd, a więc skorzystanie z nich zakończy się wyświetleniem błędu 404. Aby temu zapobiec musisz stworzyć te trzy podstrony w głównym folderze repozytorium, ale to już Twoje zadanie domowe. Ja jedynie mogę pokazać Ci kod moich podstron, aby dać materiał, na którym można się wzorować:
    - moje **about.md** - [strona na blogu](https://blog.tomaszdunia.pl/about/) a tutaj [kod źródłowy](https://raw.githubusercontent.com/to3k/to3k.github.io/refs/heads/main/about.md)
    - moje **donate.md** - [strona na blogu](https://blog.tomaszdunia.pl/donate/) a tutaj [kod źródłowy](https://raw.githubusercontent.com/to3k/to3k.github.io/refs/heads/main/donate.md)
    - moje **rodo.md** - [strona na blogu](https://blog.tomaszdunia.pl/rodo/) a tutaj [kod źródłowy](https://raw.githubusercontent.com/to3k/to3k.github.io/refs/heads/main/rodo.md)

## Wyszukiwarka
Każdy szanujący się blog powinien mieć narzędzie do wyszukiwania odpowiednich fraz w tytułach, treści i tagach jego wpisów. My jesteśmy szanującymi się autorami, więc oczywiście udostępnimy takie narzędzie swoim czytelnikom.

1. Głównym problemem do rozwiązania jest to, że w tym wpisie omawiamy statyczną stronę, która nie ma bazy danych SQL, którą możnaby przeszukać. Dlatego na potrzeby naszej wyszukiwarki musimy stworzyć plik, który będzie dynamicznie wypełniał się listą wszystkich wpisów wraz z ich zawartością. To będzie taka jakby baza danych, w której będziemy szukać odpowiednich rekordów, które będą pasować do naszego zapytania. Plik ten utworzymy w głównym folderze repozytorium, damy mu nazwę ` search.json `, a jego treść będzie następująca:
```json
---
layout: null
---
[
  {% for post in site.posts %}
    {
      "title"    : {{ post.title | jsonify }},
      "category" : {{ post.category | jsonify }},
      "tags"     : {{ post.tags | join: ', ' | jsonify }},
      "url"      : {{ post.url | relative_url | jsonify }},
      "date"     : {{ post.date | date: "%d-%m-%Y" | jsonify }},
      "content"  : {{ post.content | strip_html | strip_newlines | jsonify }}
    }{% unless forloop.last %},{% endunless %}
  {% endfor %}
]
```
2. Plik w takiej formie zapisujemy w repozytorium przy użyciu zielonego przycisku **Commit changes...** znajdującym się w prawym górnym roku i ponownie **Commit changes...** w oknie, które wyskoczy.
3. Teraz musimy jeszcze zmodyfikować plik strony głównej ` index.md `, w którym wczytamy bibliotekę ` unpkg.com/simple-jekyll-search `, napiszemy skrypt wyszukiwarki w oparciu o nią i umieścimy interaktywne pole tekstowe do wpisywania frazy. Oto gotowy kod:
```html
---
layout: default
title: Strona główna # Wpis tutaj tytuł strony głównej
---

<div style="margin-bottom: 30px;">
  <input type="text" id="search-input" placeholder="Szukaj..." style="width: 100%; padding: 8px; font-family: monospace; border: 1px solid #ccc; border-radius: 4px;">
  <ul id="results-container" style="list-style: none; padding-left: 0; margin-top: 10px;"></ul>
</div>

<div id="all-posts">
  <h3>Spis treści:</h3>
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

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '/search.json',
    searchResultTemplate: '<li style="margin-bottom: 8px;"><span style="color: #666; font-family: monospace; margin-right: 10px;">{date}</span> &raquo; <a href="{url}" style="font-weight: bold;">{title}</a></li>',
    noResultsText: 'Nie znaleziono pasujących wpisów.',
    limit: 500,
    fuzzy: false
  })
</script>
```

## Markdown
Dla osób przyzwyczajonych do Worda lub klasycznego edytora WordPressa (Gutenberg), Markdown może na pierwszy rzut oka wydawać się krokiem wstecz. W końcu zamiast klikać w wygodne ikonki, musimy wpisywać jakieś "dziwne znaczki".

W rzeczywistości **Markdown** to wolność. To lekki język znaczników, który pozwala formatować tekst bez odrywania rąk od klawiatury. Jest uniwersalny (działa na GitHubie, w Notion, Obsidianie, Discordzie) i – co najważniejsze – jest czystym tekstem. Oznacza to, że za 10 lat bez problemu otworzysz swoje wpisy w dowolnym edytorze, nie martwiąc się o to, że baza danych WordPressa się rozjechała.

W Jekyll to właśnie pliki Markdown ` .md ` są źródłem treści. Podczas budowania strony, Jekyll automatycznie zamienia je na gotowy kod HTML.

### Szybka ściąga z Markdowna

Oto absolutne podstawy, których używam przy pisaniu każdego wpisu:

- **Nagłówki:** Zamiast wybierać z listy "Nagłówek 2", stawiamy płotki.
    - `# Tytuł główny (H1)`
    - `## Podtytuł (H2)`
    - `### Mniejszy nagłówek (H3)`
- **Pogrubienie i kursywa:**
    - `**To będzie pogrubione**` → **To będzie pogrubione**
    - `*To będzie kursywą*` → *To będzie kursywą*
- **Listy:**
    - `- Element listy` (kropka)
    - `1. Element listy` (numerowana)
- **Linki i Obrazki:**
    - Link: `[Tekst linku](https://adres.pl)`
    - Obrazek: `![Opis alternatywny](link-do-obrazka.jpg)`
- **Kod (moje ulubione narzędzie na blogu technicznym):**
    - Pojedynczy grawis \`kod\` do wstawek w tekście.
    - Potrójny grawis (\`\`\`) do bloków kodu.

## Słowa końcowe
To tylko tyle i aż tyle. W mojej ocenie technicznie blog nie potrzebuje niczego więcej. Tworząc swoją stronę, szczególnie pierwszą, przeważnie łapiemy się na tym, że chcemy wycisnąć z niej co tylko się da - żeby była "na wypasie". Zarówno jeżeli chodzi o wygląd jak i bajery (np. widżety). W praktyce nie są to istotne rzeczy. Zapominamy natomiast o tym co jest najważniejsze, czyli o treści. To właśnie ona jest kluczowa i stanowi prawdziwą wartość bloga. Dlatego na wypasie powinna być treść, a wszystko wokół niej winno być możliwie jak najbardziej minimalistyczne, żeby nie przyćmiewać swoim pozornym blaskiem tego co powinno naturalnie lśnić najjaśniej. Jasny gwint, ale ze mnie filozof... Wracając już na Ziemię, mam nadzieję, że ten poradnik komuś się przyda i jeżeli będziesz to Ty to koniecznie pokaż mi swojego bloga, gdy już go opublikujesz!