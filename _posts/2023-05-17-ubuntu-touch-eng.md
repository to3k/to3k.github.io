---
title: "Not only iOS and Android… Ubuntu Touch! (on Google Pixel 3a XL) [ENG 🇬🇧]"
date: 2023-05-17
categories: 
  - "tutorials"
tags: 
  - "adb"
  - "android"
  - "bonito"
  - "bootloader"
  - "chrome"
  - "chromium"
  - "customrom"
  - "fastboot"
  - "flash"
  - "google"
  - "googlepixel3a"
  - "googlepixel3axl"
  - "googleusbdriver"
  - "ios"
  - "linux"
  - "macos"
  - "microsoftedge"
  - "microsoftvisualcplusplus"
  - "minimaladbandfastboot"
  - "oemunlocking"
  - "sargo"
  - "ubports"
  - "ubuntutouch"
  - "usbdebugging"
  - "windows"
  - "xdadevelopers"
image: "/images/ubuntutouch.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/ubuntu-touch/)

Table of contents:
* TOC
{:toc}


There's no possibility to hide the fact that we have a very limited choice in the market for mobile device systems (smartphones), as we can basically choose between two systems - _iOS_ by _Apple_ or _Android_ by _Google_ (fragmented by overlays from individual manufacturers). That's the version for ordinary mortals, because there's also a **great world of _Custom ROMs_, which are variations of the _Android_ system created by enthusiasts**. For those interested in delving into the topic, I recommend the _[XDA Developers Forum](https://forum.xda-developers.com/)_, which has been reigning in this field for years. However, in this post, I would like to show something outstanding, namely the **mobile version of _Ubuntu_**, which I will install on the _Google Pixel 3a XL_ smartphone, which is already quite an old device, as its official premiere was in May 2019. Specifically for the purpose of this post, **I purchased such device for 500 PLN (~$120)**.

## Choosing the right smartphone

