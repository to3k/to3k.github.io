---
title: "ZeroTier - home VPN without a public IP address [ENG 🇬🇧]"
date: 2025-02-08
categories: 
  - "self-hosting-eng"
  - "smarthome-eng"
  - "tutorials"
tags: 
  - "android"
  - "dhcp"
  - "duckdns"
  - "dynamicdns"
  - "homeassistant"
  - "ios"
  - "iot"
  - "nabucasa"
  - "noip"
  - "openvpn"
  - "selfhosted"
  - "vpn"
  - "wireguard"
  - "zerotier"
image: "/images/zerotier.png"
---

[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/zerotier/)

Table of contents:
* TOC
{:toc}


In previous posts from the smart home series, I described [how to set up smart lighting in your home using _Shelly_ products](https://blog.tomaszdunia.pl/shelly-smart-oswietlenie/) and [how to set up your own server with _Home Assistant_ to manage home IoT devices](https://blog.tomaszdunia.pl/home-assistant/). This way, we created the possibility of fully remote control of the lighting in our home. But is it really "fully remote" control? Not exactly, because **the server operates only within the local network**. So when we leave home and lose _Wi-Fi_ connection on our phone, we completely lose the ability to control anything. **It is necessary to enable access to the server from outside**. There is a service called _Home Assistant Cloud_, also known as _[Nabu Casa](https://www.nabucasa.com/)_, but it is a subscription service, which (in my opinion, unnecessarily) only burdens our wallet. **An ideal alternative would be to set up a _VPN_ tunnel** (_Wireguard_, _OpenVPN_, ...) on router, which serves as the gateway to our home network. This would allow us to **securely connect from the outside to our home network using a mobile device**. However, to run such a service, **a public IP address is required**. This refers to an address that directly routes network traffic to our entry router. This should not be confused with a static IP address, which many internet service providers offer for an additional monthly fee (usually around 10 PLN). A public address can be dynamic, as this can be easily managed using any (there are many free) _Dynamic DNS_ solutions such as [_NoIP.com_](https://www.noip.com/) or [_DuckDNS.org_](https://www.duckdns.org/). So, **it doesn't matter whether the address is dynamic or static, what matters is that it is public**. I mention this because **obtaining a public IP address is very difficult or even impossible when using wireless internet**. Providers like _T-Mobile_, _Plus_, _Play_, _Orange_, and others have rather complex infrastructures that resemble a large tree with branches splitting into smaller subnets. This means that **we cannot simply open a port on the router and, using the IP address** (which we can check on sites like [_WhatIsMyIP.com_](https://www.whatismyip.com/)), access the service hosted on that port from the local network. Let me demonstrate this with my own example. My wireless internet provider is _T-Mobile_. Let's check what my IP address looks like from the outside.

![](/images/tmobileipzew.png)

Now, let's see what information I can find on my router.

![](/images/tmobileipwew.png)

The address _188.146.174.60_ does not match _10.76.187.110_, does it? This is because the latter is my internal network address, or perhaps even within a subnet of _T-Mobile_. Therefore, for external traffic to reach my device, it must first be directed to _188.146.174.60_, then pass through an unknown number of routers/switches inside _T-Mobile’s_ infrastructure, and finally, at the very end, reach _10.76.187.110_. This address is essentially my unique identifier, known only to _T-Mobile_ and me, and is handled by one of these internal routers, which acts as a _DHCP_ server.

The lack of a public IP address is a problem that most often affects owners of newly built houses that **were built on plots without fiber-optic infrastructure**. In the best case, a fiber-optic network is located on a neighboring property, and in the worst case, it may not be available for several kilometers. Regardless, getting connected to the network usually involves a long wait and a lot of effort. That’s why many people, including myself, simply opt for wireless internet as a temporary solution until fiber is installed.

**However, no problem is unsolvable**, and after this slightly lengthy introduction, I will now **explain how to access your home network from outside when you do not have a public IP address**, meaning you cannot simply set up a traditional _VPN_. To do this, I will use the **free service [_ZeroTier_](https://www.zerotier.com/)**.

## Creating an account

Go to [zerotier.com](https://www.zerotier.com/) and find the _Sign Up_ button in the top right corner. You will be redirected to the login page, but skip the _Log In_ section because we are here to create a new account. Below, you will find the _Sign Up_ button. In the form, enter your email address, type your password twice, and confirm by clicking _Sign Up_. Check your email inbox, where you should already have a message with a confirmation link—click on it. Now you can log in to your newly created account using the credentials you just set.

![](/images/2025.01.21-11_27_25.png)
    
![](/images/2025.01.21-11_27_52.png)
    
![](/images/2025.01.21-11_28_04.png)
    
![](/images/2025.01.21-11_28_47.png)
    

## Creating a virtual network

After logging in, you will see an interface with just one button: _Create A Network_. It must be said that _ZeroTier_'s design is not extravagant. I appreciate this simple look without distractions—an ideal example of prioritizing functionality over aesthetics. Click the button, and just like that, a template for your new virtual network is created. Select it from the list to enter its settings. At the top, in the text field labeled _Network ID_, you will find the network identifier, which you will need later, so make sure to save it somewhere. In my case, it is _8bd5124fd63b4288_. Before you ask—this network was created solely for this tutorial and was deleted after making this guide, so no need to attempt any attacks 🙃. Scroll down to the _Name_ field to assign your own name to the network. Also, make sure that in the _Access Control_ section, you have _Private_ selected. This setting ensures that every device attempting to connect must be authorized. Enabling the _Public_ option would mean that knowing the _Network ID_ alone would be enough to connect. This would be extremely dangerous for what we plan to use _ZeroTier_ for—allowing external traffic into our home network. The last thing to configure is the internal addressing within the virtual network. It is crucial that it does not match your home _DHCP_ server's address range. For example, if my main router at home is set to use the local network range _192.168.1.0 - 192.168.1.254_, I should not set _192.168.1.\*_ for the virtual ZeroTier network, as it would cause a conflict. In this case, you can choose an address range starting with _10_, such as _10.147.17.\*_, to ensure there are no issues.

![](/images/2025.01.21-11_29_03.png)
    
![](/images/2025.01.21-11_29_27.png)
    
![](/images/2025.01.21-11_29_52.png)
    
![](/images/2025.01.21-11_30_23.png)
    
![](/images/2025.01.21-11_31_53.png)
    

## Configuration on the Home Assistant side

At this point, we have completed everything on the _ZeroTier_ interface side, so it's time to move on to the _Home Assistant_ system. Go to _Settings -> Add-ons_. Then, click the _Add-on Store_ button. In the search bar, type "zerotier," and you should see only one result—"ZeroTier One." Install the add-on by clicking the _Install_ button. Once the installation is complete, go to the _Configuration_ tab. In the _Options_ section, click the three dots in the upper right corner and select _Edit in YAML mode_. This step is optional, but it's my preferred method. A code editor will appear, where you need to enter the following content:

```yaml
networks:
  - 8bd5124fd63b4288
api_auth_token: ""
```

This is the moment when we need the previously saved virtual network ID from _ZeroTier_. After entering the correct value, save the changes by clicking the _Save_ button. Then, go back to the _Info_ tab and click _Start_. The add-on should start correctly, but to be sure, you can check the _Logs_ tab to see if there are any error messages. Don’t worry if most of the log entries seem unreadable—just make sure there are no red warnings or the word "error" appearing.

![](/images/2025.01.21-11_56_05.png)
    
![](/images/2025.01.21-11_56_50.png)
    
![](/images/2025.01.21-11_57_12.png)
    
![](/images/2025.01.21-11_57_27.png)
    
![](/images/2025.01.21-11_58_51.png)
    
![](/images/2025.01.21-12_00_07.png)
    
![](/images/2025.01.21-12_01_44.png)
    
![](/images/2025.01.21-12_02_28.png)
    
![](/images/2025.01.21-12_02_57.png)
    
![](/images/2025.01.21-12_03_48.png)
    

## Home Assistant server authorization

Return to the _ZeroTier_ control panel and go to your network settings. In the _Members_ section, you should see the first entry. In the _Auth_ column, there will be a red icon indicating that the device has not yet been authorized to join the network. To authorize it, click the icon in the _Edit_ column. A window will open where you need to check the _Authorized_ box and enter a name for this device in the _Name_ field. Finally, click the _Save_ button. In the top right corner, a green-highlighted message _Authorized_ will appear, confirming that the device is now permitted to connect to the virtual network.

![](/images/2025.01.21-12_04_37.png)
    
![](/images/2025.01.21-12_07_10.png)
    
![](/images/2025.01.21-12_07_21.png)
    

## Connecting your phone

I have an _iPhone_, so the screenshots will show how to do this on _iOS_, but the process should be similar for _Android_. On your phone, go to the app store and search for the _ZeroTier One_ app. Install and open it. At the start, it will ask you to accept the terms and conditions, so read them carefully (😎), and if you have no objections, press _Accept_. The next step is to add a new network, which is done by tapping the plus icon in the top right corner. In the _Network ID_ field, enter the previously saved network identifier and press the _Add Network_ button. The system will ask for permission to add a new _VPN_ configuration—press _Allow_. The new network has been added. Now, you need to enable it using the toggle switch on the right side.

![](/images/IMG_6917-472x1024.png)
    
![](/images/IMG_6918-472x1024.png)
    
![](/images/IMG_6919-472x1024.png)
    
![](/images/IMG_6920-472x1024.png)
    
![](/images/IMG_6921-472x1024.png)
    
![](/images/IMG_6922-472x1024.png)
    
![](/images/IMG_6923-472x1024.png)
    
![](/images/IMG_6924-472x1024.png)
    
![](/images/IMG_6925-472x1024.png)
    

At this point, there's nothing more to do on the phone. Now, it's time to return to the _ZeroTier_ control panel and authorize the phone. This is done the same way as described earlier, so I won’t repeat it. The final result should be having two devices on the list, which are now connected through the virtual _ZeroTier_ network.

![](/images/2025.01.21-12_12_01.png)
    
![](/images/2025.01.21-12_12_26.png)
    
![](/images/2025.01.21-12_12_35.png)
    
![](/images/2025.01.21-12_12_54.png)
    

## Let's see if it works

Everything went smoothly, but does it actually work? Disconnect from Wi-Fi, open your browser, and enter _10.147.17.196:8123_ in the address bar. This address will likely be different for everyone. Essentially, it consists of the virtual network server address, which can be found in the _Managed IPs_ column, followed by a colon and port _8123_. If everything was set up correctly, you should see the _Home Assistant_ login panel, and after entering the correct username and password, you'll gain access to your home _IoT_ management panel.

![](/images/IMG_6926-472x1024.png)
    
![](/images/IMG_6927-472x1024.png)
    
![](/images/IMG_6928-472x1024.png)
    

## Home Assistant app

To achieve full convenience and satisfaction, we still need the _Home Assistant_ app on our smartphone. So, we head to the app store and type _Home Assistant_ into the search bar. We download and launch it. Right away, we see the welcome screen, where we tap the _Continue_ button. The app will ask if we allow it to scan the local network for devices. You don’t have to do this, as it can be set up manually. In the next step, we get the option to enter the server address manually – _Enter Address Manually_. We input the same address we previously entered in the browser’s address bar. In my case, it was _10.147.17.196:8123_. Then, we press the _Connect_ button. A prompt will appear, informing us that we entered a plain address without specifying a protocol, so we select _HTTP (http://)_. Finally, we go through the login screen, decide whether to enable notifications, and we’re all set. Now, we have real remote control over our smart home from our smartphone!

![](/images/IMG_6929-472x1024.png)
    
![](/images/IMG_6930-472x1024.png)
    
![](/images/IMG_6931-472x1024.png)
    
![](/images/IMG_6932-472x1024.png)
    
![](/images/IMG_6933-472x1024.png)
    
![](/images/IMG_6934-472x1024.png)
    
![](/images/IMG_6935-472x1024.png)
    
![](/images/IMG_6936-472x1024.png)
    
![](/images/IMG_6937-472x1024.png)
    
![](/images/IMG_6938-472x1024.png)
    
![](/images/IMG_6939-472x1024.png)
    

## Summary

Although the method I described above is very easy, convenient, and free, it is important to remember that it is not a perfect solution. I have a few concerns about it, the main one being that we rely on third-party infrastructure, which can never be fully trusted. _ZeroTier_ has a generally good reputation, but in reality, it means letting a third party into your home network. In emergency cases, when there is no other option, or as a temporary solution, it is acceptable. However, in the long run, I always recommend trying to obtain a truly public IP address from your internet provider and setting up a standard _VPN_ tunnel for yourself, whether using _WireGuard_ or even _OpenVPN_. This is a better solution because you set up your own _VPN_ server on a router or a server running within your local network and connect it directly with your clients, without intermediaries. It’s a bit like "if you want something done right, do it yourself."
