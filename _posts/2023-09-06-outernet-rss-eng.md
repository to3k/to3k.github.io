---
title: "#Outernet - RSS [ENG 🇬🇧]"
date: 2023-09-06
categories: 
  - "outernet-eng"
tags: 
  - "android"
  - "docker"
  - "fdroid"
  - "feed"
  - "feedly"
  - "freshrss"
  - "googleplay"
  - "hashtag"
  - "ios"
  - "netnewswire"
  - "outernet"
  - "reader"
  - "reeder"
  - "rss"
  - "selfhosted"
  - "tag"
  - "wordpress"
  - "xml"
  - "yunohost"
image: "/images/outernet_rss.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/outernet-rss/)

Table of contents:
* TOC
{:toc}

[In my previous post](https://blog.tomaszdunia.pl/outernet-social-media-eng/), I presented alternatives to _mainstream social media_ that allow you to break free from the bubble, which can be briefly characterized as addictive, privacy-violating for its users, or inciting unnecessary emotions solely for the enrichment of the companies behind it.

In this post, I decided to address another topic, which is obtaining information from the world. Lately, I've noticed a trend of more and more people disconnecting from reading the news. I can find this approach healthy and understandable. Things currently served to us by mainstream news portals negatively affects us in a similar way to social media. However, I don't resonate with the idea of living under a rock, and I like to know what's happening in the world. I'm not referring to politics here, because that subject affects me like a red flag to a bull and definitely doesn't contribute positively to my well-being. I'm more interested in technological and scientific novelties, updates related to my work (buses, hydrogen, electromobility), or sports news (speedway, F1). Am I able to calmly read about all of this using _Google News_, which serves content according to its algorithm that always "knows better" what I should read and what not? Or should I limit myself just to portals where 90% of the articles are _clickbaits_, with titles written in such a way as to entice the reader to open their content at any cost, while, at the same time, not representing a high level of journalistic quality? To both of these questions, I will answer decisively - NO.

I am a conscious Internet user, and I know that on its fringes lies the _Outernet_, a place where I can decide what interests me and read about it on my own terms. The tools I use for this are channels and an _RSS_ reader.

## What is RSS?

I don't think there's anyone here who has never had contact with _RSS_ and has no idea what it is. Nevertheless, out of a sense of chronicle duty, I feel obliged to briefly mention it.

_RSS_, which stands for _Really Simple Syndication_, is a technology that enables easy and automatic tracking of new content published on selected websites. With _RSS_, users can subscribe to their favorite blogs, news sites, or even podcasts and receive updates without the need to visit each of these sites separately. This not only saves time but also helps maintain order in the sea of information available on the web, mainly reducing exposure to unnecessary stimuli that we are bombarded with when visiting mainstream news portals.

The idea behind _RSS_ is very simple. The source from which we will draw information has an _RSS_ channel (also known as a _feed_), which is actually a kind of text file (usually in _XML_ format) that lists published content in chronological order through a specified syntax. This can be compared to a table of contents that contains basic information about articles (title, link, publication date, author information, summarized content). This file can be found at various addresses, and there is no one correct method. The simplest way to find the _RSS_ channel of a given site is to enter its name in a search engine and add the phrase _RSS_ to the query. Another way is to rely on _RSS_ readers, most of which can find the appropriate channel just by entering the main page address of the source.

For example, the address of the _RSS_ channel of my blog (the one you are currently reading) is:

> https://blog.tomaszdunia.pl/rss

The blog is based on _WordPress_, so instead of _rss_, you can also use the term _feed_ at the end, and the result will be the same.

Furthermore, there is no need to subscribe to my entire blog. You can track only the topics that interest you. This way, you can limit yourself to content written in Polish, using this address [https://blog.tomaszdunia.pl/category/pl/rss](https://blog.tomaszdunia.pl/category/pl/rss), or only to those in English - the analogous link is [https://blog.tomaszdunia.pl/category/eng/rss](https://blog.tomaszdunia.pl/category/eng/rss). Or perhaps you are only interested in posts that I have tagged with a specific tag? Let's take the _selfhosted_ tag as an example. The _RSS_ feed with posts tagged this way can be found at [https://blog.tomaszdunia.pl/tag/selfhosted/rss](https://blog.tomaszdunia.pl/tag/selfhosted/rss).

A good example illustrating the operation of _RSS_ is a post I wrote some time ago, [MEWS Bot = Mastodon nEWS](https://blog.tomaszdunia.pl/mews-eng/), in which I described, in the form of a tutorial, how to create a bot that retrieves information from an _RSS_ feed and publishes it on _Mastodon_. Since we are already on the topic of _Mastodon_, it is worth noting that every user profile or hashtag has its own individual _RSS_ feed, which can be subscribed to via any _RSS_ reader. I use this mechanism, for example, in my tool _[Twittodon](https://blog.tomaszdunia.pl/twittodon-eng/)_ and when creating the weekly news roundup [_TDBNews_](https://blog.tomaszdunia.pl/automatyzacja-tdbnews-eng/).

## RSS Reader

I've mentioned a few times above something I call an _RSS_ reader, so it's about time to point to a solution that I recommend. The choice in this regard is truly vast.

You can take the easy route and simply go to the app store on your smartphone or tablet and download a specific app. For Android, I recommend the _Feeder_ reader, which is available both on [_Google Play_](https://play.google.com/store/apps/details?id=com.nononsenseapps.feeder.play) (👎) and on [_F-Droid_](https://f-droid.org/en/packages/com.nononsenseapps.feeder/) (💪). Why this one when the selection is so extensive? _Feeder_ is free, open-source, frequently updated, does not collect any user information, and works as it should, all while looking decent. Do you need anything more? For _iOS_, I recommend the paid [_Reeder 5_](https://apps.apple.com/pl/app/reeder-5/id1529445840), which is the app I use. Among the free alternatives, [_NetNewsWire_](https://apps.apple.com/us/app/netnewswire-rss-reader/id1480640210) is a recommended choice. For both systems, there's also the [_Feedly_](https://feedly.com) app, which offers paid plans, but its free version is sufficient for basic use. The final choice is up to you.

For more ambitious and self-hosted solutions enthusiasts, there's a cool option in the form of _[FreshRSS](https://freshrss.org/index.html)_. This is software that you can run on your server, for example, through _[Yunohost](https://yunohost.org/en/app_freshrss)_ or _[Docker](https://hub.docker.com/r/freshrss/freshrss)_. I recommend checking out my previous posts where I've provided all the necessary information needed to set up your own instance of _FreshRSS_:

- [what is _Yunohost_ and how to run it on your server](https://blog.tomaszdunia.pl/yunohost-oracle-eng/),

- [what is _Docker_ and what its basic usage looks like](https://blog.tomaszdunia.pl/docker-eng/),

- [how to run _Vaultwarden_ based on _Yunohost_ or _Docker_](https://blog.tomaszdunia.pl/vaultwarden-eng/),

- [how to run _Nextcloud_ based on _Yunohost_ or _Docker_](https://blog.tomaszdunia.pl/nextcloud-eng/).

_FreshRSS_ is not only an _RSS_ reader but also an aggregator that you can use to scan source channels and aggregate the found content, which you can then read on an external reader after connecting it. As I mentioned earlier, it is a solution focused on autonomy and self-sufficiency, making it a perfect fit for the _Outernet_ ideology.

![](/images/freshrss_screenshot.webp)

## My RSS Feeds

I've decided that at the end of this post, I'll share some sources that I consider my window to the world, i.e., those from which I gather information about topics that interest me. Unfortunately, most of them are polish language sources, so for some of you it would probably be useless... Nevertheless, this would give you information how _RSS_ urls can look like. So, I'm opening my reader, and below, I present the _RSS_ channels I've collected.

General cybersecurity topics - I read them as a hobby:

1. [Zaufana Trzecia Strona](https://zaufanatrzeciastrona.pl) - https://zaufanatrzeciastrona.pl/feed

3. [Niebezpiecznik](https://niebezpiecznik.pl) - http://feeds.feedburner.com/niebezpiecznik

5. [Sekurak](https://sekurak.pl) - https://sekurak.pl/feed

7. [Informatyk Zakładowy](https://informatykzakladowy.pl) - https://informatykzakladowy.pl/feed

9. [Kapitan Hack](https://kapitanhack.pl) - https://kapitanhack.pl/feed

11. [PAYLOAD](https://payload.pl/) - https://payload.pl/feed

_Rzeczpospolita_ - the only news portal I read and pay for access behind the paywall, but I only read content from specific categories:

1. [Logistics](https://logistyka.rp.pl/) - https://rp.pl/rss/4741-logistyka

3. [Climate](https://klimat.rp.pl/) - https://rp.pl/rss/5161-klimat

5. [Automotive](https://moto.rp.pl/) - https://rp.pl/rss/2651-motoryzacja

7. [Energy](https://energia.rp.pl/) - https://rp.pl/rss/4351-energetyka

9. [Digital](https://cyfrowa.rp.pl/) - https://rp.pl/rss/2991-cyfrowa

_Reddit_ - each _subreddit_ has its own _RSS_ feed, and using it this way is very convenient because there is no need to visit the ad-filled homepage with low-quality content whose only purpose is to grab your attention. I'm slowly reducing my activity on _Reddit_, so I only have one channel left here, which is hard for me to get rid of because it contains a lot of interesting content:

1. [r/TechNews](https://www.reddit.com/r/technews/) - https://reddit.com/r/technews/new

Sports - I'm interested in motorsports, specifically two - Formula 1 and speedway:

1. [Circus F1](https://www.cyrkf1.pl/) - https://cyrkf1.pl/feed

3. [MotorSport.com Formula 1](https://pl.motorsport.com/f1/) - https://pl.motorsport.com/rss/f1/news

5. [SportoweFakty WP Speedway](https://sportowefakty.wp.pl/zuzel/) - https://sportowefakty.wp.pl/zuzel/rss.xml

7. [speedwaynews.pl](https://speedwaynews.pl) - https://speedwaynews.pl/feed

Electromobility and Renewable Energy - partly as a hobby, partly professionally:

1. [Elektrowóz](https://elektrowoz.pl) - https://elektrowoz.pl/feed

3. [WysokieNapięcie](https://wysokienapiecie.pl) - https://wysokienapiecie.pl/rss

Work-related (related to my work, i.e., buses):

1. [Transinfo (Infobus)](https://transinfo.pl/infobus/) - https://transinfo.pl/infobus/rss

3. [Transport Publiczny](https://www.transport-publiczny.pl/) - https://www.transport-publiczny.pl/rss/rss.xml

5. [Sustainable Bus](https://www.sustainable-bus.com/) - https://www.sustainable-bus.com/feed

I used to have many more English-language sources in the past, but since then, several native portals have emerged that are on par in terms of quality and are worth following.
