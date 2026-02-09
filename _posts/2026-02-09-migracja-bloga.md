---
layout: post
title: "Żegnaj Wordpress, witaj Jekyll"
date: 2026-02-09
published: true
categories: 
  - "projekty"
  - "przemyslenia"
  - "self-hosting"
tags: 
  - "jekyll"
  - "wordpress"
  - "blog"
  - "github"
  - "migracja"
  - "self-hosting"
  - "open-source"
image: "/images/wptojekyll.png"
---

[🇵🇱->🇬🇧 Go to english version of this post / Przejdź do angielskiej wersji tego wpisu](https://blog.tomaszdunia.pl/migracja-bloga-eng/)

Spis treści:
* TOC
{:toc}

W KOŃCU! W końcu... znalazłem czas, uzbierałem odrobinę chęci i przezwyciężyłem obawy przed zepsuciem czegoś. Na niniejszy blog wjechał buldożer, zaorał go, a później wpadła ekipa remontowa i go odbudowała.
Dla potomnych zostawie tutaj [link do zrzutu ekranu](https://web.archive.org/web/20260208181656/http://web.archive.org/screenshot/https://blog.tomaszdunia.pl/) zrobionego przy użyciu Internet Archive obrazującego jak blog wyglądał wcześniej.

## Skąd taka zmiana?
Już od dłuższego czasu doskwierało mi to, że wydajność tej strony wołała o pomstę do nieba. Na początku łudziłem się, że znajdę tego przyczynę, ale z czasem jednak zrozumiałem, że Wordpress to bagno, w którym brodząc zostaje się tylko wciągniętym głębiej. WP na początku wydaje się super przyjaznym rozwiązaniem nawet dla niezbyt zaawansowanego użytkownika. Gotowe motywy, które instaluje się jednym kliknięciem. Wtyczki praktycznie do wszystkiego, również dostępne pod palcem. Może i tak, ale im dalej w las tym więcej drzew i to całe lśniące badziewie zapycha stronę coraz bardziej. Nie twierdzę, że Wordpress to całkowite gówno, bo wiem, że są osoby, które znają go od podszewki i są w stanie zrobić w tym środkowisku absolutnie wszystko. Jednakże ja nigdy nie miałem tyle cierpliwości, żeby przewalać się przez dokumentację tak obszerną jak ta od twórców WP.

## Dlaczego Jekyll?
Trafiłem na [to oprogramownie](https://jekyllrb.com/) w zasadzie przez przypadek. Dowiedziałem się o nim z podcastu [Nadgryzieni](https://www.youtube.com/playlist?list=PLJaCoP2ajoU_5k2VG430hU1_-MaQrEMK-) (od iMagazine), w którym Michał Śliwiński, twórca [Nozbe](https://nozbe.com/pl), przedstawił je jako silnik swojej prywatnej strony internetowej. Wszedłem na [podany przez niego adres michael.team](https://michael.team) i zobaczyłem jedną z najbardziej obrzydliwych strony internetowych jakie widziałem w ostatnim czasie. No była po prostu **PRZEPIĘKNA**. Zakochałem się od razu i zacząłem grzebać w sieci w celu zdoktoryzowania się w temacie jak sprawić sobie samemu takie szkaradztwo. Okazało się, że to szalenie proste, a najłatwiejszą drogą jest skorzystanie z **Github Pages**. Tak wiem... Github to Microsoft, a Microsoft to zło. Zanim jednak pół Mastodona mnie ukrzyżuję chciałbym powiedzieć coś na swoją obronę. Otóż wstępne uruchomienie bloga opartego o Jekyll na infrastrukturze Github nie oznacza, że to rozwiązanie permanentne. Jedną (z wielu) zalet Jekyll jest to, że bardzo prosta jest jego migracja na w zasadzie dowolne środowisko/sprzęt. Docelowo myślę o zupełnym self-hostingu i pewnie tak się to właśnie skończy, bo od mojego ostatniego wpisu na tym blogu zmieniło się w moim życiu dość sporo. Budowa domu została zakończona, uporałem się z jego wykończeniem, mam już światłowód i ogarnąłem temat serwerów domowych, więc mam zaplecze, na którym mogę się bawić.

## A dlaczego nie WriteFreely, hę?
To w sumie dobre pytanie, szczególnie ze względu na to, że jestem osobą stojącą za oficjalną polską instancją [WriteFreely.PL](https://writefreely.pl)... Wbrew pozorom Jekyll wydaje mi się prostszym i mniej złożonym narzędziem od WriteFreely. Może tutaj chodzić o tą całą federację z Fediwersum, co dalej jest dla mnie nie do końca rozwiązaną zagadką. Do tego na pewno częściowo powstrzymało mój zapał to, że w przypadku WF musiałbym samemu zadbać o zewnętrzną bazę do przechowywania grafik.

## Czy będzie z tego poradnik?
To tak jakby zapytać czy dzik sra w lesie. Myślę, że Ci którzy mnie znają lub przeczytali na tym blogu choć kilka wpisów nigdy nie zadaliby takiego pytania, gdyż oczywistym jest, że spłodzę z tego całego procesu migracji niechudy poradnik. Opiszę w nim jak krok po kroku uruchomić swojego bloga na Github Pages, wykorzystując Jekyll jako silnik, a później (możliwe, że w oddzielnym wpisie) opowiem o procesie migracji bloga z Wordpress.

## Co o tym myślisz?
Czy według Ciebie, drogi Czytelniku, zmiana której dokonałem jest na plus? Oceń ją proszę! Napisz także czy powstanie poradnika na temat Jekyll to temat interesujący i warty opisania na tym blogu. Fajnie było znowu coś napisać, więc myślę, że nawet najgorszy hejt nie byłby mnie w stanie powstrzymać, ale i tak jestem ciekaw Twojej opinii. Czuję kosmiczny przypływ chęci klepania w klawiaturę, więc myślę, że przez jakiś czas mogę być lekko upierdliwy jeżeli chodzi o ilość tekstów opublikowanych na tej stronie.

## Czy wszystko działa?
Migrację wykonałem trochę na wariata, więc nie mam tak do końca pewności, że wszystko działa jak należy, dlatego liczę na informację zwrotną jeżeli ktoś zauważy, że coś jest nie tak. To czego najbardziej żałuję to tego, że nie udało mi się zmigrować wszystkich komentarzy pod postami. Na nowym blogu jako system komentarzy wykorzystuję [Giscus](https://giscus.app/pl), który do pisania wymaga konta na Github. Nie jest to rozwiązanie idealne, ale na pewno na początek było dla mnie najłatwiejsze do implementacji. Natomiast wszystkie wpisy ze starego bloga odeszły niestety w niepamięć. Podjąłem próbę ich migracji i nawet kilka z nich udało się hurtowo przerzucić, ale zrobił się z tego straszny bałagan i zarzuciłem ten pomysł. Postanowiłem, że po prostu zacznę od nowa.