---
layout: post
title: "GrapheneOS [ENG 🇬🇧]"
published: true
categories: 
  - "thoughts"
  - "tutorials"
tags: 
  - "grapheneos"
  - "android"
  - "ungoogled"
  - "google"
  - "pixel-9a"
  - "privacy"
  - "foss"
  - "open-source"
image: "/images/grapheneos.png"
---

[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/grapheneos/)

Table of contents:
* TOC
{:toc}

## Introduction (feel free to skip)

Just a year ago, I was really deep into the Apple ecosystem. It seemed like there was no turning back from the orchard for me. Phone, laptop, watch, tablet, video and music streaming, cloud storage, and even a key tracker. All from one manufacturer. Plus shared family photo albums, calendars, and even shopping lists.

However, at some point, I discovered [Plenti](https://plenti.app), a company that rents a really wide range of different devices at quite reasonable prices. Casually, I threw the phrase "samsung fold" into the search engine on their website and it turned out that the Samsung Galaxy Z Fold 6 could be rented for just 250-300 PLN per month. That was quite an interesting option, as I was insanely curious about how it is to live with a foldable phone, which after unfolding becomes the equivalent of a tablet. Plus, I would never dare to buy this type of device, because firstly, their price is astronomical, and secondly, I have serious doubts about the longevity of the folding screen. I checked the rental conditions from Plenti and nothing raised my suspicions. Renting seemed like a really cool option, so I decided to get the Fold 6 for half a year. That's how I broke out of the orchard and slightly reopened the doors to my heart for solutions without the apple logo. I even wrote a post about the whole process - [I betrayed #TeamApple for broken phone](https://blog.tomaszdunia.pl/zdradzilem-teamapple-eng/). What I'm getting at is that this is how Android returned to my living room and I think I started liking it anew.

My adventure with Samsung ended after the planned 6 months. The Galaxy Z Fold 6 is a good phone, and the ability to unfold it to the size of a tablet is an amazing feature. However, what bothered me about it was:

1. after folding it was terribly thick,
2. it couldn't be used in a case, because all the covers either didn't fit or slipped off the part that has screens on both sides,
3. naked, it was very blocky, even sharp, which caused me discomfort; holding it was simply unpleasant,
4. paying 300 PLN (~80 USD) for rent is a good short-term solution to get something to test, but not in the long run.

All the points above made me give up on extending the rental and start wondering what to do next. Interestingly, I liked Android enough that I didn't necessarily want to go back to iOS. Around this time, an article hit my RSS reader: [Creators of the most secure version of Android fear France. Travel ban for the whole team](https://ithardware.pl/aktualnosci/grapheneos_ucieka_francja_kraj_niebezpieczny_prywatnosc_open_source-46855.html) (I think it was this one, but I'm not entirely sure, it doesn't really matter). It talked about how France wants to get its hands on the [**GrapheneOS**](https://grapheneos.org/) system and thus carry out a very serious attack on the privacy of its users. I thought then, "Hey! A European country **wants to force a backdoor into the system**, because it is too well secured to surveil its users. Either this is artificially blowing the topic out of proportion, or **there is actually something special about this system!**". At that moment, a somewhat forgotten nerd gene ignited in me. I decided to abandon not only iOS, but also mainstream Android, and try a completely alternative system.

## What is GrapheneOS

GrapheneOS is a custom, **open-source operating system** designed with the idea of **providing users with the highest level of privacy and security**. It is based on the Android Open Source Project (AOSP), but differs significantly from standard software versions found in smartphones. Its creators completely **eliminated integration with Google services** at the system level, which avoids tracking and data collection by corporations, while offering a modern and stable working environment.

The system is distinguished by advanced "hardening" of the kernel and key components, which minimizes vulnerability to hacking attacks and exploits. A unique feature of GrapheneOS is the ability to run Google Play Services in an **isolated environment** (sandbox), allowing the user to use popular applications without granting them broad system permissions. Currently, the project focuses on supporting **Google Pixel** series phones, utilizing their dedicated Titan M security chips for full data protection.

## Dedicated devices

When I used to read about GrapheneOS, the list of compatible devices included items from several different manufacturers. Now it's only Google Pixel devices. This doesn't mean you can't run this system on a Samsung, for example, but the creators simply don't guarantee it will work properly, and you have to deal with potentially porting the version yourself. Note that it's quite funny that **a system freed from Google services should be run exactly on Google devices**. If anyone wants to read more about why Pixels are the best for GrapheneOS, I recommend checking out the following keywords - Verified Boot, Titan M, IOMMU, MTE.

### List of supported devices (February 2026)
- **Pixel 10 Pro Fold (rango)**
- **Pixel 10 Pro XL (mustang)**
- **Pixel 10 Pro (blazer)**
- **Pixel 10 (frankel)**
- **Pixel 9a (tegu)**
- **Pixel 9 Pro Fold (comet)**
- **Pixel 9 Pro XL (komodo)**
- **Pixel 9 Pro (caiman)**
- **Pixel 9 (tokay)**
- **Pixel 8a (akita)**
- **Pixel 8 Pro (husky)**
- **Pixel 8 (shiba)**
- Pixel Fold (felix)
- Pixel Tablet (tangorpro)
- Pixel 7a (lynx)
- Pixel 7 Pro (cheetah)
- Pixel 7 (panther)
- Pixel 6a (bluejay)
- Pixel 6 Pro (raven)
- Pixel 6 (oriole)

_I've bolded the items that are not only supported but also recommended (at the time of writing this post, you can find the current list [here](https://grapheneos.org/faq#recommended-devices))_

### My smartphone choice
At the stage of choosing a device to test GrapheneOS on, I wasn't yet sure if such a solution would work for me at all and if I'd last with it in the long run. So it would be unreasonable to lay out a significant amount of money. Because of this, probably the only sensible choice was the **Google Pixel 9a**. This was a few months ago, when not enough time had passed since the premiere of the 10 series models for them to make it onto the fully supported devices list. At that time, the Pixel 9a was the freshest device on the list (**offering up to 7 YEARS of support!**) and on top of that, it was very attractively priced, as I bought it for around **1600 PLN** (~450 USD).

In retrospect, I still consider it a good choice and definitely **recommend this path to anyone** who is currently at the stage of deciding on what hardware to start their GrapheneOS adventure. The only thing that bothers me a bit about the Pixel 9a is the quality of the photos it takes. I switched to it having previously had the iPhone 15 Pro and Samsung Galaxy Z Fold 6, which are excellent in this regard, so it's no wonder I'm a bit spoiled, because I was simply used to a completely different level of cameras. Now I also know that **GrapheneOS will stay with me for longer**, so it's possible that knowing then what I know now, I would have opted for some more expensive gear. However, this isn't important to me now, because for the time being I don't plan to switch to another device, and by the time that changes, the market situation and the list of available options will certainly have changed too. Besides, I'm **positively surprised by the battery life and overall performance of this phone**.

## Installing GrapheneOS

### We need

1. A suitable **smartphone** - in my case, it's a Google Pixel 9a.
2. A **cable** to connect the phone to a computer; it can't be just any cable, but one that is used not only for charging but also for data transmission. It's best to just use the cable that came with the phone.
3. A **computer with a Chromium-based browser** (e.g., Google Chrome, Brave, Microsoft Edge, Vivaldi?). Unfortunately, I must recommend Windows 10/11 here, because then you don't have to mess around with any drivers; it's the simplest option.

### Phone preparation

1. If it's new, we take it out of the box and **turn it on**. If it was previously used, we **restore it to factory settings** (Settings -> System -> Reset options -> Erase all data (factory reset) -> Erase all data). I think it's stating the obvious, but I'll write it anyway - a factory reset results in the deletion of all user data from the device, so if you have anything important on it, you need to back it up.
2. We must **go through the basic setup** until we see the home screen. We do the absolute minimum. Here is a breakdown of the steps:
    - on the welcome screen, you can change the language to whatever suits you
    - we skip the GSM services setup (SIM card)
    - we don't connect to Wi-Fi, so we skip this step too
    - the date and time settings should be correct
    - we turn off all Google Services (location, scanning, sending diagnostic data) and accept
    - we don't need to do anything with the warranty terms, so just the Next button
    - we accept the Legal Terms
    - we set some easy PIN, e.g., 12345
    - there is no need to waste time setting up biometrics, so we politely decline and skip fingerprint and face scan
    - a moment of waiting
    - we skip the tutorial
    - swipe up and we're done, we are on the home screen.
3. First of all, we need to make sure that **our phone's software is updated** to the latest available version. For this purpose, we go to **Settings -> System -> System update**. If necessary, we update.
4. Next, we go to **Settings -> About phone -> find the Build number field** and tap it 7 times until we see the message **You are now a developer**. In the meantime, the phone will ask for the PIN we set during the phone setup.
5. We go back and now enter **Settings -> System -> Developer options -> turn on the OEM unlocking option**. The phone will ask for the PIN again. After entering it, we still have to confirm that we definitely want to remove the lock.

### Unlocking the bootloader

1. We start the bootloader unlocking process by **turning off the phone**.
2. When the screen goes completely dark, **we simultaneously press and hold the power and volume down buttons** until the text-based **Fastboot Mode** interface appears. If the phone starts up normally, it means we performed one of the earlier steps incorrectly.
3. We connect the **phone to the computer**.
4. We go to the computer and open the browser (based on the Chromium engine) to the address **[https://grapheneos.org/install/web](https://grapheneos.org/install/web)**.
5. We go to the [Unlocking the bootloader](https://grapheneos.org/install/web#unlocking-the-bootloader) section and press the **Unlock bootloader** button.
6. A window with a list of devices to choose from will pop up in the browser. There should basically be only one item on it, and that should be our Pixel. **We select it and press the Connect button**.
7. Changes will occur on the phone's display. A message will appear asking to confirm that we actually want to unlock the bootloader. To do this, we must press one of the volume buttons so that instead of **Do not unlock the bootlader**, **Unlock the bootlader** appears. At this point, we can confirm by **pressing the power button**.
8. If everything succeeded, among the data displayed in Fastboot Mode we should see **Device state: unlocked** (in red).

### Downloading and flashing the system image

1. On the GrapheneOS website, we scroll down to the [Obtaining factory images](https://grapheneos.org/install/web#obtaining-factory-images) section and press the **Download release** button. If the phone is still connected to the computer, the website will decide on its own which system image to download.
2. We wait for the download to finish. It is obvious that the time needed for this depends directly on the speed of the internet connection.
3. When the download is complete, we can go to the [Flashing factory images](https://grapheneos.org/install/web#flashing-factory-images) section below and press **Flash release**.
4. Spit over your left shoulder now, hold your breath, and under no circumstances unplug the phone from the computer. Best not to touch either device at all.
5. When the process is complete, the phone will restart itself and return to the Fastboot Mode interface. In the browser, we will see the message **Flashed ...**.

### Re-locking the bootloader

Locking the bootloader is crucial because it enables the full operation of the Verified Boot feature. It also prevents the use of fastboot mode to flash, format, or wipe partitions. Verified Boot detects any modifications to the OS partitions and blocks the reading of any altered or corrupted data. If changes are detected, the system uses error correction data to attempt to recover the original data, which is then verified again – thanks to this mechanism, the system is resilient to accidental (non-malicious) file corruption.

However, before re-securing the bootloader, I recommend checking if the system was flashed correctly and everything works as it should, because if it doesn't, locking the bootloader might brick (completely block, or even damage) the phone. Therefore:

1. Being in Fastboot Mode, when we see the **Start** message, we press the power button, which will cause the system to start normally. If we don't see **Start** at the height of the power button, we have to press the volume buttons and find this option.
2. When the phone starts up, we can immediately perform the basic setup. The bootloader won't run away.
3. This is a standard procedure, so we will only go through it briefly:
    - welcome screen
    - we choose the **language**
    - we choose the time zone and thus set the **date and time**
    - we connect to **Wi-Fi**
    - if you can, you can immediately set up the **SIM card**, but you can also postpone it for later
    - I recommend turning off the **location service**, because it's better to configure it calmly later by granting permissions only to apps that really need it
    - securing the phone with a **fingerprint**; I personally am an advocate of this solution, so I recommend using it, GrapheneOS does not (yet) support face unlock, so fingerprint and a standard password are the only methods we have to choose from (of course I reject pattern unlock right at the start as a form of screen lock that cannot even in good conscience be called any security)
    - I assume that if you are reading this post, you are a graphene freshman and you have no **backup** to restore, so we just skip this step
    - **Start** button and we are on the home screen.
4. If everything is working correctly, you can now go ahead and turn off the phone and turn it on while holding the power button and volume down, just like we did earlier.
5. We land back in Fastboot Mode. I assume the phone was connected to the computer the whole time (if not, reconnect it). We return to the browser on the computer. We find the [Locking the bootloader](https://grapheneos.org/install/web#locking-the-bootloader) section and press the **Lock bootloader** button.
6. Again, confirmation of this operation on the phone is required. It looks analogous to unlocking, except this time, using the volume buttons, we have to make the **Lock the bootloader** option active and confirm it with the power button.
7. The result should be a change of **Device state** to **locked** (in green).

### Restoring the OEM lock

The final step before starting to play with the new system is reapplying the OEM lock.

1. Just like when removing the lock, we go to **Settings -> About phone -> find the Build number field** and tap it 7 times until we see the message **You are now a developer**. In the meantime, the phone will ask for the PIN we set during the phone setup.
2. We go back and now enter **Settings -> System -> Developer options -> turn off the OEM unlocking option**. The phone will ask us to restart to change this setting, but for now we cancel this request, because we still want to **completely turn off Developer options**, which is done by unchecking the box next to the first option at the very top, **Use developer options**.
3. Now we can **restart the device**.

## My vision of using GrapheneOS

Now the real fun begins. You'll hear/read as many opinions on what you should and shouldn't do regarding GrapheneOS hardening as there are people. Some are conservative, while others approach the topic a bit more liberally. In my opinion, there is no one right path, and everyone should dig around, test things out, and decide what suits them and fits their security profile. You'll quickly find out that **GrapheneOS is really one big compromise between convenience and privacy**. While this same rule applies to everything belonging to the digital world, it's only in this case that you'll truly notice it, because **GrapheneOS will show you how many things you can control, which you can't do using conventional Android**.
I don't intend to use this post to promote some "one and only" method of using GrapheneOS. I'll simply present how I use this system. This way, I'll show the basics to people fresh to the topic, maybe I'll manage to suggest an interesting trick they didn't know to those who have been users for a while, and on a third note, maybe some expert will show up who, after reading my ramblings, will suggest something interesting or point out what I'm doing wrong / could do better. I'm sure that's the case, since my adventure with GrapheneOS has practically only been going on for 3 months. I warn you right away that I'm not sure if I'll be able to maintain a logical train of thought, as I'll probably jump around topics a bit. **The subject of GrapheneOS is vast** and in today's post I'll only manage to slightly touch upon it.

### Additional user profile

One of the first things I did after booting up the freshly installed system was to create a second user profile. This is done in **Settings -> System -> Multiple users**. The idea is for this feature to allow two (or more) people to use one phone, each having a separate profile with their own settings, apps, etc. Who in their right mind does that? While I can imagine sharing a home tablet, sharing a phone completely eludes me. It therefore seems like a dead feature, but nothing could be further from the truth.

For me, it works like this: on the ***Owner*** user, because that's the name of the main account created automatically with the system, I installed the **Google Play Store** along with **Google Play services** and **GmsCompatConfig**. This is done through the **App Store** application, which is a component of the GrapheneOS system. Please don't confuse this with Apple's app store, even though the name is the same. From the Play Store I only installed the following applications:

- **mBank** - paying via contactless BLIK through NFC is possible only having Google services installed and only works for me on the user profile with administrator privileges (Owner),
- **Mój T-Mobile** - without Google services, the Magenta Moments tab didn't work for me at all.

And that's it. As you can see, this profile serves me only for apps that absolutely require integration with Google services. In practice, I switch to it only when I want to pay contactlessly in a store, which I actually do rarely lately, because if there's an option, I pay using BLIK codes. Right after switching from Samsung there were more apps on this profile, but one by one I successively gave up on those that made me dependent on the big G.

It's on the **second profile**, which let's assume I called _Tommy_, that I keep my entire digital life. What does this give me? For instance, the main profile cannot be easily deleted, but the additional one can. Let's imagine a situation where I need to quickly wipe my phone, but in a way that its basic functions still work, i.e., without a full factory reset. An example could be, say, arriving in the USA and undergoing immigration control. They want access to my phone, so I delete the _Tommy_ user, switch to the _Owner_ user, and hand them the phone. It makes calls, sends SMS messages, even has a banking app, so theoretically it shouldn't arouse suspicion. However, it lacks all my contacts, a browser with my visited pages history, a password manager, and messengers with chat histories. This is rather a drastic scenario, but not really that improbable, as actions like searching a phone upon arrival in the States are something that happens on a daily basis. Besides, the basic rule of security is **not to use an account with administrator privileges on a daily basis**. 

### Obtainium

On GrapheneOS, Obtainium is my **primary aggregator for obtaining .apk installation files and automating app updates**. It's like the Google Play Store, but privacy-respecting and for open-source applications. It would be a sin to use GrapheneOS and not at least try to switch to open-source apps. Below I present a list of apps that I use. Additionally, I'm tossing in links to the source code repositories of each of them.

#### List of my open-source applications
- [**AntennaPod**](https://github.com/AntennaPod/AntennaPod) - podcast app (I haven't completely switched to it from Pocket Casts yet, but I plan to),
- [**Aurora Store**](https://github.com/whyorean/AuroraStore) - if there is no other option to download an .apk file, this very app can serve as an alternative to the Google Play Store, I'll mention it again later,
- [**Bitwarden**](https://github.com/bitwarden/android) - password manager,
- [**Brave**]() - web browser,
- [**Breezy Weather**](https://github.com/breezy-weather/breezy-weather) - weather,
- [**Catima**](https://github.com/CatimaLoyalty/Android) - app for storing loyalty cards (I have my Biedronka and Lidl cards in it, but the rest are waiting to be added too),
- [**Collabora Office**](https://github.com/CollaboraOnline/online) - office suite that will open everything that Microsoft Office or LibreOffice does,
- [**DAVx2**](https://github.com/bitfireAT/davx5-ose) - app for syncing things via DAV (calendars, contacts, to-do lists, or cloud files), I need it to sync the calendar I share with my wife,
- [**Ente Auth**](https://github.com/ente-io/ente) - two-factor authentication, an alternative to Google/Microsoft Authenticator or Authy, 
- [**FairScan**](https://github.com/pynicolas/FairScan) - document scanning, simple without advanced features,
- [**Feeder**](https://github.com/spacecowboy/Feeder) - RSS reader,
- [**Home Assistant**](https://github.com/home-assistant/android) - smart home management,
- [**Klawiatura FUTO**](https://github.com/futo-org/android-keyboard) - I highly recommend this keyboard, and plus to it the [FUTO Voice Input](https://voiceinput.futo.org/) package, which generates text from speech based on an LLM model running offline on the device,
- [**Librera**](https://github.com/foobnix/LibreraReader) - ebook reader,
- [**Obtainium**](https://github.com/ImranR98/Obtainium) - yes, Obtainium can update itself,
- [**Organic Maps**](https://github.com/organicmaps/organicmaps) - maps with navigation based on OpenStreetMap,
- [**Pachli**](https://github.com/pachli/pachli-android) - Mastodon client,
- [**Signal**](https://github.com/signalapp/Signal-Android) - messenger,
- [**Simplenote**](https://github.com/Automattic/simplenote-android) - notes,
- [**Stremio**](https://github.com/stremio) - torrent-based VOD (I'll definitely write a post about it soon),
- [**Thunderbird**](https://github.com/thunderbird/thunderbird-android) - email client (it's actually K-9 Mail after a rebranding).

To understand how Obtainium works and how to use it, **I recommend checking out [this video guide](https://odysee.com/@%C5%81%C4%85cze:4/aplikacje_bez_Google...2025_:f)**.

### Aurora Store

I have a few apps that are not open-source, but I still need them. In this case, I don't download them from the Google Play Store, but exactly from the **Aurora Store**, which I mentioned above.

Aurora Store is an open-source client of the Google Play store (I guess you could call it a frontend) that **allows downloading applications from Google servers without needing Google services** (GMS) on the phone.

The Internet characterizes this solution as follows:

- **Privacy** - you don't need to log in with a Google account to download free apps (you can use built-in anonymous accounts).
- **Security** - you install original .apk files straight from Google servers, not from unverified third-party sites.
- **Functionality** - allows bypassing regional restrictions and installing apps that Google Play considers "incompatible" with a given device.
- **Open Source** - the entire application code is transparent and auditable.

Sounds perfect, right? A bit, yes, but unfortunately not everything holds up completely. I have **two main complaints** about Aurora Store.

With these anonymous accounts, the thing is that **sometimes they work, and sometimes they don't**, due to limits that are unreachable with a normal account used by one person, but when a thousand people download apps from one account at once, it starts to get suspicious, and the limits are exceeded quite quickly. Using Aurora Store violates the Google Play Store terms of service, so on the other hand **if we use our Google account, it might be temporarily blocked** or permanently banned. Some option here is to create a "burner" account just for this, but that takes away some of our privacy, because Google can still index us based on what we downloaded. Anonymous accounts in this case provide almost complete anonymity, because then we are just a drop in the ocean.

When it comes to security, yes, in theory we download .apk files from a verified source, but **only under the condition that the Aurora Store creators don't serve us a [Man in the Middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attack**. The decision whether you trust the creators of this app is up to you.

#### List of apps whose functionality without GMS I have verified

Below I present a list of applications that I downloaded from the Aurora Store, checked, and can confirm that they work without GMS (Google Mobile Services).

- **Allegro** - shopping
- **Apple Music** - yes, I didn't manage to give this up when ditching the iPhone
- **Apple TV** - comes in a bundle, but if it didn't I'd cancel the subscription, because Stremio is enough for me
- **Biedronka** - grocery promos
- **Bolt** - taxis
- **Booksy** - barber
- **BPme** - fuel promos
- **CityParkApp** - city parking
- **Decathlon** - I got rid of it, but it worked
- **DeepL** - translator, is there any open-source alternative that is equally good?
- **Discord** - after recent events I'll probably get rid of it, because I basically don't use it
- **Duolingo** - the owl! learning Italian together is a daily routine for my daughters
- **DWService** - remote desktop
- **Ekstraliga** (speedway) - I'm a psycho fan
- **epark** - city parking
- **Formula 1** - I'm a psycho fan
- **Geoportal Mobile** - spatial development plans, buggy as hell app, but works better than the mobile web version
- **GitHub** - I know there is the OpenHub alternative, but it crashes for me after logging into GH
- **My municipality's app** - because I need to know when they'll collect my trash :)
- **Jakdojade** - bus schedules
- **Lidl Plus** - grocery promos
- **LiveKid** - communication with my daughter's kindergarten
- **Messanger** - shame on me, but unfortunately I have friends who can't imagine life without FB...
- **OLX** - local classifieds, I basically only use it for notifications
- **OpenVPN** - I use it as a tunnel to my home network
- **park4night** - great app for finding parking on vacation (not only in a camper)
- **Pepper** - bargain hunting
- **Perplexity** - I switched to Gemini, but I confirm it works
- **Synology Photos** - my home photo gallery on a NAS
- **Pocket Casts** - podcasts, I plan to migrate to AntennaPod
- **Reddit** - honestly I don't know why I need the app, but it works
- **Reolink** - home monitoring
- **SmartLife** - anyone who has anything smart from China knows what this is for
- **Tapo** - home cameras
- **Termius** - here I'm also looking for some open-source alternative
- **Tether** - managing TP-Link routers
- **TickTick** - to-do lists, it's hard for me to find a sensible alternative that is multiplatform and has all the features I need
- **TV Time** - tracking what series and movies I've watched (I might actually be interested in finding an alternative here too)
- **Zepp** - dedicated app for the Amazfit Balance smartwatch I use
- **ZeroTier** - I used it instead of OpenVPN back when I didn't have fiber optic yet, just radio internet

### Full control over app permissions

GrapheneOS allows for full control over what permissions each application can have. For example, in conventional Android forks, every application by default has granted **Network** (internet access) and **Sensors** (access to all sensors like the accelerometer) permissions.

Has anyone ever wondered **if all apps on a phone need Internet access?** Indeed, in the vast majority of cases, a mobile app without network access is useless, but you can't generalize like that, because for example, the previously mentioned **FUTO Voice Input** uses a local LLM to convert speech to text, which works offline on the device. Why would such an app need Internet access then? For nothing, so **it shouldn't have such permission**. Now let's take apps like FairScan (document scanning), Catima (loyalty card aggregator), Collabora Office (office suite), or Librera (ebook reader). They too **do not need Internet access!**

The situation looks even more bizarre when you look at which apps actually need access to all of our device's sensors. If we think about it calmly, we'll conclude that in this specific case it's completely the opposite of the previous one, meaning **practically no app needs this information**. And I remind you that **by default on Android with Google services, all apps have such permissions**.

To manage a given application's permissions, just **tap and hold on its icon**, select **App info** from the pop-up menu, and find the **Permissions** tab. A list categorized by things like - **Allowed**, **Ask every time**, and **Not allowed** will appear. I recommend reviewing this list for each app separately right after installing it. This is **the foundation of GrapheneOS hardening**.

A collective menu where you can view specific permissions and which apps have them granted is available in **Settings -> Security & privacy -> Privacy -> Permission manager**. Another interesting place is the **Privacy dashboard** available in the same location. It's a tool that shows not only app permissions, but also how often a given app reaches for the permissions granted to it.

### Private space

In GrapheneOS we don't only have user profiles, but each user can also have something called a **Private space**. I encountered something similar on Samsung, where it was called **Secure Folder**, so I assume this might just be an Android feature implemented differently by each manufacturer.

Private space is turned on in **Settings -> Security & privacy -> Private space**. It acts like a sort of separated sandbox that is part of the environment you use, but at the same time is isolated from it. For me, it's a place that gives me quick access to apps that nevertheless require Google services. You might ask - why then do I keep the mBank and T-Mobile apps on the **Owner** user if I could keep them here? Well, for reasons unknown to me, I'm unable to configure my private space so that paying with contactless BLIK via NFC works correctly in it. The same goes for Magenta Moments from T-Mobile, which don't work correctly despite GMS being installed in the private space.

#### List of apps in my private space

- **Google Drive** - I use it as a cloud to share files with clients
- **Finax** - saving for retirement under PEPP
- **IKO** - PKO BP bank app, treasury bonds plus PPK
- **InPost Mobile** - parcel lockers, location doesn't work for me in the private space either (the phone doesn't send its position to the app), so I use QR codes like some Neanderthal
- **mBank** - again, because while contactless payment doesn't work for me here, other banking app functions work normally (including BLIK code payments, as well as confirming transactions with biometrics)
- **mObywatel** - at first I kept this app in the main profile as downloaded from Aurora Store and everything somewhat worked, but every now and then the app caught a total freeze and stopped responding, I think it might be related to the fact that it does send some Google services-related requests in the background and doesn't respond until such a request times out, I have this on my list to investigate
- **mojeIKP** - lately I've been having more and more health problems, I'm clearly not as indestructible anymore, so such a geriatric app is simply essential for me
- **Mój T-Mobile** - duplicated just like the mBank app, because everything works except Magenta Moments
- **Orlen Vitay** - this app didn't work for me without GMS, so sort of a D minus for Orlen, because the app from BP doesn't have such a problem
- **Revolut** - basically it probably doesn't require GMS, but I decided I'll just keep all financial apps in the private space
- **Santander** - another banking app...
- **Play Store** - I have to download all these apps from somewhere, doing it via Aurora Store in the private space wouldn't make sense since I have the whole Google services package installed here anyway
- **XTB** - another investing app... works without GMS, but like I said, I keep all financial ones in one place

## Summary

Oof... I did it again, sorry. I'm just counting the characters and it comes out to just under 35,000... I'll probably break that barrier with these next few sentences. Well, long again, but purely meaty again, so I don't think anyone has reason to complain. As I mentioned earlier, I've only touched upon the topic of GrapheneOS, which is extensive, and it's a good thing, because it's a **great system**, and the biggest **respect goes to the people behind this project**. It's thanks to them that we even have the option of at least partially **freeing ourselves from Google (Android) and Apple (iOS)**. Therefore, I highly invite you to the final chapter of this post.

## Supporting the GrapheneOS project

Finally, I would like to encourage you to **support the GrapheneOS project**. The developers behind it are doing a really great job and in my opinion deserve to have some money thrown at them. Information on where and how this can be done can be found **[here](https://grapheneos.org/donate)**.