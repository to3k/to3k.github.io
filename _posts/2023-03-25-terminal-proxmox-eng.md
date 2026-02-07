---
title: "Terminal with Proxmox - more ambitious home server [ENG 🇬🇧]"
date: 2023-03-25
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "allegro"
  - "cpu"
  - "dellwyse"
  - "fujitsu"
  - "intelnuc"
  - "minipc"
  - "opensource"
  - "proxmox"
  - "ram"
  - "raspberrypi"
  - "selfhosted"
  - "terminal"
  - "virtualmachine"
  - "vm"
coverImage: "/images/proxmox1.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/terminal-proxmox/)

I have already discussed how to easily and relatively inexpensively set up a home server based on platforms such as _Raspberry Pi_. However, there are also other, slightly more ambitious solutions. An example of this is a home server built on devices that, due to their specific nature, I like to call _terminals_. Such devices include [_Intel NUC_](https://www.intel.pl/content/www/pl/pl/products/details/nuc.html). Of course, such a _NUC_ in a sensible configuration will cost quite a bit, especially compared to _Raspberry Pi_. **However, there is a way out to not ruin your wallet!** This is to buy used or refurbished hardware. There are many companies that offer this type of equipment, even providing a warranty of up to 6 months. Many interesting offers can be found, for example, on _Allegro_ (info for non-Poles: _Allegro_ is our polish equivalent to Amazon, eBay etc.).

## Terminal vs Raspberry Pi

I decided to visually present the advantages and disadvantages of _terminals_ compared to the previously described _Raspberry Pi_.

### Advantages

- More powerful processors

- x86 architecture processors (not just ARM)

- Processor mounted in a normal socket, e.g. LGA 1150, rather than soldered onto the motherboard, allowing for replacement

- More RAM (even solutions with 16GB are reasonable in terms of price)

- Compact case with integrated cooling and space for drives

- More advanced virtualization is possible

### Disadvantages

- Price, especially for a reasonable specification

- One should rather aim for used equipment, not to go bankrupt

- Higher energy consumption

- Working culture - active cooling (fan)

- Larger size

As you can see, this solution has its advantages, but it also has disadvantages. However, if someone wants to seriously get into self-hosting, I think it will still end up with buying a _terminal_.

## Reasonable parameters

Due to the price-to-quality ratio, _Dell Wyse 5070_ is very popular. If we focus on budget optimization, I definitely recommend considering this option. However, in my opinion, 8GB of RAM is too little. If I had to define my **minimum parameters**, which we start talking about really cool hardware, they would be:

- **4-core** x86 architecture processor,

- **16GB** RAM,

- **512GB** **SSD** disk,

- **1 Gbps** standard Ethernet (RJ45) port.

This is the minimum that will allow you to run quite decent 4 virtual machines (of course, this is just an example, as resources can be divided as desired), each of which will get one dedicated core and 4GB of RAM. It will be a similar experience to owning four Raspberry Pi 4Bs, and the price won't be that crazy, which I'll show you in a moment.

## Study on my example

As an example, I'll use what I bought some time ago. I bought my _terminal_ as an one from shop exhibition on _Allegro_ (a Polish e-commerce platform). If anyone is interested, for convenience, I prepared a [link to _Allegro_](https://allegro.pl/kategoria/komputery-stacjonarne-486?order=d&monitor=brak&liczba-rdzeni-procesora=4&liczba-rdzeni-procesora=6&liczba-rdzeni-procesora=8&liczba-rdzeni-procesora=32&wielkosc-pamieci-ram=16%20GB&wielkosc-pamieci-ram=24%20GB&wielkosc-pamieci-ram=32%20GB&wielkosc-pamieci-ram=64%20GB&typ-dysku-twardego=SSD&typ-dysku-twardego=SSD%20\(M.2\)&typ-dysku-twardego=brak%20dysku&offerTypeBuyNow=1&price_to=1000) with the appropriate search filters, which can be a good starting point for your search. There are also computers of much larger size (the size of a normal PC) than the solutions we are talking about here, because they meet the hardware requirements specified in the search filters, and cannot be filtered out in any way in terms of size or even type, so unfortunately, you, dear Reader, will have to do that part of the job yourself. By the way, this is not an affiliate link, so **I don't have any benefits** from pasting it here.

Returning to the subject, the terminal that I bought is the **_Fujitsu Q920_** equipped with a **4-core Intel i5-4590T processor**, which is an aging but still respected 4th generation processor, with a clock speed of 2.0GHz (max. 3.0 GHz) and **16GB of RAM** (which was probably the most important thing for me). I paid around **630 PLN** (~$150) for it, but that was some time ago, so prices may be slightly different now, but the order of magnitude should remain the same, and that's already a valuable piece of information. I also had to buy a **512GB SSD drive** in the standard 2.5" size (I decided that was enough for me). It's worth noting that I decided to pay a little extra for an _SLC_ drive, which is known for its greater durability and is a dedicated solution for server applications. _SLC_ drives are also associated with slightly higher prices, but current memory prices are so low that I easily managed to fit this drive into the budget of **200 PLN** (~$50).

## Proxmox Installation

In my opinion, the **best operating system** to install on such a terminal is **_Proxmox_**. It is a **free** virtualization environment with **open-source** code, based on the _Debian_ system. In [one of my previous posts](https://blog.tomaszdunia.pl/docker-eng/), I wrote about _Docker_. _Proxmox_ is a more advanced _Docker_, which allows you to run not just containers with services, but full-fledged operating systems. It's more like running multiple _Raspberry Pi_ boards in one _terminal_. _Proxmox_ also has its own requirements that you need to pay attention to when buying a _terminal_, the main ones being:

- 64-bit processor architecture,

- Support for virtualization (Intel processors - Intel-VT, and for AMD - AMD-V)

The installation is extremely easy and analogous to the one I described in [the post about setting up a home server](https://blog.tomaszdunia.pl/serwer-domowy-eng) based on the _Raspberry Pi_ platform and similar. In short, we download the _Proxmox_ image from the [creators' website](https://www.proxmox.com/en/downloads/category/iso-images-pve) and upload it to a pendrive using the [_balenaEtcher_](https://www.balena.io/etcher) program, creating a _bootable USB_ which we then plug into the _terminal_ and start it up. Here the situation looks a bit different because we cannot perform a so-called _headless setup_ like we did with the _RPi_. We will need at least a monitor and keyboard. The installation of _Proxmox_ is quite simple, but I will go through the whole process briefly.

1. **Welcome screen** where we select _Install Proxmox VE_.

3. Acceptance of the **license**.

5. Selecting the **disk** on which to install.

7. Choosing a **location** (country/city) and **time zone**.

9. Setting the **administrator password** and the email address to receive all important messages related to our server.

11. **Network settings** - this will look different for everyone. First, we select the _network card_ to be used (important, if our server has more than one card, I don't need to say that it is recommended to connect the server directly to our router via LAN and select the network card corresponding to the cable interface, not the one responsible for wireless communication). Then it is quite important to set the appropriate _Hostname_, which will be the identifier of our server on the local network. Later, we just need to check if the automatically provided _IP address on the local network_, _gateway_, and _DNS server_, which handles our network traffic, have been indicated correctly. _Proxmox_ always tries to determine default values ​​on its own, which should be corrected if necessary.

13. **Summary screen** of everything we have set up. It is worth checking everything again and if it is OK, **start the installation**.

15. Unfortunately, we have to be patient because the process is not instantaneous. It also depends a lot on the power of our device and, for example, the speed of the disk.

17. After the installation is completed (if we did not uncheck this option), the device should **restart** by itself.

19. A properly started server should display the following message on the monitor:

> Welcome to the Proxmox Virtual Environment. Please use your web browser to configure this server - connect to:
> 
> https://\[server IP address\]:8006/

According to the message, you just need to copy the given address and use another computer to enter the _Proxmox_ management panel. At this point, you can also disconnect the monitor and keyboard from the server as they will no longer be needed. Additionally, there is no need to worry about browser warnings that will likely appear after accessing the given address. This is because we are using an _HTTPS_ connection and our server does not have an _SSL certificate_, so the browser will report that something is wrong and warn us with a large message. The server management panel will only be accessible from the local network, so there is no need to mess with any certificates, and any messages of this kind should be clicked through with buttons saying _I understand the risks and wish to proceed_ or something similar.

## To be continued...

Unfortunately, this post has started to become uncomfortably long, and I still have a lot of information to share, so at this point, I will stop and invite you to [the next post](https://blog.tomaszdunia.pl/proxmox-vm-eng/) where I will describe **how to start the first virtual machine** in a freshly installed _Proxmox_ environment.
