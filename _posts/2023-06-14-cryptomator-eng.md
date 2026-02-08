---
title: "Cryptomator - vault in cloud [ENG 🇬🇧]"
date: 2023-06-14
categories: 
  - "tutorials"
tags: 
  - "android"
  - "backblaze"
  - "cloud"
  - "container"
  - "cryptomator"
  - "dropbox"
  - "googledrive"
  - "icloud"
  - "ios"
  - "linux"
  - "macos"
  - "mega"
  - "nextcloud"
  - "onedrive"
  - "safe"
  - "vault"
  - "windows"
image: "/images/cryptomator.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/cryptomator/)

Table of contents:
* TOC
{:toc}


[In my previous post, I wrote about _Nextcloud_](https://blog.tomaszdunia.pl/nextcloud-eng/), which is a way to run your own network drive, commonly referred to as a cloud for files. But what if we run such a service on a server that is not located in our home, i.e., **we don't have full control over who can access it**? Or what if we still want to **entrust our data** to services like _Dropbox_? Can we secure our data in such situations? **Of course, we can**, and one of the most interesting ways is a free tool called _[Cryptomator](https://cryptomator.org/)_.

The principle of operation of this tool is **amazingly simple, yet brilliant**. It's a typical case where beauty lies in simplicity. _Cryptomator_ allows you to create a kind of **encrypted container** (a safe or a vault), whose content is only accessible after entering a password. We place such a container on a network drive, which is synchronized between all connected devices. Then, on the end devices, the container is decrypted through the _Cryptomator_ application and shared as an additional network drive. In practice, after proper initial configuration, **the security level is dramatically increased**, and **the convenience of use is not disrupted in any way**.

## Installation and Configuration

Let's start with [downloading the application](https://cryptomator.org/downloads/) suitable for our system. I believe that everyone will manage to install it. After launching _Cryptomator_, we immediately start the process of adding a container by using the _\+ Add Vault_ button.

![](/images/IMG_0075.jpg)

In the pop-up window, we have two options to choose from:

- _**Create New Vault**_ - creating a new container and this is the option we will use,

- **_Open Existing Vault_** - opening (adding to this device, e.g. after reinstalling the application) a container that was previously created.

![](/images/IMG_0076.jpg)

In the next window, **we enter a working name** for the container being created and proceed by clicking the _Next_ button.

![](/images/IMG_0077.jpg)

It's time to **indicate where this container should be located**. As you can see in the screenshot below, we have immediately available options such as _iCloud_, _Dropbox_, _Google Drive_, or _OneDrive_. At the end, there is also an option to manually specify a location on the local disk, which can also be a shared folder with any other cloud service (e.g. our Nextcloud network drive). After correctly specifying the location, click the _Next_ button.

![](/images/IMG_0078.jpg)

At this step, we set the most important aspect, which is the **password**. I think I don't need to explain why it should be strong, i.e., consisting of as many characters as possible (preferably lowercase and uppercase letters, numbers, and special characters). After entering the chosen character string twice, we still have to decide whether we want a special recovery code to be generated, which can be used in case of forgetting the password. I recommend generating such code and keeping it in a safe place.

![](/images/IMG_0079.jpg)

The _Create Vault_ button completes the container creation process, but at the end, we will still receive a window with the generated recovery code, which should be kept safe.

![](/images/IMG_0080.jpg)

Done, the container has been created. We get a window informing us about this and the option to unlock it immediately (the _Unlock Now_ button) or just proceed (the _Done_ button). At this point, I suggest using the latter.

![](/images/IMG_0081.jpg)

We return to the main _Cryptomator_ window, where the new container is already listed. Let's select it and go to its settings (_Vault Options_).

![](/images/IMG_0082.png)

In the first _General_ tab, we can enable the option to unlock the vault when the _Cryptomator_ application starts, which I recommend for convenience. Then we have a choice of what should happen in such a case, whether it should be shown as a new file manager window, ask each time what to do, or simply be opened in the background and do nothing more. I always use the latter option. In the next _Mounting_ tab, as the name suggests, we have settings related to mounting the container, i.e. the ability to change the name under which it should appear in our disk tree, whether it should be read-only (sometimes this is a useful feature), we don't deal with flags because it's a more advanced operation, and finally, we have the ability to edit the location where it should be mounted. The last tab is _Password_, where we can change the password and view existing or generate a new recovery code.

![](/images/IMG_0086.png)
    
![](/images/IMG_0087.png)
    
![](/images/IMG_0088.png)
    

Let's go back to the main window and this time click on the _Unlock_ button. When you open it for the first time, you will be asked to enter a password, which you can save in the application memory by checking the _Save Password_ option below. Everything depends on the usage, but if you want to have protection only from the outside and prioritize convenience on your own computer, then selecting this option is justified. With this configuration, you can set _Cryptomator_ to start up with the operating system, and along with it, the vault will be unlocked and immediately connected as a network drive, without the user's involvement, ready to be used.

![](/images/IMG_0083.png)
    
![](/images/IMG_0084.png)
    

## Mobile devices

_Cryptomator_ is also available as a mobile application. Instructions for installation and configuration are available for _[Android](https://docs.cryptomator.org/en/latest/android/setup/)_ and _[iOS](https://docs.cryptomator.org/en/latest/ios/setup/)_ devices, following the same steps as above.

## What it looks like from the cloud

As I mentioned before, from our device, the vault will appear as a normal network drive or even as a regular folder on our local drive, which synchronizes with a standard cloud solution. However, I believe it is also worth showing how the container files look like from the perspective of the cloud. For example, I took a screenshot from Dropbox.

![](/images/cryptomatordropbox.png)

As you can see, the encrypted content stored on an external drive is actually a folder with many strangely named subfolders (unreadable), containing all the files saved inside the vault, an informational document in RTF format (short for Rich Text File, which is similar to a DOCX file), the encrypted _masterkey.cryptomator_ key and its backup. That's it. For someone who doesn't have _Cryptomator_ and the password to decrypt it, these files seem like complete gibberish, and that's the point of it all.
