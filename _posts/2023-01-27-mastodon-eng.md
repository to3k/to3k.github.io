---
title: "Mastodon - Twitter v2.0? [ENG 🇬🇧]"
date: 2023-01-27
categories: 
  - "thoughts"
  - "tutorials"
tags: 
  - "activitypub"
  - "facebook"
  - "fediverse"
  - "friendica"
  - "instagram"
  - "instance"
  - "lemmy"
  - "mastodon"
  - "peertube"
  - "pixelfed"
  - "reddit"
  - "twitter"
  - "youtube"
coverImage: "/images/mastodonfediverseactivitypub_eng.png"
---

If you are reading this, you will probably notice in a moment that this entry is in English, but the rest of the blog is written in Polish. This is due to the fact that I am Pole and I write my blog in my native language, but today I decided that I will translate some of my posts into English so that I can present them to a wider audience. I would also like to apologize for my not so perfect English, but I hope it will be understandable enough 😉 🇵🇱 The Polish and original version of this post can be found [in this link](https://blog.tomaszdunia.pl/mastodon/). Let's move on to the main part of the story!

* * *

To write about Mastodon that it is Twitter v2.0 is like writing nothing. A statement of this type may be acceptable when we want to quickly explain to a not very oriented person what Mastodon is. For me, Mastodon is the discover of (the end of) 2022! To say more, at the beginning of 2023 it became **my main social media**. It took over this name after Twitter on which I'm (or rather I've been?) present since December 2011, which is **over 11 years**! The frenzy of bitterness was ultimately outweighed by blocking the API for third-party applications, specifically the Tweetbot, without which it became impossible for me to use Twitter.

## Practice first then theory

You don't need to know what Mastodon is to start using it! You can always just create an account and see for yourself. The only thing you have to do to start with is to choose an instance (I will tell you about what it is later in the post) and register on it. If you are reading this, I assume that you are not a Pole, so you have a very big choice. However, I know very well that sometimes a big choice is a problem, not an advantage, so I will recommend you the one I am on myself - [mstdn.social](https://mstdn.social).

## What is Mastodon?

For all curious, I recommend reading a rather extensive, but well-written guide that describes practically all aspects related to this topic in a not very complicated way:  
[https://github.com/joyeusenoelle/GuideToMastodon/](https://github.com/joyeusenoelle/GuideToMastodon/)

I wouldn't want to take the easy way out either, so I'll try to describe here in my words how I see it. It seems to me that no one has described Mastodon's (or rather the Fediverse) topics in this way yet, so take your coffee and hold on tight, because space journey begins!

## Fediverse = universe

I am writing this "subsection" for the second time, because when I read what I wrote the first time, I decided that if someone had given me such an explanation, I would not understand it myself… The second approach, simplified to a minimum, start over!

Well, Mastodon is really only part of a larger world called the Fediverse, which in my opinion is a conglomeration of the words Federated Universe (a universe of interconnected galaxies).

## Services/platforms = galaxies

This universe is divided into galaxies, which are specific services/platforms, from which I have selected several, and for ease I will indicate their equivalents, known to us so far:

- Mastodon - Twitter

- PeerTube - YouTube

- Pixelfed - Instagram

- Friendica - Facebook

- Lemmy - Reddit

Of course, there is much, much more of it, but that's enough for the purpose of this post.

## Instances = planets (decentralization)

At this point, the important keyword enters - **decentralization**. All listed services/platforms (TT, YT, Insta, FB or Reddit) are run in a centralized manner. This means that, maybe they don't work on one server, but each of them has one entity as the owner. This is problematic, because in such a situation it is not possible for us to control our data in any way. To say more, we can't even be sure that the service, we use today, will work tomorrow. See what is currently happening to Twitter after it was taken over by Elon Musk. Such a central authority can do practically anything with a given service, whenever it wants. The solution to this is decentralization, i.e. breaking it down into smaller planets - instances, smaller servers, each with its own administrator and manager. Their number is arbitrary and they can be created by ordinary people. **Even you can create one!** In addition, it is relatively easy to jump between them, so you can start with one at first, and when it stops to suit you, jump to another or become completely independent and, as I said earlier, create your instance.

## ActivityPub = interplanetary communication

Instances can communicate and exchange data with each other, thanks to a common communication protocol called ActivityPub. It is also important that not only two instances of Mastodon can "talk" to each other. ActivityPub works globally within the Fediverse, so the Mastodon instance can effectively exchange data with the Pixelfed instance, so we are talking here not only about interplanetary, but also **intergalactic communication**! In practice, this is that a Mastodon user can access the profile of a photographer posting on Pixelfed, start following him (to see his future publications on his timeline on Mastodon), share and/or like his photos, and write a comment.

## Handle = address of our house

In principle, it remains to explain where such and not other profile addresses come from. From what I know it's called "handle". For my main account on Mastodon, it is [**@to3k@mstdn.social**](https://mstdn.social/@to3k). The syntax is as follows:

- @ sign which is the beginning of a handle,

- username,

- @ sign which is a separator,

- instance url.

This format is necessary, because it is not enough to indicate your username, which can be vividly compared to the address of your house, but it is also necessary to indicate on which planet you are stationed. The handle built in this way can be entered in the search engine of your instance to go to the profile of a specific user. However, in order to send someone a direct link to your profile, you need to slightly reformat the link to - [https://mstdn.social/@to3k](https://mstdn.social/@to3k), i.e. first the address of the instance and after the slash the @ sign with the username assigned.

## Types of timelines (city, planetary, galactic)

Each Mastodon user can use three types of timelines:

- **Home** - it contains toots (this is the name of posts on Mastodon) of people you follow and the content they forwarded (boosts),

- **Local** - it contains toots and boosts of all people with whom you share one instance,

- **Global / Federated** - it contains content from all instances with which your instance federates, i.e. exchanges data (is connected in any sort).

In this post I try to present everything very vividly through allegories, so this time I will take up the glove too. The home timeline is the equivalent of the city, the local is the planet (in the nomenclature of this entry - instance), and the global is the galaxy (the whole Mastodon, and maybe even the Fediverse).

Mastodon also supports **lists**, just like Twitter, so this feature should be familiar to you. It is a very pleasant way to group the people you observe, e.g. thematically.

## Concluding...

It seems to me that this post came out quite concise, and the substantive effect, I wanted to get here, satisfies me. Fediverse topic is very extensive and it is certainly a new teaser for me, right after the open-source and self-hosting, to which it fits perfectly, so it will probably come back here again. See you in Fedi! You know where to find me.
