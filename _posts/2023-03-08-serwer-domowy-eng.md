---
title: "Home server at low cost [ENG 🇬🇧]"
date: 2023-03-08
categories: 
  - "ipad-only-eng"
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "arm"
  - "debian"
  - "ipadonly"
  - "linux"
  - "odroid"
  - "ovh"
  - "raspberrypi"
  - "ssh"
  - "termius"
  - "ubuntu"
  - "vps"
image: "/images/ssh.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/serwer-domowy/)

In this post, I will describe how to create a home server that will be a perfect helper (support or complement) for an _iPad_. This is not entirely in line with the _#iPadOnly_ ideology, as it assumes using not only the tablet itself, but treat it like the relationship between Batman and Alfred 😉

This post was based on my second blog - [odroid.pl](https://odroid.pl/blog/), which is a guide for beginners and possibly intermediate users, that strongly focuses on self-hosted topics, specifically about how to create a small home server at relatively low cost, on which you can run several useful tools and services. Despite not covering all the topics I planned to describe, I haven't published anything on odroid.pl for some time. Nevertheless, the knowledge contained there is still up-to-date and may be useful for some. I will use some of these materials here, refer to them, and also plan to finish the topics that I couldn't describe there. The knowledge I will summarize in this post is more developed on [odroid.pl](https://odroid.pl/blog/), so if any of the following issues are unclear, I recommend visiting the second blog as well. Unofortunatelly, odroid.pl is written in Polish without any English versions of post like here.

## Hardware needed

We start with equipping ourselves with the necessary hardware:

1. **Raspberry Pi or equivalent alternative** - I recommend boards with specifications similar to the RPi 4B with 4GB of RAM, ODROID C4 or more powerful (the key is a 4-core processor and at least 4GB of RAM),

3. **Case** - there won't be much choice here, as each board has 2-3 dedicated cases, so just choose the cheapest one,

5. **Cooling** - it's usually included in the kit with the board or case, don't bother with cooling other than passive (aluminum radiator), because first of all, I don't anticipate such a heavy load, secondly, even under load, these boards don't heat up extremely, and thirdly, passive cooling provides acoustic comfort that cannot be achieved even with the highest-class fan,

7. **Power supply** - pay attention to the connector type, power supply voltage, and the maximum current that the board needs, and when choosing a power supply, add at least 1A to have a power reserve for any peripherals (such as external drives) that we may want to connect in the future,

9. **MicroSDXC card** - a 64GB capacity is sufficient to start with, the decision to purchase a larger one is left to individual assessment,

11. **RJ-45 cable (Ethernet)** - if you don't have one, you'll need it to connect the server directly to your home router.

A set with the above specifications **should not cost more than 500 PLN (less than $120)**, and that's only due to the skyrocketing prices recently. Normally, Raspberry Pi could be bought much cheaper than it is now. You can read more about choosing the equipment [here](https://odroid.pl/blog/odroid-c4-zakup/).

## Is it even worth it?

Let's calculate whether it's more cost-effective to have a server based on the RPi platform at home than to rent a VPS (Virtual Private Server - a machine that operates in a data center outside of our home).

For comparison, let's take the most popular provider of such solutions in Poland - [OVH](https://www.ovhcloud.com/pl/vps/), where for a server comparable to Raspberry Pi 4B, with two virtual cores (vCore), 4GB of RAM and an 80GB disk, we would have to pay about **70 PLN per month (approx. $17)**. Don't be fooled by the prices listed on the website, because first of all, the amount of 45 PLN (approx. $11) is without taxes, and secondly, it applies only for the first month.

How does it look for the Raspberry Pi? In this case, we have a higher initial cost, but let's break it down into months and see how quickly it will pay off. First, we need to consider the cost of electricity because the device is in our home and requires power, which we obviously pay for. For the sake of easy calculation and to cut off any discussions, let's take the worst case scenario, in which the server will be running constantly at maximum power. The Raspberry Pi 4B model manufacturer recommends using a power supply with a voltage of 5V and a maximum current of 3A, which in the worst case gives us a power of (5V x 3A =) 15W, so we will be using 15 Wh per hour. Let's convert it to kilowatt hours, which are used as the standard unit on electricity bills, and multiply it by 24 hours to determine how much electricity we will consume per day - (0.015 kWh x 24 h =) 0.36 kWh. I looked at my historical electricity bills and taking into account all additional costs (such as transmission, etc.), I pay an average of about 0.81 PLN (approx. $0.19) per kilowatt hour, and that's already after those legendary price increases because previously it was no more than 0.60 PLN (approx. $0.14)... Continuing the calculation, let's now take the daily consumption multiplied by the average price and multiplied by 30 days, which will give us the **monthly cost** - (0.36 kWh x 0.81 PLN x 30 days =) **8.75 PLN (approx. $2.1)**.

To sum up, VPS is about 8 times more expensive per month, which means that every month VPS costs over 60 PLN (approx. $14) more than the cost of electricity to power a locally running server. Taking into account the initial cost of components, at the level of 500 PLN (approx. $120), we can easily calculate that the return on investment will occur after just 8 months, and then the profit will be exponential.

## Installing the system

I am a supporter of the Ubuntu system, but anyone can choose what he/she prefer. There are plenty of dedicated system images for practically every distribution for RPi, and if it works for RPi, it will also work on alternatives like ODROID. The only thing to keep in mind is that these boards are based on ARM architecture, so you need to choose the correct version of the system.

Assuming we have already chosen the system, we need to flash it onto a microSD card. For this purpose, I usually use a program called [balenaEther](https://www.balena.io/etcher), as it is available on every system. It is extremely easy to use, so I won't go into detail about the process of flashing the system onto the card, as it is done by pressing literally 3 buttons (select image, select drive, flash... done!).

You can find more details about this [here](https://odroid.pl/blog/odroid-instalacja-ubuntu/).

## Connecting via SSH

We can perform the configuration in two ways: by connecting a monitor and keyboard or by using a **headless setup via _SSH_**. For the latter, we need another computer (host), but we don't need any peripherals.

To establish an _SSH_ connection, we first need to determine the address of the newly launched server on our local network. A detailed description of how to do this for beginners can be found [here](https://odroid.pl/blog/odroid-ssh/). Then we will need the login and password of the default user. This information is included in the documentation of the distribution whose image you downloaded. For example, it could be:

- _root_:_(no password)_ - standard for Debian

- _pi_:_raspberry_ - for Raspberry Pi

- _odroid_:_odroid_ - for ODROID

Due to _#iPadOnly_, I use my _iPad_ as a host and manage my servers using the _[Termius](https://apps.apple.com/pl/app/termius-terminal-ssh-client/id549039908)_ app. All I need to do is create a new tunnel and enter the above information. If you don't want to use _Termius_, you can achieve the same result using any terminal and the following command:

```bash
ssh pi@192.168.1.69
```

Replace _pi_ and _192.168.1.69_ with the appropriate information for your case.

## To be continued...

The server has been purchased, the system has been installed, and a connection has been established, so everything is working as it should. In the [next post](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja-eng/), we will cover the basic configuration, which includes fundamental actions that need to be performed on every freshly installed server.
