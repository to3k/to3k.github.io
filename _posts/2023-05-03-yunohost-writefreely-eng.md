---
title: "YunoHost - How to run WriteFreely instance [ENG 🇬🇧]"
date: 2023-05-03
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "a"
  - "aaaa"
  - "activitypub"
  - "blog"
  - "caa"
  - "cloudflare"
  - "dns"
  - "fediverse"
  - "https"
  - "mx"
  - "opensource"
  - "oracle"
  - "proxy"
  - "selfhosted"
  - "ssl"
  - "txt"
  - "vps"
  - "writefreely"
  - "yunohost"
image: "/images/writefreelycloudflareyunohost.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/yunohost-writefreely/)

It all started with me writing a particularly well-received post on [how to get a pretty interesting cloud server for free with _Oracle_](https://blog.tomaszdunia.pl/oracle-free-tier-eng/). Then I wrote a guide on [how to install _YunoHost_](https://blog.tomaszdunia.pl/yunohost-oracle-eng/), which makes it easier to run your own applications/services, on that server. Later, using all of this, [I launched a Polish instance of _WriteFreely_ (Polska)](https://blog.tomaszdunia.pl/writefreely-polska-eng/), which is a blogging platform heavily embedded in _Fediverse_. And in this post, I'll describe step by step how I did it, and therefore, how you, dear Reader, can launch such an instance yourself!

## Adding a domain and installing the application on YunoHost

First and foremost, we need a domain on which the _WriteFreely_ instance we're about to launch will run. The domain provider can be any, and the only requirement is that we can set at least DNS records for it, i.e. point to the server that will tell it where we want people, who visit it, to be redirected. It's also desirable to be able to set _A_, _AAAA_, _MX_, _TXT_, and _CAA_ records, but if your domain provider doesn't offer this option, we'll manage without it. Once we have the domain, we can get started.

![](/images/yhwf1-1024x503.png)
    
![](/images/yhwf2-1024x503.png)
    
![](/images/yhwf3-1024x503.png)
    
![](/images/yhwf8-1024x503.png)
    
![](/images/yhwf9-1024x503.png)
    
![](/images/yhwf10-1024x503.png)
    
![](/images/yhwf11-1024x503.png)
    
![](/images/yhwf12-1024x503.png)
    
![](/images/yhwf14-1024x503.png)
    

1. Login to the administration panel of your _YunoHost_.

3. From the main menu, select the _Domains_ \[1\] tab.

5. In the upper right corner, find the _\+ Add domain_ \[2\] button and click it.

7. Select the option _I have my own domain..._ \[3\] and in the text field _Domain name_ \[4\], enter the address of your domain, then confirm by clicking the _Add_ \[5\] button.

9. Go back to the main menu and this time select the _Applications_ \[6\] tab.

11. In the upper right corner, find the _\+ Install_ \[7\] button and click it.

13. In the search text field \[8\], enter _writefreely_. The available applications will be filtered and limited to one item whose name matches the phrase we are looking for. Of course, click on it \[9\].

15. A page briefly describing what _WriteFreely_ is will appear. We can even use the _Try demo_ button to try out a demo version of this platform. However, we scroll down where we have a few things to set up.

17. In the text field _Label for WriteFreely_ \[10\], enter the name under which we want to see this application in the list of applications in our _YunoHost_. We can change this later, so no stress.

19. From the drop-down list below \[11\], select the previously configured domain.

21. Next, we have a choice field with the options _Yes_/_No_ \[12\], where selecting _Yes_ means that access to the site will not require an account on our _YunoHost_ server. What we choose here depends on the type of service we are launching. If we want our instance of _WriteFreely_ to be publicly available, we select _Yes_, but if we are creating an instance for use only by, for example, our friends, the _No_ option is appropriate.

23. The next drop-down list \[13\] is used to indicate which _YunoHost_ user should be the administrator of this application, and the text field \[14\] below it is used to set the access password to this application for that user (its administrator).

25. Finally, we have to answer the question \[15\] whether we want to create an instance only for ourselves (_Single User Blog_) or if we intend to allow others to register. _Yes_ means an instance only for us, and _No_ means an instance open to others.

27. We confirm everything by clicking on the _Install_ button \[16\].

## Adding and configuring a domain in Cloudflare

I know that there will be those who strongly criticize my recommendation to use _[Cloudflare](https://cloudflare.com)_, seeing it as another corporate solution that offers seemingly free services but in reality has almost a monopoly in what it offers. Maybe that's true, but I'm not imposing anything here. I'm just going to show you a universal way to set up DNS records correctly because, first of all, not all domain providers offer the possibility of applying such specific settings for the domain, and secondly, it would be impossible to write instructions for each of these providers because there are so many of them. In short, below I'll show you how to do it using _Cloudflare_, and you, dear Reader, will decide whether you want to do it the same way or try your own skills and set it up without using _Cloudflare_.

![](/images/cf1-1024x503.png)
    
![](/images/cf2-1024x503.png)
    
![](/images/cf3-1024x503.png)
    
![](/images/cf4-1024x503.png)
    
![](/images/cf5-1024x503.png)
    
![](/images/cf6-1024x503.png)
    
![](/images/cf7-1024x503.png)
    
![](/images/cf9-1024x503.png)
    
![](/images/cf10-1024x503.png)
    
![](/images/cf11-1024x503.png)
    
![](/images/cf12-1024x503.png)
    
![](/images/cf13-1024x503.png)
    
![](/images/cf14-1024x503.png)
    
![](/images/cf15-1024x503.png)
    
![](/images/cf18-1024x503.png)
    

1. We start by registering a new account on _[Cloudflare](https://dash.cloudflare.com/sign-up?lang=en-US)_ or logging into an existing one.

3. In the _Websites_ tab, we find the _\+ Add a Site_ \[1\] button in the upper right corner.

5. In the text field \[2\], we enter the domain we want to add and confirm it with the _Add site_ \[3\] button.

7. On the next page, we need to choose which plan we want to use. At the bottom, there is a free plan \[4\]. We choose it and confirm with the _Continue_ \[5\] button.

9. We will be taken to a page where the current (detected) DNS record settings of this domain will be presented. I suggest deleting all items at this stage because we will add later new ones, and proceed using the _Continue_ \[6\] button.

11. The last of the three most important steps is to change the DNS records of the domain to those of _Cloudflare_. Here, we come to the core of how _Cloudflare_ works, which is a kind of proxy between the domain and the server that handles it. Everything depends on redirecting traffic from the domain to _Cloudflare_, which filters it appropriately (if necessary) and forwards it according to the settings we have specified. _Cloudflare_ provides a wide range of options, and managing top-level domains (not subdomains of another domain) is free for basic functions. Returning to the topic, on this page, _Cloudflare_ informs us of the detected settings (in my case, it was pointing the domain to _ns1.cba.pl_, _ns2.cba.pl_, and _ns3.cba.pl_) and proposes what they should be changed to include the _Cloudflare_ mechanism. To do this, we take the two provided NSs (short for Name Servers) \[7\]\[8\] and put them into the domain settings in the management panel of our domain provider (on the screenshot, I showed how it looks in my case). In the case of _Cloudflare_, it is always a pair, but it may appear in configurations with different first elements.

13. After making changes, we confirm with the _Done, check nameservers_ \[9\] button.

15. Now we just have to wait for the DNS record changes of our domain to propagate. _Cloudflare_ will monitor this process for us, and we will be notified by email when the changes are made. In extreme cases, this can take up to 24 hours.

17. Meanwhile, we receive a proposal for quick configuration of basic settings. We start this process by clicking the _Get started_ button \[10\]:
     - _Automatic HTTPS Rewrites_ \[11\] - a function that rewrites all _HTTP_ links to _HTTPS_, I recommend turning it on and proceeding with the _Save_ button \[12\],
     
     - _Always Use HTTPS_ \[13\] - forcing the use of only _HTTPS_, i.e., automatically redirecting all unencrypted _HTTP_ traffic to the encrypted channel, I recommend turning it on and proceeding with the _Save_ button \[14\],
     
     - _Brotli_ \[15\] - a function that optimizes page loading times by using compression, it can cause incorrect operation of running services, so I recommend turning off this function by default and possibly later turning it on and checking if there will be any conflict, proceed with the _Save_ button \[16\]

19. We end the whole process by clicking the _Finish_ button \[17\].

## Redirecting a domain to a YunoHost server

After receiving a confirmation email from _Cloudflare_ that our domain has been properly set up, we can proceed with configuring the DNS records. First, we need to determine what needs to be set. To do this, we go to _YunoHost_ and access the diagnostic tool (just like we did in [this post](https://blog.tomaszdunia.pl/yunohost-oracle-eng/)). _YunoHost_ informs us that the most important, necessary for operation, is setting the _A_(_@_) record \[1\], while the rest are only recommended - _MX_ \[2\], _TXT_ \[3\]\[4\]\[5\], _A_(_\*_) \[6\], _CAA_ \[7\].

![](/images/yhwf17-1024x503.png)
    
![](/images/yhwf18-1024x503.png)
    
![](/images/yhwf19-1024x503.png)
    

Correctly set DNS records for a _WriteFreely_ instance running on a server with _YunoHost_ look like this:

![](/images/yhwf30-1024x542.png)

Note that it is possible to set _Proxy status_ to _DNS only_ for _A_ records, which means that traffic is not filtered in any way by _Cloudflare_, but only forwarded according to the settings.

## SSL certificate (HTTPS)

Finally, we need to set up an _SSL_ certificate, which is required to establish a secure _HTTPS_ connection. _YunoHost_ has _Let's Encrypt_ built in by default, which is a tool that allows for free and automatic issuance of _SSL_/_TLS_ certificates. To use it, simply go to the settings of a specific domain, then to the _Certificate_ tab and find the green _Install Let's Encrypt Certificate_ button at the bottom.

![](/images/yhwf21-1024x503.png)

## Ready!

Everything is ready, so now you can go to the aforementioned domain and start using our freshly launched instance of _WriteFreely_. Configuration can be accessed by logging into the administrator account, which has additional options unavailable to other users.
