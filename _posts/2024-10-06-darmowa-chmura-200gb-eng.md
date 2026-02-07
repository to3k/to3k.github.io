---
title: "~200GB Free Cloud for Your files [ENG 🇬🇧]"
date: 2024-10-06
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "cloudflare"
  - "docker"
  - "dockerhub"
  - "dockerio"
  - "freetier"
  - "freedns42"
  - "https"
  - "iptables"
  - "letsencrypt"
  - "linux"
  - "mariadb"
  - "mysql"
  - "nextcloud"
  - "nginxproxymanager"
  - "opensource"
  - "oracle"
  - "portainer"
  - "putty"
  - "selfhosted"
  - "ssh"
  - "ssl"
  - "termius"
  - "ubuntu"
  - "ufw"
  - "vps"
coverImage: "/images/Darmowa-chmura-200GB.png"
---

[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/darmowa-chmura-200gb/)

My post about the [free _VPS_ server from _Oracle_](https://blog.tomaszdunia.pl/oracle-free-tier-eng/) is a true **hit on this blog**. Looking at the stats, it has more views than all other posts combined. It's no wonder, because I think everyone likes to save a little and **get something cool for free**. Of course, there will be voices saying that if something is free, then the product is actually us, or rather our data. Probably true, but I have to admit that personally, I didn't think twice before taking advantage of this **interesting _Oracle_ promotion**, where you can actually get **three servers** — one with a **4-core processor and 24GB RAM** based on the _ARM_ architecture, and **two with much weaker processing power (1/8 OCPU) and only 1GB RAM** based on _AMD_ architecture. The first one is a **real powerhouse, where you can do some seriously awesome things**, and the other two are like satellites that **work great as training grounds or for smaller projects**. Interestingly, last week I completely wiped my _Oracle_ infrastructure and set it up from scratch, which gave me the chance to check if the method I described still works, and I'm pleased to say it does. So, to officially answer the many questions I've received over the past months — **yes, the servers in the _Always Free Tier_ are still available, and my [guide](https://blog.tomaszdunia.pl/oracle-free-tier-eng/) is up-to-date**.

## What interesting thing are we doing today?

In today's post, on this free _VPS_ from _Oracle_, **we're going to set up a private cloud for files, where we can store up to 200 GB of data**. We'll do this by launching a _Docker_ container, which will host _Nextcloud_, and we'll do it using _Portainer_. We'll also link our own domain to it, using _NGINX Proxy Manager_, which will run as a separate container, and _Cloudflare_ (though for those not keen on _CF_, I'll also describe how to do it via _FreeDNS::24_). Of course, we'll also take care of encrypting the communication, i.e., _SSL/HTTPS_, which we'll achieve through _NGINX Proxy Manager_ using a _Let's Encrypt_ certificate.

## Table of Contents

