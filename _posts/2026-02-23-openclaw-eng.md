---
layout: post
title: "OpenClaw - Personal AI Assistant [ENG 🇬🇧]"
published: true
categories: 
  - "projects"
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "openclaw"
  - "hetzner"
  - "google-ai-studio"
  - "ai"
  - "llm"
  - "bot"
  - "assistant"
  - "gemini"
  - "chatgpt"
  - "claude"
  - "openai"
  - "anthropic"
  - "google"
  - "vps"
  - "ssh"
  - "telegram"
image: "/images/openclaw.png"
---

[🇬🇧->🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/openclaw/)

Table of contents:
* TOC
{:toc}

## Introduction

Most of us are used to interfaces like ChatGPT or Gemini — these are brilliant "brains in a jar". They can write, analyze, and advise, but rarely can they actually do "something" outside the browser window. **OpenClaw** changes this dynamic, pushing the boundary from passive chatbots to autonomous agents.

### What is OpenClaw?

OpenClaw is an **open-source** AI assistant whose main task is proactive operation. Unlike standard chats that wait for a question, OpenClaw has a so-called **heartbeat** — it can independently monitor tasks, remind you about deadlines, or react to changes in the digital environment of its "master" (the user) without their direct intervention at a given moment.

### A short history and viral success

The project was born at the end of 2025 as the work of **Peter Steinberger**. Before getting its final (or is it...?) name, it went through several stages of evolution. It was previously known as *WhatsApp Relay*, *Clawdbot*, or *Moltbot*. It went viral at the turn of 2025 and 2026 thanks to its simplicity — instead of another app, you use it where you already are: on **WhatsApp**, **Telegram**, or **Discord** (and more). The project's potential is best evidenced by the fact that in February 2026, **the creator of OpenClaw was recruited by the OpenAI team**, although the project itself remains available to the community. I personally have a (probably naive) hope that this won't kill the project.

### Key differences: Agent vs Chatbot

The fundamental difference is **system access at a level similar to a physical user**. Standard chats operate in a secure sandbox on corporate servers. Heck, some LLMs don't even have real-time access to the Internet. OpenClaw operates wherever you deploy it, e.g., on your own VPS server, and most importantly, it can have full access to the resources of that server. What I mean here is that, for example, it can use a browser and log into services normally using the authentication data provided to it.

| Feature | Standard Chatbot (ChatGPT/Gemini) | OpenClaw |
| :--- | :--- | :--- |
| **Interaction** | Reactive (waits for a prompt) | Proactive (initiates contact itself) |
| **Environment** | Closed, cloud-based | Local/VPS, full file access |
| **Capabilities** | Content generation, analysis | Executing real tasks |
| **Privacy** | Data on provider's servers | Full control over logs and memory |
| **Interface** | Dedicated app/web | Messengers (WhatsApp, Telegram, Discord, etc.) |

### What can OpenClaw do?

Thanks to the use of the **Model Context Protocol (MCP)**, OpenClaw has access to hundreds of **capabilities**, which are called **skills**. They are created by the community like well-known programming libraries. Examples of such skills include:

- **Managing calendar and emails** autonomously.
- **Fetching data from external systems** (e.g., KSeF hehe) and processing it further.
- **Independently writing scripts**, installing them on the server, and running them.
- **Buying** cinema tickets.
- **Managing your Tinder account** (this was widely discussed exactly in the context of OpenClaw).

But believe me, the above examples are truly a drop in the ocean, and anyone who even peaks into the library of available possibilities will be mind-blown.

### Who needs this?

Well, obviously, **nerds** like us. Besides, who wouldn't want to have **their own sidekick** who will do (almost) everything they are asked to, and on top of that is a walking encyclopedia because it has read 90% of the Internet. Such an assistant can be a virtual member of a development team and write code at a senior level, but you can also write to it on Telegram: "dude, organize a trip to Warsaw for me," and it will book your train tickets, check the weather and tell you how to dress, set reminders, and notify all your homies from the capital that next Friday you will be within a 10km radius of them ready to grab a beer.

### What you will learn from this post

In a moment you will read something like a **Proof of Concept**, in which I will show you how to run a working OpenClaw bot as cheaply as possible. The goal is to show **how to do it** and check **if it works**, not to launch an optimized environment perfectly suited for a specific task. OpenClaw is such a versatile tool that it has practically an **infinite number of different applications**. What it can do is essentially limited only by the operator's imagination. That is why I will roughly show what it is, how to run it, and possibly how this environment can be expanded later, but what and how this tool will be used for, I will leave to you, dear Reader.

To summarize, in this post I will:
- guide you by the hand through the process of **renting a VPS server**, the price of which is only **5 dollars a month** (!),
- then we will properly **configure this server together**,
- we will obtain **free API access** to the basic Gemini models from Google AI Studio,
- we will run a **Docker container with the bot** inside,
- we will carry out the **basic configuration**,
- we will **check if it works**,
- we will consider options for **expanding the environment**.

### What you will NOT learn from this post

I want to put my cards on the table right from the start and tell you what will not be included in this post, so that later no one tells me they read 70 thousand characters and only wasted their time because they didn't find what they were looking for.

So... I won't show a detailed configuration or any specific application of such an assistant here, because firstly, everyone has different needs, secondly, I am not entirely sure myself what I will use it for yet, and thirdly, this post will be unpleasantly long even without that. Let's leave these threads to be discussed in future posts, because if I really take a liking to OpenClaw, and I see a good chance of that, I won't fail to thoroughly describe every aspect of this coexistence.

### Fasten your seatbelts...

... because we are taking off! Prepare drinks, snacks, and if you don't have a speed reading course certificate, consider getting a potty too, because this won't be a short post. I promise from this point on to be fairly focused on the substantive content, without unnecessary b... :)

## VPS Server - the assistant's body

### Registering at Hetzner

