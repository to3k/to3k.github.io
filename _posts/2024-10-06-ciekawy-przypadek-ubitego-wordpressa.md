---
title: "Ciekawy przypadek ubitego Wordpress'a"
date: 2024-10-06
categories: 
  - "shorts"
  - "szorty"
tags: 
  - "activitypub"
  - "enablemastodonapps"
  - "friends"
  - "hackernews"
  - "htaccess"
  - "plugin"
  - "wordpress"
  - "wtyczka"
image: "/images/szorty.png"
---

Opublikowałem dzisiaj wpis [_Darmowa chmura ~200GB na Twoje pliki_](https://blog.tomaszdunia.pl/darmowa-chmura-200gb/), który stał się dość popularny. Udostępniłem go w kilku miejscach, a jednym z nich był portal [_Hacker News_](https://news.ycombinator.com/item?id=41756220), gdzie wpis wybił się na chwilę na stronę główną. Licznik odwiedzin wystrzelił co z początku mocno mnie ucieszyło. Jednakże po paru minutach zacząłem dostawać wiadomości, że blog działa, ale sam wpis się nie ładuje. Sprawdziłem i faktycznie tak było. Żadna z podstron bloga nie wczytywała się prawidłowo, a zamiast niej pojawiała się domyślna strona hostingu. Myślę sobie - pięknie, to tyle ze spokojnej niedzieli...

Był to już nie pierwszy raz kiedy blog mi eksplodował na skutek dużej liczby wyświetleń, która uderzała gwałtownie. Przeważnie były to problemy z bazą danych _MySQL_, która osiągała limit zapytań. Uznałem, że tym razem to pewnie to samo. To co jednak zwróciło moją uwagę to fakt, że strona główna działała prawidłowo, tak samo jak panel administracyjny. Na tej podstawie doszedłem do wniosku, że to musi być coś innego. Ale co?

Jak nie wiem co zrobić to przeważnie uderzam w klawisze i publikuję toota z prośbą o pomoc na [_Mastodonie_](https://infosec.exchange/@to3k). Tak też zrobiłem i tym razem. Na szczęście na pomoc przyszedł mi [_@m0bi_](https://mastodon.com.pl/@m0bi), który skierował mnie we właściwym kierunku. To już nie pierwszy raz kiedy _m0bi_ ratuje mi skórę za co z tego miejsca dziękuję! Jego podpowiedź brzmiała "_sprawdź rewrite'y i ogólnie .htaccess_". Bingo! Gdy zajrzałem do zawartości pliku _.htaccess_ mojego bloga okazało się, że wygląda tak:

```markup
<Files "wp-login.php">
AuthType Basic
AuthName "User: [...] Password: [...]"
AuthUserFile /etc/apache2/AUTH/[...]
Require valid-user
</Files>

# BEGIN WordPress
# The directives (lines) between "BEGIN WordPress" and "END WordPress" are
# dynamically generated, and should only be modified via WordPress filters.
# Any changes to the directives between these markers will be overwritten.

# END WordPress
```

Jak widać wszystkie reguły z sekcji _Wordpress'a_ zostały wyczyszczone. Zatem rozwiązanie było bardzo proste i ograniczało się do dopisania:

```markup
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
```

To oczywiście rozwiązało problem i strona wróciła do swojej pełnej sprawności. Uf... Kryzys zażegnany, więc przyszła pora zastanowić się co spowodowało wyczyszczenie pliku _.htaccess_ z reguł _rewrite_. W przypadku _Wordpress'a_ winę za katastrofę przeważnie ponosi nieprawidłowo działająca lub wręcz złośliwa wtyczka (plugin). Nie mam stuprocentowej pewności, bo nie udało mi się odtworzyć tej sytuacji, ale mam bardzo poważne podejrzenia, że mogła to być konkretnie wtyczka [_Enable Mastodon Apps_](https://wordpress.org/plugins/enable-mastodon-apps/). Jak na złość zainstalowałem ją dzisiaj, bo trochę grzebałem w ustawieniach wtyczki [_ActivityPub_](https://wordpress.org/plugins/activitypub/) oraz [_Friends_](https://pl.wordpress.org/plugins/friends/) i natrafiłem na nią jako rozszerzenie działania tej drugiej. Co ciekawe po jej instalacji nie miałem czasu się dalej bawić, więc nawet jej nie włączyłem i odroczyłem kucowanie na kiedy indziej. Czy to możliwe, że jedynie zainstalowana, ale nie włączona wtyczka mogła tak nabruździć? To pytanie pozostawiam na razie bez odpowiedzi, ale na pewno będę jeszcze drążył ten temat.

* * *

## An interesting case of Wordpress being killed

I published a post today titled [_~200GB Free Cloud for Your files_](https://blog.tomaszdunia.pl/darmowa-chmura-200gb/), which became quite popular. I shared it in several places, one of them being [_Hacker News_](https://news.ycombinator.com/item?id=41756220), where it briefly made it to the homepage. The visitor counter skyrocketed, which at first made me very happy. However, after a few minutes, I started receiving messages saying that the blog was working, but the post itself wasn’t loading. I checked, and indeed that was the case. None of the blog’s subpages were loading correctly, and instead, the default hosting page appeared. I thought to myself - great, so much for a peaceful Sunday...

This wasn’t the first time the blog crashed due to a large number of views that hit suddenly. Usually, it was _MySQL_ database issues, reaching the query limit. I figured it was probably the same this time. However, what caught my attention was the fact that the homepage was working fine, as well as the admin panel. Based on this, I concluded that it must be something else. But what?

When I don’t know what to do, I usually hit the keys and publish a toot asking for help on [_Mastodon_](https://infosec.exchange/@to3k). That’s what I did this time as well. Fortunately, [_@m0bi_](https://mastodon.com.pl/@m0bi) came to help, pointing me in the right direction. It’s not the first time _m0bi_ has saved my day, so I would like to thank him once again from here! His advice was "_check the rewrites and the .htaccess file_". Bingo! When I looked into the contents of my blog’s _.htaccess_ file, it turned out to look like this:

```markup
<Files "wp-login.php">
AuthType Basic
AuthName "User: [...] Password: [...]"
AuthUserFile /etc/apache2/AUTH/[...]
Require valid-user
</Files>

# BEGIN WordPress
# The directives (lines) between "BEGIN WordPress" and "END WordPress" are
# dynamically generated, and should only be modified via WordPress filters.
# Any changes to the directives between these markers will be overwritten.

# END WordPress
```

As you can see, all the rules from the _WordPress_ section were cleared out. So, the solution was very simple, and it was just a matter of adding the following:

```markup
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
```

This, of course, solved the problem, and the site returned to full functionality. Phew… Crisis averted. Now, it was time to figure out what caused the _.htaccess_ file to lose its _rewrite_ rules. In the case of _WordPress_, the culprit is usually a malfunctioning or even malicious plugin. I’m not 100% sure, as I wasn’t able to reproduce the issue, but I have a strong suspicion that it could have been the [_Enable Mastodon Apps_](https://wordpress.org/plugins/enable-mastodon-apps/) plugin. As luck would have it, I installed it today because I was tinkering with the settings of the [_ActivityPub_](https://wordpress.org/plugins/activitypub/) and [_Friends_](https://pl.wordpress.org/plugins/friends/) plugins and came across it as an extension for the latter. Interestingly, after installing it, I didn’t have time to play with it further, so I didn’t even activate it and postponed having fun for another time. Is it possible that just an installed, but not activated plugin could cause such trouble? I’ll leave this question unanswered for now, but I will definitely investigate further.
