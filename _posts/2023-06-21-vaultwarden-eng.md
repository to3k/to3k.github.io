---
title: "Vaultwarden - self-hosted password manager [ENG 🇬🇧]"
date: 2023-06-21
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "2fa"
  - "android"
  - "backup"
  - "bitwarden"
  - "chrome"
  - "docker"
  - "dockerhub"
  - "firefox"
  - "https"
  - "ios"
  - "ipados"
  - "opensource"
  - "passwordmanager"
  - "selfsignedcertificate"
  - "selfhosted"
  - "ssl"
  - "totp"
  - "u2f"
  - "vaultwarden"
  - "yubico"
  - "yubikey"
  - "yunohost"
coverImage: "/images/vaultwarden.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/vaultwarden/)

Strong passwords are incredibly **important**! It is one of the foundations of internet security. The best solution is to have passwords consisting of **at least** 16 characters, including lowercase and uppercase letters, as well as numbers and special characters. It is also crucial **not to have the same password for each service**, because if it leaks from one of them, scammers/thieves/burglars will first check it on other popular portals. Looking at all of this raises the question - _How to remember all these complex character strings in your head?!_ Saving them in a notepad on your computer is not a very secure solution, and typing them from a physical notebook kept in a safe is a hassle. In such a situation, the password manager rides in on a white horse, and not just any, but specifically _**Bitwarden**_, which can be **self-hosted on your own server**, which is what we will do because we don't like to entrust our data to third parties, especially when it comes to our passwords.

