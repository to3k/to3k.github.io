---
title: "WSL - Ubuntu on Windows [ENG 🇬🇧]"
date: 2023-08-09
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "amd"
  - "bios"
  - "intel"
  - "intelvirtualizationtechnology"
  - "microsoft"
  - "microsoftstore"
  - "microsoftvisualcplusplus"
  - "powershell"
  - "ubuntu"
  - "uefi"
  - "windows"
  - "wsl"
coverImage: "/images/winbuntu.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/wsl-ubuntu-windows/)

I have written quite a bit about setting up various types of home servers. I talked about _Raspberry Pi_ as well as slightly more powerful _terminals_. But does everyone need a server in the form of a separate machine? What if someone wants to start learning and/or check if it's even for him/her, while at the same time minimize costs? It turns out that **all you need is any laptop with _Windows_** _10_ (or _11_), on which **you can easily install a virtual Linux environment**, specifically Ubuntu, and have the equivalent of a server, but running on your computer. We're not talking about installing a second system or replacing Windows with Linux. In this post, I will show you how to run Linux as a subsystem inside Windows. Of course, this is not a solution that will create a server running 24/7 (unless your computer is always on), but rather a simulation of a server that will only run when you need it.

## Preparing your computer

To install _Ubuntu_ inside the Windows operating system, we first need to enable virtualization in the _BIOS_. To access the _BIOS_/_UEFI_, follow these steps: _Start menu_ -> _Change advanced startup settings_ -> _Recovery_ tab -> _Advanced startup_ -> _Restart now_ button -> _Troubleshoot_ -> _Advanced options_ -> _UEFI Firmware Settings_ -> _Restart_ button.

Unfortunately, from here on, it's a bit more difficult for me to provide the correct path, as there are as many different arrangements of settings in _BIOS_/_UEFI_ as there are computers. Similarly, I can say that for computers with _Intel_ processors, we are looking for an option called _Intel(R) Virtualization Technology_, which needs to be turned on (set to _Enabled_), but I don't know what the equivalent for AMD devices will be called. It seems that everyone will have to google this for themselves.

![](/images/winubu1-scaled.jpg)

In addition to enabling virtualization, we also need to install [Microsoft Visual C++](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B), which is an essential component. Simply download the installation file from [this page](https://learn.microsoft.com/pl-pl/cpp/windows/latest-supported-vc-redist?view=msvc-170) and install it.

## Ubuntu environment installation

We access the _PowerShell_, which is the Windows terminal. It is important to run it as an administrator.

![](/images/winubu2.png)

We install _WSL_ (short for _Windows Subsystem for Linux_), using the command:

```powershell
wsl --install
```

![](/images/winubu3.png)

After successfully completing the installation, it is necessary to restart the computer. After restarting the system, we go to the _Microsoft Store_, type _Ubuntu_ in the search box, and go to the application page from which we can install and run the _Ubuntu_ environment. After installation, it is also available normally from the _Start menu_ or if we have created the appropriate icon on the desktop. In the _Microsoft Store_, we also have the option to install a specific version of _Ubuntu_, such as 22.04 LTS or 20.04 LTS, which is giving us a choice in case we want that particular version and not another one.

![](/images/winubu4.png)

After clicking on the _Open_ button, a terminal window will be launched, in which the main installation will begin. During the process, we will need to provide a username and password twice. After successfully completing the entire process, we will have access to a shell that is no different from an _Ubuntu_ system running, for example, on a _Raspberry Pi_.

![](/images/winubu5.png)

## Summary

I don't think there is anyone who would say it wasn't easy. _WSL_ is a very interesting creation that has opened up the Windows environment to distributions under the sign of the penguin. However, _WSL_ also has its drawbacks and is rather a solution for occasional use or for use as a test environment. If you are serious about _self-hosting_, the best solution is still to dedicate a separate machine to it.
