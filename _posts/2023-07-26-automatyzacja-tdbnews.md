---
title: "Prosta automatyzacja TDBNews"
date: 2023-07-26
categories: 
  - "poradniki"
  - "projekty"
tags: 
  - "automatyzacja"
  - "cron"
  - "mastodon"
  - "php"
  - "reddit"
  - "rss"
  - "xml"
coverImage: "/images/automatyzacja_tdbnews.png"
---

[🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/automatyzacja-tdbnews-eng/)

Już od kilku tygodni publikuję serię niedzielnych wpisów _#TDBNews_, w której wypisuję ciekawe rzeczy, na które natrafiłem w danym tygodniu. Ręczne zbieranie tych, w mojej ocenie, interesujących artykułów byłoby bardzo żmudną i niezwykle nieefektywną pracą, którą musiałbym powtarzać cyklicznie co tydzień, poświęcając na to część niedzielnego czasu, który mógłbym przeznaczyć na inne zajęcia. Z uwagi na to postanowiłem to zautomatyzować i to w baaardzo prosty sposób. Zasada działania jest trywialna i dla ułatwienia przedstawię ją w punktach.

1. Codziennie przeglądam moje źródła _RSS_ (używam aplikacji _[Reeder](https://reederapp.com/)_), oś czasu na _Mastodon_ oraz _Reddita_, czyli moje trzy główne okna na informacje ze świata.

3. Gdy natrafię na jakiś pozornie ciekawy artykuł to zapisuję go do listy _Przeczytaj później_, do której wracam przeważnie dopiero wieczorem.

5. Następnie te faktycznie ciekawe rzeczy udostępniam na [moim profilu na _Mastodonie_](https://mastodon.tomaszdunia.pl/@to3k) dopisując do niego specjalny hashtag _#TDBNews_.

7. Skrypt _PHP_ śledzący kanał _RSS_ mojego _mastodonowego_ profilu wyłapuje te tooty i zapisuje je do pliku tekstowego.

9. Pod koniec tygodnia (w niedzielę) uruchamiam drugi skrypt, który z zebranych tootów tworzy mi gotowy kod wpisu zgodnego z notacją używaną przez _Wordpress_. W praktyce składa się on ze statycznego wstępu i zakończenia, które w każdym wpisie _TDBNews_ są takie same, i części zmiennej znajdującej się w środku, w której embeduję (osadzam) zebrane _tooty_ w postaci ramek _iframe_.

11. Pozostaje mi tylko nadać tytuł wpisu, co ogranicza się do podania aktualnej daty, i opublikować go.

Przykłady tego typu wpisów można zobaczyć przechodząc [tutaj](https://blog.tomaszdunia.pl/category/tdbnews/). A w tym wpisie pokażę od kuchni jak wyglądają te skrypty, dzięki którym realizuję tę prostą automatyzację.

## Skrypt zbierający moje tooty oznaczone hashtagiem #TDBNews

Standardowo wytłumaczę jego działanie poprzez komentarze umieszczone w środku kodu. Tutaj może się też przydać znajomość treści wpisu, w którym pokazywałem [jak zrobiłem bota do publikacji wiadomości ze znanych portali na _Mastodonie_](https://blog.tomaszdunia.pl/mews/).

```php
<?php
    header('Content-Type: text/html; charset=utf-8');
    
    // URL DO MOJEGO PROFILU NA MASTODONIE
    $url = "https://mastodon.tomaszdunia.pl/@to3k.rss";

    // PLIK Z JUŻ ZNALEZIONYMI TOOTAMI
    $file_all = file_get_contents("tdbnews_all.txt");

    // ZAŁADUJ PLIK XML (FEED RSS)
    $feeds = simplexml_load_file($url);

    // USTAW STREFĘ CZASOWĄ
    date_default_timezone_set("Europe/Warsaw");

    // DATA PONIEDZIAŁKU W TYM TYGODNIU DO ODFILTROWANIA WSZYSTKIEGO PRZED TĄ DATĄ
    $monday = strtotime("Monday this week");
    $monday = date("Y-m-d", $monday);
    
    // JEŻELI FEED RSS NIE JEST PUSTY
    if(!empty($feeds))
    {
        // ROZBIJ FEED NA ODDZIELNE PRZEDMIOTY (TOOTY)
        foreach ($feeds->channel->item as $item)
        {
            // PRZEKONWERTUJ LINK NA CIĄG (BEZ TEGO FUNKCJA STR_CONTAINS WYWALI BŁĄD)
            $link = strval($item->link);
            
            // POBIERZ DATĘ PUBLIKACJI I ZMIEŃ JEJ FORMAT NA RRRR-MM-DD
            $pubDate = $item->pubDate;
            $pubDate = strtotime($pubDate);
            $pubDate = date("Y-m-d", $pubDate);

            // POBIERZ TREŚĆ
            $description = strval($item->description);

            if(str_contains($file_all, $link) OR $pubDate < $monday OR !str_contains($description, "https://mastodon.tomaszdunia.pl/tags/TDBNews"))
            {
                // JEŻELI LINK JEST JUŻ W PLIKU (BYŁ JUŻ PRZETWORZONY)
                // LUB JEŻELI DATA PUBLIKACJI JEST PRZED PONIEDZIAŁKIEM W TYM TYGODNIU (JEST ZA STARY)
                // LUB JEŻELI TOOT NIE ZAWIERA HASHTAGA TDBNEWS (JEST O CZYMŚ INNYM)
                // POMIŃ GO I IDŹ DO NASTĘPNEGO
                continue;
            }
            else
            {
                // JEŻELI WSZYSTKIE WARUNKI SPEŁNIONE
                // DOPISZ LINK DO ZMIENNEJ Z KWALIFIKUJĄCYMI SIĘ TOOTAMI
                $file_all .= $pubDate.";".$link."\n";
            }
        }
    }

    // ZAKTUALIZUJ PLIK Z LISTĄ KWALIFIKUJĄCYCH SIĘ TOOTÓW
    file_put_contents("tdbnews_all.txt", $file_all);
?>
```

## Skrypt generujący gotowy wpis Wordpress

Tak samo jak w przypadku poprzedniego kodu tak i tutaj wszystko wyjaśnione w komentarzach.

```php
<?php
    // PLIK ZE ZNALEZIONYMI TOOTAMI
    $file_all = file_get_contents("tdbnews_all.txt");

    // PODZIEL ZAWARTOŚĆ PLIKU NA ODDZIELNE LINIE
    $explode_file = explode("\n", $file_all);

    // USTAW STREFĘ CZASOWĄ
    date_default_timezone_set("Europe/Warsaw");

    // DATA PONIEDZIAŁKU W TYM TYGODNIU DO ODFILTROWANIA WSZYSTKIEGO PRZED TĄ DATĄ
    $monday = strtotime("Monday this week");
    $monday = date("Y-m-d", $monday);

    // DEKLARACJA TABLICY Z NEWSAMI Z TEGO TYGODNIA
    $news_array = array();
    
    // PRZEJDŹ PRZEZ WSZYSTKIE LINIE JEDNA PO DRUGIEJ
    foreach($explode_file as $line)
    {
        // JEŻELI LINIA NIE JEST PUSTA
        if(!empty($line))
        {
            // ODSEPARUJ DATĘ PUBLIKACJI I LINK
            $explode_line = explode(";", $line);
            // JEŻELI DATA PUBLIKACJI NIE JEST PRZED ZESZŁYM PONIEDZIAŁKIEM
            if($explode_line[0] >= $monday)
            {
                // DODAJ TEGO TOOTA DO TABLICY Z NEWSAMI Z TEGO TYGODNIA
                array_push($news_array, ['pubDate' => $explode_line[0], 'link' => $explode_line[1]]);
            }
        }
    }
    
    // ODWRÓC ZAWARTOŚĆ TABELI (SORTOWANIE TOOTÓW OD NAJSTARSZEGO DO NAJNOWSZEGO)
    $news_array = array_reverse($news_array);
?>

<!-- SEKCJA Z WYNIKIEM, STATYCZNY WSTĘP, KOD PHP Z FUNKCJĄ FOREACH, KTÓREJ REZULTATEM JEST WYŚWIETLENIE WSZYSTKICH TOOTÓW W RAMCE IFRAME, STATYCZNE ZAKOŃCZENIE -->
<!-- ELEMENT PLAINTEXT JEST UŻYWANY DO WYŚWIETLENIA KODU HTML W NIEPRZETWORZONEJ FORMIE (WSZYSTKO PO TYM TAGU) -->
<plaintext>
<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph -->
<p>🇵🇱 <em>#TDBNews</em> to nazwa pochodząca od <em>Tomasz Dunia Blog News</em>. Pod taką nazwą co niedzielę publikuję zbiór ciekawych wiadomości na jakie udało mi się natrafić w ubiegłym tygodniu. Zdecydowana większość linkowanych artykułów będzie anglojęzyczna, bo wszystkie źródła polskojęzyczne, które śledzę, są za <em>paywall'ami</em>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph -->
<p>🇬🇧 <em>#TDBNews</em> is a name coming from <em>Tomasz Dunia Blog News</em>. Under this name, every Sunday I publish a collection of interesting news that I came across in the previous week. The vast majority of linked articles will be in English, because all the Polish-language sources, I follow, are behind <em>paywalls</em>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:heading -->
<h2 class="wp-block-heading">W tym tygodniu znalazłem / This week I found 👇</h2>
<!-- /wp:heading -->
<?php
    foreach($news_array as $news)
    {
        echo "
<!-- wp:html -->
<iframe src=\"".$news['link']."/embed\" class=\"mastodon-embed\" style=\"max-width: 100%; border: 0\" width=\"100%\" allowfullscreen=\"allowfullscreen\"></iframe><script src=\"https://mastodon.tomaszdunia.pl/embed.js\" async=\"async\"></script>
<!-- /wp:html -->
        ";
    }
?>

<!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph -->
<p>🇵🇱 Jak widzisz to zestawienie powstaje poprzez osadzenie tootów (inaczej postów), które opublikowałem w poprzednim tygodniu na <em>Mastodonie</em>. Są one oznaczone specjalnym hashtagiem. To oznacza, że informację o tych treściach możesz uzyskać jeszcze przed publikacją tego zestawienia. Wystarczy śledzić <a href="https://mastodon.tomaszdunia.pl/@to3k">mój profil na <em>Mastodonie</em></a> lub sam <a href="https://mastodon.tomaszdunia.pl/tags/TDBNews">hashtag <em>#TDBNews</em></a>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph -->
<p>🇬🇧 As you can see, this compilation is created by embedding toots (also known as posts) that I published last week on <em>Mastodon</em>. They are marked with a special hashtag. This means that you can access information about these contents even before this compilation is published. Just follow <a href="https://mastodon.tomaszdunia.pl/@to3k">my profile on <em>Mastodon</em></a> or the <a href="https://mastodon.tomaszdunia.pl/tags/TDBNews">hashtag <em>#TDBNews</em></a> itself.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->
```

## Podsumowanie

Czyż nie było to proste? W mojej ocenie nie dość, że proste to jeszcze warte zachodu! Jak to? Mam zasadę, że każda automatyzacja czynności, która z jednej strony jest niezbyt wymagająca intelektualnie, a z drugiej powtarza się cyklicznie, ma sens i na dłuższą metę oszczędzi wiele czasu. Weźmy przykład _TDBNews_. Tworzenie takiego zestawienia ręcznie zajęłoby mi co tydzień przynajmniej 20 minut, natomiast z wyżej opisaną automatyzacją zajmuje mi to nie więcej niż 3 minuty. Weźmy zatem te 15 minut co tydzień. W roku mamy 52 tygodnie, a więc rocznie zyskuję 780 minut, czyli 13 godzin! To ponad pół dnia, które mogę poświęcić rodzinie, czy nawet na tworzenie kolejnego wpisu na ten blog.