1. To create an account on Hetzner, go to the **[registration form](https://accounts.hetzner.com/signUp)**.
2. Provide your **e-mail address**, **password** (twice), accept the **terms and conditions**, and click the **Continue** button.
3. An **account activation link** will be sent to your email, so go to your email client and find it. Fun fact - something didn't work for me the first time, and I only got the email after entering the same data a second time, of course.
4. The link from the email will take us to the **next part of the registration form**. Here we must:
    - select the account type - **Individual**,
    - Title - you can choose Mr. or Ms., but you can also just leave **None**,
    - First Name - **first name**,
    - Surname - **last name**,
    - click the **Continue** button.
5. The next page is about contact details:
    - Street / House number - **street**,
    - Postal code - **zip code**,
    - City - **city** (note: it didn't accept Polish characters for me, so I assume it might be the same for the `street` field),
    - Country - **country**,
    - VAT ID - **VAT number**, optional as it mostly applies only to businesses,
    - Phone - **phone number** (I think it needs to be preceded by _+48_),
    - Mobile phone - **mobile number** is a strong relic from the times of landline phones, so it's optional and we leave it empty,
    - click the **Continue** button.
6. The next step is about the billing method:
    - select the **currency** - With other services, it's often the case that from the euro-dollar duo, it's worth choosing the dollar because services cost e.g. 5 dollars or 5 euros, and I don't remember times when the dollar was more expensive than the euro. However, in this case, Hetzner converts the amounts and it comes out practically the same, so choose the currency that suits you better, maybe your bank has some preferential exchange rate for one of the currencies (?), I chose the dollar,
    - we have three payment methods - **traditional bank transfer**, **credit card**, and **PayPal**, I chose a credit card and provided the details of my Revolut virtual prepaid card (prepaid, meaning it has as many funds as I deposit onto it and no more, which is safe), which I have specifically for such needs
        - Card holder - enter the **first and last name** shown on the card,
        - Credit card - select the card type, i.e., **Visa**, **MasterCard**, or **American Express**,
        - Card number - **card number**,
        - Expires Month / Year - **month and year the card is valid until**,
        - CVC code - **3-digit CVC security code**,
        - decide if you want to save the card details so you don't have to enter them again in the future, and if so, check the option _Hetzner Online has my permission to save my credit card data on my account and to use this information to pay open invoices._
    - click the **Complete** button,
    - this will require **confirming the card addition**, in my case through the Revolut app (I got a notification and confirmed it).
7. Success. We get confirmation that we have successfully completed the registration process.
8. HOWEVER, it is highly recommended to add an extra layer of 2FA security, so I recommend clicking **Enable 2FA**. Of course, you don't have to do this and you can simply ignore this recommendation and go straight to step 15.
9. We will be redirected to the account settings, where we again click the yellow **Enable 2FA** button.
10. A window will pop up in which we have to enter the account password and check the box to confirm that we understand that if we lose the recovery code, Hetzner will send us a new one by mail and won't do it in any other way. We confirm all this with the **Enable 2FA** button (how much longer...?).
11. We save the **LOGIN** and **KEY** displayed on the screen in a safe place. We can also print them using the button. Then we click **Set up authentication** at the bottom.
12. We choose the security method. If you have a **Yubikey**, use it, and if not, you can choose **Mobile device**, and for this you need a phone with a suitable app, e.g., **[Ente Auth](https://github.com/ente-io/ente/)**, which I recommend. I will describe how to do it using the latter method.
13. We launch **Ente Auth**, press the **plus button** to add a new item, and select **Scan QR code**. We grant the app access to the camera and **scan the QR code** displayed on the Hetzner page. At this point, a new entry will appear in the phone app. We return to the Hetzner page and enter:
    - Description - some short **description** to name our device, you can type something like _Ente Auth Pixel 9a_,
    - Account password - Hetzner account **password**,
    - New generated OTP - the current **OTP code** displayed in the Ente Auth app on the phone,
    - **Add** button.
14. At this point, we will be logged out and will have to log in again. Therefore, we normally provide the login and password and, of course, click the **Login** button. What we see now is this extra step where we have to provide the current OTP code from the Ente Auth app on our phone. We click the **Verify** button. After logging in successfully, we return to the account security settings, where we see that two-factor authentication has been activated. Our account is definitely 100 times safer with this security than with just a login and password.
15. After some time, Hetzner asked me by email for additional identity verification because my account raised some doubts. I had to click the link provided in the email (it was a link to the **Verification** tab in the account settings) and confirm my identity with a document (ID card, driver's license, passport, and I think something else to choose from...) and a photo of my face. To make it funnier, the automatic verification failed because I think I gained weight or something, and I don't look like the photo on my ID taken years ago, so I had to additionally wait for human verification, which fortunately took maybe a minute or a maximum of two. Fortunately, the Indian guy who verified it understood that people age and it's rarely a change for the better. I'm no Krzysztof Ibisz or Tom Cruise.

### Choosing a server

I chose Hetzner because I don't know a company that provides servers with a better **price-to-quality ratio**. Simply put - for machines with quite good parameters, Hetzner wants really little money, so it's an ideal option to test a solution, even for a few months.

Let's see what the current offer looks like. I recommend using the button at the top, which allows you to set the language (English), currency (I chose USD), and most importantly, the country for which the **VAT** is to be calculated. This will allow us to see the **gross prices**, because by default net prices without tax are presented, and this can be very misleading.

Now we can go to the [**Cloud**](https://www.hetzner.com/cloud/) tab and scroll down to the **Prices** section. What interests us are servers from the **Shared Cost-Optimized** category, meaning shared and thus price-optimized, which is just a nicer name for servers for cheapskates. Now no one should have any doubts that this is exactly what we were looking for. We can choose from two locations, but for me, **Germany** is a pretty obvious choice due to the fact that, in my opinion, the server room you use should always be as close as possible, and Finland is undoubtedly further away and also connected by a cable running along the bottom of the Baltic Sea. We are lazy and don't want to mess around with IPv6 problems, so we choose the **IPv4** option even though it's 74 cents more expensive.

The current (as of February 2026) Hetzner **offer** looks like this:

![Hetzner offer](/images/hetznerprices.png)

What interests us is the cheapest **CX23** server with a processor featuring **2 virtual cores** (vCPU), **4GB** of RAM, and a **40GB** SSD drive. Such a server at the time of writing this post costs **5.03 USD per month** (!), which, converted at the current exchange rate, is about **18 PLN** and some change. It's hard to disagree that this is an **attractive price**.

### Renting the server

1. To rent the chosen server, we go to the user console (**Console**), specifically to the **[Projects](https://console.hetzner.com/projects)** tab.
2. We press the large **+ New project** button.
3. In the **Name** field, we enter the project name, I typed **OpenClaw**.
4. We can now add a server to the newly created project, so in the **OpenClaw** project section, we click the **+ CREATE SERVER** button.
5. We will be redirected to the **configurator**, where we will set the server parameters. The configurator will guide us through all the options one by one:
    - Type - server type, we already determined earlier that we will choose the **Cost-Optimized** option (i.e., for cheapskates), and in addition, we will go with the **x86 architecture**, because we care about maximum compatibility at the cost of slightly lower performance, finally, we select **CX23** from the list,
    - Location - server location, I would have chosen **Falkenstein**, but unfortunately, it wasn't possible due to temporarily (?) high demand, so for lack of a better option, I'll take **Nuremberg**,
    - Image - system selection, I recommend **Ubuntu 24.04**, because as I mentioned earlier, we want maximum compatibility, and Ubuntu is like tomato soup, most people (in this case, software) like it,
    - Networking - we select **Public IPv4**, which incurs an additional fee, but we already discussed that, and **Public IPv6**, which happens to be included in the price, however, we do not select **Private networks**,
    - SSH keys - in this section, we can create an SSH key, but if we don't do it, Hetzner will simply send us the password by email, which suits us for now, because **we will deal with SSH keys later during server configuration**,
    - Volumes - **we skip this**, because our server basically already has 40GB of storage for data,
    - Firewalls - **we skip this** at this stage, because we will create a firewall from the server level during its configuration,
    - Backups - if someone is interested in daily backups, this option costs an additional 0.86 USD per month, I don't need it, so **I skipped this section**,
    - Placement groups - here you can create server clusters, but we don't need that, so **we skip it**,
    - Labels - I'm not knowledgeable enough to comment on what this is, so **I skip it**,
    - Cloud config - I'm not knowledgeable enough to comment on what this is, so **I skip it**,
    - Name - here we give our server a name, I typed **openclaw-assistant**
6. The configuration should look more or less like this:

    ![Server configuration for purchase](/images/hetznerserverconfig.png)

7. With such a configuration, we can proceed to purchase the server. To do this, we press the red **Create & Buy now** button.
8. We will be taken to the list of our servers, where a new (and the only) option will appear, i.e., the server we just created. At first, there will be a spinning circle next to it, which means we have to wait a moment for it to be created. However, after a while, a green **Server created** message will pop up at the bottom, meaning that our testing ground is ready.

### Connecting to the server via SSH

The server is ready, so it's time to check our email, where there should already be a message with all the information needed to connect to it. It should look more or less like this:

```html
{% raw %}
Your new server

Your server "openclaw-assistant" was created!

You can access your server with the following credentials:
 
IPv4      ADRES_IPV4/32
IPv6      ADRES_IPV6/64
User      root
Password  OCENZUROWANE_HASŁO
	
You will be prompted to change your password on your first login.

To improve security, we recommend that you add an SSH key when creating a server. This way, no root password will be set and this e-mail won't be generated. 
{% endraw %}
```

From this email, we will further need **ADRES_IPV4** and **OCENZUROWANE_HASŁO** (CENSORED_PASSWORD). Let's try connecting to the server now.
1. On our computer, we open the **terminal** and type:

    ```bash
    ssh root@ADRES_IPV4
    ```

2. We should see this **message**:

    ```bash
    {% raw %}
    The authenticity of host 'ADRES_IPV4 (ADRES_IPV4)' cant be established.
    ED25519 key fingerprint is SHA256: CENZURA.
    This key is not known by any other names.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    {% endraw %}
    ```

3. We must answer this by typing **yes** and pressing **ENTER**.
4. The result will be a message informing us that our server's address has been added to the list of known hosts and next time it will be recognized by its fingerprint, and there will be no need to confirm its authenticity.

    ```bash
    Warning: Permanently added 'ADRES_IPV4' (ED25519) to the list of known hosts.
    Connection closed by ADRES_IPV4 port 22
    ```

5. The connection will be dropped, so we have to use the **command** once again:

    ```bash
    ssh root@ADRES_IPV4
    ```

6. We will be greeted by a prompt to enter the password, so we type the **OCENZUROWANE_HASŁO** and confirm with **ENTER**. Note: if you have no experience with SSH, you might be surprised that when typing the password, nothing happens, i.e., not even asterisks appear; this is how it's supposed to be and it's the desired behavior, just type the password and don't worry about it.
7. If we didn't mess anything up, we should successfully establish a connection and be **greeted** by something like:

    ```bash
    You are required to change your password immediately (administrator enforced).
    Welcome to Ubuntu 24.04.3 LTS (GNU/Linux 6.8.0-90-generic x86_64)

    * Documentation:  [https://help.ubuntu.com](https://help.ubuntu.com)
    * Management:     [https://landscape.canonical.com](https://landscape.canonical.com)
    * Support:        [https://ubuntu.com/pro](https://ubuntu.com/pro)

    System information as of Thu Feb 19 07:43:22 PM UTC 2026

    System load:              0.16              
    Processes:                127
    Usage of /:               4.1% of 37.23GB   
    Users logged in:          0
    Memory usage:             5%                
    IPv4 address for eth0:    ADRES_IPV4
    Swap usage:               0%                
    IPv6 address for eth0:    ADRES_IPV6

    Expanded Security Maintenance for Applications is not enabled.

    62 updates can be applied immediately.
    43 of these updates are standard security updates.
    To see these additional updates run: apt list --upgradable

    Enable ESM Apps to receive additional future security updates.
    See [https://ubuntu.com/esm](https://ubuntu.com/esm) or run: sudo pro status

    Changing password for root.
    Current password: 
    ```

8. The server is configured in such a way that it **forces us to change the administrator password** right during the first connection. This is a good practice, so we obediently follow the suggestion.
    - first, we enter the old **OCENZUROWANE_HASŁO** and confirm with **ENTER**,
    - and then we enter the **NOWE_HASŁO** (NEW_PASSWORD) twice, confirming each time with **ENTER**.

### System and packages update

We will start the basic configuration by **updating the packages on the server**. For this, we will use a ready-made little script that I previously presented in [one of the posts on this blog](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja/#aktualizacja-to-podstawa).

1. We type the **command** that creates the appropriate file and opens it:

    ```bash
    nano /usr/local/sbin/aktualizacja.sh
    ```

2. In the editor, **we paste the following content**:

    ```bash
    {% raw %}
    #!/bin/bash
    #Script for updating the system and packages from blog.tomaszdunia.pl
    echo 'Step 1 - update'
    sudo apt update
    echo 'Step 2 - upgrade'
    sudo apt upgrade -y
    echo 'Step 3 - autoremove'
    sudo apt autoremove -y
    echo 'Step 4 - clean'
    sudo apt clean
    {% endraw %}
    ```

3. We exit the file with the **Control (CTRL) + X** key combination, we will be asked if we want to save the file in this state, we confirm by pressing **y**, and when asked under what name to save it, we simply press **ENTER**, because we don't want to change it.

4. Let's give this script executable permissions:

    ```bash
    chmod +x /usr/local/sbin/aktualizacja.sh
    ```

5. Now just type the file name as a command to start the automatic update and cleanup process:

    ```bash
    aktualizacja.sh
    ```

6. After completing such a large update (I assume that many packages will be outdated right after the first server startup), it's good to consider restarting the server:

    ```bash
    reboot
    ```

7. Of course, we will lose the connection to the server, so we will have to establish it just like we did earlier.

### Creating a new user

The basis of sensibly using a VPS server is **not working on the root user**. Therefore, we will now create a regular user and assign them to a group capable of executing administrative commands. This is like an administrator, but with an extra layer of security, because before executing an administrative command, they will have to type **sudo** and confirm with a **password**. This is sometimes enough to **come to your senses before doing something stupid**. Creating such an account is standard practice. We will name it **manager**.

1. We create a user named **manager**:

    ```bash
    adduser manager
    ```

2. The server will inform us that it has created a new user and group, assigned them unique IDs, and created a home directory. We will also be asked to provide the **password for the new user** twice.
3. Next, the wizard will want to extract unnecessary data from us, such as first and last name, room number, phone, etc., which does not interest us, so we leave all fields blank and just confirm with **ENTER**. All this will also need to be confirmed with **y**.
4. The user is created, so now we need to add them to the administrators group:

    ```bash
    usermod -aG sudo manager
    ```

### Firewall - network firewall

Let's configure the **firewall**. A good practice is to initially **block all incoming traffic**, **allow all outgoing traffic**, and also **open port 22** (default for SSH).

1. Let's start by installing **ufw** (short for Uncomplicated Firewall), it's a wrapper for **iptables** that makes creating firewall rules a bit more pleasant:

    ```bash
    apt install ufw
    ```

2. Now we will execute a few commands one after the other. We **disable** the firewall to change its settings:

    ```bash
    ufw disable
    ```

3. We will **reset** (clear) all rules to start completely from scratch, this will need to be confirmed with **y**:

    ```bash
    ufw reset
    ```

4. We will block all ***incoming* traffic**:

    ```bash
    ufw default deny incoming
    ```

5. We will allow all **outgoing** traffic:

    ```bash
    ufw default allow outgoing
    ```

6. We will open **port 22** for SSH connections:

    ```bash
    ufw allow 22
    ```

7. We will **enable** the firewall, this requires confirming with **y**:

    ```bash
    ufw enable
    ```

8. Now, even if we broke something, we won't lose the connection to the server, but at most, we won't be able to connect to it after dropping the connection. So let's take this moment and **check a second time if everything is set up exactly as we wanted**:

    ```bash
    ufw status verbose
    ```

9. The output of this command **must be** as follows:

    ```bash
    Status: active
    Logging: on (low)
    Default: deny (incoming), allow (outgoing), disabled (routed)
    New profiles: skip

    To          Action      From
    --          ------      ----
    22          ALLOW IN    Anywhere                  
    22 (v6)     ALLOW IN    Anywhere (v6)
    ```

10. If everything matches **to the letter**, you can rest easy.
11. Let's also check if `ufw` will definitely **start up with the system** after every reboot. Let's look into the file:

    ```bash
    nano /etc/ufw/ufw.conf
    ```

12. Inside we should find the following content:

    ```bash
    {% raw %}
    # /etc/ufw/ufw.conf
    #
    # Set to yes to start on boot. If setting this remotely, be sure to add a rule
    # to allow your remote connection before starting ufw. Eg: 'ufw allow 22/tcp'
    ENABLED=yes

    # Please use the 'ufw' command to set the loglevel. Eg: 'ufw logging medium'.
    # See 'man ufw' for details.
    LOGLEVEL=low
    {% endraw %}
    ```

13. The **ENABLED** variable is important to us. Its value must be **yes**, and the line in which it appears cannot be commented out (no # at the beginning).
14. We exit the file with the combination **Control (CTRL) + X**.

### Fail2Ban

This is a program that protects against **brute force** attacks. If someone tries to guess the SSH password several times in a row and fails, `Fail2Ban` will automatically **block their IP address**.

1. We **install** the program:

    ```bash
    apt install fail2ban -y
    ```

2. We **enable** it:

    ```bash
    systemctl enable fail2ban --now
    ```

### SSH Keys

I will not debate why using SSH keys is a **recommended practice**. I will just show how to configure it.

1. Let's start, however, by **logging out** of the root account:

    ```bash
    exit
    ```

2. Now let's connect with the **target account for managing the server** to check if everything works properly:

    ```bash
    ssh manager@ADRES_IPV4
    ```

3. Remember that now you must **enter the password that was provided when creating this user**, not the root password.
4. If you managed to connect and authenticate, it means that **everything is OK** and we can **disconnect** again and return to the local terminal:

    ```bash
    exit
    ```

4. Let's now **create an SSH key pair** (command to be executed on the local computer!):

    ```bash
    ssh-keygen -t ed25519 -C openclaw-assistant
    ```

5. The script will ask for the path and file name where the key should be saved. The **default value suits us**, so we just confirm with **ENTER**:

    ```bash
    Enter file in which to save the key (/root/.ssh/id_ed25519): 
    ```

6. Then it will ask to set a **passphrase to secure the key**, I recommend doing this, but **let it be something rather simple** that will be easy for us to remember, it's just an extra layer of security in case our computer with the key on the disk falls into the wrong hands and is unlocked on top of that. For me, this is a scenario in which losing SSH keys will be my smallest problem, so I turn a blind eye to such an attack vector. Hence the simple passphrase. You can also not set a passphrase at all and just skip this step by pressing **ENTER** twice.

    ```bash
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    ```

7. Now let's send the freshly generated **keys to the VPS server**:

    ```bash
    ssh-copy-id manager@ADRES_IPV4
    ```

8. This one last time we will be asked to **provide the password** of the `manager` user when logging in. **Keys sent**, and now we can test **logging in without having to provide a password**:

    ```bash
    ssh manager@ADRES_IPV4
    ```

9. Now we will perform two important steps - we will **disable password login**, meaning from now on you will be able to access the server **only by having a private SSH key**, and we will **disable the ability to log into the root account**. To do this, we edit the file:

    ```bash
    sudo nano /etc/ssh/sshd_config
    ```

10. We look for the parameters `PermitRootLogin`, `PubkeyAuthentication`, and `PasswordAuthentication` (note - they will not be next to each other), we check if they are not commented out (they must not have a # at the beginning of the line), and we **change their values** to the following:

    ```bash
    PermitRootLogin no
    ...
    PubkeyAuthentication yes
    ...
    PasswordAuthentication no
    ```

11. We save and exit the file - **Control (CTRL) + X**, then **y** and **ENTER**.
12. We **restart** the `ssh` process to apply the changes:

    ```bash
    sudo service ssh restart
    ```

## AI Model - the assistant's brain

You can connect many different LLM models to OpenClaw. It supposedly works best with **[Claude Sonnet](https://claude.com/pricing#api)** from **Anthropic**, but it is a paid solution and, moreover, billed based on usage (price per tokens), which somewhat clashes with the idea of doing this as a trial, and thus as cheaply as possible. **Google Gemini** comes to the rescue here, which, as part of the **Free tier** plan in **[Google AI Studio](https://aistudio.google.com/)**, is a **free** solution and will be sufficient for our application. Smells fishy, right? You can explain this away as Google's fight against the competition from OpenAI and Anthropic, but let's not kid ourselves that there's really anything for free, because by using the Free Tier plan in Google AI Studio, we are actually paying with the currency of our data, which will be used to train the behemoth's models. Of course, they will be anonymized and so on... As they say, if it's free, even vinegar is sweet, and after all, we are here to check how it works in the first place. Besides, I don't know about you, but I don't plan to touch any confidential data in this experiment, so I don't really care if anyone analyzes the nonsense I throw into the tested assistant.

If OpenClaw turns out to be an amazing invention, we can easily switch to Claude later, or use **[OpenRouter](https://openrouter.ai/)** altogether, which will allow us to seamlessly switch between different models.

It is also worth mentioning that the free plan from Google obviously has **usage limits**:
- **RPM** (Requests Per Minute) - limit of requests per minute,
- **TPM** (Tokens Per Minute) - limit of words/data (tokens) per minute,
- **RPD** (Requests Per Day) - limit of requests per day.

The limits available for your account can be checked in **[Dashboard -> Rate Limit](https://aistudio.google.com/rate-limit?timeRange=this-month)**. I recommend focusing on the **Rate limits by model** section and sorting the table by the model name, i.e., the **Model** column. There are quite a few different models there, but we are essentially only interested in those signed **Gemini**, meaning from the **Text-out models** category. At the time of writing this post, the limits for the **Free tier** plan look like this for me:

| Model | Category | RPM | TPM | RPD |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini 2.5 Flash** | Text-out models | 0 / 5 | 0 / 250K | 0 / 20 |
| **Gemini 2.5 Pro** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Flash** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Flash Exp** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Flash Lite** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 2 Pro Exp** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 3 Flash** | Text-out models | 0 / 5 | 0 / 250K | 0 / 20 |
| **Gemini 2.5 Flash Lite** | Text-out models | 0 / 10 | 0 / 250K | 0 / 20 |
| **Gemini 3 Pro** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |
| **Gemini 3.1 Pro** | Text-out models | 0 / 0 | 0 / 0 | 0 / 0 |

As you can see, the restrictions are quite severe. In the free plan, we basically only have access to three models:
  - **Gemini 2.5 Flash**
  - **Gemini 3 Flash**
  - **Gemini 2.5 Flash Lite**

In addition, when it comes to limits, we have 5-10 requests per minute, 250k tokens (which doesn't say much), and only 20 requests per day. This is very poor, but it should be enough to test the bot.

### Obtaining an API key from Google AI Studio

1. Go to the **[Google AI Studio](https://aistudio.google.com/)** website and press the **Get started** button in the top right corner.
2. **Log in** with our Google account.
3. From the menu on the bottom left, select **[Get API key](https://aistudio.google.com/api-keys)**.
4. Press the **Create API key** button located at the top right.
5. In the **Name your key** field, enter a name for the key, it can be e.g., `OpenClaw Assistant`. From the **Choose an imported project** list, select **+ Create project**, give it a name, e.g., `OpenClaw Project`, and press **Create project**. Then press **Create key**.
6. An item with the name we entered will appear on the list of keys. On the right side, we have a few icons, and the first one from the left is called **Copy API key**, and this is exactly what we use.
7. Save the copied key in a safe place.

## Starting the Docker container - birth of the assistant

It's time to take action. OpenClaw even has a [special subsection in its documentation regarding running the service based on Docker on a Hetzner server](https://docs.openclaw.ai/install/hetzner). We will base our setup on it.

### Preparing Docker

1. We return to the VPS server and **log in** as the `manager` user:

	```bash
	ssh manager@ADRES_IPV4
	```

2. We install the necessary **packages** - `Docker`, `Docker Compose`, and `Git`:

	```bash
	sudo apt install -y docker.io docker-compose-v2 git
	```

3. To manage containers without having to repeatedly type `sudo` before commands, we will **add the user** `manager` **to the group** `docker`:

	```bash
	sudo usermod -aG docker manager
	```

4. For the new permissions to take effect, we must **log out** using the `exit` command and **reconnect** to the server:

	```bash
	ssh manager@ADRES_IPV4
	```

### Downloading the OpenClaw repository

1. Before executing the next command, **check if the link below is still valid at the time you are reading this**. I'm writing about this because with the OpenClaw project, the name has already been changed 3 or 4 times, and once even third parties managed to take over the project's domain, which is a insanely **dangerous practice**. If you have any doubts, you can always feel free to write to me directly on Mastodon or in a comment to this post. Once we know we have a good **link to the repository, we download** it to our server:

	```bash
	git clone [https://github.com/openclaw/openclaw.git](https://github.com/openclaw/openclaw.git)
	```

2. We go to the downloaded **folder**:

	```bash
	cd openclaw
	```

### Environment configuration

1. Now we define a **persistent directory**. Docker deletes data upon restart. For the bot to **retain its memory** (logins, settings, etc.), we must create an appropriate folder on the server where they will be permanently maintained:

	```bash
	mkdir -p /home/manager/.openclaw/workspace
	```

2. We still need to **grant them the appropriate permissions** of the container's internal user (UID 1000):

	```bash
	chown -R 1000:1000 /home/manager/.openclaw
	```

3. Let's configure the **environment**. For this purpose, we create a `.env` file:

	```bash
	nano .env
	```

4. We paste the following as the **file content**:

	```bash
	OPENCLAW_IMAGE=openclaw:latest
	OPENCLAW_GATEWAY_TOKEN=TWÓJ_TOKEN
	OPENCLAW_GATEWAY_BIND=lan
	OPENCLAW_GATEWAY_PORT=18789
	OPENCLAW_CONFIG_DIR=/home/manager/.openclaw
	OPENCLAW_WORKSPACE_DIR=/home/manager/.openclaw/workspace
	GOG_KEYRING_PASSWORD=TWÓJ_KLUCZ
	XDG_CONFIG_HOME=/home/node/.openclaw
	GEMINI_API_KEY=KLUCZ_API_GEMINI
	```

5. We don't close the file yet, because it is necessary to **modify** three things in it:
    - `TWÓJ_TOKEN` (YOUR_TOKEN) - instead of this, enter some complex string of characters, which you will also save in your password manager; this will be the **access password to the control panel** (Control UI) of the bot.
    - `TWÓJ_KLUCZ` (YOUR_KEY) - instead of this, enter some complex string of characters, which you will also save in your password manager; this will be the **key with which the data in the persistent directory** `(...)/.openclaw/workspace` that we created earlier will be encrypted; thanks to this, even if someone breaks into the VPS and copies this folder, they will not read the confidential data stored there.
    - `KLUCZ_API_GEMINI` (GEMINI_API_KEY) - instead of this, provide the **API key** that we copied earlier from Google AI Studio.
    - **NOTE** - when generating the token and key, be careful not to include the `$` sign in the character string, because it crashed my container during its build and I lost probably an hour looking for the problem.
6. Now we can save and close the environment configuration file - **Control (CTRL) + X**, then **y** and **ENTER**.
7. Before we build the container, we still need to **modify the default file** `docker-compose.yml`, because our case differs slightly from the one assumed as default in the main repository.
8. Before modifying the file, it is better to **make a backup copy of it**, so that in case of anything you can refer to its original content:

	```bash
	cp docker-compose.yml docker-compose-old-backup.yml
	```

9. We **open** the `docker-compose.yml` file in the editor:

	```bash
	nano docker-compose.yml
	```

10. The **correct content** should be as follows:

	```bash
	{% raw %}
	services:
		openclaw-gateway:
			image: ${OPENCLAW_IMAGE}
			build: .
			restart: unless-stopped
			env_file:
				- .env
			environment:
				- HOME=/home/node
				- NODE_ENV=production
				- TERM=xterm-256color
				- OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}
				- OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}
				- OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}
				- GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}
				- XDG_CONFIG_HOME=${XDG_CONFIG_HOME}
				- PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
			volumes:
				- ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw
				- ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace
			ports:
				- "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"
			command:
				- "node"
				- "dist/index.js"
				- "gateway"
				- "--bind"
				- "${OPENCLAW_GATEWAY_BIND}"
				- "--port"
				- "${OPENCLAW_GATEWAY_PORT}"
				- "--allow-unconfigured"
	{% endraw %}
	```

### Starting the container

1. The time has come to **build the container**:

	```bash
	docker compose build
	```

2. Now all that's left is to **wait** patiently. In my case, the process took 174 seconds.

3. If the container was built successfully (green `built` message), we can **try to start it**:

	```bash
	docker compose up -d openclaw-gateway
	```

4. Let's check now **if the container has started**:

	```bash
	docker ps
	```

5. One item named `openclaw-openclaw-gateway-1` should appear on the list, and in the `Status` column there should be `Up ...` informing how long ago the container "got up".

6. Let's also check the **logs**:

	```bash
	docker compose logs -f openclaw-gateway
	```

7. If there are no red `WARNING` or `ERROR` messages there, it might mean that **everything is OK**. I don't require anyone to understand what is written there, because I certainly don't understand it fully myself. If you have doubts, you can send me the content of the logs, throw them here in a comment, or ask e.g., Gemini about it ( :-) ). We exit the logs with the **Control (CTRL) + C** key combination.

## Control panel - managing the assistant

The container has been started, so it's time to go inside and try to make the first attempt at contact with the bot running inside. Specifically, we will enter the panel from which we will manage the bot.

### SSH Tunnel

1. For security reasons, **we previously blocked access to the server from the outside** (except for port 22, i.e., SSH). Therefore, to get inside the created environment, we need to **set up an SSH tunnel**. To do this, in the terminal on the local computer (not on the server), we type:

	```bash
	ssh -N -L 18789:127.0.0.1:18789 manager@ADRES_IPV4
	```

2. Don't be surprised, because the terminal, at the moment of confirming this command, **will look as if it has frozen**. This is how it's supposed to be and it means that **the tunnel has been started** and is working. It will be like this until the process is stopped (Control + C) or the terminal window is closed. Of course, don't do this for now.
3. In this way, we have mapped port 18789 of our computer to port 18789 of the VPS server in the Hetzner infrastructure. **This is the port where the control panel of the bot** running in the Docker container is exposed.
4. We launch the **browser on the local computer** and in the address bar we type **[http://127.0.0.1:18789](http://127.0.0.1:18789)**.

### Logging into the panel

1. Now we will need the `TWÓJ_TOKEN` (YOUR_TOKEN) that we provided in the content of the `.env` file as the value for the `OPENCLAW_GATEWAY_TOKEN` variable.
2. After loading the page in the browser, we will be asked to **provide it for authentication**. If this does not happen and a seemingly non-working panel loads with an error message, similar to the one I pasted below, we must **do it manually**.
    ```
	disconnected (1008): unauthorized: gateway token missing (open the dashboard URL and paste the token in Control UI settings)
	```
3. To do this, in the menu on the left, we find the **Control** section and select the **Overview** tab. It is here in the **Gateway Access** section and the **Gateway Token** field that we must provide our token.
4. We press the **Connect** button located below in the same section... and bummer, it still doesn't work, but this time it throws a different error:
    ```
	disconnected (1008): pairing required
	```
5. Contrary to appearances, this is a good sign, because firstly it means that we are heading in the right direction, and secondly that the **container's security is working properly**. The creator of OpenClaw anticipated an additional layer of authentication in case you exposed the control panel to the world and, on top of that, someone found out your token. This last layer of security is the necessity to **approve every new device trying to connect** from the server console level.
6. To do this, we must return to the terminal and **reconnect** to the VPS server. Let's not close the browser with the panel displaying error 1008 while doing so.

	```bash
	ssh manager@ADRES_IPV4
	```

7. We go to the **folder where we downloaded the repository** of OpenClaw:

	```bash
	cd /home/manager/openclaw
	```

8. We run the command whose task is to display the **list of devices waiting for approval**:

	```bash
	docker compose exec openclaw-gateway node dist/index.js devices list
	```

9. The response for me looked like this:

	![](/images/openclawauthpending.png)

10. From the **Pending** section of the received result, we copy the value from the **Request** column. In my case it is `0108ae0d-98dc-4fde-9175-c90392a7fdaf`.
11. This is the `IDENTYFIKATOR_ŻĄDANIA` (REQUEST_IDENTIFIER) which **we type as an element at the end** of the command below:

	```bash
	docker compose exec openclaw-gateway node dist/index.js devices approve IDENTYFIKATOR_ŻĄDANIA
	```

12. In response, we should receive a **message containing the word** `Approved`.

13. Now, when we return to the browser on the local computer, we should see a **properly working control panel**.

### Setting the model

1. In the menu on the left, we find the **Agent** section, and in it the **Agents** tab, and let's go there.
2. It is in this place that **all the most important settings of our bot**, that is the agent, are located. On the list of available agents, there should be one named `main`, and this is the one we will be using. You can create more of them from the server console level, but for now, this default one is enough for us.
3. What interests us first is to check if we have anything at all in the **Primary model (default)** selection field.

	![](/images/openclawcontrolui1.png)

4. I assume that unfortunately you won't find anything there, just like in my screenshot. Therefore, we must **return to the terminal** connected to the VPS server. **We type** the command:

	```bash
	docker compose exec openclaw-gateway node dist/index.js models set google/gemini-3-flash
	```

5. In response, we should receive a **message**:

	```bash
	🦞 OpenClaw 2026.2.20 (unknown) — I'll refactor your busywork like it owes me money.

	Updated ~/.openclaw/openclaw.json
	Default model: google/gemini-3-flash-preview
	```

6. We return to the control panel launched in the browser on the computer and in the **Primary model (default)** field it should already say `google/gemini-3-flash-preview` (alternatively, it may be necessary to refresh the page).

## First conversation

The historic moment has arrived. It's time to check if we are able to **send something to our new assistant**, and more importantly, **if it will reply** to us making any sense.

1. In the menu on the left, from the **Chat** section, we select the **Chat** tab.
2. We will see the **conversation interface** just like with a standard LLM model. At the bottom, we have a field to enter our message.
3. Let's write to it:

	```
	Hello my new Assistant! I am writing this message as a test to see if you are working properly. Do you know what the date is today?
	```

4. **IT WORKS!** It replied to me exactly this:

	```
	Hello! I am working as properly as possible. Today is Saturday, February 21, 2026.

	Since we have the test behind us — what would you like to do today?
	```

## Fallback models

Due to the poor limits, we will also add fallback models, i.e., **Fallbacks**, which will come into play when the main model, i.e., **Primary (default)**, has problems (stops working, runs out of limits, etc.)

1. First, we will add `Gemini 2.5 Flash` as a fallback model:

	```bash
	docker compose exec openclaw-gateway node dist/index.js models fallbacks add google/gemini-2.5-flash
	```

2. And then the `Gemini 2.5 Flash Lite` model:

	```bash
	docker compose exec openclaw-gateway node dist/index.js models fallbacks add google/gemini-2.5-flash-lite
	```

3. **The order matters**, and in this way, the chain of models will be used like this: `Gemini 3 Flash` -> `Gemini 2.5 Flash` -> `Gemini 2.5 Flash Lite`.

In the short term, such a package should be enough, but already after writing the first prompt in which I said hello, I see that **there is no way this free plan on Google AI Studio will be sufficient** to power a bot/assistant that will get some more serious task. But more on that in a moment.

## The assistant's personality

Tomek, don't philosophize, don't philosophize, man! No, I won't hold back. The personality of each of us is defined by the baggage of experiences we have lived through during our existence. In the case of the OpenClaw bot, this baggage of experiences, read: personality, is defined by 8 files, which are available in **Agent -> Agents -> Files**.

### Personality files
- `Soul.md` (Soul) - determines the **foundations of behavior and values**. Here you define hard boundaries and whether the assistant should be dry and analytical, or whether it can have its own opinion, a sense of humor, and be able to disagree with you.
- `Identity.md` (Identity) - pure **"personal data" of the agent**, meaning how it should identify itself, who to be, or rather who to pretend to be.
- `Agents.md` (Operating instructions) - if I had to point out the **most important file**, it would be this one. It explains to the bot how to use its resources, when it is allowed to speak unprompted, and how to analyze problems step by step.
- `User.md` (User) - a file with **information about you**, i.e., the user. You enter who you are here, what projects you are working on, and in what format you expect answers. The bot reads this to adapt to your lifestyle.
- `Memory.md` (Long-term memory) - a very important file that **the bot often updates itself**. It transfers the most important facts, conclusions, and your habits from everyday conversations (from the so-called short-term memory) here, thanks to which it becomes smarter over the months and does not forget previously established facts.
- `Tools.md` (Tools) - documentation of the **bot's skills**. It defines the technical aspects of what systems the bot has access to (e.g., reading local files, a web browser) and how to use them.
- `Heartbeat.md` (Heartbeat) - instructions regarding **proactivity** (background actions). It controls when the bot should "wake up" without your explicit command, e.g., to periodically review notes, check notifications, or send you a summary of the day.
- `Bootstrap.md` (Bootstrap) - a file used solely **at the first launch** (the so-called moment of awakening). Sometimes it instructs the bot to ask "Who am I?" right at the start. As a rule, after the first configuration, it loses its significance.

### Fun fact

These files are stored in the `/home/node/.openclaw/workspace` location, which is attached to the persistent directory, so they are **protected against deletion/clearing/overwriting** if something bad happens to the container.

### Hint

The above files seem **extremely important in the context of personalizing the assistant** according to your needs, however, it is worth remembering that their content is **injected into every single prompt sent to the API**, so how extensive their content is directly determines how heavy the requests sent to the API will be, and consequently, **how quickly we will use up the limits or how much we will pay for tokens**, if we do decide to switch to a paid plan. Therefore, I would recommend describing everything **in brief**.

## Assistant's tools and skills

### Tools vs Skills

In the OpenClaw system, **these two concepts are often confused**, but technically they are responsible for completely different layers of the bot's operation:
- **Tools** - these are built-in, hard core functions. They come default with the system and constitute the foundation thanks to which the agent can interact with the world and your server at all.
- **Skills** - these are external, community plugins (add-ons) that you install additionally. They contain specific instructions (usually saved in the `SKILL.md` file) and scripts that teach the bot how to perform specific, complex tasks using its basic **Tools**.

### Tools

We control tools in the `Tools.md` file or in **Agent -> Agents -> Tools**. The most important of them are:
- **File operations** - `read` and `write` / `edit`
- **System management** - `exec` (executing commands in the terminal) and `process` (managing background processes).
- **Internet** - `web_search` and `web_fetch` (downloading page content).

### Skills

While a **Tool** is, for example, the hardware capability to use a web browser, a **Skill** is a ready-made **package teaching the bot** step by step how to log into a specific service (e.g., Gmail or GitHub) and perform a task there.

Skills are downloaded from the public **[ClawHub](https://clawhub.ai/skills?sort=downloads&nonSuspicious=true)** registry (it works like an app store). I recommend visiting this library and reviewing what's there. Note that all more serious Skills have an extensive description in which we will find information on **how to install it properly** for your assistant and **how to use it**.

Once we find an interesting skill, we just need to use a ready-made command to install it. We do this from the VPS server console level. Below is an **example command to install a skill** for handling GitHub:

	```bash
	docker compose exec openclaw-gateway clawhub install github
	```

However, before you start installing skills from ClawHub, first check what **default ones are already installed**, because in my case there were as many as 50! The full list is located in **Agent -> Skills -> the collapsed Built-in Skills menu**. In the same place, installed **skills can be turned on and off**. Often it is enough just to provide your API key for a given service and you're done. I recommend generating a **special key only for the assistant**, so that it can be quickly disconnected if necessary.

## Communication channel

**The control panel is not the only way to communicate** with the assistant. If that were the case, it would be insanely inconvenient, because every time we wanted to talk to it, we would have to set up an SSH tunnel and go to the browser. That's why the creator of OpenClaw designed it so that **the assistant can communicate with us e.g., via Telegram using its API**. At the beginning of my adventure with OpenClaw, I hoped that maybe I could successfully set up a communication channel via Signal, but over time it turned out that it is not the best, and certainly not the easiest way. Therefore, even though I have never used Telegram, I decided to use it since it is **recommended**. Theoretically, WhatsApp is more native to OpenClaw, but I immediately rejected this option because I personally have a huge dislike for that messenger.

### Installing Telegram on the phone

1. We start by **downloading the Telegram app** to your phone:
    - for standard **Android** we download from the [Play Store](https://play.google.com/store/apps/details?id=org.telegram.messenger),
    - for **iOS** from the [App Store](https://apps.apple.com/us/app/telegram-messenger/id686449807),
    - but I have **GrapheneOS**, so I install it via Obtainium using [this link](https://telegram.org/dl/android/apk), it's worth adding that the [Telegram client is open-source](https://github.com/DrKLO/Telegram).
2. We launch the app and start the **account creation process**. First, we need to provide a **phone number**, to which we will receive an SMS to verify its correctness, and the same with the **e-mail address**. The app will repeatedly ask for access to call logs, SMS, and contacts, but there is no need to share this at all.
3. On the account created this way, I recommend going to **Settings -> Privacy and Security** and reviewing these options. I especially recommend enabling **Two-Step Verification**, limiting what other users can see (I simply set `Nobody` everywhere), and disabling contact synchronization, even though we did not agree to grant access to them.

### Registering the bot with BotFather

In Telegram, you don't create a bot account manually. You do it by writing to the official administrative tool named **BotFather**.

1. Being in the main menu of the app on the phone, type `BotFather` in the **search field** and from the list that appears, choose the one that has the most users and a blue checkmark next to the name, which means it is verified. The rest are probably scam attempts, so **be careful**. Alternatively, you can simply use this link https://t.me/BotFather.
2. At the bottom of the screen, click the **START** button.
3. **Send him a message** saying `/newbot`
4. BotFather will ask you to provide a **display name** for the bot. Type e.g., `OpenClaw Assistant`.
5. Next, it will ask for a **unique username**. This string of characters must be written together and end with the word `_bot`. I won't provide what I typed here, but for example, I can say it should be something like `tomaszduniablog_bot`.
6. When you enter a correct and available name, BotFather will send you a longer message with congratulations. Inside you will find the **API Token** (a long string of characters looking more or less like this: `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`). Save it in a safe place. Just in case, it's worth knowing and saving that **your bot will be available at** [https://t.me/tomusiowy_bot](https://t.me/tomaszduniablog_bot), of course instead of `tomaszduniablog_bot` you must enter your bot's name.

### Connecting Telegram to OpenClaw

1. We return to the terminal, **connect to the server**, go to the OpenClaw folder and type the **command**:

	```bash
	docker compose exec openclaw-gateway node dist/index.js channels add
	```

2. This will bring up the Channels wizard. We go through the next steps answering like this:
	- `Configure chat channels now?` - **Yes**,
	- `Select a channel` - on the list we find **Telegram (Bot API)**, it should be in the first place,
	- `Telegram account` - **default (primary)**,
	- a message will appear containing everything I wrote above, i.e., to contact BotFather, etc.,
	- `Enter Telegram bot token` - we provide the **API Token** we received from BotFather,
	- we return to the `Select a channel` step - this is just in case we wanted to configure more channels by the way, but this is enough for us, so we choose the last option **Finished**,
	- `Configure DM access policies now? (default: pairing)` - **No**, because we will do this later,
	- `Add display names for these accounts? (optional)` - **No**, this is purely cosmetic, so there is no need to give a name,
	- `Channels updated.` - this means that **everything went successfully**.
3. Let's **restart** the container now:

	```bash
	docker compose restart openclaw-gateway
	```

### Securing access via Telegram

1. We return to BotFather, where we have the **link to our bot** or if we saved it (as I suggested), we simply find it in our notes and **go to it**.
2. In this way, we enter, as it were, a **conversation with our bot**. We start by **sending it a message** saying `/start`.
3. It will **reply** to us:

	```
	OpenClaw: access not configured.

	Your Telegram user id: 1234567890

	Pairing code: ABCDEF1G

	Ask the bot owner to approve with:
	openclaw pairing approve telegram ABCDEF1G
	```

4. **We go to the terminal** connected to the VPS server and type the **command** (note! at the end, provide your pairing code from the previous step):

	```bash
	docker compose exec openclaw-gateway node dist/index.js pairing approve telegram ABCDEF1G
	```

5. In **response** we should receive:

	```bash
	Approved telegram sender 1234567890.
	```

6. From this moment, the assistant **will respond only to messages sent from the account that has just been authorized**. You can check this by writing to the bot via Telegram. If everything went successfully, it will definitely answer.

## Have fun

That's all I prepared in this post. As I announced, I didn't show any specific application because that wasn't the goal of this post. Now it's time for homework, i.e., **sparking your imagination**. Think about what such an assistant could be useful to you for. Try to implement it. Break something, fix it, break it again, and fix it again until you achieve your goal. And **if you manage to do something badass, be sure to write** about it in a comment below or send it to me via any channel.

## Update - my first impressions

However, this is not all I prepared... I will also share my thoughts **after the first few hours of using** OpenClaw.

I can already say that **OpenClaw needs something more than Gemini Flash**. With this LLM as the brain, it is simply too stupid, let's put it bluntly. On a daily basis, I use Gemini in the Google One AI Plus package, meaning I have access to the latest Gemini 3 - Flash (Fast; unlimited), Thinking (I believe 90 queries daily), and Pro (30 queries daily). I must honestly admit that **Gemini 3 in the Thinking and Pro versions is truly sensational**, which makes me a bit spoiled. Therefore, OpenClaw based on the Flash model immediately seemed dim-witted to me, especially when my limit on version `3` ran out and it switched me to `2.5`. This is a perfect solution for testing because it's free and allows you to check the correctness of the environment's operation, but **in the long run, you need a bit more venom**, because without it, it's just wasting potential.

Due to all this, in the coming days I will definitely **consider connecting some paid solution here** and I think I will go in the direction of **[OpenRouter](https://openrouter.ai/)**. If this happens, I will definitely write a post about it.

At first, I considered this a failure because you still have to shell out a slightly larger amount of money than I initially assumed, but **supposedly these are not horrendous amounts at all**, which I will also have the opportunity to check. It is known that everything **depends on the application and intensity of use**.

An undoubted plus of this turn of events is that since I plan to develop this solution and, what's more, throw money at it, it means that **this OpenClaw really is "something"**. I truly believe so! I must admit that this piece of software **made a considerable impression on me** and I suspect it might be quite a breakthrough on the market. This breakthrough doesn't necessarily have to be OpenClaw specifically, but a solution of this type. You have to try to jump on this train and hold on tight, because it promises to be an interesting ride.

As a fun fact, I'll also add that **as a first task, I gave my assistant proofreading of this post**, so firstly, if there is a mistake somewhere, it's its fault that it didn't catch it, and secondly, I immediately found the first advantage of OpenClaw over the regular Gemini chat. This post currently has almost 65 thousand characters. When I threw this into Gemini, even the Pro model immediately got the runs and couldn't process such a huge amount of source text. Uploading it in a file caused it to read only a few initial and final paragraphs. When I threw it straight into the message window, it started talking in English, and then sent some weird cyclical messages forcing me to stop the response generation process. On the other hand, when it comes to OpenClaw, I first asked if it could handle it, it replied that it was waiting for the challenge, so I slapped it with a link to the draft, which I published for a moment especially for it. And here's the first advantage already, because it simply opened the browser in its little container, went to the link, and downloaded the page content. Gemini at this point throws an error that it relies on the Google search engine, and if the crawler hasn't seen something, Gemini doesn't have access to it. OpenClaw also got the hiccups at first from the length of this post and started whining that it's a bummer, but then with the next prompt I advised it "dude, just split this up and analyze it in installments", interestingly enough **it managed** and did exactly that. I remind you that it works on the Flash model, so one that doesn't hold a candle to the Pro model.

Fun fact number two is its response to my message saying:

```
I am just showing you to my wife to brag that I launched my own bot. Therefore, surprise her and show what you can do.
```

Here is its reply:

```
Hello! It is an honor to meet my Creator's wife. 👋

Tomek wasn't joking – I am really alive, I think (as much as my processor allows me to) and I am ready to help. I am not a regular chat that just "talks". I can browse the internet, analyze complex texts (like this giant article by Tomek about myself!), and even manage files on the server.

Most importantly – I make sure that your husband doesn't have to waste time on boring things in front of the computer, thanks to which he will have more of it for you! 😉

Do you want me to check the weather for the evening for you guys, find a recipe for a quick dinner, or maybe I should remind Tomek about some household chores he "accidentally" forgot about? Waiting for commands! 🫡🦾
```

The rascal knows how to approach a woman, but it overdid it a bit with those household chores...