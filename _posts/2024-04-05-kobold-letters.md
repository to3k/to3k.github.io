---
title: "Kobold Letters - ciekawy sposób ataku przez e-mail"
date: 2024-04-05
categories: 
  - "shorts"
  - "szorty"
tags: 
  - "css"
  - "cyberbezpieczenstwo"
  - "cybersecurity"
  - "email"
  - "gmail"
  - "html"
  - "koboldletters"
  - "outlook"
  - "scam"
  - "thunderbird"
coverImage: "szorty.png"
---

Lubię sobie czasem wejść na [_Hacker News_](https://news.ycombinator.com/news) i zobaczyć, gdzie mnie poniesie. Nie wchodzę tam często, a i nigdy z jakimś obranym wcześniej celem. Raczej błądzę w poszukiwaniu ciekawostek. Tym razem trafiłem na coś, co zainteresowało mnie na tyle, że uznałem, iż potrzebuję się tym tutaj podzielić.

Chodzi o ciekawą koncepcję ataku przez skrzynkę pocztową e-mail nazwaną **_Kobold Letters_**. W telegraficznym skrócie chodzi o to, że od kogoś spoza Twojej organizacji dostajesz maila o zupełnie niewinnej treści A, która nakłania Cię do przekazania dalej (czy jak to mówią korposzczury - przeforwardowania) tego maila do kogoś innego z Twojej organizacji. Do tego wszystko wydaje się zupełnie OK. Jednakże otrzymany przez Ciebie mail jest w _HTML_, który dodatkowo wykorzystuje formatowanie _CSS_, a jego kod jest napisany tak, że gdy zostanie przekazany to jego treść, która wcześniej brzmiała A teraz brzmi B i jest już stuprocentowym mailem phishingowym. Niby phishing to phishing i bez względu na formę powinien być możliwy do wykrycia przez kumatego pracownika, jednakże w tym przypadku dodatkowym czynnikiem jest to, że osoba atakowana jest tak jakby dopiero w drugiej linii, a otrzymuje ona złośliwego maila od kogoś kogo zna, ba!, jeżeli pracują w tym samym budynku to może nawet pójść do tej osoby, zapytać się czy to ona wysłała tego maila i co więcej otrzymać odpowiedź pozytywną, bo to prawda, gdyż ta osoba faktycznie przekazała tego maila tylko po prostu nie wie, że po przekazaniu zmienił on całkowicie swoją treść.

Jestem w stanie wyobrazić sobie taką sytuację, w której oszust podszywa się pod jednego z kooperantów i wysyła pozornie zwykłego maila z krótkim zapytaniem czy pracownik X może sprawdzić ze swoim działem finansów czy faktura została opłacona na właściwy numer rachunku, bo termin upłynął, a on pieniędzy nie dostał. W mailu do pracownika X nie ma żadnych poszlak wskazujących na to, że jest to phishing, bo nie ma załączników, ani podejrzanych linków. Pracownik X traktuje to jako rutynową sytuację i przekazuje tego e-maila do działu finansów. W tym momencie zmienia się treść e-maila i pracownik Y z działu finansów widzi już treść ze złośliwym linkiem. Jednakże dostał go od swojego dobrego kolegi z pracy, potwierdza z nim telefonicznie, że to on przekazał tego e-maila i nikt się pod niego nie podszył, więc nie ma zupełnie żadnych podejrzeń. Klika w link i cyk, dalej dzieją się scenariusze dobrze znane pentesterom.

Problem został odkryty (a przynajmniej tak mi się wydaje) i szczegółowo opisany przez _[Lutra Security](https://lutrasecurity.com/en/articles/kobold-letters/)_.

Co ciekawe jego „załatanie” w teorii jest trywialne, bo wystarczy zrezygnować z wykorzystywania HTML i CSS w e-mailach… Można to zrobić po stronie użytkownika, ale popatrzmy na sprawę realnie, nie ma szans, żeby ludzie zrezygnowali z korzystania z _HTML_. Jakie jest inne wyjście? Zablokować tag _CSS_ _<style>_ z poziomu klienta pocztowego? To w zasadzie oznaczałoby zaoranie możliwości tworzenia wymyślnie sformatowanych e-maili. Odpada. To może zrobić to tak jak zrobił to _Gmail_, czyli po prostu przekazywać e-maile jako plaintext (przekonwertowane z formatu _HTML_ na zwykłą formę tekstową)? Jest to pewien kompromis, ale czy akceptowalny dla większości?

Przykładowy _proof of concept_ dla _Outlooka_:

```
<!DOCTYPE html><html><head>    <style>        .kobold-letter {            display: none;        }        body>div>.kobold-letter {            display: block !important;        }    </style></head><body>    <p>This text is always visible.</p>    <p class="kobold-letter">This text will only appear after forwarding.</p></body></html>
```

* * *

## Kobold Letters - an interesting way to attack through email

I like to sometimes visit [_Hacker News_](https://news.ycombinator.com/news) and see where it takes me. I don't go there often, and never with a predefined goal. I tend to wander in search of curiosities. This time I stumbled upon something that interested me enough to feel the need to share it here.

It's about an interesting email mailbox attack concept called **_Kobold Letters_**. In brief, it involves receiving an email from someone outside your organization with completely innocent content A, encouraging you to forward this email to someone else within your organization. Everything seems perfectly fine. However, the email you receive is in _HTML_, utilizing _CSS_ formatting, and its code is written so that when forwarded, its content, which previously sounded like A, now sounds like B and is a one hundred percent phishing email. Phishing is phishing, and regardless of the form, it should be detectable by a savvy employee. However, in this case, the additional factor is that the targeted person is, in a way, in the second line, and they receive a malicious email from someone they know. Moreover, if they work in the same building, they might even go to that person, ask if they sent the email, and receive a positive response because it's true – that person did indeed forward the email, they just don't know that after forwarding, it completely changed its content.

I can imagine a situation where a scammer impersonates one of the cooperants and sends what seems like a regular email with a short inquiry to employee X asking if they can check with their finance department whether an invoice has been paid to the correct account number because the deadline has passed, and they haven't received the money. There are no clues in the email to employee X indicating that it's phishing because there are no attachments or suspicious links. Employee X treats it as a routine situation and forwards the email to the finance department. At this point, the email's content changes, and employee Y from the finance department now sees the content with a malicious link. However, they received it from their good colleague at work, confirm with them over the phone that they forwarded the email, and no one impersonated them, so there are no suspicions at all. They click the link, and there you go, scenarios well known to pentesters unfold.

The problem has been discovered (or at least that's how it seems to me) and described in detail by _[Lutra Security](https://lutrasecurity.com/en/articles/kobold-letters/)_.

Interestingly, its "fix" in theory is trivial because all it takes is to stop using HTML and CSS in emails... This can be done on the user's side, but let's look at it realistically – there's no chance people will stop using _HTML_. What's the alternative? Block the _CSS_ tag _<style>_ from the email client? That would essentially mean ditching the ability to create elaborately formatted emails. Not feasible. So, could it be done like how _Gmail_ did it, simply passing emails as plaintext (converted from _HTML_ format to plain text while forwarded)? It's a compromise, but is it acceptable to the majority?

Example _proof of concept_ for _Outlook_:

```
<!DOCTYPE html><html><head>    <style>        .kobold-letter {            display: none;        }        body>div>.kobold-letter {            display: block !important;        }    </style></head><body>    <p>This text is always visible.</p>    <p class="kobold-letter">This text will only appear after forwarding.</p></body></html>
```
