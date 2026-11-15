---
title: "Limit obserwowanych na Mastodonie"
date: 2023-03-25
categories: 
  - "szorty"
tags: 
  - "api"
  - "follow"
  - "followers"
  - "following"
  - "limit"
  - "mastodon"
  - "obserwowani"
  - "obserwujacy"
  - "spambot"
image: "/images/szorty.webp"
description: "Szukając w dokumentacji Mastodona czegoś zupełnie innego natrafiłem na pewien ciekawy wątek na GitHub dotyczący sugestii wprowadzenia limitu kont jakie..."
---

Spis treści:
* TOC
{:toc}

Szukając w dokumentacji _Mastodona_ czegoś zupełnie innego natrafiłem na pewien [ciekawy wątek na GitHub](https://github.com/mastodon/mastodon/issues/2311) dotyczący sugestii wprowadzenia **limitu kont jakie można obserwować z jednego konta**. Okazuje się, że w 2017 pierwotni _mastodonowicze_ zauważyli problem z użytkownikami, którzy wysyłają kosmiczne ilości zapytań do _API_. Były to boty ustawione na zdobywanie jak największej ilości obserwowanych. Po co? Jak nie wiadomo o co chodzi w Internecie, to chodzi o **spam**! Mechanizm był prosty - nazwa oraz awatar bota zawierały reklamę, a bot obserwując danego użytkownika niejako pojawiał mu się z automatu w zakładce _Powiadomienia_. Sprytne... Ale nie bardziej sprytne niż deweloperzy stojący za konstrukcją _Mastodona_. Reakcja na sugestię nie była natychmiastowa, ale po lekko ponad roku od powstania _issue_ został wykonany [_Commit_ (aktualizacja), która wprowadzała odpowiedni limit](https://github.com/mastodon/mastodon/pull/8807).

Limit od tamtej pory polega na tym, że z jednego konta bez ograniczeń można obserwować **7500 kont**. Po przekroczeniu tej wartości wchodzi w grę **dodatkowy warunek**:

> Możesz obserwować więcej niż 7500 kont jeżeli Twoja liczba obserwujących pomnożona przez 1.1 jest większa.

W praktyce oznacza to, że do posiadania możliwości obserwowania 7501-ego konta konieczne jest posiadanie (7501 / 1.1 =) **6820 obserwujących**. To w praktyce rozwiązało problem, gdyż boty tego typu nie zdobywały porównywalnej ilości obserwujących do tego ile posiadały obserwowanych.

Na koniec chciałbym jeszcze dodać, że zarówno próg 7500 jak i mnożnik 1.1 **są modyfikowalne w przypadku posiadania swojej własnej _instancji_**. Niestety otwiera to okno do dalszych nadużyć, ale trzeba pamiętać, że taka "odblokowana" instancja spamera:

1. jest dość prosta do zablokowania,

3. posiadając konta z dużą ilością obserwowanych strasznie zapycha sobie przestrzeń dyskową danymi, które te osoby generują,

5. utrudnia utrzymanie anonimowości, bo zawsze jest możliwość łatwiejszego śledzenia spamera po IP czy nawet danych rejestracyjnych domeny, na której stoi _instancja_.

Czy jest to gra warta świeczki? Nie wiem, nie jestem spamerem.

Toot dotyczący tego tematu na Mastodonie:

<iframe src="https://mastodon.tomaszdunia.pl/@to3k/110085181200571476/embed" class="mastodon-embed" style="max-width: 100%; border: 0" allowfullscreen="allowfullscreen" width="100%"></iframe>

<script src="https://mastodon.tomaszdunia.pl/embed.js" async="async"></script>
