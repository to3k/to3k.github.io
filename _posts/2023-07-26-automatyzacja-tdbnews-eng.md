---
title: "Simple automation of TDBNews [ENG 🇬🇧]"
date: 2023-07-26
categories: 
  - "projects"
  - "tutorials"
tags: 
  - "automation"
  - "cron"
  - "mastodon"
  - "php"
  - "reddit"
  - "rss"
  - "xml"
image: "/images/automatyzacja_tdbnews.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/automatyzacja-tdbnews/)

Table of contents:
* TOC
{:toc}


For several weeks now, I have been publishing a series of Sunday posts called _#TDBNews_, in which I share interesting things I came across during the week. Manually collecting these, in my opinion, interesting articles would be a very tedious and highly inefficient task that I would have to repeat weekly, dedicating part of my Sunday time to it, which I could spend on other activities. That's why I decided to automate it in a very simple way. The operating principle is trivial, and for clarity, I will present it in bullet points.

1. Every day, I browse through my _RSS_ sources (using the _[Reeder](https://reederapp.com/)_ application), my timeline on _Mastodon_, and _Reddit_, which are my three main windows to the world of information.

3. When I come across an article that seems interesting, I save it to the _Read Later_ list, which I usually revisit in the evening.

5. Then, I share these truly interesting things on [my _Mastodon_ profile](https://mastodon.tomaszdunia.pl/@to3k) with a special hashtag _#TDBNews_.

7. A _PHP_ script monitoring the _RSS_ feed of my _Mastodon_ profile picks up these toots and saves them to a text file.

9. At the end of the week (on Sunday), I run a second script that creates a ready-to-use post code from the collected toots, following the notation used by _Wordpress_. In practice, it consists of a static introduction and conclusion, which are the same in every _TDBNews_ post, and a variable part in the middle where I embed the collected toots as _iframe_ frames.

11. All that's left is to give the post a title, which simply involves providing the current date, and publish it.

Examples of such posts can be seen by going [here](https://blog.tomaszdunia.pl/category/tdbnews/). And in this post, I'll show you behind the scenes how these scripts, which I use to implement this simple automation, look like.

## Script collecting my toots tagged with #TDBNews

As usual, I'll explain its operation through comments placed inside the code. Here, familiarity with the content of the post in which I showed [how I made a bot for publishing news from popular portals on _Mastodon_](https://blog.tomaszdunia.pl/mews/) may also come in handy.

```php
<?php
    header('Content-Type: text/html; charset=utf-8');

    // URL TO MY MASTODON PROFILE
    $url = "https://mastodon.tomaszdunia.pl/@to3k.rss";

    // FILE WITH ALREADY FOUND TOOTS
    $file_all = file_get_contents("tdbnews_all.txt");

    // LOAD A XML FILE (RSS FEED)
    $feeds = simplexml_load_file($url);

    // SETTING TIME ZONE
    date_default_timezone_set("Europe/Warsaw");

    // DATE OF MONDAY THIS WEEK TO FILTER EVERYTHING BEFORE THAT DATE
    $monday = strtotime("Monday this week");
    $monday = date("Y-m-d", $monday);
    
    // IF FEED IS NOT EMPTY
    if(!empty($feeds))
    {
        // SPLIT FEED INTO SEPARATE ITEMS (TOOTS)
        foreach ($feeds->channel->item as $item)
        {
            // CONVERT LINK TO A STRING VARIABLE (WITHOUT THAT STR_CONTAINS GIVES ERROR)
            $link = strval($item->link);

            // GET PUBLISHING DATE AND CHANGE IT'S FORMAT TO YYYY-MM-DD
            $pubDate = $item->pubDate;
            $pubDate = strtotime($pubDate);
            $pubDate = date("Y-m-d", $pubDate);

            // GET DESCRIPTION
            $description = strval($item->description);

            if(str_contains($file_all, $link) OR $pubDate < $monday OR !str_contains($description, "https://mastodon.tomaszdunia.pl/tags/TDBNews"))
            {
                // IF LINK IS IN A FILE (IS ALREADY PROCESSED)
                // OR IF PUBLICATION DATE IS BEFORE MONDAY THIS WEEK (IS TOO OLD)
                // OR IF TOOT DOES NOT CONTAIN HASHTAG TDBNEWS (IS ABOUT SOMETHING ELSE)
                // THEN SKIP IT AND GO TO NEXT ONE
                continue;
            }
            else
            {
                // IF ALL CONDITIONS MET
                // PUSH LINK INTO A VARIABLE WITH QUALIFYING TOOTS
                $file_all .= $pubDate.";".$link."\n";
            }
        }
    }

    // UPDATE THE FILE WITH LIST OF QUALIFYING TOOTS
    file_put_contents("tdbnews_all.txt", $file_all);
?>
```

## Script generating a ready-made WordPress post

Just like in the previous code, everything is explained in the comments here as well.

```php
<?php
    // LOAD FILE WITH ALL TDBNEWS TOOTS
    $file_all = file_get_contents("tdbnews_all.txt");

    // DIVIDE FILE CONTENT INTO SEPARATE LINES
    $explode_file = explode("\n", $file_all);

    // SET TIME ZONE
    date_default_timezone_set("Europe/Warsaw");

    // DATE OF MONDAY THIS WEEK TO FILTER EVERYTHING BEFORE THAT DATE
    $monday = strtotime("Monday this week");
    $monday = date("Y-m-d", $monday);

    // DECLARATION OF AN ARRAY WITH THIS WEEK'S NEWS
    $news_array = array();
    
    // GO THROUGH ALL LINES OF FILE ONE BY ONE
    foreach($explode_file as $line)
    {
        // IF LINE IS NOT EMPTY
        if(!empty($line))
        {
            // SEPARATE PUBLISHING DATE AND LINK
            $explode_line = explode(";", $line);
            // IF PUBLISHING DATE IF NOT BEFORE MONDAT THIS WEEK
            if($explode_line[0] >= $monday)
            {
                // PUSH THIS TOOT INTO ARRAY WITH NEWS FOR THIS WEEK
                array_push($news_array, ['pubDate' => $explode_line[0], 'link' => $explode_line[1]]);
            }
        }
    }
    
    // REVERSE TABLE (SORT TOOTS FROM OLDER TO NEWER)
    $news_array = array_reverse($news_array);
?>

<!-- SECTION WITH RESULT, STATIC INTRODUCTION, PHP CODE WITH FOREACH FUNCTION WHICH RESULT IS PRINT ALL TOOTS EMBEDED WITH IFRAME, STATIC ENDING -->
<!-- PLAINTEXT ELEMENT IS USED TO PRINT HTML CODE IN RAW FORM -->
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

## Summary

Wasn't it easy? In my opinion, it was not only simple but also worth the effort! How so? I have a principle that any automation of tasks, that are intellectually undemanding yet repetitive, makes sense and ultimately saves a lot of time. Let's take the example of _TDBNews_. Creating such a summary manually would take me at least 20 minutes every week, but with the automation described above, it takes me no more than 3 minutes. Let's consider those 15 minutes per week. In a year, we have 52 weeks, so I gain 780 minutes, which is 13 hours! That's over half a day that I can spend with my family or even use to create another post for this blog.