In this post, I will approach the matter similarly to the [article about _Nextcloud_](https://blog.tomaszdunia.pl/nextcloud-eng/), that is, I will show two ways to run your own instance of _Bitwarden_ (specifically, the implementation of _Vaultwarden_):

1. [on a server with YunoHost](#yunohost),

3. [using Docker on any other server](#docker).

![](/images/vaultwarden2.png)

## Running on YunoHost

The installation process will be similar to the one described in the [WriteFreely post](https://blog.tomaszdunia.pl/yunohost-writefreely-eng/), but when running _Vaultwarden_, we don't need a separate domain (just like in the [Nextcloud post](https://blog.tomaszdunia.pl/nextcloud-eng/)). In fact, when running it only for ourselves, it's not even recommended to create a special domain. Firstly, it's an additional cost, and secondly, it's better not to reveal all our cards and expose our data by using a subdomain like _bitwarden.tomaszdunia.pl_, which would clearly indicate that all our passwords are located at that address. In general, I advocate for **keeping such services in a local network accessible only through a VPN** like _WireGuard_. However, I will discuss this in a completely different post at another time.

We start by logging into our _YunoHost_ admin panel and immediately go to _Applications_. Then, in the top right corner, click the green _\+ Install_ button, search for the _Vaultwarden_ application, and select it from the list. Scroll down to the _Installation settings_ section and begin the configuration:

![](/images/vaultwarden_yunohost2.png)

1. In the text field _Label for Vaultwarden_ \[1\], enter the name under which you want to see this application on the list of applications in your YunoHost.

3. From the drop-down list below \[2\], select the domain on which Vaultwarden should be installed. As you can see, I chose the main domain on which my YunoHost is running. You can do the same or choose a different domain from the list.

5. In the next text field \[3\], define the exact path under which Vaultwarden should be installed. By default, entering the value _/vaultwarden_ will install it at _example.domain.com/vaultwarden_, where _example.domain.com_ is the domain you selected above. If you have decided to use a dedicated domain only for Vaultwarden, you can enter _/_ here, which will mean installation in the parent directory of the domain.

7. Next, we have a decision field \[4\] _Should this application be accessible to anonymous users?_ Here, I suggest selecting _Yes_ because otherwise, Vaultwarden clients (referring to the official Bitwarden application) will not work, as an additional authentication step will appear, requiring login to YunoHost, which is not supported.

9. Another drop-down list \[5\] is used to indicate which YunoHost user should be an administrator for this application.

11. Confirm the above settings by clicking the _Install_ button \[6\], which will start the installation process, which unfortunately is not the shortest, so patience is required.

After the installation process is completed, connect to the server where YunoHost is running via SSH. Then, log in as the _root_ user:

```bash
sudo su
```

We open the application settings file for _Vaultwarden_:

```bash
nano /etc/yunohost/apps/vaultwarden/settings.yml
```

In this file, we need to locate the following line:

```yaml
admin_token: [token]
```

We copy the value _\[token\]_, which we will need to log in to the admin panel of _Vaultwarden_. At this stage, we no longer need the SSH connection to the server. The admin panel is accessible at the address, beginning with the address we selected for the _Vaultwarden_ application during installation, and ending with _/admin_. We enter the copied _token_ there, which will allow us to access the admin panel, where we immediately go to the _Users_ tab \[1\].

![](/images/vault1.png)

At the bottom, there is an _Invite User_ section. In the text field \[2\], enter your email address and confirm with the _Invite_ button \[3\].

![](/images/vault2.png)

The above action will result in a new user appearing on the list \[4\].

![](/images/vault3a.png)

In the meantime, an invitation with an activation link will be sent to the provided email address. Click the _Join Organization Now_ button \[5\].

![](/images/vault4.png)

You will be redirected back to the browser, where you will see a message saying that you have been invited to the organization and can now proceed. Click the _Create an Account_ button \[6\].

![](/images/vault5a.png)

We will be redirected to the standard registration form, where we provide an email address \[7\], username \[8\], password (twice) \[9\], and optionally a password hint \[10\]. In the end, we can also decide \[11\] whether we want our password to be checked against known password breaches. However, I use the website [HaveIBeenPwned.com](https://haveibeenpwned.com/) for this purpose, so I always uncheck this option. Confirm the filled form by clicking the _Create Account_ button \[12\].

![](/images/vault6a.png)

## Running as a Docker container

Don't have a _YunoHost_ server? No worries! You can do the same using _Docker_! I recommend first reading my post on [_Docker - one server, multiple services_](https://blog.tomaszdunia.pl/docker-eng/). We will use a fork called [_Vaultwarden_ available on _Docker Hub_](https://hub.docker.com/r/vaultwarden/server) as the image.

We start by creating a folder for this container:

```bash
mkdir -p /home/$USER/docker/vaultwarden
```

Next, we create a configuration file for this container:

```bash
nano /home/$USER/docker/vaultwarden/docker-compose.yml
```

The configuration process for _Vaultwarden_ as a container is relatively simple:

```yaml
version: "3"

services:
  vaultwarden:
    container_name: vaultwarden
    image: vaultwarden/server:latest
    ports:
      - "80:80"
    environment:
      PUID: '1000'
      PGID: '1000'
      TZ: 'Europe/Warsaw'
    volumes:
      - '/home/$USER/docker/vaultwarden/volumes/data:/data'
    restart: unless-stopped
```

In the above configuration, you need to check and adjust the following according to your needs:

- the port on which this container should run, for example, I entered port _80_,

- _PUID_ and _PGID_, as described in the [Nextcloud container post](https://blog.tomaszdunia.pl/nextcloud-eng/).

At this stage, we still need to create the appropriate _volume_ that we declared as the location for storing container data:

```bash
mkdir -p /home/$USER/docker/vaultwarden/volumes/data
```

Let's also check if the port for accessing this container is open in our _firewall_:

```bash
sudo ufw allow 80
```

Finally, all that's left is to build and run the _Vaultwarden_ container:

```bash
docker-compose -f /home/$USER/docker/vaultwarden/docker-compose.yml up -d
```

To access the website, open your browser and enter the address consisting of the server's _IP_ and the port on which the container is running (if it's port _80_, there's no need to specify it since it's the default port). Check if the Vaultwarden page loads correctly. Unfortunately, it will display properly, but it won't function correctly, as you can see when trying to create a new user account. You will receive a message stating that an _HTTPS_ certificate is required to use our vault. So, for now, let's stop the container:

```bash
docker stop vaultwarden
```

Next, let's remove it:

```bash
docker rm vaultwarden
```

We need to create a so-called _self-signed certificate_, which is sufficient when using _Vaultwarden_ on a local network. If you want to share it with third parties (outside the local network), you can use [_Let's Encrypt_](https://letsencrypt.org) and associate it with a domain. However, for the purpose of this post, I have chosen a much safer solution and deployed the vault in a local network accessible via _VPN_ - _[Wireguard](https://www.wireguard.com/)_. Therefore, an external certificate is not needed.

First, we need to create a _Root Certificate Authority_, abbreviated as _CA_, which will be our private _certificate authority_ that will sign certificates for specific domains.  
We start by generating the _CA_ key:

```bash
openssl genpkey -algorithm RSA -aes128 -out private-ca.key -outform PEM -pkeyopt rsa_keygen_bits:2048
```

You need to provide a _passphrase_ that is 4 to 1024 characters long. Remember it! In this case, the risk is minimal, so I suggest following the _KISS_ rule - _Keep It Simple Stupid_. I strive for the _passphrase_ not to be complicated because if someone gains access to our local network and thus to the password manager, the possibility of them knowing the _passphrase_ will be our least concern. The result of the above command will be the creation of the _private-ca.key_ file.

Based on the generated key, we generate the _CA_ certificate:

```bash
openssl req -x509 -new -nodes -sha256 -days 3650 -key private-ca.key -out self-signed-ca-cert.crt
```

During the execution of this process, we need to enter the previously provided _passphrase_ and fill in a short survey where you can simply enter a dot (".") in each field and confirm with _ENTER_. The only thing worth filling in is the _Common name_ field, where you should enter the name of our certificate. I entered _vaultwarden_. As you can see in the command, we provided _\-days 3650_, which means our _CA_ will have a validity period of 10 years.

```bash
Enter pass phrase for private-ca.key: [podaj passphrase]
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
Country Name (2 letter code) [AU]:.
State or Province Name (full name) [Some-State]:.
Locality Name (eg, city) []:.
Organization Name (eg, company) [Internet Widgits Pty Ltd]:.
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:vaultwarden
Email Address []:.
```

The result of this command will be the creation of the file _self-signed-ca-cert.crt_.

Now we need to generate a key for the _Vaultwarden_ certificate:

```bash
openssl genpkey -algorithm RSA -out vaultwarden.key -outform PEM -pkeyopt rsa_keygen_bits:2048
```

The file _vaultwarden.key_ will be created. Next, we need to create a _certificate request file_:

```bash
openssl req -new -key vaultwarden.key -out vaultwarden.csr
```

Here's another quick survey where we insert dots everywhere except for the _Common name_ field, where we need to enter the address of our server, which can be an address on the local network (server's _IP_ address).

```bash
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
Country Name (2 letter code) [AU]:.
State or Province Name (full name) [Some-State]:.
Locality Name (eg, city) []:.
Organization Name (eg, company) [Internet Widgits Pty Ltd]:.
Organizational Unit Name (eg, section) []:.
Common Name (e.g. server FQDN or YOUR name) []:[adres ip serwera]
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.
```

A _vaultwarden.csr_ file will be created. The last file we need to create is:

```bash
nano vaultwarden.ext
```

Into which we paste:

```bash
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
IP.1 = [adres ip serwera]
```

As the _IP.1_ parameter, we enter the same address as before, which is the server's IP address. Save the file in this form and exit the editor.

Now we need to sign the created certificate with the previously created _CA_:

```bash
openssl x509 -req -in vaultwarden.csr -CA self-signed-ca-cert.crt -CAkey private-ca.key -CAcreateserial -out vaultwarden.crt -days 365 -sha256 -extfile vaultwarden.ext
```

The end result will be the creation of the _vaultwarden.crt_ file. It is worth noting that we set the validity of the certificate to 365 days. Why didn't we sign it for 10 years like we did for the _CA_? Unfortunately, some entities only consider certificates that are valid for a maximum of one year (plus or minus a few days) to be valid. In the case of _Apple_, for example, it is 398 days. Therefore, every year we will have to perform this last step and renew the _Vaultwarden_ certificate for another period.

Next, move the created and signed _Vaultwarden_ certificate along with its key to the certificates folder on our server:

```bash
sudo mv vaultwarden.crt vaultwarden.key /etc/ssl/certs
```

I suggest keeping the remaining files in the _/etc/ssl_ folder for future reference:

```bash
sudo mkdir /etc/ssl/CA
sudo mv vaultwarden.csr vaultwarden.ext private-ca.key self-signed-ca-cert.crt self-signed-ca-cert.srl /etc/ssl/CA
```

Once we have resolved the issue with the certificates, we enter the configuration file of the _Vaultwarden_ container:

```bash
nano /home/$USER/docker/vaultwarden/docker-compose.yml
```

and change its content analogously to the example below:

```yaml
version: "3"

services:
  vaultwarden:
    container_name: vaultwarden
    image: vaultwarden/server:latest
    ports:
      - "80:80"
    environment:
      PUID: '1000'
      PGID: '1000'
      TZ: 'Europe/Warsaw'
      ROCKET_TLS: '{certs="/ssl/vaultwarden.crt",key="/ssl/vaultwarden.key"}'
    volumes:
      - '/home/$USER/docker/vaultwarden/volumes/data:/data'
      - '/etc/ssl/certs:/ssl'
    restart: unless-stopped
```

As you can see, one environment variable and a _volume_ in which we saved the generated certificate have been added.

Unfortunately, this is not the end because creating your own certificate involves **transferring it to all devices** that will use the password manager. Without this, they will not be properly authenticated. To do this, we need to extract the _self-signed-ca-cert.crt_ file from the server and upload it to the memory of all devices we intend to use _Vaultwarden_ on.

Let's discuss how to apply it to the most popular browsers and devices:

- **_Firefox_** - _Settings_ -> _Privacy & Security_ -> _Certificates_ -> _View Certificates..._ -> _Certificate Authorities_ tab -> _Import..._ select the certificate from the disk, check the box _Trust this CA to identify websites._, and finally confirm with the _OK_ button. It's a good idea to restart the browser.

- **_Chrome_** - _Settings_ -> _Privacy & Security_ -> _Security_ -> _Manage certificates_ -> a _Certificates_ window will open -> _Trusted Root Certification Authorities_ tab -> _Import..._ -> _Next_ -> _Browse..._ -> select the certificate from the disk -> _Next_ -> _Finish_. You will probably see a _Security Warning_, confirm with _Yes_. It's a good idea to restart the browser.

- _**iOS**_ / _**iPadOS**_ - here it is enough to transfer the certificate to the device in any way and run it. A window will appear _Choose the device on which you want to install this profile_, where you select _iPhone_, and then the certificate should appear in _Settings_. Simply enable it in _Settings_ -> _General_ -> _VPN & Device Management_ -> _Configuration Profile_ section -> our certificate should be available for selection with the name we gave it -> _Install_ -> enter the device unlock code -> _Install_ -> exit _OK_. It is also necessary to add the certificate to trusted in _Settings_ -> _General_ -> _About_ -> _This Device..._ -> at the very bottom _Trusted Certificates Settings_ -> _Enable Full Trust for Root Certificates_ section -> activate our certificate so that the switch next to it is green -> in the window that appears, press _Next_ and it's done.

- **_Android_** - just like on _iOS_, you need to download the certificate to your phone in any way and open it. You will be asked if you want to open the _Certificate Installer_, confirm and you will be taken to a window where you enter the certificate name and select from the dropdown list that it should be used for _VPN and apps_.

Now that we have installed certificates for all devices, we can go to the address where _Vaultwarden_ is running and log in to the _vault_.

## Applications and browser extensions

When it comes to password managers, it's useful to have **mobile applications and/or browser extensions** that can search the password database and fill in the appropriate passwords on the respective websites. [_Bitwarden_ provides applications](https://bitwarden.com/download/) for all popular operating systems and extensions for all browsers. **They work with _Vaultwarden_**. However, in our case, to use these applications/extensions, **we need to specify our custom server**. After installation, on the login screen, go to settings (click the gear icon) and enter the server address (preceded by _https://_) where _Vaultwarden_ is running as the _Server URL_.

## Backup

Creating backups is always a **very important matter**. However, having a backup of a password manager vault is a matter of **life or death**. It doesn't matter whether we run _Vaultwarden_ in the cloud or on a home server, on new or old hardware. It is always necessary to **assume that something can go wrong and be prepared for it**. Personally, I cannot imagine losing access to my password database because it would kill my digital life. That's why I have multiple backups located in various places, on various types of media, and I recommend this practice to everyone.

## Bitwarden - basic configuration

In my case, besides taking care of backups, the configuration right after setting up my _vault_ consists of only two steps.

![](/images/vault7.png)

The first one is **enabling two-factor authentication during login**, because securing your passwords is essential. You can do this by expanding the user menu located in the upper right corner \[1\], entering _Account Settings_ \[2\], then on the left, the _Security_ tab \[3\], and _Two-Factor Authentication_ \[4\]. Here, you can configure security measures such as _TOTP_ (time-based one-time password apps), _Yubico_ hardware keys (_YubiKey_), or as a last resort (because it's the worst option) codes sent to your email inbox.

![](/images/vault8a.png)

The second task is **migrating my password database**. The import tool can be found in the _Tools_ tab \[5\] under _Import Data_ \[6\].

![](/images/vault9.png)
