---
title: "DWService - remote desktop via browser [ENG 🇬🇧]"
date: 2023-06-28
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "2fa"
  - "agent"
  - "anydesk"
  - "authy"
  - "cli"
  - "client"
  - "dwservice"
  - "remotedesktop"
  - "server"
  - "teamviewer"
  - "totp"
  - "vnc"
  - "xwayland"
image: "/images/dwservice.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/dwservice/)

Table of contents:
* TOC
{:toc}


I assume that the phrase _**remote desktop**_ is familiar to anyone. It is a very convenient way to access (control) a computer operating in another part of the world or simply a server operating without peripherals attached. When hearing the term _remote desktop_, many even non-technical people will surely think of _TeamViewer_ or _AnyDesk_, but the king in this area is the _[VNC](https://en.wikipedia.org/wiki/Virtual_Network_Computing)_ protocol (short for _Virtual Network Computing_). There are many programs that operate based on _VNC_ (_RealVNC_, _TightVNC_, _UltraVNC_, _TigerVNC_, _Vinagre_, ... and many others), and the vast majority of them rely on the need to install two applications - one on the server (the computer we will control) and the other on the client (the computer we will control from). Such tools are a basic working tool for any network administrator consisting of more than one computer, so every beginner starting their adventure as a Sysadmin (system administrator) should at least know what it is.

In this post, I would like to point out one service that, in my opinion, stands out from the crowd by the fact that, firstly, it works through a web browser, secondly, it is free in its basic range (and even paid plans are attractive in terms of price), and thirdly, the source code of the client is available as open-source software. This tool is [_DWService.net_](https://www.dwservice.net/)!

## How is it possible through a web browser?

As I mentioned earlier, what distinguishes _DWService_ from the competition is the interface that works through any ordinary web browser. Of course, there is a need to install a special _agent_ (_client_) on the computer/server that we will control, but the actual control from another device is done entirely using the web interface, without the need to install any additional software.

Below are a few screenshots showing what it looks like for one of my servers:

![](/images/dwservice1-1024x503.png)
    
![](/images/dwservice2-1024x503.png)
    
![](/images/dwservice3-1024x503.png)
    
![](/images/dwservice4-1024x503.png)
    
![](/images/dwservice5-1024x503.png)
    

## Account registration and creating an agent

Let's start with [creating an account on _DWService_](https://www.dwservice.net/en/loginsignup.html). After signing up and logging in to the account, we select the _Groups_ button from the menu and find the _+_ button labeled _New_ on the top bar. A simple wizard will appear, in which we only need to enter any name for our first group in the _Name_ field (it could be, for example, _Servers_). We return to the main menu and this time we choose the _Agents_ button, where we also find the _+_ button labeled _New_. In this equally simple wizard, we choose the previously created group and enter a name for the _agent_ that we will install shortly. After creating a new _agent_, it will appear on the list with a 9-digit code on a yellow background. This code is the so-called _Installation Code_ and we will need it during installation, so I recommend saving it somewhere.

## Consider enabling 2FA

I recommend securing your account with _TOTP_ (_Time-based One-Time Password algorithm_), which is one of the forms of _two-factor authentication_. This security measure, which requires an additional one-time code in addition to the login and password when logging in, is used by me wherever possible. I use the [Authy](https://authy.com/) application, available on both Android and iOS, to implement this solution. _TOTP_ can be enabled in the _My Account_ tab.

## Agent installation

The installation can be done both using a graphical interface and from the terminal. Let's start by downloading the _agent_ installation script. If you are using a graphical interface, simply go to the website [_https://www.dwservice.net/pl/download.html_](https://www.dwservice.net/pl/download.html) and download the installer for your system. For installation via the _CLI_, first navigate to the appropriate folder:

```bash
cd /usr/src
```

Next, download the installation script using _wget_:

```
wget https://www.dwservice.net/download/dwagent.sh
```

We still need to give the downloaded script permission to run:

```bash
chmod +x dwagent.sh
```

It's time to run the script. From now on, all actions will be practically identical for the graphical and _CLI_ installation variants.

```bash
./dwagent.sh
```

First, we will be asked what action we want to perform. We have the following options:

- **_Install_** - standard installation,

- **_Run_** - one-time run,

- **_I do not accept_** - this option is for those who have read the license agreement, terms of use, and privacy policy, do not agree with them, and want to opt-out.

We choose _Install_, so we type _1_ on the keyboard and continue with _ENTER_.

```bash
1. Install
2. Run
3. I do not accept
Option (3): 1
```

Next, we will be asked to specify the path where the _agent_ should be installed. The default suggested path is _/usr/share/dwagent_, which is fine for us, so we don't change anything and confirm with _ENTER_. Then we will be asked to confirm this choice, so we type _1_ on the keyboard and continue with _ENTER_.

```bash
Select the installation path:
Path (/usr/share/dwagent): [ENTER]
Waiting…
Would you want install DWAgent to '/usr/share/dwagent'?
1. Yes
2. No
Option (2): 1
```

The last step is to indicate how we want to configure the _agent_, we choose option _1_, which means that we want to use the previously generated code (_Installation Code_, which was mentioned in the previous chapter), and confirm with _ENTER_. Then we will be asked to enter this code, so we type it in (including dashes in the appropriate places), which we also confirm with _ENTER_ at the end.

```bash
How would you like to configure the agent?
1. Enter the installation code
2. Creating a new agent
Option (1): 1
Waiting…
Enter the installation code
Code: [enter the code from the website]
```

Done. The _agent_ should now be properly installed, and after refreshing the web interface, we should see green instead of yellow background. Clicking on this _agent_ will take us to the management panel, which I showed in the screenshots above in this post.

Finally, I also recommend cleaning up after installation, which means removing the downloaded installation script, which we will no longer need at this stage:

```bash
rm /usr/src/dwagent.sh
```

## Known problem with XWaylands

For some users, attempting to access a remote computer's screen may result in an error message:

> Error: XWayland is not supported.

This is a known problem resulting from the fact that, as the message states, _DWService_ does not work with _XWayland_. It can be easily resolved by disabling _XWayland_ on the server, and interestingly, this can be done directly from the _DWService_ interface.

Let's go back to the main _agent_ management menu and click on the _Files and folders_ button. This is nothing more than a file manager where we navigate to the _/etc/gdm3/_ folder. In this folder, we need to find a file named _custom.conf_ or _daemon.conf_. Open it in a text editor. Now we need to find a line that looks like this:

> #WaylandEnable=false

and remove the _#_ character from the beginning of the line (uncomment this command). After that, save the file and close it. This way we have disabled _XWayland_.

A quick restart of the machine can be done from the console by using the _reboot_ command or from the _DWService_ _Agents_ list by clicking on the three vertical dots and selecting the _Restart system_ option.

## Consider supporting the project

_DWService_ is a really useful tool and offers access to a free plan, which is definitely enough for basic users since the plans differ mainly in the maximum connection bandwidth. The free plan offers 6 Mbps, which is sufficient for streaming the computer's screen. However, there are paid plans, which are justified by the desire to support the project. I did it myself and to prove it, you can find me on the subscribers list available [here](https://www.dwservice.net/pl/contribute-subscriptions.html) (if you want to check me, look for _tomaszdunia.pl_ 😉).
