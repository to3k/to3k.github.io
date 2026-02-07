---
title: "Brawo dla PKO BP za U2F ?"
date: 2024-10-05
categories: 
  - "przemyslenia"
tags: 
  - "2fa"
  - "pkobp"
  - "santander"
  - "u2f"
  - "yubico"
  - "yubikey"
image: "/images/pkou2f.png"
---

Dostałem dzisiaj rano maila od _PKO BP_, w którym trzymam swoje obligacje skarbowe. Jakaż była moja radość, gdy zobaczyłem, że mail dotyczy tego, że _PKO_ zaimplementowało w swoim systemie możliwość uwierzytelnienia się podczas logowania przy pomocy klucza bezpieczeństwa _U2F_ np. _Yubikey_. Myślę sobie "WOW! W końcu branża bankowości wstępuje w XXI wiek". Czy jednak faktycznie jest się z czego cieszyć i zostało to wprowadzone prawidłowo? No niestety według mnie nie do końca...

Zacznijmy jednak od tego, że polska (nie wiem jak to wygląda na arenie międzynarodowej, bo może jest taka samo) branża bankowości jest w totalnym średniowieczu w zakresie IT. Mówię tu głównie o zabezpieczeniach i procedurach, które są przysłowiowe "sto lat za murzynami". Pewnie częściowo jest to związane z tym, że sektor finansów jest dość mocno obwarowany regulacjami i przepisami, a jak wiadomo wszędzie gdzie jest silna kontrola urzędowa tam wszystko idzie po prostu wolniej i wprowadzenie świeżości jest naprawdę niekiedy karkołomne. Weźmy taki _Santander Consumer Bank_, w którego [polityce dotyczącej haseł](https://www.blog.santanderconsumer.pl/bank-mozliwosci/silne-haslo-to-podstawa,1,13.html) możemy wyczytać:

> Pamiętajmy, hasło do Bankowości Internetowej Santander Consumer Banku:
> 
> \- Składa się z minimalnie 10 i **maksymalnie 20 znaków**;

Że co proszę? Maksymalny limit 20 znaków? Wszystkie moje hasła mają aktualnie powyżej 30. Dlaczego?

1. Bo znacznie utrudnia to ich złamanie poprzez wykładnicze zwiększenie z każdym kolejnym znakiem liczby możliwych kombinacji, a co za tym idzie wydłużenie czasu potrzebnego do „zgadnięcia” hasła,

3. Bo używam menedżera haseł i ich długość nie jest dla mnie żadnym ograniczeniem, tj. mogą mieć nawet 256 znaków i nie będzie to dla mnie stanowiło żadnego utrudnienia,

5. Bo po prostu mogę (no nie w przypadku _Santander'a_…).

Pomijam już fakt, że logowanie do _Santander'a_ to istna katorga dla korzystających z menedżera haseł, a to za sprawą tego, że bank przy logowaniu nie wymaga zwykłego podania loginu i hasła, a jedynie np. 3, 7, 11, 12, 13 i 19 znaku hasła, czego nie rozumie chyba żaden menedżer i trzeba to robić ręcznie. Ktoś kto to wymyślił powinien zostać srogo ukarany za najgłupszy pomysł na "zabezpieczenie" procesu logowania.

Cóż, jak to pisze _Santander_ „silne hasło to podstawa”, ale na pewno nie jest to wystarczające rozwiązanie, które uchroni nas przed każdym rodzajem ataku. Takim rozwiązaniem może być w wielu przypadkach silne hasło i właśnie klucz _U2F_, czyli _Universal 2nd Factor_ (z ang. uniwersalny drugi składnik). Taki klucz _U2F_ to oprócz loginu i hasła kolejna bariera do pokonania przez oszustów, która (przynajmniej póki co) jest niemożliwa lub bardzo trudna do pokonania. Toteż dodanie takiego sposobu uwierzytelnienia przez _PKO BP_ jako pierwszy polski bank może nieść pewnego rodzaju pocieszenie i nadzieję na to, że już niedługo we wszystkich bankach zacznie się nieco bardziej dbać o cyberbezpieczeństwo na poziomie użytkownika.

Brzmi pięknie i wiele portali informacyjnych wpadło w natychmiastowy zachwyt. Problem w tym, że redaktorzy, w nich pracujący, przeczytali jedynie notatkę prasową i nie zgłębili tematu. Okazuje się, że _PKO_ na ten moment pozwala na skonfigurowanie tylko jednego klucza bezpieczeństwa... Każdy kto ma choć zgrubne pojęcie jak to działa wie, że pierwszą zasadą używania kluczy _U2F_ jest posiadanie dwóch sztuk. Robi się tak ze względu na to, że jeden nosimy cały czas przy sobie, a drugi trzymamy w bezpiecznym miejscu. Ten drugi to zabezpieczenie na wypadek np. zgubienia klucza głównego. Bez takiego podejścia gubiąc klucz utracilibyśmy całkowicie dostęp do tego co zabezpiecza, bo przecież ta metoda ma sens tylko wtedy, gdy bez klucza nie jesteśmy w stanie uzyskać dostępu do zabezpieczonego zasobu. Taka para kluczy bliźniaczych jest właśnie rozwiązaniem tego problemu. Oczywiście jeżeli ktoś ma paranoję to może mieć ich więcej. Wszystko aby tylko nie jeden!

No, ale dobra fakty są takie, że _PKO_ pozwala na jeden klucz. Zapytasz zatem co w przypadku, gdy zgubimy taki klucz? Otóż jak czytamy w [materiale prasowym](https://media.pkobp.pl/355099-klucze-bezpieczenstwa-nowa-metoda-logowania-do-serwisu-ipko-pomoze-w-walce-z-cyberprzestepcami), _PKO_ ma na to takie rozwiązanie:

> W przypadku utraty klucza bezpieczeństwa np. jego zgubienia czy kradzieży, klient powinien zadzwonić na infolinię banku, aby zmienić narzędzia do potwierdzenia logowania do serwisu iPKO i usunąć klucz bezpieczeństwa.

No przyznam, że śmiech na sali. Zrozumiałbym jeszcze jakby konieczne było stawienie się do placówki banku okazanie dokumentu potwierdzającego tożsamość i poddanie się prześwietleniu do 5 pokoleń wstecz. Zamiast tego bank wymaga kontaktu telefonicznego, co jest jawnym zaproszeniem do próby socjotechniki. Dla mnie taka forma zabezpieczenia nie zabezpiecza niczego, więc póki nic się z tym tematem nie zmieni nie ma co bić brawa _PKO BP_ za wprowadzenie kluczy (nie)bezpieczeństwa. Brawa należą się na razie tylko za chęci, ale póki co dam 2+ i czekam na poprawę, co nie będzie trudne, bo wystarczy tylko zmienić kilka małych rzeczy w polityce banku.

Skwituję to wszystko cytatem z [piosenki _Fix You_ zespołu _Coldplay_](https://www.youtube.com/watch?v=k4V3Mo61fJM):

> When you try your best, but you don't succeed...

_Aktualizacja 07-10-2024:_  
Muszę nieco sprostować mój wpis, gdyż [Szymon Zielonka](https://mas.to/@szymonzielonka) trafnie wskazał mi w komentarzu na _Mastodon'ie_, że _PKO BP_ nie jest pierwszym bankiem, który zaimplementował klucze _U2F_. [Był nim bank _ING_](https://www.ing.pl/indywidualni/bankowosc-internetowa/bezpieczenstwo/klucze-zabezpieczen-u2f)! I z tego co widzę implementacja tej funkcji przez _ING_ została przeprowadzona lepiej, gdyż można dodać więcej niż tylko jeden klucz.
