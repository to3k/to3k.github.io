---
title: "Portainer - GUI for Docker [ENG 🇬🇧]"
date: 2023-11-15
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "container"
  - "docker"
  - "dockerhub"
  - "dockerio"
  - "http"
  - "https"
  - "nextcloud"
  - "oracle"
  - "port443"
  - "port8000"
  - "port9443"
  - "portainer"
  - "vps"
image: "/images/portainer.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/portainer/)

Table of contents:
* TOC
{:toc}


For all Readers of this blog, _Docker_ should be familiar, as I extensively covered it in [this post](https://blog.tomaszdunia.pl/docker-eng/). However, today I will take it a step further and introduce a tool called _[Portainer](https://www.portainer.io/)_, which is a kind of graphical interface that makes managing _Docker_ containers more enjoyable and intuitive. Interestingly, _Portainer_ runs as a container itself - [one ring container to rule them all](https://blog.tomaszdunia.pl/wp-content/uploads/2023/11/one-ring-to-rule-them-all.jpg)!

## Docker environment installation - short version

As I mentioned earlier, I discussed Docker in detail in [this post](https://blog.tomaszdunia.pl/docker-eng/), but here I will briefly remind you how to do it by listing the necessary commands.

```bash
sudo apt install docker.io -y
sudo groupadd docker
sudo usermod -aG docker $USER
```

## How to run Portainer

As mentioned before, you run _Portainer_ as a regular container, so let's start by creating a volume dedicated to it. We'll call it _portainer\_data_.

```bash
docker volume create portainer_data
```

We will use an image in the _CE_ (_Community Edition_) version available on [_Docker Hub_](https://hub.docker.com/r/portainer/portainer). For your convenience, I have prepared a ready-made command that will correctly launch a properly configured container with a running _Portainer_.

```bash
docker run -d \
-p 8000:8000 \
-p 9443:9443 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
--name Portainer \
--restart unless-stopped \
portainer/portainer-ce:latest
```

Let's go briefly line by line to describe what we are actually doing with this command. We start with a simple command to run the container in _detached mode_, hence the _\-d_ flag, which, in simple terms, runs the container in the background and keeps it running. Next, we bind (redirect traffic) ports _8000_ (_HTTP_) and _9443_ (_HTTPS_) between the container and the machine on which it is running. The access panel to _Portainer_ will be located under these ports. It is important to note that if we want external access, i.e., from the Internet or in any other way outside the local network or even the machine on which it is running, we must unlock the ports on both the server (e.g., in _iptables_) and the router and/or other infrastructure where it operates (I'm looking towards _Oracle's Virtual Cloud Networks_). Moving on, we define two volumes. The first one mounts the _docker.sock_ file, allowing _Portainer_ to control the entire _Docker_ environment in which it operates and manages. The second is a regular place for _Portainer_'s files. The last three lines are standard - giving a name to the container, specifying the restart policy (in this case, _run until manually stopped_), and specifying which image to use.

To execute this command, confirm with _ENTER_, and after the container is launched, you can go to the browser and enter the following in the address bar:

> https://localhost:9443

You will see a very simple installer, where you only need to set a name and password for the administrator. On the next page, click the _Get Started_ button, as we want _Portainer_ to use the environment on the local machine on which it is running. Finally, you will be redirected to the list of available environments, where there will be only one named _local_. To start managing this environment, click the blue _Live connect_ button on the right side. This will result in tabs with management options appearing on the left side, replacing _Environment: None selected_.

![](/images/portainer1.png)
    
![](/images/portainer2.png)
    
![](/images/portainer3.png)
    

## How to launch a sample container

Simply launching _Portainer_ is just the beginning of the fun, and I would feel remiss if I ended the post at this point. Therefore, I will show you how to start a sample container. As a representative example, I have chosen _[Nextcloud](https://nextcloud.com/)_, which I have written about in [this post](https://blog.tomaszdunia.pl/nextcloud-eng/).

After selecting _Environment - local_, choose the _Containers_ tab on the left. This is where you will create and list all containers. As you can see, at this point, the only container on the list is _Portainer_ itself. Before attempting to expand this list with another container, we first need to go to the _Volumes_ tab, where we will create two volumes necessary for the proper functioning of _Nextcloud_.

![](/images/portainer_nextcloud1.png)
    
![](/images/portainer_nextcloud2.png)
    

Using the blue _Add volume_ button located in the top right corner, create volumes _nextcloud\_config_ and _nextcloud\_data_. In the volume creator, simply enter the name in the _Name_ field and confirm with the _Create new volume_ button.

![](/images/portainer_nextcloud4.png)
    
![](/images/portainer_nextcloud3.png)
    
![](/images/portainer_nextcloud5.png)
    

On the _Volumes_ list, two volumes marked with the _Unused_ tag will appear, and their mount points on the server are _/var/lib/docker/volumes/(...)/\_data_. Now that we have prepared a location for the _Nextcloud_ container, we can proceed to create it. Let's go back to the _Containers_ tab and use the blue _Add container_ button located in the upper right corner. This will open the wizard window, where in the first section at the top, we fill in the fields:

- _Name_ - _Nextcloud_

- _Image_ - _lscr.io/linuxserver/nextcloud:latest_

- _Manual network port publishing_ (after pressing the _publish a new network port_ button):
    - _host_ - _443_
    
    - _container_ - _443_

![](/images/portainer_nextcloud6.png)

Move on to the bottom section, where we need to go through several tabs. The first one to check is _Volumes_, where we will attach the volumes created earlier to the container. To do this, press the _map additional volume_ button twice (since we will be configuring two volumes) and map as follows:

| **container** |  | **volume** |
| --- | --- | --- |
| /config | \=> | nextcloud\_config - local |
| /data | \=> | nextcloud\_data - local |

![](/images/portainer_nextcloud7.png)

The crucial part here is to ensure that the _Volume_ fields are selected (not _Bind_) and _Writable_ (not _Read-only_). The next tab we navigate to is _Env_, which is an abbreviation for _Environment variables_. For _Nextcloud_, we need to set three variables here, so we press the _Add an environment variable_ button three times and enter the following values:

- _PUID_ - _1000_

- _PGID_ - _1000_

- _TZ_ - _Europe/Warsaw_

![](/images/portainer_nextcloud8.png)

The last tab that interests us at this point is _Restart policy_, where we choose the _Unless stopped_ option.

![](/images/portainer_nextcloud9.png)

Now all that remains is to go back to the top section, where at the end, you'll find the blue _Deploy the container_ button. This will download the image and launch the properly configured _Nextcloud_ container, as observed in the container list.

![](/images/portainer_nextcloud10.png)

The container is running, so we can open a browser to access the freshly launched _Nextcloud_. We started it on port _443_, which is the default port for _HTTPS_ communication. Therefore, in the browser's address bar, simply enter the following phrase:

> https://localhost

First, we will see the installer where we set the name and password for the administrator and can configure the database. However, in this case, I leave it as default, which uses _SQLite_ because it's just a solution made only for demonstration. The last thing left to do is press the _Install_ button.

![](/images/portainer_nextcloud11.png)

## Accessing Nextcloud from the Internet

It was supposed to be a post about the _Portainer_ tool, but I'll take the opportunity to expand on the _Nextcloud_ topic a bit more. In the previous paragraph, I described how to launch _Nextcloud_ and access it from the local network. But what if we want to access it from the outside?

If you are using a [_VPS_ from _Oracle_](https://blog.tomaszdunia.pl/oracle-free-tier-eng/), the first step should be to unblock traffic on the _Oracle_ infrastructure level for port _443_. This can be done in _Networking_ -> _Virtual cloud networks_ -> select your _VPS's_ _VNC_ -> _Security Lists_ -> go to the list appropriate for your _VPS_. You need to add an _Ingress Rule_ similarly to the screenshot below.

![](/images/portainer_nextcloud14.png)
    
![](/images/portainer_nextcloud15.png)
    

The situation looks similar in the case of a home server and a router, whose ports need to be opened as it is the main gateway in the home network.

Next, you need to connect to the server via _SSH_ and log in as the root user:

```bash
sudo su
```

Open _iptables_ for editing:

```bash
nano /etc/iptables/rules.v4
```

Locate the line:

```bash
(...)
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
(...)
```

And right after it, on the next line, paste:

```bash
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT
```

Network traffic has been successfully opened, so the website should be accessible by entering the address:

> https://\[Server IP Address\]

However, most likely, you will see something like this...

![](/images/portainer_nextcloud13.png)

Solving this problem is relatively simple, but finding it is not entirely straightforward, as you need to dig a bit into the documentation. They could have made it much more intuitive... Fortunately, you have me, the guy who has already done all the work and will now present a ready and concise solution. Open the _config.php_ file mentioned in the message in a text editor - location of it is not that obviouscurious about its location, right?

```bash
nano /var/lib/docker/volumes/nextcloud_config/_data/www/nextcloud/config/config.php
```

Locate the _trusted\_domains_ section in it and fill it out similarly to this:

```bash
(...)
'trusted_domains' =>
    array (
      0 => 'localhost',
      1 => '[VPS IP]',
  ),
(...)
```

Of course, instead of _\[VPS IP\]_, you should provide the _IP address_ of your server. After all these steps, you can refresh the page in the browser, and access should be possible.
