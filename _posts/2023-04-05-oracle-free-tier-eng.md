---
title: "Free VPS with 4 OCPU, 24GB RAM and 200GB storage [ENG 🇬🇧]"
date: 2023-04-05
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "amd"
  - "amperea1"
  - "arm"
  - "cloud"
  - "cpu"
  - "ddns"
  - "firewall"
  - "freetier"
  - "http"
  - "https"
  - "ocpu"
  - "oracle"
  - "port22"
  - "port443"
  - "port80"
  - "ram"
  - "selfhosted"
  - "ssh"
  - "sshkeys"
  - "termius"
  - "ubuntu"
  - "vm"
  - "vps"
image: "/images/oraclefreetier.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/oracle-free-tier/)

Surprisingly, it's **not a scam**, and despite the title sounding like clickbait, in fact it's **not**! We're talking about _[Oracle Cloud Free Tier](https://www.oracle.com/cloud/free/)_. Don't ask me how they manage to offer it completely for free, especially with such specifications... Is there a catch? It's possible, but I don't see it. Perhaps the only one is that _Oracle_ is another huge corporation that is eager to get its hands on our data, and we're giving it to them by using their seemingly free services. Everyone will have to make their own decision whether to use this offer or not. In this post, **I will describe step by step how to get such a _VPS_** (let's remind ourselves that this acronym stands for _Virtual Private Server_).

## What do I have from it?

