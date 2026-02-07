---
title: "Let's write a friendly privacy policy  [ENG 🇬🇧]"
date: 2023-05-31
categories: 
  - "thoughts"
  - "tutorials"
tags: 
  - "automattic"
  - "eu"
  - "europeanunion"
  - "gdpr"
  - "googlefonts"
  - "gravatar"
  - "independentanalytics"
  - "internetczasdzialac"
  - "jetpack"
  - "omgf"
  - "privacy"
  - "privacypolicy"
  - "rentgen"
  - "rodo"
  - "wordpress"
coverImage: "rodogdpr.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/rodo-gdpr/)

I must admit that the popularity of this blog has exceeded my wildest expectations. At first, I thought I wouldn't gain many readers and I would be writing to an empty audience. As a result, **I never even thought about writing a privacy policy**. However, with such growth, **it's embarrassing that I still don't have such a document**, so I decided to do something about it. In this post, I will describe the entire process of writing a privacy policy for this blog.

Right from the start, I want to emphasize that **I am not an expert in this field, and the regulations like _[GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)_ are like black magic to me**. I will simply write based on the information I have gathered from the Internet and rely on common sense. I hope no lawyer will crucify me for what I write below. However, I am more than open to constructive criticism!

_UPDATE 11.06.2023:_ My post caught the attention of [Attorney Agnieszka Rapcewicz](https://mastodon.internet-czas-dzialac.pl/@agnieszka), who is an expert in the field of GDPR and also seems to have a grasp of the slightly more technical aspects related to privacy, which only a few lawyers possess. This combination is very valuable, and I am delighted to have had the opportunity to seek an opinion from such an individual! Based on this, I have modified certain sections below, indicating them with the word _Update_ and the date.

_UPDATE 18.07.2023:_ One of the Readers [in a comment](https://blog.tomaszdunia.pl/rodo-gdpr/#comment-409) rightfully pointed out (thank you for that!) that the hosting provider is a processor, not a data controller. The data is entrusted to them, not shared – they cannot do whatever they want with it, but only process it for server administration purposes. If it were shared (which I believe is not the case), they would be a controller, and therefore they could do "whatever they want" with it. This is a valid point, so I have clarified this post and the privacy policy of this blog.

## Initial assumptions

Based on my own example, I see a **reluctance towards any kind of topics related to _GDPR_**. I think this is **due to the form** used to create privacy policy statements, terms of service, and other regulations. In most cases, they are simply massive blocks of text divided into paragraphs, which are supposed to look super professional in that form. I believe my attitude is not unique, and more people (if not the majority) have the same thoughts. Reading anything in this form can be an enjoyable experience only for lawyers and hardcore enthusiasts. But is that really the point? To write something in the most convoluted and incomprehensible way possible? Perhaps it **makes sense for someone who wants to hide something** or smuggle it within a stream of clever and intimidating words. In practice, _GDPR_ is a great thing, whose fundamental assumption should be to protect privacy and ensure the security of ordinary people, citizens, and service users. **Everyone should have the right to ensure the security of their data and have the tools to enforce this right**.

Can a privacy policy be created fulfilling its role without unnecessary hassle? In my opinion, yes! **It is enough to consider the purpose of writing such a document, ask the right questions, and conscientiously answer them** while maintaining a coherent form, focusing only on the substance.

## What are these questions?

Contrary to appearances, **the task of a privacy policy is very simple**. As the owner (Administrator) of a website/service/application, **we need to provide the user with all the information regarding their data**. I have divided this into 6 questions that need to be asked:

1. **Who** is the Administrator (responsible person) of the data collected on this blog?

3. **What** data is collected?

5. **Why** are these data collected?

7. **Where** are these data stored?

9. **To whom**, besides the Administrator, are these data disclosed entrusted?

11. **What** control does the user have over their data?

Let’s start writing!

## 1\. Who

**I am the Administrator for the data collected on my blog**. Since I am an individual and not a company, and I don't have any registered business activity related to this blog, the amount of data I need to provide is limited to just the first name, last name, mailing address, and email address, which fulfill the **legal requirement of providing a communication channel for users to contact me**. In this case, I offer the option of contact through standard postal correspondence or electronically via email.

## 2\. What

At this point, we need to **list the types of collected (and processed) data**. I must admit that I had a hard time with it myself because _Wordpress_ is not like an open book to me, which I fully understand and know where to find specific things. In the case of other scripts that I've written from scratch, I have no problem at all. Then I can confidently state that my tools don't use cookies and don't collect any data about the people using them, which I usually confirm by making them open-source. However, with a blog, we have external actors such as plugins or even themes that I didn't write myself, and it's harder to maintain 100% control over them.

![](/images/proxy-image.png)

Extension for the _Firefox_ browser called [_Rentgen_](https://addons.mozilla.org/pl/firefox/addon/rentgen/) proved to be very helpful in handling this matter. It was created by the team _[Internet. Czas działać!](https://www.internet-czas-dzialac.pl)_. It allows scanning your own (or someone else's) website and generating a report focused on whether the page meets all the legal requirements of _RODO/GDPR_ and how it generally takes care (or not) of the privacy of its users. Based on that, I defined what I needed to improve on my website.

Firstly, I dealt with _Google Fonts_, which are external fonts downloaded from _Google_ servers. It's a very interesting tactic used by the behemoth, which involves hosting fonts used by many websites on their own servers. Usually, this is done through the _gstatic.com_ domain. But what's clever about it? Well, every person who visits a website using _Google Fonts_ connects to _Google_'s servers and downloads those fonts as an external resource while loading the webpage. **This way, _Google_ can effectively monitor internet traffic, profile people, and analyze their online activities**. All of this is done to know as much as possible about you and serve you content (mostly ads) that will have the strongest impact on you. However, these practices carry many other privacy risks for users. Alright, but how did I protect my readers from this? In a very simple way. **All the fonts used on this blog have been downloaded by me and hosted on the server where this blog is hosted**. This means that when a user enters here for the first time, he/she has to download the fonts just like before, but does it without contacting _Google_'s servers. There are many different ways to achieve this, but in my opinion, the simplest one is to use a plugin dedicated to this purpose with a not-so-serious name, called [_OMGF | GDPR/DSGVO Compliant, Faster Google Fonts. Easy_](https://pl.wordpress.org/plugins/host-webfonts-local/). The simplicity of this plugin makes it a solution that anyone can handle.

Another topic that was problematic on my blog was the _Jetpack_ plugin, specifically its _Stats_ module used for collecting blog visit statistics. _Jetpack_ is a plugin made by _Automattic_, the creators of _Wordpress_ itself. This provides a certain level of peace of mind regarding user data processing because it is a **fairly trusted company that values the privacy of its users**, judging by the documentation they provide. **However, I didn't like the idea of my readers' data being sent outside the server** on which the blog is hosted, so I decided to find an alternative. After a brief market research, I decided to use the _[Independent Analytics](https://pl.wordpress.org/plugins/independent-analytics/)_ plugin, which convinced me because it **does not use cookies, does not store any data that can identify specific individuals, and stores all statistics on the blog owner's server**.

![](/images/independentanalytics.png)

After appropriate _trimming_ (removing unnecessary functions), _Jetpack_ will still remain on my blog as a plugin because it offers several really useful tools such as a nice and convenient gallery block in the form of a slideshow, which I often use, a _Firewall_ module to secure the blog, and an _Akismet_ module that helps me fight waves of spam attacks that have targeted my blog. **These are tools that do not collect any data from my readers**, which is confirmed by the documentation provided by the creators of _Jetpack_, who must be commended for placing a significant emphasis on privacy transparency, with each module of their plugin listing whether it collects data and, if so, what kind. All this information are available [here](https://jetpack.com/support/privacy/#data-usage).

As the Administrator of this blog, am I not collecting and processing any data from my readers? I do so through the comment system and contact form, for example.

Let's start with the simpler case, which is the contact form. Users are required to fill in two fields (email address and message content), while the other two (name and message subject) are optional. All these fields are stored in the database, thus **constituting the data I collect**. However, it must be acknowledged that none of this information can be considered critical personal data. At most, it could be the email address and/or if someone provides their full name. I would like to point out that these fields can be filled with any information, and the email will still be delivered to me, although I may not be able to reply if the provided address is fictitious. Nevertheless, **it is necessary to inform users that this data is being collected in your privacy policy**.

In the case of the comment system, the situation is similar, and seemingly even easier since users provide less information - comment content, name, and email address. I intentionally used the word _seemingly_ because, in practice, it is much more complex. This is due to the fact that **by default, after a user provides their email address, it is sent to the _WordPress_ server, which then passes it to _Gravatar_**, another tool by _Automattic_ (the creators of _WordPress_). The user-provided email address is forwarded **for the purpose of retrieving the user's profile picture**, which will be displayed after adding the comment, provided that the email address is associated with a _Gravatar_ account. Thus, we have two options. The first is to include in your privacy policy that the email address is subject to processing and is transferred to third parties, specifically _Automattic_, namely _WordPress_ and _Gravatar_. However, I chose the second option, which may detract from the charm but **is definitely better for the privacy of those who comment on my blog**. **I have completely disabled the _Gravatar_** support, so I do not forward the email address anywhere instead, I only store it in my database as an integral part of the comment. **_WordPress_ automatically also retains the commenter's _IP_ address**, so that should be mentioned as well.

After performing the above actions, I used the _Rentgen_ plugin again, and this time, I achieved the ideal state that I would like to see on all websites on the Internet, not just my own.

![](/images/Rentgenperfect.png)

Now I can say with a clear conscience that **my website does not use cookies and does not transmit any data to third-party domains**. However, this does not end the matter because data is still stored and processed on my server. Let's summarize this chapter. My blog collects the following data from readers:

- email address (when using the contact form or commenting),

- name (when using the contact form or commenting),

- IP address (when commenting),

- comment content,

- title of the contact form message,

- content of the contact form message,

- fully anonymized statistical information (number of page views, referring medium, time spent on the page).

I'm not sure if it's necessary to mention the last one (anonymized statistical information), but it certainly won't hurt to mention it for full transparency.

_UPDATE 11.06.2023:_ Atty. Rapcewicz confirmed my suspicions regarding the necessity of disclosing statistical data as personal data that is collected. I will quote her - _Anonymous data, which cannot be attributed to a specific individual, is not considered personal data. Therefore, you wouldn't have to mention them, but I agree that it's worth mentioning for transparency purposes._

## 3\. Why

In the previous chapter, we indicated what data is collected, and now **we need to justify it**. It is important to demonstrate, and here I quote the law, _the legally justified interest of the Administrator_. In the case of my blog, the matter is quite simple, and I have already explained why I collect data in the previous chapter. I collect data for the following purposes:

- Contact form - thus allowing readers to directly contact me,

- Comment system - thus allowing readers to publicly express their opinions about the content I create,

- Statistics - allowing me to analyze the popularity of posts in order to choose future topics effectively.

Finally, it is necessary to include a short statement, which I mostly took from the Internet, stating that **the data is processed until the user withdraws consent and is processed lawfully, for the specified purposes, which are fully justified and no longer than necessary**.

_UPDATE 11.06.2023:_ Here's a slight clarification based on what I learned from atty. Rapcewicz. I wrote that the data is processed until consent is withdrawn, but for consent to be withdrawn, there must first be such consent collected. In my case, this doesn't happen at all because all the data processed by me is processed for the purpose of fulfilling a legitimate interest, for which I do not need consent, so there is nothing to withdraw. In this case, I should state that **the data is processed until an effective objection is raised** (or until the completion of this matter, but I don't know what could be the deadline in this case, so I will stick to the objection only) ****and is processed lawfully, for the specified purposes, which are fully justified and no longer than necessary****. Therefore, I replaced the withdrawal of consent with raising an objection. If it wasn't for atty. Rapcewicz pointing it out, I would have never realized that this is such an important distinction. In summary, how I collect and process data is justified and does not require user consent. There is no consent to withdraw, but users can raise objections. The effect is practically the same, but there is still a difference, and it cannot be said that it doesn't make sense.

## 4\. Where

In this section, it is important to indicate the **specific location where the previously mentioned data is stored (and processed)**. Additionally, if there are any copies of the data (e.g., backups), it is good practice to indicate their storage location as well. It's worth noting that often the company's registered office (or the address under which it is registered) may be different from the data center that handles its infrastructure. This is the case with my blog.

The hosting provider for this blog is **_ABC Hosting Ltd._** (known more by the domain name [CBA.pl](https://cba.pl)), but the entire infrastructure is hosted in the data center of **_LeaseWeb Netherlands B.V._** located at _Hessenbergweg 95, 1101 CX, Amsterdam, Netherlands_, **within the European Union**. It is **crucial for all data to be stored and processed within the EU** because European _GDPR_ regulations apply in such cases. While it would be optimal for a Polish website to have everything located in Poland, being within the EU is also acceptable since the regulations are the same.

_UPDATE 11.06.2023:_ Here's a slight clarification from atty. Rapcewicz's side - _GDPR regulations also apply to storing data outside the EU (more broadly: EEA). However, in such cases, there are additional legal requirements that must be met to ensure that storing data outside the EEA is in compliance with the law (generally speaking, appropriate safeguards for such data must be guaranteed)._

## 5\. To Whom

It is hard to find a simpler situation than mine because the data processed on this blog is not shared with (or untrusted to) third parties and does not leave the server on which it is stored. However, **if in the case of your website, this data is indeed shared with (or entrusted to) third parties, it should be indicated here**. For example, if I had not stopped using _Gravatar_, I would have to write in this section that data such as email addresses are transferred to _Automattic_ through the _wp.com_ domain and all its subdomains, which means that they are processed not only outside the server managed by the administrator but also outside the hosting provider's infrastructure on which this blog is running.

_UPDATE 11.06.2023:_ Atty. Rapcewicz rightly pointed out that I should indicate the hosting provider in this point as the entity to whom the data is made available entrusted. This is logical since they are the owner of the infrastructure on which this blog is running and where the data collected through it is stored.

## 6\. What (control does the user have?)

The final chapter in which **you should include a basically ready-made formula informing about the user's possible claims**. It's about the fact that _GDPR_ imposes **five basic obligations** on every administrator:

1. to give every user who requests it, the possibility of inspecting **accessing** the personal data collected about them,

3. to give them the possibility of **rectification**,

5. to give them the possibility of **restriction** of processing,

7. to give them the possibility of **objection**,

9. to give them the possibility of **deletion** and consequently **ceasing further processing** of their personal data upon request.

The above requests must be made through one of the contact methods with the administrator indicated in the first chapter.

_UPDATE 11.06.2023:_ Atty. Rapcewicz informed me regarding this point that instead of the phrase _inspection of the content of collected data_, I should use _access to the content of collected data_. Additionally, apart from the right to access, rectify, and delete, the user should also have the right to restrict processing (I understand that this refers to processing certain data and not others) and the right to object, which is related to what I mentioned in chapter _3\. Why_. Due to the above, I have modified the above list of administrator's obligations. Additionally, Atty. Rapcewicz pointed out the obligation to mention that the user, if there are grounds for it, may file a complaint with the President of the Personal Data Protection Office (PPDPO, which polish short form is PUODO).

## That's it!

Now I suggest taking a look at the privacy policy that I have written for this blog. **It is available [here](https://blog.tomaszdunia.pl/polityka-prywatnosci-privacy-policy/)**. Was it difficult? I don't think so. Is this format more user-friendly than most privacy policies I have seen? Definitely. Is a privacy policy in this format less valuable? I don't think so, as it contains all the key information.

I consider this a success. I'm glad I finally wrote a privacy policy for my blog. It also brought me joy to share the progress of this whole process. I also hope that content of this kind will interest someone, help and show that **_GDPR_ is not a bad thing at all**. When the _GDPR_ regulations came in, everyone rolled their eyes and said that it was just another set of dead regulations that would surely serve corporations. However, it turns out to be quite the opposite, **as evidenced by the fines imposed on entities that do not respect (either negligently or intentionally) the privacy of their users**. These regulations, as well as the entire system associated with them, are a **weapon to fight for your right to privacy**. In my opinion, **it is worth knowing them, knowing how to use them, and not being afraid to do so**.
