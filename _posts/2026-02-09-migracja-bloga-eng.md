---
layout: post
title: "Goodbye Wordpress, hello Jekyll [ENG 🇬🇧]"
date: 2026-02-09
published: true
categories: 
  - "projects"
  - "self-hosting-eng"
  - "thoughts"
tags: 
  - "jekyll"
  - "wordpress"
  - "blog"
  - "github"
  - "migration"
  - "self-hosting"
  - "open-source"
image: "/images/wptojekyll.png"
---

[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/migracja-bloga/)

Table of contents:
* TOC
{:toc}

Finally... Finally, I found the time, gathered a bit of will, and overcame the fear of breaking something. A bulldozer drove onto this blog, razed it, and then a renovation crew moved in and rebuilt it.
For posterity, I’ll leave a [link to a screenshot](https://web.archive.org/web/20260208181656/http://web.archive.org/screenshot/https://blog.tomaszdunia.pl/) here, showing how the blog used to look, made using the Internet Archive.

## Why such a change?
For a long time, the fact that this site's performance was tragic had been bothering me. At first, I hoped to find the cause, but over time I realized that WordPress is a swamp—the more you wade in, the deeper you sink. WP seems like a super friendly solution at first, even for less advanced users. Ready-made themes installed with one click. Plugins for practically everything, also available at your fingertips. Maybe so, but the further into the forest, the more trees you find, and all that shiny junk clogs up the site more and more. I’m not saying WordPress is total garbage, because I know there are people who know it inside out and are able to do absolutely anything in that environment. However, I never had the patience to plow through documentation as extensive as that provided by the WP creators.

## Why Jekyll?
I stumbled upon [this software](https://jekyllrb.com/) pretty much by accident. I learned about it from the [Nadgryzieni](https://www.youtube.com/playlist?list=PLJaCoP2ajoU_5k2VG430hU1_-MaQrEMK-) podcast (by iMagazine), in which Michał Śliwiński, the creator of [Nozbe](https://nozbe.com/pl), presented it as the engine for his private website. I visited [the address he provided, michael.team](https://michael.team), and saw one of the most hideous websites I’ve seen lately. It was simply **STUNNING**. I fell in love immediately and started digging online to "get a PhD" in how to get such a monstrosity for myself. It turned out to be incredibly simple, and the easiest path is using **GitHub Pages**. Yes, I know... GitHub is Microsoft, and Microsoft is evil. Before half of Mastodon crucifies me, I’d like to say something in my defense. Launching a Jekyll-based blog on GitHub infrastructure doesn't mean it’s a permanent solution. One of Jekyll's many advantages is that migrating it to almost any environment/hardware is very simple. Ultimately, I’m thinking of full self-hosting, and that’s likely how it will end, as quite a lot has changed in my life since my last post. House construction is finished, I’ve handled the interior, I have fiber optics, and I’ve sorted out home servers, so I have the infrastructure to play with.

## And why not WriteFreely, huh?
It’s actually a good question, especially since I’m the person behind the official Polish instance [WriteFreely.PL](https://writefreely.pl)... Despite appearances, Jekyll seems like a simpler and less complex tool than WriteFreely. It might be about the whole Fediverse federation thing, which is still a bit of an unsolved mystery to me. Also, the fact that with WF I’d have to manage an external database for images myself definitely cooled my enthusiasm.

## Will there be a tutorial?
That’s like asking if a bear shits in the woods. I think those who know me or have read at least a few posts on this blog would never ask such a question, as it’s obvious I’ll produce a substantial guide from this whole migration process. I’ll describe step-by-step how to launch your blog on GitHub Pages using Jekyll as the engine, and later (possibly in a separate post), I’ll go through the process of migrating from WordPress.

## What do you think?
Dear Reader, do you think the change I made is a positive one? Please rate it! Also, let me know if a tutorial on Jekyll is an interesting topic worth covering on this blog. It was great to write something again, so I think even the harshest hate wouldn't stop me, but I’m still curious about your opinion. I feel a massive surge of motivation to hit the keys, so for a while, I might be slightly annoying regarding the volume of texts published on this site.

## Is everything working?
I did the migration a bit on the fly, so I’m not entirely sure if everything is working exactly as it should. I’m counting on your feedback if you notice anything’s off. What I regret most is that I didn't manage to migrate all the comments from the posts. On the new blog, I’m using [Giscus](https://giscus.app/pl) as the comment system, which requires a GitHub account to post. It’s not an ideal solution, but it was certainly the easiest for me to implement at the start. As for the old blog posts—unfortunately, they have faded into oblivion. I tried migrating them and even managed to bulk-transfer a few, but it turned into a total mess, so I scrapped the idea. I decided to simply start from scratch.

PS: I almost forgot to add that from now on the source code of this blog is open and available in [public repository on Github](https://github.com/to3k/to3k.github.io).