I've mentioned this before, but I'll repeat it again here: as usual, **I'm not playing any affiliate links or partner programs**, which means that **I'm not receiving any financial benefits** for recommending this solution to you. **Content on my blog is free** from such tactics, and I create it solely with the purpose of sharing knowledge, as well as to have a creative outlet from my daily activities. However, if you, dear Reader, feel like supporting me financially, it would be greatly appreciated! You can do this through my accounts on [_Patreon_](https://www.patreon.com/bePatron?u=67755731) and/or [_Patronite_](https://patronite.pl/patronuj/to3k-za-5pln/128901).

## What's the deal here?

Returning to the topic of free _VPS_, the point is that _Oracle_ has something called the _Free Tier_ program, which can be accessed after registration and confirmation of identity by attaching a credit or debit card. **You don't need to do anything else**. On the start, you also get an additional $300 (which in Polish currency is 1150PLN) for 30 days, which can be used to test paid features. We won't be using that, as we will focus on the _Free Tier_ itself, which is a **program offering free (supposedly forever) _VPSs_**. Of course, there are certain limitations on what is free and what is not, but I am leaning towards this solution because in my opinion, **you can get quite a decent _machine_ out of it**. An additional bonus is that _Oracle_ also offers a **dedicated public IPv4 address**, which is a huge advantage that **is not even available in some paid VPSs** from other providers. Thanks to this option, we won't have to deal with any Dynamic DNS configurations.

The limits refer to the fact that larger cloud solution providers like to charge everything on an hourly basis. On the one hand, it is convenient for both them and the user, who firstly has the option of flexibly renting services, and secondly, can easily scale them. However, on the other hand, it is really difficult to calculate the real cost that will be incurred, for example, after a month or a year. Oracle has two main converters: _OCPU hours_ and _GB hours_. _OCPU_ stands for _Oracle Compute Unit_, and in this converter, it is about how much computing power we use per month. In the case of Oracle's free plan, we have the option of using up to 4 _virtual machines_ equipped with a **_Ampere A1_ processor in _ARM_ architecture**, with a maximum of 3000 _OCPU hours_ per month. It depends on you what structure you plan to run in the Oracle cloud, but I will consolidate all these parameters into one _machine_, so I will **create a _VPS_ with 4x _OCPU_**. The _GB hour_ converter refers to the amount of RAM we use. In the _Free Tier_, we get 18000 _GB hours_ per month, which, when divided by the number of days in a month and the number of hours in a day, gives us 25GB per hour, so we can run one or many _machines_ with a total of 24GB of RAM. Of course, I will **put the entire 24GB of RAM into one _machine_**.

An additional restriction that _Oracle_ imposes on the _Free Tier_ program is the amount of available disk space. We have a total of up to **200GB of memory for data** to use. It can be divided into parts of 50GB between _machines_ or assigned as a whole to one, which is exactly what I intend to do.

There is also an **option to run up to two _instances_ based on _AMD_ processors in parallel**, but they do not have parameters that match the specification mentioned earlier, because they are virtual _machines_ with only **1/8 _OCPU_ power and 1GB of RAM**. Therefore, we will stick to the solution based on the _ARM_ architecture. _ARM_ has been on the market for some time now and it's really hard to find software that has not yet been ported to this architecture and does not work on it. As a reminder, the entire _Raspberry Pi_ platform and its alternatives run on _ARM_.

## Registering with Oracle Cloud

I will simplify the process only to points enriched with screenshots, describing step by step the whole process.

![](/images/oracle1.png)
    
![](/images/oracle2.png)
    
![](/images/oracle3.png)
    
![](/images/oracle4.png)
    
![](/images/oracle5.png)
    
![](/images/oracle6.png)
    
![](/images/oracle7.png)
    
![](/images/oracle8.png)
    
![](/images/oracle9.png)
    
![](/images/oracle10.png)
    
![](/images/oracle11.png)
    
![](/images/oracle12.png)
    
![](/images/oracle13.png)
    

1. Go to [oracle.com](https://oracle.com), find the _View Accounts_ button \[1\] in the upper right corner, and click it to bring up a window. Then click the _Sign in to Cloud_ button \[2\].

3. You will be redirected to the login panel. Under the section _Not an Oracle Cloud customer yet?_, click the _Sign Up_ button \[3\].

5. The page will take you to a registration form, where you provide basic information such as your country \[4\], first name \[5\], last name \[6\], and email address \[7\]. You will receive a confirmation email at the email address you provided, so it must be a valid one. Note that some people like to use temporary email solutions (such as a 10-minute email) in these cases. Finally, confirm that you are not a robot \[8\] and click the _Email Verification_ button \[9\].

7. Check your email inbox for an email from _Oracle_, which will contain a button to confirm your email address \[10\]. In my case, it took quite a while for the email to arrive, despite the fact that the website states that the email is valid for 30 minutes. Nonetheless, it worked out eventually. It is possible that you will need to be patient, as the _Oracle_ registration system seems to be quite buggy... Nevertheless, you can take this time to do something else entirely and even close the _Oracle Cloud_ registration form tab, as you will be redirected back there after clicking the link in the email.

9. After confirming the email and returning to the form, its scope expands. We provide the password for the account twice \[11\]. In the _Customer type_ section, we select _Individual_ \[12\] (interesting that this is seemingly the only thing that has not been translated into Polish). In the _Cloud Account Name_ field, we enter our identifier \[13\], which we will use to log in, and it is important to note that this is not a login, as the email address is used as the login during the login process. However, this name is equally important during the login process, so it must be remembered. Finally, we need to set our primary region \[14\]. The region selection is important because with a free account, _machines_ can only be registered in the region that we declare during registration. Only in a paid plan is it possible to have access to all regions. I recommend choosing the region that is closest to our place of residence, so for Poland, it will be the German Frankfurt. Anyone who has ever bought a VPS knows that in Europe, the two most popular regions are Helsinki (Finland) and Frankfurt (Germany).

11. The next page concerns address data, so we provide our residential address \[15\], city \[16\], postal code \[17\], and phone number \[18\]. After that, we confirm by clicking the _Continue_ button \[19\].

13. The section concerning the address is collapsed, and identity verification through payment card is expanded. Here, I am not sure, because I did not check, but I assume that the card information on the card must match what we provided earlier. I am writing this because if a minor reads this and performs all of this with parental consent and also uses their card, they must provide the parent's information from the very beginning, not just now. After clicking the _Add Payment Verification Method_ button \[20\], a window will appear, which was supposed to be a selection window, but in practice, it only allows us to choose the _Credit Card_ option \[21\], which we also select. At this point, the payment form will open, pre-filled with the previously provided data, and at the end of it, there are fields where we should enter the card number, expiration date, and CVV number. We start the payment process, and here it will look different for each bank. I assume that for most, we will have to confirm this transaction on the phone or in the transaction service. The verification process is standard and involves _Oracle_ charging us a sum of about $1 (when I did it, it was 4.80 PLN) and then returning the same amount after a second. In most banks, the transaction is immediately treated as invalid and will not appear on the billing at all. I also have to add that _Oracle_ is quite picky when it comes to accepting some cards, as confirmed by the opinions that can be found on the Internet. Virtual or temporary cards will most likely be immediately rejected. Apparently, there is also a general problem with _Revolut_. I tried with a card from _mBank_, and it didn't work, so for the second attempt, I used _Citi Bank_, and it went through. After a successful verification, we will receive a green window...

15. After closing the aforementioned window, we return to the registration form, where our card should have been added. We scroll down the page, select the required consent to activate the free trial version \[23\], and finalize everything with the _Launch my free trial_ button \[24\].

17. Now we just have to wait for the confirmation email that our account has been successfully created and all the resources available with the free account have been granted to us.

## Creating an Oracle Cloud Instance

_Oracle_ refers to _virtual machines_ as _instances_. In this chapter, we will create exactly such an _instance_ as described in the title of this post and in one of the above chapters.

![](/images/oracle20.png)
    
![](/images/oracle21.png)
    
![](/images/oracle22.png)
    
![](/images/oracle23.png)
    
![](/images/oracle24.png)
    
![](/images/oracle25.png)
    
![](/images/oracle26.png)
    
![](/images/oracle27.png)
    
![](/images/oracle28.png)
    
![](/images/oracle29.png)
    
![](/images/oracle30.png)
    
![](/images/oracle31.png)
    
![](/images/oracle32.png)
    
![](/images/oracle33.png)
    
![](/images/oracle34.png)
    
![](/images/oracle35.png)
    
![](/images/oracle36.png)
    
![](/images/oracle37.png)
    
![](/images/oracle38.png)
    
![](/images/oracle39.png)
    

1. Just like in the previous chapter, we go to [oracle.com](https://oracle.com), find the _View Accounts_ button in the upper right corner, and after clicking it, a window will pop up where we click the _Sign in to Cloud_ button.

3. We will be redirected to the login panel and this time we fill in the _Cloud Account Name_ \[1\] field according to what we entered in the _Cloud Account Name_ field during registration (this is the important identifier I wrote about earlier). We confirm with the _Next_ button \[2\].

5. We go to the standard login page where we enter our email address as the login \[3\] and password \[4\], and then confirm with the _Log in_ button \[5\].

7. We are in our control center. We activate the main menu by clicking the button with three horizontal lines in the upper left corner \[6\]. Then go to the _Compute_ tab \[7\], and in it, select _Instances_ \[8\].

9. We will be taken to the center for managing our _instances_ (_virtual machines_). First, if not already selected, we need to choose the _Compartment_ \[9\], we will only have one choice, which will be _\[our account name\] (root)_. In the screenshot I made, you can see that there is already one _instance_, in your case, it won't be there because we are just about to create it. We click the _Create instance_ button \[10\].

11. We will be presented with a new instance creator. The first step is to give it a name \[11\], which can be anything and probably doesn't need to be unique in a global context, only within our _instances_. The next step is to expand the _Placement_ section by clicking _Edit_ \[12\].

13. In the _Placement_ section, we decide in which _Domain_ we will create our _machine_ \[13\]. If we previously chose _Frankfurt_ as our region, we will have three domains to choose from here. It seems to me that it doesn't matter which one we choose. However, there is a chance that we will have to come back to this place later and change the domain, because during the finalization of creating the _instance_, we may encounter an error that there are no available _machines_ with the parameters we have selected in the one we just chose. Then we switch from, for example, AD-2 to AD-3 and try again.

15. We proceed to the _Image and shape_ section and expand it just like the previous one \[14\]. After expanding it, we are presented with the option to choose the operating system and the parameters of the _instance_. We start with the operating system by using the _Change image_ button \[15\]. In the window that appears, I suggest selecting _Ubuntu_ \[16\], scrolling down, selecting version _22.04_ \[17\], and confirming with the _Select image_ button \[18\]. Now we click the _Change shape_ button \[19\], which opens the machine parameter configurator. We select _Virtual machine_ \[20\], _Ampere_ \[21\], check _VM.Standard.A1.Flex_ \[22\], change the _Number of OCPUs_ to 4 \[23\], check if the _Amount of memory (GB)_ is set to 24GB \[24\], and confirm with the _Select shape_ button \[25\].

17. The next section we're interested in is _Networking_, which we of course expand \[26\]. In this section, there are three things we need to set up. The first is the _Primary network_, which can be visualized as a home Wi-Fi network that includes all our devices. We're just starting out, so let's create a new virtual cloud network by selecting _Create new virtual cloud network_ \[27\] and giving it a name \[28\]. The second thing is the _Subnet_, which is a subset of our main network. It's like setting up subnets on a home router with addresses ranging from 192.168.0.1 to 192.168.0.255. Here, we also create a new subnet by selecting _Create new public subnet_ \[29\] and giving it a name \[30\]. The last thing we need to do in the network settings is make sure we have selected _Assign a public IPv4 address_ \[31\], which means requesting a dedicated, public _IPv4_ address for our _instance_. I would like to emphasize again that this is a great option that is not available for many paid _VPSs_.

19. The next section is _Add SSH keys_, which, as you can guess, is about keys we will use to authenticate during _SSH_ communication. _Oracle_ (rightly) does not allow logging in to the server using only a username and password, but instead requires the use of _SSH keys_. When creating a new _instance_, I suggest simply selecting the option _Generate a key pair for me_, allowing _Oracle_ to generate a pair of keys for us and downloading the keys - _private_ \[33\] and _public_ \[34\]. It is important not to lose these keys, as we will not be able to access our server without them.

21. The last section is _Boot volume_, where we can increase the disk space that will be allocated to this _instance_. This is done by selecting the option _Specify a custom boot volume size_ \[35\] and entering a value from 50 to 200 in the _Boot volume size (GB)_ field \[36\]. By default, it's 50GB, but in the _Free Tier_ range, we can use 200GB, and I recommend entering that value. I also suggest selecting the _Use in-transit encryption_ option \[37\] in the lower part of this section, as encrypting data during transfer is always a good option.

23. That's it. Now all you have to do is confirm the above settings by clicking the _Create_ \[38\] button and thus create your first _virtual machine_ in the _Oracle_ cloud. At this point, we may still see the message I wrote about in point 7 above. In that case, simply choose a different domain and try again.

## SSH connection to the instance

Looking at this post now, I can see that it has already become monstrous, and it will only get bigger because I would like to turn it into such a mega-guide about _Oracle Free Tier_. The form I have chosen, which is to write as explicitly as possible, also does not contribute to this being a concise post. I'm sorry!

![](/images/clarkson.jpg)

Returning to the subject. In this post, I have already discussed how to create an account in _Oracle Cloud_ and how to create the first _virtual machine_, making the most of the free plan's capabilities. Now it's time to describe how to connect to that _machine_.

I have described how to connect to servers via _SSH_ in [this post](https://blog.tomaszdunia.pl/serwer-domowy-eng/#ssh). Meanwhile, in [this post](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja-eng/#sshkeys), I explained how to use SSH keys. I won't describe all of this again. We'll focus only on what's not obvious for a specific case. To connect via SSH, we basically need four things:

1. _IP_ address of the server,

3. username we will log in as,

5. public _SSH_ key,

7. private _SSH_ key.

The first two steps can be achieved by accessing the instance management center (as we did in point 4 of the chapter about creating _instances_). After successfully creating the instance, we should see it on the list of our _instances_, so let's go to its properties \[1\].

![](/images/oracle40.png)

The information we are looking for (server IP address \[2\] and username \[3\]) can be found in the _Instance information_ tab under the _Instance access_ section on the right-hand side.

![](/images/oracle41.png)

We have already downloaded the necessary _SSH_ keys to our disk when creating the _instance_. We have everything we need, so now we just need to put it all into _Termius_ (or use another method) and connect to our brand new _VPS_. After connecting via _SSH_, I recommend to change (set) the passwords for the current root and ubuntu users.

```bash
sudo su
passwd
   [enter root password twice]
sudo passwd ubuntu
   [enter ubuntu user password twice]
exit
```

By the way, I also remind you of my post [Home server - basic configuration](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja-eng/).

## Opening ports

It must be admitted that _Oracle_ actively takes care of the basic security of its customers. In addition to the firewall (based on iptables) that we can configure on our virtual machines, there is also an additional firewall that is part of the parent infrastructure. Assuming that you already have plans for which services you will run on your server, dear Reader, to access them from the outside, you need to have open ports on your server. By default, _Oracle_ opens only port _22_ for each virtual machine, which is used for SSH communication. The remaining ports are closed. Therefore, the last thing I will try to convey in this post is how to open other ports of your virtual machine. I will show this on the example of ports _80_ (HTTP) and _443_ (HTTPS), which are necessary, for example, to run a website.

First of all, let's open the ports in the aforementioned parent firewall. This is done through the web interface, which I previously colloquially referred to as the control center.

![](/images/oracle50-1024x503.png)
    
![](/images/oracle51-1024x503.png)
    
![](/images/oracle52-1024x503.png)
    
![](/images/oracle53-1024x503.png)
    
![](/images/oracle54-1024x503.png)
    
![](/images/oracle55-1024x503.png)
    
![](/images/oracle56-1024x503.png)
    
![](/images/oracle57-1024x503.png)
    

1. To access the firewall settings, first go to the instance management center (as we did in step 4 of the chapter on creating _instances_).

3. Next, enter the properties of our _instance_ \[1\].

5. In the _Instance details_ section, there is a link to the _Virtual cloud network_ \[2\], which is a link to the virtual cloud network where our _instance_ is located. It is in its settings that we will find what we are looking for, namely the network firewall rules.

7. In the network settings on the left panel, select _Security Lists_ \[3\].

9. On the list, there should be an item whose name starts with _Default Security List for..._ \[4\]. Enter its properties, as this is the parent firewall's settings.

11. The firewall settings are divided into rules for incoming traffic _Ingress Rules_ and outgoing traffic _Egress Rules_. Add a new rule using the _Add Ingress Rules_ button \[5\].

13. In the _Source CIDR_ field \[6\], enter the value _0.0.0.0/0_, which means that the connecting address does not matter. Then in the _Destination Port Range_ field \[7\], enter the value _80_, and confirm with the _Add Ingress Rules_ button \[8\]. This rule opens port 80.

15. We do the same for port _443_. In the _Source CIDR_ field \[9\], enter the value _0.0.0.0/0_, then in the _Destination Port Range_ field \[10\], enter the value _443_, and confirm with the _Add Ingress Rules_ button \[11\].

From the level of the main firewall, ports _80_ and _443_ have been opened, so we still need to open the final doors, which is the firewall running on the server. This is done by modifying _iptables_, which is the built-in Ubuntu firewall. Let's start with port 80:

```bash
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 80 -j ACCEPT
sudo netfilter-persistent save
```

We do the same for port 443 (HTTPS):

```bash
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 443 -j ACCEPT
sudo netfilter-persistent save
```

As you can see, to open any other port, you just need to change one number representing the port number in the first of the above commands.

Let's now check if all the above actions were successful. When I did it myself, my first idea was to use an online port scanner (e.g. [this one](https://www.whatismyip.com/port-scanner/)), but it turned out that all ports except _22_ are still closed... I feel like laughing at myself because I wasted almost an hour before I figured out that the scanner shows that the port is closed because no service is running on it. I write this to save you time, dear Reader.

So how do we check if we have correctly opened port _80_? We will run a simple _HTTP_ server using _Python_. Below I have prepared a ready set of commands:

```bash
mkdir /tmp/port80
echo 'Port 80 is open!' > /tmp/port80/index.html
sudo python3 -m http.server 80 --directory /tmp/port80/
```

In short: we create a temporary folder, place an _index.html_ file inside it, and run an _HTTP_ server on port _80_. Now we enter the _IP address_ of our _VPS_ in the browser's address bar and confirm with _ENTER_. If we see the message _Port 80 is open!_, it means that everything has gone as it should. We go back to the terminal and stop the _HTTP_ server with the CTRL+C key combination and clean up its files so as not to leave any garbage on our fresh _virtual machine_.

```bash
rm -rf /tmp/port80
```

## IPv6 Support

After publishing this post, I remembered that I should also discuss another topic, which is enabling _IPv6_ support. Without it, the machine will function correctly, but for some services that we may want to run on it, _IPv6_ support is recommended. An example of such a service is the _Mastodon_ instance, which will only work on _IPv4_, but without _IPv6_, it won't be able to communicate with other instances that operate based on this addressing. _Oracle_ provides us with the ability to enable IPv6 and assign an address to our _instance_, so that's what we'll do.

![](/images/ipv61-1024x503.png)
    
![](/images/ipv63-1024x503.png)
    
![](/images/ipv64-1024x503.png)
    
![](/images/ipv65-1024x542.png)
    
![](/images/ipv66-1024x542.png)
    
![](/images/ipv67-1024x503.png)
    
![](/images/ipv68-1024x542.png)
    
![](/images/ipv69-1024x542.png)
    
![](/images/ipv610-1024x542.png)
    
![](/images/ipv611-1024x542.png)
    
![](/images/ipv612-1024x542.png)
    
![](/images/ipv613-1024x542.png)
    
![](/images/ipv613bis-1024x503.png)
    
![](/images/ipv614-1024x542.png)
    
![](/images/ipv615-1024x542.png)
    
![](/images/ipv616-1024x542.png)
    
![](/images/ipv617-1024x542.png)
    
![](/images/ipv618-1024x542.png)
    

1. We go to the settings of the virtual cloud network of our instance as we did in points 1-3 of the chapter on opening ports.

3. In the section on the left-hand side, we find _CIDR Blocks/Prefixes_ \[1\] on the list.

5. We click on the _Add CIDR Block/IPv6 Prefix_ button \[2\].

7. In the window that slides out on the right-hand side, we scroll down where we select the _Assign an Oracle allocated IPv6 /56 prefix_ option \[3\] and confirm it with the _Add CIDR Blocks/Prefixes_ button \[4\].

9. After a while, in the upper right corner, we will see a tooltip confirming the assignment of an IPv6 address to our instance \[5\].

11. Now we need to assign the created IPv6 address to the subnet where our _instance_ is located. In the section on the left, we go to _Subnets_ \[6\]. We find the appropriate subnet \[7\] on the list and go into its properties.

13. We click on the _Edit_ button \[8\].

15. In the window that slides out on the right-hand side, in the _IPv6 Prefixes_ section, we select the _Assign an Oracle allocated IPv6 /64 prefix_ option \[9\], and when we do, an additional text field \[10\] will appear, in which we must enter any two-digit hexadecimal value between _00_ and _FF_. It does not matter what we enter here, so let's assume it is _69_ (😎). We only need to confirm it with the _Save changes_ button \[11\].

17. Now we need to properly configure the _firewall_. To do this, we go back to the virtual cloud network settings, and on the left-hand side, we find _Security Lists_ \[12\] on the list. On the displayed list, we find the entry that interests us and go into its properties \[13\].

19. At this point, the task is to open the appropriate ports for incoming traffic in _Ingress Rules_ (as we did in the chapter on opening ports), but this time we do it for _IPv6_ instead of _IPv4_, so we enter _::/0_ instead of _0.0.0.0/0_ as the _Source CIDR_ \[14\]. Just like with rules related to _IPv4_, we add them for all ports we want to open (_80_ and _443_).

21. In the firewall settings, we still need to go to _Engress Rules_ \[15\] and use the _Add Egress Rules_ \[16\] button to add a rule that will open all outgoing traffic through _IPv6_, just like we have it done for _IPv4_.

23. As the _Destination CIDR_ \[17\], we enter _::/0_, from the _IP Protocol_ drop-down list, we select _All Protocols_ \[18\] and confirm with the _Add Egress Rules_ \[19\] button.

25. After configuring the firewall, we still need to set up the _routing_. We go back to the cloud network settings and find the _Route Tables_ \[20\] section on the left-hand list. From the displayed list, we find the entry that starts with _Default Route Table for_... \[21\] and go into its properties.

27. As we can see, we already have the correct _routing_ for _IPv4_, but for _IPv6_ we need to create it. We click the _Add Route Rules_ \[22\] button.

29. In the window that will slide out from the right side, in the _Protocol Version_ \[23\], we select _IPv6_, from the _Target Type_ drop-down list \[24\], we select _Internet Gateway_, in the _Destination CIDR Block_ text field \[25\], we enter _::/0_, from the _Target Internet Gateway_ drop-down list \[26\], we select our cloud network and confirm everything with the _Add Route Rules_ \[27\] button.

31. Finally, we need to assign an _IPv6_ address to our _instance_. To do this, we go to the _instance_ settings (three horizontal bars in the upper left corner -> _Compute_ -> _Instances_ -> select our _instance_ from the list).

33. In the left-hand section, we find _Attached VNICs_ \[28\], from the list that will be displayed, we select the only _VNIC_ (_Virtual Network Interface Card_) \[29\] that will be displayed, and go into its properties.

35. In the left-hand section, we find _IPv6 Addresses_ \[30\] and click the _Assign IPv6 Address_ \[31\] button.

37. In the window that will appear on the right-hand side, from the _Prefix_ \[32\] dropdown list, choose the prefix that was created earlier (there should be only one option available to choose from). Below, I suggest leaving the default selection for _IPv6 address assignment_ \[33\], which is _Automatically assign IPv6 addresses from prefix_, meaning that the address for our _instance_ will be selected automatically. Of course, if desired, we can always change this setting to manual and define a specific address ourselves. Confirm by clicking the _Assign_ \[34\] button.

## Summary

Phew, I must admit that writing this post wasn't easy for me. It took me a lot of time just to prepare screenshots showing everything step by step. Nevertheless, I am very satisfied with the final result. I think that in this post, I managed to explain in a clear way how to use this undoubtedly interesting _Oracle_ offer. Moreover, I guided you from the very beginning to the very end, without any ambiguities. I think that such a _VPS_ is a great solution for learning and more, because its parameters are reasonable enough to run many services on it.
