---
title: "Nextcloud - private cloud for files [ENG 🇬🇧]"
date: 2023-06-07
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "2fa"
  - "backblaze"
  - "cloud"
  - "docker"
  - "dockercompose"
  - "dropbox"
  - "googledrive"
  - "icloud"
  - "mariadb"
  - "mega"
  - "mysql"
  - "nextcloud"
  - "onedrive"
  - "opensource"
  - "pgid"
  - "port443"
  - "port80"
  - "postgresql"
  - "puid"
  - "selfhosted"
  - "sqlite"
  - "totp"
  - "yaml"
  - "yunohost"
coverImage: "/images/nextcloud.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/nextcloud/)

[Dropbox](https://www.dropbox.com/plans), [OneDrive](https://www.microsoft.com/pl-pl/microsoft-365/onedrive/compare-onedrive-plans?activetab=tab%3aprimaryr1), [Google Drive](https://one.google.com/about/plans?hl=pl), [iCloud](https://support.apple.com/pl-pl/HT201238), [MEGA](https://mega.io/pl/pricing), [Backblaze](https://www.backblaze.com/b2/cloud-storage-pricing.html) are probably the most popular solutions for storing files in the [so-called](https://blog.tomaszdunia.pl/wp-content/uploads/2023/05/nocloudbutsomeonescomputer.jpg) cloud. It must be admitted that this form of aggregation and access to one's data is **very convenient** and also serves as a kind of backup. All of the mentioned services offer more or less disk space in free packages, but to store larger amounts of data, we need to consider purchasing one of the paid plans, **which may not be cost-effective**, especially when dealing with a large number of photos. Another, crucial **disadvantage of such a solution is the necessity to entrust our data to third parties**, or even worse, corporations. So what can we do? **Launch our own "cloud" for data**, and the best solution for this is _**[Nextcloud](https://nextcloud.com/)**_! It is a tool that is now described as a collaboration platform because it consists of not one, but many tools. As a few examples, we can list:

- **_Files_** - network drive,

- **_Photos_** - photo gallery,

- **_Talk_** - video/audio chat,

- **_Groupware_** - calendar organization, contacts, and mail,

- **_Office_** - office suite.

However, it all started with _Nextcloud_ being simply an **open-source** software designed to run on your own network-attached storage server.

In this post, I will show you how to run such a platform for yourself. I will offer two options:

1. [running it on a server with _YunoHost_](#yunohost),

3. [running it on any other server using _Docker_](#docker).

## Running it on YunoHost

The installation process will be similar to the one described in my [post about _WriteFreely_](https://blog.tomaszdunia.pl/yunohost-writefreely-eng/), but in the case of running _NC_, we don't need a separate domain. In fact, if you're only running it for yourself, creating a special domain isn't recommended because, firstly, it's just an additional cost, and secondly, it's better not to reveal all your cards and thus expose your data by using a subdomain like _nextcloud.tomaszdunia.pl_, which would clearly indicate that all our data is located at that address. I generally prefer to keep such services in the local network, which can only be accessed through a _VPN_ such as _WireGuard_, but that's a topic for a completely different post.

We start by logging into our _YunoHost_ administrator panel and immediately go to _Applications_. Then, in the top right corner, click the green _\+ Install_ button, search for the _Nextcloud_ application and select it from the list. Scroll down to the _Installation settings_ section and start configuring:

![](/images/nc1.png)

1. In the text field named _Label for Nextcloud_ \[1\], enter the name under which you want to see this application in the list of applications in your _YunoHost_.

3. From the dropdown list below \[2\], choose on which domain you want to install _NC_. As you can see, I chose the main domain on which my _YunoHost_ is running. You can do the same or choose a different domain from the list.

5. In the next text field \[3\], define the exact path under which _NC_ should be installed. By providing the value (as default) of _/nextcloud_, _NC_ will be installed at _example.domain.com/nextcloud_, where of course _example.domain.com_ is the domain you selected above. If you have decided to attach a domain dedicated only to _NC_, you can only enter _/_ here, which will mean installing _NC_ in the parent directory of the domain.

7. The next dropdown list \[4\] is used to indicate which _YunoHost_ user should be the administrator for this application, and thus its first user.

9. Next, we have two decision fields, the first of which \[5\] is the question _Should this application be made available to anonymous users?_. Here, I suggest choosing _Yes_, as otherwise _Nextcloud_ clients (referring to _Nextcloud Desktop_, which is used to access _NC_ on end-user devices) will not work, as an additional authentication step will appear, requiring logging into _YunoHost_, which is not provided for.

11. The second dropdown \[6\] is the question of whether we want to give _Nextcloud_ access to the _/home_ folder on our server. Personally, I don't see the need for this, and it's definitely a risky business, because if you choose _Yes_, _NC_ will gain access to other applications running on _YunoHost_. Everyone will decide for themselves, as everything depends on the specific application. However, I leave the _No_ option selected.

13. We confirm the above settings with the _Install_ button \[7\], and thus start the installation process, which unfortunately is not the shortest, so you need to be patient.

After the installation is complete, we will be redirected to the _YunoHost_ applications list, where _Nextcloud_ will appear as a new item. To access _NC_, we can select it from the list and use the _Open this application_ button or simply enter the path defined during the above configuration into the browser's address bar.

## Running as a Docker container

Don't have a _YunoHost_ server? No problem! You can do the same thing using _Docker_! I recommend first reading my post on [Docker - one server, many services](https://blog.tomaszdunia.pl/docker-eng/).

We start by creating a directory for this container:

```bash
mkdir -p /home/$USER/docker/nextcloud
```

Next, we create a configuration file for this container:

```bash
nano /home/$USER/docker/nextcloud/docker-compose.yml
```

_Nextcloud_ as a _Docker_ container can be configured in many different ways, especially with regard to the database that we choose for it. We can choose, for example, MySQL/MariaDB or PostgreSQL. However, the default solution is to use SQLite, which we will use in this post, as it significantly simplifies the configuration process and is perfect for this guide, which aims to show only the basic configuration of _Nextcloud_, without going into details. In this case, the _docker\_compose.yml_ configuration file created by us should be filled with the following content:

```yaml
version: "3"

services:
  nextcloud:
    container_name: nextcloud
    image: nextcloud:latest
    ports:
      - "80:80"
      - "443:443"
    environment:
      PUID: '1000'
      PGID: '1000'
      TZ: 'Europe/Warsaw'
    volumes:
      - '/home/$USER/docker/nextcloud/volumes/var/www/html:/var/www/html'
    restart: unless-stopped
```

In the above code, the only new elements can be the _environment variables_ _PUID_ and _PGID_. These variables inform the container how to write its data, specifically, who to set as the owner of these files. _PUID_ corresponds to the user identifier, and _PGID_ corresponds to the group identifier to which this user belongs, and to which other users who are to have access to these files may also belong. These identifiers for your user can be set using the command:

```bash
id $USER
```

In response, you will get something similar to:

```bash
uid=1000(dockeruser) gid=1000(dockergroup) groups=1000(dockergroup)
```

The value given as _uid_ and _gid_ is exactly what should be entered in the _docker\_compose.yml_ configuration file as _PUID_ and _PGID_, respectively. We can now save the constructed configuration file and exit from it.

At this point, we still need to create the appropriate _volume_ that we declared as the place to store the container's data:

```bash
mkdir -p /home/$USER/docker/nextcloud/volumes/var/www/html
```

Let's also check whether the ports for handling this container are open in our _firewall_:

```bash
sudo ufw allow 80
sudo ufw allow 443
```

Finally, all that remains is to compile and run the _Nextcloud_ container:

```bash
docker-compose -f /home/$USER/docker/nextcloud/docker-compose.yml up -d
```

You can additionally verify the correct operation of the container using the command:

```bash
docker ps
```

If everything is okay, we can now go to the browser and enter the IP address of our server under which the freshly launched Nextcloud should be running. On the welcome page, we still need to complete the configuration by creating an administrator account and choosing the database type as SQLite. We confirm everything with the _Install_ button and we're done.

## Results of the work

After following any of the above instructions, the resulting welcome screen should look like this (or similar):

![](/images/nc3.png)

As you can see at first glance, Nextcloud is a very user-friendly, clean, and intuitive interface. I won't go into detail about the capabilities of this environment here, but I recommend going to the application installation and management tool (the user icon in the upper right corner \[1\] and select _Apps_ from the list \[2\]). Please note how many possibilities are now available in the Nextcloud library!

What I always do after the first launch of _Nextcloud_ is go to the _Files_ tool \[3\] and clear everything inside. However, these are demo materials showing basic functionalities that may be useful to new users, so I recommend checking them out. Then of course you can delete them and plan your disk space your own way.

It is also important not to forget to enable two-factor authentication during login. A clear instruction on how to do this can be found in the [_Nextcloud_ documentation](https://docs.nextcloud.com/server/latest/user_manual/en/user_2fa.html), so I won't repeat that information here.

## Nextcloud Applications - Connecting Devices

Dedicated _Nextcloud_ applications are available for _Windows_, _Linux_, _macOS_, _Android_, and _iOS_. All of them can be accessed through [this link](https://nextcloud.com/install/). Installation on each system is identical, so I will demonstrate the entire process on _macOS_. After installing the appropriate application, we launch it and on start-up, we are presented with a window where we select the _Log in to Nextcloud_ button. In the next window, we are asked to enter the server address, so we provide it and confirm with the _Next >_ button.

![](/images/nc1.webp)
    
![](/images/nc2.webp)
    

We will be redirected to the browser, where we need to authenticate the new client.

![](/images/nc3-1.webp)
    
![](/images/nc4.webp)
    
![](/images/nc5.webp)
    

Finally, we return to the freshly installed _Nextcloud_ application, where we still need to perform the basic client configuration. We provide the folder in the local computer memory to which _Nextcloud_ should be connected. The rest can be changed according to ones preferences. Finally, we confirm by clicking the _Connect_ button and that's it. This configured client will update our files in real time, which means that when we modify, add, or delete a file on any device, these changes will be reflected on the server in a moment, and then on other connected devices.

![](/images/nc6.webp)
