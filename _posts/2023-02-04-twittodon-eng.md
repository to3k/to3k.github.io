---
title: "Twittodon.com - lifeboat [ENG 🇬🇧]"
date: 2023-02-04
categories: 
  - "projects"
tags: 
  - "api"
  - "curl"
  - "github"
  - "mastodon"
  - "mysql"
  - "nitter"
  - "opensource"
  - "php"
  - "pregmatch"
  - "regexp"
  - "rss"
  - "twitter"
  - "twittodon"
image: "/images/twittodon.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/twittodon/)

Table of contents:
* TOC
{:toc}


[Twittodon](https://pl.twittodon.com) is my response to the mass migration of people from Twitter, which has been taken over and slowly destroyed by Elon Musk. These people are now fleeing to Mastodon. Twittodon, as a project, has exceeded my expectations, as it is not only quite popular, but has been written about by media such as [Forbes.com](https://www.forbes.com/sites/daveywinder/2022/12/15/how-to-get-twitter-verified-on-mastodon-8-elon-musk-tax-not-required/), [Spider's Web](https://spidersweb.pl/2022/12/twittodon-twiter-mastodon-narzedzie.html), and [iMagazine](https://imagazine.pl/2023/01/13/nadgryzieni-397-nowosci-z-ces-2023-roborock-zapomnial-gdzie-mieszka-i-oreo/).

## What is Twittodon?

It is a tool for verifying connections between accounts on Mastodon and Twitter. The goal is to create a publicly accessible database of such connections in order to facilitate people's migration to the Fediverse (specifically Mastodon) by making it easier for them to recreate their contact networks from Twitter. There are similar tools for this, but mine stands out because it is secure, as it does not require users to provide credentials to third-party applications, and it is available in an open-source model.

## Some statistics

I must admit that the popularity of my tool has surprised me a bit. At the time of writing this post, there are **over 1400 verified connections** in the Twittodon database, and the **average daily pageviews are around 30,000 views**. Of course, there are more and less active days, but the **record is over 84,000 views**. The full statistics mentioned above are available for viewing [in this link](https://twittodon.com/stats.php).

## Advantages

- This is a **completely free** tool and I can promise with a clear conscience that it will remain so forever.

- **Simple to use**. The process of verifying accounts is simplified to a minimum, so in practice it is enough to indicate only two of your accounts, the first on Twitter and the second on Mastodon, publish posts with specific content and start the verification process. Twittodon script will find the published posts and conduct the verification process.

- As I mentioned earlier, it is not required to share any credentials to your accounts, so this is a **solution focused on user safety**. There are many solutions that allow for similar effects, but each of them requires granting access permissions to third-party applications/people. It is certainly convenient, as all you need to do is log in and give permission to access your account, and everything will happen automatically. However, as people who are knowledgeable about internet security, you surely see that something is not right here.

- **Independence from Twitter API**. This aspect is important because, looking at recent events, such as Twitter's blocking of API access for larger unofficial clients, any application based on that API may stop working tomorrow. Twittodon does not use the API because verification is done in a different way, so it will be much harder to cut off access. Since its creation, Twittodon has only been down for a few hours when Elon blocked the ability to publish tweets with links to other social media sites. This happened while I was sleeping, but as soon as I woke up and realized what was happening, I solved the problem in 30 minutes, so Twittodon quickly returned to normal functioning.

- **Transparency**, which is confirmed by the fact that it is an open-source project, and its full code is available on [my GitHub under this link](https://github.com/to3k/twittodon).

- **Full access to the created database for everyone**. The database can be browsed and easily searched from the [Verified List](https://pl.twittodon.com/verified.php) page or downloaded as a .CSV file to your computer with just one button and further processed in any way.

- The Twittodon.com website **does not use cookies**, **does not have any tracking scripts whatsoever**, and as the author, **I do not display any ads on it**, although I have already received such proposals.

- The website is **available in two languages** - Polish and English.

- After a successful verification process, Twittodon generates a special link to a confirmation page, **which, when added to your profile, will be recognized by Mastodon as verified**.

![](/images/D0ACB0F6-2A23-4476-9886-24C2E21C4662-1024x440.png)

## What does it look like from the inside?

Twittodon code is too extensive to go through all its elements and discuss them one by one, so in this post, I will focus only on the two most interesting aspects - **how account verification works on Twitter and Mastodon**.

**Let's start with Twitter**. The process begins with providing username by the user. Then user is asked to publish a tweet with the following content:

> This is my account on Mastodon - \[LINK TO MASTODON\] - verified by @twittodon\_com Twittodon.com

After publishing the tweet, the user presses the _Verify_ button and the main part of the script starts working. The task of this part of code is to gain access to Twitter, read the user's latest tweets and check if there is a tweet containing the content defined above among them.

> https://twitter.com/theto3k  
> https://nitter.net/theto3k

Let's describe how the script works. It will look like this: we will load the user's profile on Nitter, then we will download the page source using _cURL_, search for the appropriate part using a regular expression (I recommend reading about [regexp](https://en.wikipedia.org/wiki/Regular_expression)) using the _preg\_match()_ function, and if we find the appropriate phrase, we will change the record in the database, which will mean that the Twitter account data has been verified.

I have decided that the easiest way for me to discuss the code will be by placing comments in it. In PHP language, comments are placed after _//_ or, if the comment must contain more than one line, it is placed between _/\*_ and _\*/_.

```php
// If the button named "verify_twitter" has been pressed then...
if(isset($_POST['verify_twitter']))
{
    // Creates a link to Nitter (the user's login is stored in the $twitter variable)
    $nitter_link = "https://nitter.net/".$twitter;
    // Initializes a cURL request
    $curl = curl_init($nitter_link);
    // URL to which the request will be directed
    curl_setopt($curl, CURLOPT_URL, $nitter_link);
    // Instructs cURL to return the result of the request
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    // Sets the user agent for the script to appear as a standard browser
    curl_setopt($curl, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36');
    // Request timeout, how long it should wait before giving up
    curl_setopt($curl, CURLOPT_TIMEOUT, 30);
    // No header is set, so the value of header is zero
    curl_setopt($curl, CURLOPT_HEADER, 0);
    // Executes the request
    $site_source_code = curl_exec($curl);
    // Loop set to run 5 times
    for($i = 1; $i <= 5; $i++) 
    {
        // If the source code could not be retrieved...
        if($site_source_code == "") 
        {
            // ...then execute the cURL request again
            $site_source_code = curl_exec($curl);
        }
        // If it was successful...
        else 
        {
            // ...then break out of the loop
            break;
        }
    }
    // The function searches for tweets with a specified regular expression
    preg_match("(<div class=\"tweet-content media-body\" dir=\"auto\">.+?".$mastodon_link.".+?Twittodon.com)is", $site_source_code, $phrase);
    // If the desired phrase is found...
    if(!empty($phrase[0])) 
    {
        // Saves today's date in a variable (needed for the MySQL query)
        $today = date("Y-m-d");
        // MySQL query that will modify the appropriate record in the database
        // In short, it changes the value of twitter_verified to 1 (verified) for a specific Twitter account
        $update = "UPDATE connections SET twitter_verified='1', date='".$today."' WHERE twitter_login='".$twitter."' AND mastodon_login='".$mastodon."'";
        // Executes the above query
        mysqli_query($mysqli, $update);
    }
    // If the desired phrase could not be found...
    else 
    {
        // ...then the verification has failed
        $twitter_verified_error = true;
    }
}
```

I would like to focus on the most interesting part of the above code, which is the line where we used the _preg\_match()_ function. The simplified syntax of this function looks like this:

> preg\_match("(\[REGULAR EXPRESSION\])is", \[SEARCHED TEXT\], \[RESULT\]);

In the regular expression, I used a certain special phrase _.+?_, which means a sequence of any characters of any length. For example, let's write such a regular expression "Ala .+? cat" and this expression will be true for both the sentence "Ala has a cat" and for "Ala doesn't have a dog but has a cat". It's like an ultra-fast regexp course 😁 However, once again, I recommend reading about this topic because **regexp is a really powerful tool**.

It's time to review analogous code, but **used for verifying an account on Mastodon**. The operating principle is roughly the same, except that the user publishes a toot on Mastodon with slightly different content:

> This is my account on Twitter - \[LINK TO TWITTER\] - verified by @twittodon@fosstodon.org https://Twittodon.com

After a successful publication and clicking the _Verify_ button, a script for verifying the Mastodon account is launched. In this case, it's easier than with Twitter because instead of using something like Nitter, it's enough to load **RSS feed of a given user's profile**. Yes, every Mastodon profile has its own RSS channel with straight-listed toots! The URL address for this feed can be obtained by adding _.rss_ at the end of the profile link.

```php
// If the "verify_mastodon" button has been pressed...
if(isset($_POST['verify_mastodon'])) 
{
    // Creates a link to the RSS feed (the complete link to the profile is stored in the $mastodon_link variable)
    $mastodon_rss = $mastodon_link.".rss";
    // Initializes the cURL request
    $curl = curl_init($mastodon_rss);
    // URL to which the request should be directed
    curl_setopt($curl, CURLOPT_URL, $mastodon_rss);
    // Instructs cURL to return the result of the request
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    // Sets the user agent for the script (standard browser user agent)
    curl_setopt($curl, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36');
    // Request timeout, how long it should wait before giving up
    curl_setopt($curl, CURLOPT_TIMEOUT, 30);
    // We don't set the header, so the header value is zero
    curl_setopt($curl, CURLOPT_HEADER, 0);
    // Executes the request
    $site_source_code = curl_exec($curl);
    // Loop set to 5 runs
    for($i = 1; $i <= 5; $i++) 
    {
        // If the source code could not be retrieved...
        if($site_source_code == "") 
        {
            // ...then execute the cURL request again
            $site_source_code = curl_exec($curl);
        }
        // If it was successful...
        else 
        {
            // ...then break out of the loop
            break;
        }
    }
    // The function searches for toots with a specified regular expression
    preg_match("(<description>.+?twitter.com/" . $twitter . ".+?Twittodon.com)is", $site_source_code, $phrase);
    // If the desired phrase was found...
    if(!empty($phrase[0])) 
    {
        // Saves today's date in a variable (needed for the MySQL query)
        $today = date("Y-m-d");
        // The MySQL query that will modify the appropriate record in the database
        // In short, it changes the value of mastodon_verified to 1 (verified) for a specific Mastodon account
        $update = "UPDATE connections SET mastodon_verified='1', date='" . $today . "' WHERE twitter_login='" . $twitter . "' AND mastodon_login='" . $mastodon . "'";
        // Executes the above query
        mysqli_query($mysqli, $update) or die('ERROR TD03');
    }
    // If the desired phrase could not be found...
    else 
    {
        // ...then the verification has failed
        $mastodon_verified_error = true;
    }
}
```