1. [Obtaining a free VPS Server from Oracle](#oracle)

3. [Initial Server Configuration](#conf)

5. [Firewall](#firewall)

7. [Docker and Portainer](#portainer)

9. [Connecting a domain via Cloudflare](#cloudflare)

11. [Alternative solution with FreeDNS::42 instead of Cloudflare](#freedns42)

13. [NGINX Proxy Manager](#nginx)

15. [Nextcloud and MariaDB](#nextcloud)

17. [Closing ports (update 07-10-2024)](#cleanup)

## Obtaining a free VPS Server from Oracle

If you don't have such a server yet, I described the entire process in great detail in a [separate](https://blog.tomaszdunia.pl/oracle-free-tier-eng/) [post](https://blog.tomaszdunia.pl/oracle-free-tier/). For the purpose of this guide, I suggest creating an instance with the following parameters:

- Region - **_EU-Frankfurt-1_** (recently, I haven't had any issues getting a _VPS_ from the **_AD2_** region),

- Shape (machine type) - go to the _Virtual Machine_ tab, then _Ampere_, and choose **_VM.Standard.A1.Flex_**,

- Image - **_Ubuntu 22.04_**, which we will upgrade to _24.04 LTS_ during the initial setup, as _Oracle_ claims (incorrectly) that _24.04 LTS_ does not work with this machine type (_ARM_ is the issue for them?), so they don't allow you to start directly with that version (I will prove this wrong),

- CPU - **4 cores**,

- RAM - **24GB**, we don't need that much for _Nextcloud_, but let's not limit ourselves and take the maximum available, as it will allow us to run other things in the future,

- **Public _IPv4_ Address** - make sure to assign it during the creation of the machine to simplify the process. Also, consider assigning an _IPv6_ address, which might be useful in the future,

- **SSH keys** - Oracle won’t let you proceed without this, which is a good practice. Simply create a new key and save it, or use your own and provide public part to _Oracle_,

- Disk capacity - (this is defined in the _Boot volume_ section after selecting _Specify a custom boot volume size_) - for free, we can get **a maximum of 200GB to be shared across all machines**. You can assign all of it to this _ARM_ machine, or split it so that some remains for the two _AMD_ machines,

- Encryption of communication between the instance and storage - select the **_Use in-transit encryption_** option.

## Initial Server Configuration

We start as usual by connecting to the previously created instance. I typically use the [_Termius_](https://termius.com/) application for this purpose, but you can also use _[PuTTY](https://www.putty.org/)_ or any other method that allows for _SSH_ communication. How to connect to servers via _SSH_ is described in [this post](https://blog.tomaszdunia.pl/serwer-domowy-eng/#ssh). And in [this post](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja-eng/#kluczessh) on how to use _SSH_ keys. I won’t repeat all of that again. Here, we will focus only on what is not obvious for this specific case. To connect via _SSH_, we essentially need four things:

1. Server _IP_ address

3. Username

5. Public _SSH_ key

7. Private _SSH_ key

We will get the first two by accessing the _Oracle_ instance management center. After successfully creating it, we should see it on the list of our instances, so let’s go to its properties \[1\].

![](/images/oracle40.png)

The information we're looking for (server IP address \[2\] and username \[3\]) is located in the _Instance information_ tab, in the _Instance access_ section on the right-hand side.

![](/images/oracle41.png)

The _SSH_ keys required for authentication were already downloaded to our disk during instance creation. Now we have everything, so we just need to input all of this into _Termius_ (or another program) and connect to our brand-new _VPS_.

Now, we will perform the **basic server configuration**. We'll start, of course, by updating the packages. After completing this, you may consider restarting the server.

```bash
sudo apt update
sudo apt upgrade -y
sudo reboot now
```

For obvious reasons, you'll be disconnected from the server. Wait a moment for it to restart, and then reconnect via _SSH_. Now, we will proceed to upgrade the _Ubuntu_ system from version 22.04 to 24.04 LTS.

```bash
sudo do-release-upgrade
```

The entire process is intuitive, so I won’t go into detail here. Maybe one day I’ll make a separate post about it if there’s a demand for it. If you need confirmation that the upgrade was successful, you can use the command:

```bash
lsb_release -a
```

The result of the command should look something like this:

```bash
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 24.04.1 LTS
Release:        24.04
Codename:       noble
```

As part of the basic configuration, I always check the _SSH_ authorization settings, as they're often not configured the way I prefer. So, let's open the text editor and modify the entries in the _sshd\_config_ file.

```bash
sudo nano /etc/ssh/sshd_config
```

We need to find the appropriate lines and change their values to the ones below. Note that these lines may not only be in different places but also in a different order.

```bash
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
PasswordAuthentication no
```

## Firewall

When using _Oracle_, I actually use a **three-layer firewall**. The first layer is the **firewall in the _Oracle_ infrastructure**. The second is _**iptables**_ on the server, and the third is the _**ufw**_ package, which I always install myself. Let’s configure them one by one.

How to open ports in the _Oracle_ infrastructure is described in [this post](https://blog.tomaszdunia.pl/oracle-free-tier-eng/#porty). In short, you do it by going to _Virtual Cloud Networks_ (remember to select the correct _Compartment_ first) -> find your network on the list and go to its properties -> from the _Resources_ menu on the left, select _Security Lists_ -> there should be only one list called _Default Security List for..._. Here, we're interested in _Ingress Rules_, and by using the _Add Ingress Rules_ button, we add rules to open **ports 80, 443, 81, 444, 9443**. We do this by filling out the form for each port, as shown below, where I demonstrate how to do it for port 80.

![](/images/obraz-300x215.png)

We have now opened the following ports:

- **80** - standard _HTTP_ for _NGINX Proxy Manager_,

- **443** - standard _HTTPS_ for _NGINX Proxy Manager_,

- **81** - _HTTP_ port for the _NGINX Proxy Manager_ admin panel,

- **444** - _HTTPS_ port for _Nextcloud_,

- **9443** - _HTTPS_ port for _Portainer_.

That’s all you need to do on the _Oracle_ side. The next step is to update _iptables_ on the server. This is an internal table of network rules that determines what traffic to and from the server is allowed. Let’s go to the server and use the following commands:

```bash
sudo su
nano /etc/iptables/rules.v4
```

This will open a text editor. Find the line:

```bash
(...)
-A INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT
(...)
```

Right after it, add the following new lines:

```bash
-A INPUT -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 81 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 444 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 9443 -j ACCEPT
```

We save and close the _rules.v4_ file by using "control + x", "y" and ENTER. Now, we still need to configure the last gateway, which is the _ufw_ application.

```bash
sudo apt install ufw
sudo ufw disable
sudo ufw reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw allow 81
sudo ufw allow 444
sudo ufw allow 9443
sudo ufw enable
sudo ufw status verbose
```

The final result should look like this:

```bash
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
-- ------ ----
22                         ALLOW IN    Anywhere                  
80                         ALLOW IN    Anywhere                  
443                        ALLOW IN    Anywhere                  
444                        ALLOW IN    Anywhere                  
81                         ALLOW IN    Anywhere                  
9443                       ALLOW IN    Anywhere                  
22 (v6)                    ALLOW IN    Anywhere (v6)             
80 (v6)                    ALLOW IN    Anywhere (v6)             
443 (v6)                   ALLOW IN    Anywhere (v6)             
444 (v6)                   ALLOW IN    Anywhere (v6)             
81 (v6)                    ALLOW IN    Anywhere (v6)             
9443 (v6)                  ALLOW IN    Anywhere (v6) 
```

To be sure, we should still verify that the _ufw_ service will start automatically with the system (e.g., after a restart). This option should be enabled by default, but it's always good to check it yourself. We go into the _ufw_ configuration file:

```bash
sudo nano /etc/ufw/ufw.conf
```

Here, we want to ensure that the _ENABLED_ variable is set to _yes_:

```bash
# Set to yes to start on boot. If setting this remotely, be sure to add a rule 
# to allow your remote connection before starting ufw. Eg: 'ufw allow 22/tcp' 
ENABLED=yes
```

Now, all that remains is to restart the machine.

```bash
sudo reboot now
```

## Docker and Portainer

I have described this in detail in a [separate post](https://blog.tomaszdunia.pl/portainer-eng/), so here I will only quickly go over it as a reminder.

```bash
sudo apt install docker.io -y
sudo groupadd docker
sudo usermod -aG docker $USER
```

Docker is installed, so we move on to creating a volume for _Portainer_ data.

```docker
docker volume create portainer_data
```

The next step is to create a properly configured container.

```docker
docker run -d \
-p 9443:9443 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
--name Portainer \
--restart unless-stopped \
portainer/portainer-ce:latest
```

_Portainer_ is running on port 9443, so now we need to locate the server address we used for the _SSH_ connection, open a browser, and type in the address bar:

> https://<oracle\_vps\_ip>:9443

A very simple installer will appear before us, where we only need to set the login and password for the administrator. On the next page, we select the _Get Started_ button, as we want _Portainer_ to use the environment located on the local machine it is running on. Finally, we will be taken to the list of available environments, where there will be only one called _local_. To start managing this environment, press the blue _Live connect_ button on the right-hand side. As a result, tabs with management options will appear on the left instead of _Environment: None selected_.

![](/images/portainer1.png)
    
![](/images/portainer2.png)
    
![](/images/portainer3.png)
    

## Connecting the domain via Cloudflare

1. Log in to [Cloudflare.com](https://cloudflare.com) and press the _Add a domain_ button.

3. Enter the address of your domain. In my case, it's the example _exampleforblog.com_. Choose _Manually enter DNS records_ because we want to start with a clean slate without _CF_ guessing which records we want. Confirm with the _Continue_ button.

5. On the next page, scroll down because the plan we are interested in (obviously the only right one, the free one) is at the very bottom.

7. Select the _Free_ plan and confirm by pressing _Continue_.

9. On the next page, scroll down to the information that interests us.

11. First, _CF_ asks us to disable the _DNSSEC_ feature at our domain provider. Not all providers enable it by default, but for example, _OVH_ probably does, so I thought it was worth mentioning.

13. On the same page, but lower, _CF_ lists two _DNS_ addresses to which we need to point all traffic from our domain. This is done on the domain provider's site.

15. From the left menu, select the _DNS_ tab and then _Records_. Start adding records by pressing the _Add record_ button.

17. Leave _A_ as the default in the _Type_ field. In the _Name_ field, enter _portainer_. In the _IPv4 address_ field, provide the address of your _VPS_ server from _Oracle_—the bare address without any ports, e.g., _101.102.103.104_ (I made up this address, so enter yours here). We want the traffic to be proxied by _CF_, so leave the _Proxied_ setting. _TTL_ remains _Auto_. In the _Comment_ field at the bottom, you can enter any comment to help you understand what this record is for and where it came from in the future. Just write in your own words what you want and how you will use this record. Finally, confirm by pressing the _Save_ button.

19. The first record is added, but for this guide, we will need a total of three, so add more using the _Add record_ button again.

21. In this way, we will also add records for _Name_ - _cloud_ and _nginx_. What we have done now is created three subdomains for the parent domain. They are, respectively, _portainer.exampleforblog.com_, _cloud.exampleforblog.com_, and _nginx.exampleforblog.com_.

23. Go back to the menu on the left and this time select the _SSL/TLS_ tab, and from there _Overview_. In the section labeled _SSL/TLS encryption_, press the _Configure_ button.

25. In the window labeled _Custom SSL/TLS_, press the _Select_ button.

27. Change the option from _Full_ to _Flexible_ and confirm your choice by pressing _Save_.

29. In the same tab from the left menu, select _Edge Certificates_. Find the window labeled _Always Use HTTPS_ and enable this feature.

31. Scroll down, find _Automatic HTTPS Rewrites_, and also enable this feature.

![](/images/cf1.png)
    
![](/images/cf2.png)
    
![](/images/cf3.png)
    
![](/images/cf4.png)
    
![](/images/cf5.png)
    
![](/images/cf6.png)
    
![](/images/cf7.png)
    
![](/images/cf8a.png)
    
![](/images/cf9.png)
    
![](/images/cf10.png)
    
![](/images/cf10a.png)
    
![](/images/cf11.png)
    
![](/images/cf12.png)
    
![](/images/cf13.png)
    
![](/images/cf14.png)
    
![](/images/cf15.png)
    

Done. We can now log out of _Cloudflare_ and proceed to the next step.

## Alternative solution with FreeDNS::42 instead of Cloudflare

The same result as in _Cloudflare_ can be achieved by using, for example, _[FreeDNS::42](https://freedns.42.pl)_ or another similar tool.

1. We start by logging into our _FreeDNS::42_ account. Then, we go to _Create Zone_.

3. For _Zone Name_, we enter our domain. For _Zone Type_, we select _Primary_. Then, we press the _Create_ button.

5. Now that the zone is created, we move to the _modification tab_.

7. Scroll down...

9. ... until we find the _DNS Server Records (NS)_ section. It will show two addresses: _fns1.42.pl_ and _fns2.42.pl_. We need to point all traffic from our domain to these DNS addresses. This is done on the domain provider's website.

11. On the same page, scroll a little further down to the _Address Records (A)_ section, where we add three records. In the _Name_ column, they will have the following values: _portainer_, _nginx_, and _cloud_, respectively. In the _IP_ column, we enter the IP address of our _VPS_ from _Oracle_ three times.

13. We finalize this configuration by pressing the _Create Zone Configuration_ button at the very bottom.

15. Finally, a summary will be displayed where we can check if everything is correct.

![](/images/fdns1.png)
    
![](/images/fdns2.png)
    
![](/images/fdns3.png)
    
![](/images/fdns4.png)
    
![](/images/fdns5.png)
    
![](/images/fdns6.png)
    
![](/images/fdns7.png)
    
![](/images/fnds8.png)
    

## NGINX Proxy Manager

_NGINX Proxy Manager_ will be used for properly **routing traffic to our server via the domain** that we just added in _Cloudflare_/_FreeDNS::42_. The goal is to ensure that, for example, traffic from the subdomain _portainer.exampleforblog.com_ is directed exactly to port 9443, which is where the _Portainer_ admin panel is running. In simple terms, _NGINX Proxy Manager_ acts as a **traffic sign**.

We start launching the _NGINX Proxy Manager_ container by logging into the _Portainer_ admin panel. In the _Environments_ section, we select _local_ and press the _Live connect_ button. From the menu on the left, select _Stacks_ and press the _Add stack_ button. In the _Name_ field, enter _nginx\_proxy\_manager_. In the _Build method_ section, leave the default _Web editor_. Paste the following code into the _Web editor_ text area:

```docker
version: '3.8'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80' # Public HTTP Port
      - '443:443' # Public HTTPS Port
      - '81:81' # Admin Web Port
    volumes:
      - /var/lib/docker/volumes/nginx_proxy_manager/data:/data
      - /var/lib/docker/volumes/nginx_proxy_manager/letsencrypt:/etc/letsencrypt
```

Let me briefly comment on it. We are using the image _[jc21/nginx-proxy-manager](https://hub.docker.com/r/jc21/nginx-proxy-manager)_, which will be downloaded from _Docker Hub_. The container will automatically restart every time it stops, unless we manually stop it ourselves. It will use ports 80 (HTTP), 443 (HTTPS), and 81. The admin panel will be accessible via the last port. This is where we will point the subdomain _nginx.exampleforblog.com_ to. We are creating two volumes to extract the folders _/data_ (configuration data) and _/etc/letsencrypt_ (where the _SSL_ certificates will be stored) from the container.

After pasting this code, there’s not much else we need to do because we only need to create this configured container by using the _Deploy the stack_ button located in the _Actions_ section at the bottom. Doing this from the _Stacks_ level has the advantage that everything is handled at once, i.e., creating the container and the volumes needed for it to function.

Let’s now proceed to the _NGINX Proxy Manager_ admin panel. You can access it through the browser by typing in the address bar:

> https://<oracle\_vps\_ip>:81

You will be greeted by the login form. But what’s the username and password? The documentation helps us out here, stating that the container is created with default credentials, which you are required to change upon first login. These are:

```
Email:    admin@example.com
Password: changeme
```

Log in with these credentials, and immediately create a new administrator account based on your own details. Go to the _Hosts_ tab at the top bar and select _Proxy Hosts_. Using the _Add Proxy Host_ button, add the first one. In the _Domain Names_ field, enter _portainer.exampleforblog.com_ (of course, replace _exampleforblog.com_ with your own domain). In the _Scheme_ field, select _https_. In _Forward Hostname / IP_, enter your server’s **local** IP address. To find it, you need to install _net-tools_:

```bash
sudo apt install net-tools
```

And use the following command:

```bash
ifconfig
```

The IP address you're looking for will be in the _enp0s6_ section. Here's a snippet from the output of the _ifconfig_ command:

```bash
enp0s6: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9000
        inet 10.0.0.195  netmask 255.255.255.0  broadcast 10.0.0.255
        inet6 ...  prefixlen 128  scopeid 0x0<global>
        inet6 ...  prefixlen 64  scopeid 0x20<link>
        ether 02:00:17:06:21:40  txqueuelen 1000  (Ethernet)
        RX packets 335922  bytes 763693420 (763.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 301753  bytes 418933520 (418.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

The address we are looking for is in my case _10.0.0.195_ (in your case it will almost certainly be different). All that's left to do is to enter _9443_ in the _Forward Port_ field. The correctly filled form in my case looks like this:

![](/images/obraz-3-273x300.png)

But this is not the end, because we still need to switch from the _Details_ tab to _SSL_, where from the drop-down menu titled _SSL Certificate_ we select _Request a new SSL Certificate_. Additionally, we select the _Force SSL_ option and _I Agree to the Let's Encrypt Terms of Service_.

![](/images/obraz-4-273x300.png)

Now we can confirm by clicking the _Save_ button. We repeat this same process two more times for the remaining two subdomains we created in _Cloudflare_.

- for _nginx.exampleforblog.com_ enter port _81_

- for _cloud.exampleforblog.com_ enter port _444_

## Nextcloud and MariaDB

The last thing we have to do is create a _Nextcloud_ container, for which the database will be _MariaDB_ running in a separate but linked container. We will do this similarly to how we did it for the _NGINX Proxy Manager_, i.e., through _Stacks_ in _Portainer_. So we go to _Stacks_ and press the _Add stack_ button. For _Name_, enter _nextcloud_, and in the _Web editor_, paste the following ready-made code:

```docker
version: '2'

services:
  db:
    image: mariadb:latest
    restart: unless-stopped
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW
    volumes:
      - /var/lib/docker/volumes/Nextcloud_Database:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=<database_root_password>
      - MYSQL_PASSWORD=<nextcloud_user_password>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud

  app:
    image: lscr.io/linuxserver/nextcloud:latest
    restart: unless-stopped
    ports:
      - 444:443
    links:
      - db
    volumes:
      - /var/lib/docker/volumes/Nextcloud_Application/config:/config
      - /var/lib/docker/volumes/Nextcloud_Application/data:/data
    environment:
      - MYSQL_PASSWORD=<nextcloud_user_password>
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_HOST=db
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Warsaw
```

This code essentially creates a tandem of two containers. The first is the database, and the second is our _Nextcloud_ cloud. Interestingly, I didn't assign any port to the database, though I could have, as I might want to use it in the future. This isn’t a major problem, since it can be modified later. For _Nextcloud_, I assigned port 444, as port 443 is already used to handle _NGINX Proxy Manager_, but we’ve already sorted that out with proper forwarding during the _NGINX Proxy Manager_ configuration stage. As for the Docker image, I used the _[lscr.io/linuxserver/nextcloud](https://hub.docker.com/r/linuxserver/nextcloud)_, not the official image, which is also available on _Docker Hub_. The reason is that the image from _linuxserver_ (probably) was the first to support the _ARM_ architecture, and I’ve just been using it for a long time. I’ve also had mixed experiences with the official one, so I prefer this one and recommend it. Note that in the code, there are two placeholders _<database\_root\_password>_ and _<nextcloud\_user\_password>_, so replace them with your chosen passwords. This parameterized _Stack_ is created by confirming with the _Deploy the stack_ button, and we’re done.

To access our freshly created cloud, we no longer need to fiddle with IP addresses, just type _cloud.exampleforblog.com_ in the browser’s address bar. All that’s left is to create an admin account and complete the installation. During the installation, you may need to re-enter the database credentials for MariaDB, as for some unknown reason, they occasionally don’t get saved properly in the container during its creation. This is not a major issue, as you just need to expand the advanced settings menu during the _Nextcloud_ installation, select _MariaDB_, and fill in the four fields with the data you provided when creating the _Stack_ in the _Web editor_.

```
MYSQL_PASSWORD=<nextcloud_user_password>
MYSQL_DATABASE=nextcloud
MYSQL_USER=nextcloud
MYSQL_HOST=db
```

I wrote quite a bit about _Nextcloud_ in two posts, so I’ll link them here as they may be useful:

- [Nextcloud – Private Cloud for Files](https://blog.tomaszdunia.pl/nextcloud-eng/)

- [Portainer – GUI for Docker](https://blog.tomaszdunia.pl/portainer-eng/)

Finally, here’s one more thing that everyone will probably encounter, and that’s this error message:

![](/images/portainer_nextcloud13.png)

The solution to this problem is relatively simple, but finding it is not so straightforward, as it requires some searching through the documentation. They could have made it definitely more intuitive... Fortunately, you have me, the guy who has already done all the work and will soon present a ready and concise solution. We open the _config.php_ file mentioned in the message in a text editor.

```bash
sudo su
nano /var/lib/docker/volumes/Nextcloud_Application/config/www/nextcloud/config/config.php
```

We find the section _trusted\_domains_ and fill it out similarly to this:

```bash
(...)
'trusted_domains' =>
    array (
      0 => 'localhost',
      1 => 'cloud.exampleforblog.com',
  ),
(...)
```

Of course, instead of _cloud.exampleforblog.com_, you should provide your subdomain, which you configured earlier. Now refresh the page in your browser, and access will be possible.

## Closing ports (update 07-10-2024)

Lastly, we can also close ports 81, 444, and 9443 at the _Oracle_ and _iptables_ firewall levels. This isn't a necessary security measure, but it's certainly considered good practice. These ports are removed in the same way they were added, so I won't describe that. However, I will mention that doing this will ensure that _Portainer_, _NGINX Proxy Manager_, and _Nextcloud_ will still be accessible from the outside, but only through the appropriate subdomains we assigned to them in the _NGINX Proxy Manager_. It will no longer be possible to access, for example, _Portainer_ by entering _https://<oracle\_vps\_ip>:9443_. However, the ports must remain open at the _ufw_ level, because if they are closed there, it won't be possible to access the resources from the outside even through _NGINX_.

## Summary

Once again, I’ve ended up with a terrible lengthy post, but I believe you like it. This entry contains a **piece of solid information**. I hope it will be useful to someone. If it helped you, feel free to contact me in any way possible (comment below, [Mastodon](https://infosec.exchange/@to3k), etc.) and **show off your new and, most importantly, fully free cloud**. **Recommend this method to your friends**, so they can benefit from it too. If you encounter any problems, also **don't hesitate to write**. I promise I will **do my best to help** as much as I can. Good luck!

Oh, and finally, note that this environment, as created, is basically **an ideal foundation for setting up various other valuable services on this server**. I think I will return to this topic more than once in future posts. If you have any interesting ideas on how to use such a machine, I would love to read about it!
