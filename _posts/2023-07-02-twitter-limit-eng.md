---
title: "Another step to Twitter's downfall [ENG 🇬🇧]"
date: 2023-07-02
categories: 
  - "shorts"
tags: 
  - "api"
  - "elonmusk"
  - "fediverse"
  - "mastodon"
  - "nitter"
  - "twitter"
  - "twittodon"
image: "/images/szorty.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/twitter-limit/)

Table of contents:
* TOC
{:toc}

Do you remember my tool called [_Twittodon_](https://twittodon.com)? I wrote about it [here](https://blog.tomaszdunia.pl/twittodon-eng/). It was a tool for verifying the connection between _Mastodon_ and _Twitter_ accounts. I used the past tense because unfortunately, since yesterday, it's not working correctly and there's a good chance it never will again. All of this is due to the latest significant steps taken by _Twitter_.

It all started just over half a year ago when shortly after _Elon Musk_ bought it, access to the _Twitter API_ started to be restricted. Many unofficial clients ceased to exist at that time. A really big migration of people to _Mastodon_, and to the _Fediverse_ in general, began. _Twittodon_ gained immense popularity then, and the lack of access to the _API_ was not an obstacle because the operating principle relied on the use of the [_Nitter_](https://github.com/zedeus/nitter) tool, which allowed access to Twitter content by scraping it without utilizing the _API_.

However, yesterday a new _Twitter_ policy was implemented, which introduced the requirement of having an account to access tweets and profiles. This rendered _Nitter_ useless, along with many other developer solutions that were still functional despite the lack of access to the _API_. Unfortunately, _Twittodon_ is one of those solutions.

And that's not all, as the next step planned by _Elon_ is the introduction of additional limits that will define how many tweets one can read per day.

![](/images/IMG_0107.jpeg)

According to Elon's tweet, there will be 6000 tweets per day for verified accounts, which are the ones paying for the _Twitter Blue_ subscription, 600 tweets for unverified accounts, and 300 tweets for new accounts. No respectable developer will pay $8 per month for access to this ridiculously small limit of 6000 tweets. However, a limit of 600 is too small even for an average user.

We'll see how everything develops, but I don't expect any changes for the better. At the moment, _Twittodon_ doesn't work for adding new connections, but the existing database is still accessible and will remain so, at least for now.

_UPDATE 12.06.2023_: [_Nitter_ is back alive](https://github.com/zedeus/nitter/pull/927) and with it also [_Twittodon_](https://twittodon.com), so I invite you to create a verified connection of your _Twitter_ and _Mastodon_ accounts while you can!