[The list of devices supporting _Ubuntu Touch_](https://devices.ubuntu-touch.io/) at the time of writing this post consists of 55 items, so it's not as short as it may seem. As I mentioned in the introduction, I chose the _Pixel 3a XL_. And it is precisely for this model and its smaller version, the _Pixel 3a_ (without the _XL_ in the name), that I will describe the entire procedure.

When it comes to the purchase, **it is important to choose a model that has the ability to unlock the _bootloader_** (the phone's boot program). Not all _Pixels_ have this capability, and it cannot be determined, for example, by the serial number. Unfortunately, this needs to be checked individually for each phone. In the case of online purchases, we need to ask the seller about it, and in the case of direct purchases, we need to do it ourselves after obtaining permission from the seller.

How to check this? You need to go to the phone's settings, then _About phone_, find _Build number_ at the very bottom, and tap it repeatedly until the message _You are now a developer!_ appears. This is how you unlock additional (hidden from the standard user) settings for developers.

![](/images/deweloper1.png)

![](/images/deweloper2.png)

Now we return to the main settings window and go to _System_ and then _Developer options_, which we have just unlocked. Here we need to enable two options:

1. **_OEM unlocking_** (_Allow the bootloader to be unlocked_) - as the hint suggests, this option allows unlocking the _bootloader_ of this device.

3. **_USB debugging_** (_Debug mode when USB is connected_) - USB debugging mode, which allows manipulating the device via USB, in other words, it enables the interaction with the device from a computer to which we will later connect the _Pixel_ and install a new system along with all the necessary components.

**Phones that have the bootloader unlocking option disabled will have the first option (_OEM unlocking_) grayed out, meaning it's unavailable**. This is how you can identify a phone that should not be purchased.

If a prompt appears regarding whether to allow USB debugging (_Allow USB debugging?_), select the option _Always allow from this computer_ and click _Allow_.

![](/images/allowusbdebug2.png)

Before proceeding with further actions, I suggest doing two things:

1. Restart your phone,

3. Charge it fully.

While the phone is charging, let's prepare the computer accordingly.

## Preparing the computer for bootloader unlocking

Before starting the process of unlocking the _bootloader_ and _flashing_ (installing) a new system, we need to prepare the computer that will be used for these actions. I chose my special-purpose laptop (a rugged _Getac S410_) running on _Windows_, but there's nothing stopping you from doing the same on a computer with _Linux_ or even _macOS_. Just keep in mind that some steps may vary slightly, but the general idea remains the same, and you will achieve the same result. It's also important to have a reliable and functioning USB cable that allows data transfer, not just charging (yes, such cables are available on the market in case someone hasn't come across them). Additionally, it is recommended to perform risky actions like installing a system on another device using a laptop. Why? It's simple. In case of a power outage, the laptop will switch to battery power instead of losing power and bricking your phone.

On a Windows computer, we basically need to perform four actions:

1. install (if not already installed) _Microsoft Visual C++_, which can be downloaded from the [Microsoft website](https://www.microsoft.com/en-us/download/details.aspx?id=52685) (this is the 2015 version, but I read somewhere that it is also recommended to install the 2012 version available [here](https://www.microsoft.com/en-us/download/details.aspx?id=30679)),

3. install _Minimal ADB and Fastboot_, for which you can always find the current link in [this thread on the XDA Developers forum](https://forum.xda-developers.com/t/tool-minimal-adb-and-fastboot-2-9-18.2317790/),

5. install the _UBports_ installer, which is available at [this link](https://devices.ubuntu-touch.io/device/sargo#installerDownload),

7. install the _Google USB Driver_, which is available at [this link](https://developer.android.com/studio/run/win-usb).

While steps 1-3 shouldn't be a problem for anyone, I would like to focus for a moment on the action indicated in step 4. Under the provided link, there is a .ZIP package (archive) that needs to be unpacked in any location. Then, connect your phone to the computer and open the _Notification Center_ on your phone (swipe down from the top edge of the device). Find the option _Charging this device via USB_ (_Tap for more options_) and tap on it. This is the _USB Preferences_ setting that allows you to change how the phone communicates with the computer. By default, the option allowing only charging the phone without data transfer (_No data transfer_) is selected. However, we want to change it to (_Use USB for_) _File transfer / Android Auto_. This way, we enable data transfer between both devices, and the phone will appear on our computer as an external drive.

![](/images/usbprefs1.png)

![](/images/usbprefs2.png)

On the computer, we go to the _Start Menu_ and then _Device Manager_. A list of all devices connected to or present in our computer will be displayed. If we haven't previously installed the _Google USB Driver_, there should be one entry on this list with a yellow triangle icon, with exclamation mark and labeled as _Android_, _Pixel 3a_, or something similar. When you see this, you will know what it refers to. For clarification, it will probably be in the _Other devices_ section. Right-click on this device and select _Update driver_ from the context menu. This will open a window where we choose the second option, which is _Browse my computer for drivers_. Then select _Let me pick from a list of available drivers on my computer_, click _Next_, and when you're in the window asking _Select the device driver you want to install for this hardware_, use the _Have Disk..._ button. Another window will appear where we need to find the _Browse..._ button, click on it, and locate the _android\_winsub.inf_ file from the downloaded and extracted _Google USB Driver_ package. Proceed by clicking _Open_, _OK_, _Next_, _Yes_, _Install_, and after successful installation, finish by clicking _Close_. After all this, the device that previously had a yellow triangle with an exclamation mark should no longer have it and should be recognized as a normal device with the correct drivers installed.

If someone needs a visual guide for the above steps, I recommend watching [this video by a (presumably) Hindu gentleman](https://yewtu.be/watch?v=ajdcWIY-5yo).

## Unlocking the bootloader

_Leave the Pixel_ still connected to the computer. On the computer, launch the previously installed _Minimal ADB and Fastboot_ program, which should open a command prompt window. Start by checking if our phone is properly connected, configured, and visible to the _bootloader_ unlocking tool:

```bash
adb devices
```

When you first enter this command under _List of devices attached_, you may see a message with a device identifier (serial number) and the phrase _unauthorized_ next to it, which means you need to give permission for USB debugging on your phone again. Repeat the above command, and this time you should see the phrase _device_ next to the device identifier. This confirms that everything has been done correctly up to this point.

The next command will trigger the phone to enter _Bootloader_ mode:

```bash
adb reboot bootloader
```

On the phone, something similar to what is visible in the photo below should appear:

![](/images/IMG_1809.jpeg)

As you can see, we have entered the _Bootloader_, but the _Device state_ is displayed as _locked_. Our goal is to change this state to _unlocked_. We go back to the command line on the computer and this time we enter:

```bash
fastboot flashing unlock
```

We switch to the phone, where we need to confirm that the _bootloader_ should be unlocked. To do this, press any volume button once (in this mode, they are used to switch between options we want to select) until the _Unlock the bootloader_ option is selected, and confirm the selection with the _Power_ button.

![](/images/IMG_1811-scaled.jpeg)

After a short while, we will return to the main bootloader menu, where we should see "Device state: unlocked." Success! The bootloader is unlocked, and the device is now open before us.

![](/images/IMG_1812.jpeg)

Finally, it is good to properly end the operation of the _Minimal ADB and Fastboot_ tool by issuing the command:

```bash
adb kill-server
```

and then close the command prompt window.

## Restoring the required Android system version

In the [UBports documentation](https://devices.ubuntu-touch.io/device/sargo/), you can read that in order to install Ubuntu Touch, it is necessary to revert the Android operating system version on our device to a specific release. At the time of writing this guide, the designated release is _PQ3B.190801.002_. I mention this because I do not know how much time has passed since this guide was written until you are using it, and it is possible that newer versions of _Ubuntu Touch_ will require a different version of _Android_ for installation. That is why I always recommend going [here](https://devices.ubuntu-touch.io/device/sargo/) and checking this information just before proceeding with further steps. The so-called code names are also important, and they are different for each Pixel model:

- for _Google Pixel 3a_, it is **_SARGO_**,

- for _Google Pixel 3a XL_, it is **_BONITO_**.

This is important later on, and knowing these names will help avoid confusion between system images and taking an image for the wrong model, which can essentially cripple the phone in the worst case. I will be working with _Bonito_ since I have a _Pixel 3a XL_, but the same steps can be performed for the _Pixel 3a_ using the image labeled _Sargo_.

_Flashing_ the system onto _Pixel_ devices is done using the _Chrome_ browser. Well... it's a phone from _Google_, so they made it so their browser is necessary. Clever, right? Maybe, but we're even more clever because not many people may know that you don't actually need the specific _Chrome_ browser, but any browser based on the _Chromium_ engine, which means we can just as well use _Microsoft Edge_! We'll use it to take a step towards removing the _Google_ system from the phone, so we're totally outsmarting the corporation 😉

We launch the _Microsoft Edge_ browser, go to the website [https://developers.google.com/android/images?hl=en#bonito](https://developers.google.com/android/images?hl=en#bonito), scroll to the bottom where we see the blue _Confirm_ button next to _I have read and agree to the above terms and conditions_, and click it. We will be taken to a list of factory images for _Nexus_ and _Pixel_ smartphones. As mentioned before, we are looking for the release labeled _PQ3B.190801.002_, making sure it is an image dedicated to our device.

![](/images/googleflash1-1024x473.png)

After finding the appropriate image, we click _Flash_ which is next to. We will be taken to a web-based _Android_ system flashing tool. This time, I won't describe the process in detail because what needs to be done step by step is perfectly visible in the screenshots below.

![](/images/aft1.png)
    
![](/images/aft2.png)
    
![](/images/aft3.png)
    
![](/images/aft4.png)
    
![](/images/aft5.png)
    
![](/images/aft6.png)
    
![](/images/aft7.png)
    
![](/images/aft8.png)
    
![](/images/aft9.png)
    
![](/images/aft10.png)
    
![](/images/aft11.png)
    
![](/images/aft12.png)
    
![](/images/aft13-1024x549.png)
    

The result will be restoring the _Android 9_ system on our _Pixel_. The phone has also been wiped clean, so we need to go through the basic configuration again, where I suggest skipping most options and simply using the _Skip_ button. It's not even worth configuring the Wi-Fi because the phone will be wiped again after installing the target system (_Ubuntu Touch_). The only thing that matters after the basic system configuration is to go to the settings, re-enable developer options, and check if USB debugging is enabled. If it's not, we obviously enable it and allow USB debugging from our laptop (as I described earlier).

## Flashing Ubuntu Touch

We will flash _Ubuntu Touch_ using the previously installed _UBports_ installer. Just like before, I have shown the entire process in the screenshots below.

![](/images/ubp1.png)
    
![](/images/ubp2.png)
    
![](/images/ubp3.png)
    
![](/images/ubp4.png)
    
![](/images/ubp5.png)
    
![](/images/ubp6.png)
    
![](/images/ubp7.png)
    
![](/images/ubp8.png)
    
![](/images/ubp9.png)
    
![](/images/ubp10.png)
    

## Ubuntu Touch - first impressions

![](/images/IMG_1816-scaled.jpeg)

![](/images/IMG_1817-scaled.jpeg)

![](/images/IMG_1818-scaled.jpeg)

The initiative that is the _Ubuntu Touch_ project is very, and I mean very, significant, worthy of respect, and deserving of support. It is clearly an attempt to give people freedom in choosing an operating system that won't spy on them at every step. Moreover, it is open and completely free. The system is quite well adapted to the size of the devices on which it is intended to run, and it is evident that the authors prioritized ensuring that all basic phone functionalities work. I have here working basics like Wi-Fi or cellular data transmission, but also details such as a fingerprint reader.

![](/images/ubuntutouchpixel.png)

However, the aforementioned basics are not everything. The worst part about using _Ubuntu Touch_ is the absolute lack of applications. Unfortunately, there are dramatically few items in the "store" of applications, as can be seen in the screenshots below. I played the role of a pharmacist and counted all of them - at the time of writing this post, there are 184 items...

![](/images/ubuntustore1.png)

![](/images/ubuntustore2.png)

Can _Ubuntu Touch_ installed on the _Google Pixel 3a XL_ smartphone be used as a daily device? In my opinion, unfortunately not. However, it is definitely a very interesting topic and I recommend everyone to give it a try. I dream that this project will be taken much further than where it currently stands. I will definitely continue to observe it.
