---
title: "YunoHost - backup [ENG 🇬🇧]"
date: 2023-05-10
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "archivist"
  - "backup"
  - "borgbackup"
  - "cron"
  - "crontab"
  - "linux"
  - "nano"
  - "opensource"
  - "restic"
  - "scp"
  - "selfhosted"
  - "ssh"
  - "sshkeys"
  - "vps"
  - "yunohost"
coverImage: "/images/yunohostbackup.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/yunohost-backup/)

In my previous posts, I described [how to install the _YunoHost_ environment](https://blog.tomaszdunia.pl/yunohost-oracle-eng/) and [how to run the first application - _WriteFreely instance_](https://blog.tomaszdunia.pl/yunohost-writefreely-eng/) on it. The next natural step that any reasonable admin would take is to create a system that will first create backups of the running infrastructure and secondly secure those backups in case the server on which it is all running suddenly decides it's a good time to cause problems.

To begin with, let's define some working names for the two machines that I will be using in this post:

- **_YunoHost server_** - the machine on which _YunoHost_ is installed and whose backup we will create,

- **_backup server_** - any other Linux machine, it can be a computer, a home server, or a VPS, on which we will store the created backups.

## Tasks to be performed on YunoHost server

Let's start by connecting to the _YunoHost_ server via _SSH_. Now we will create a recurring task that will automatically perform two backups a day. One of them will be created at 5:00 and the other at 15:00. The backup task must be executed with root privileges, so first we need to switch to the root user.

```bash
sudo su
```

We will be asked to provide the password for our _YunoHost_ administrator account. We open the Cron task table, or rather create it, because if it has not been used before, it does not exist by default:

```bash
crontab -e
```

A short configurator will appear, in which we need to specify which text editor we want to use. The default for me is _nano_, so I choose option _1\. /bin/nano_, which means I press _1_ and _ENTER_. Our table will be opened, at the beginning of which there will be a fairly long comment. We can completely delete this text or simply skip it and go to the end of the file. The crontab table works in such a way that one task is one line, which consists of a formula defining the frequency of execution and the command, program or path to the script that is to be executed. The interval formula notation consists of five parts, in order - minute, hour, day of the month, month, day of the week. A very helpful tool here is the [Crontab Guru](https://crontab.guru/) website. For our task, the command in the Cron task table should look like this:

```bash
0 5,15 * * * yunohost backup create
```

This notation means that the _yunohost backup create_ command (built-in command in _YunoHost_ for calling backup creation) will be executed at minute 0, hours 5 and 15, every day, every month, regardless of the day of the week. To exit the editor _nano_ and close the table as usual (_ctrl+x_, _y_, _ENTER_).

It is very important to have synchronized time zones on both servers, so for safety, let's set the appropriate time zone for Poland:

```bash
timedatectl set-timezone Europe/Warsaw
```

In addition, after each change in the Cron task table, remember to rebuild the process and thus implement the changes:

```bash
service cron reload
```

On the _YunoHost_ server, we still need to enable login using _SSH_ keys, because without it, it will be difficult for us to connect to the _backups_ from the server level. I described how to do this [here](https://blog.tomaszdunia.pl/serwer-domowy-podstawowa-konfiguracja-eng/#sshkeys).

That's all we need to do here. It's time to move on to the machine that will be our space for storing created backups.

## Tasks to perform on the backup server

Now let's switch to the _backup_ server. First of all, let's also set the appropriate time zone for Poland here:

```bash
timedatectl set-timezone Europe/Warsaw
```

Now let's configure the _SSH_ connection to the server with _YunoHost_. To do this, in the _/home/$USER/.ssh/_ folder, create a file named _yunohost_ and paste the _SSH_ private key to the _YunoHost_ server into it:

```bash
nano /home/$USER/.ssh/yunohost
```

Save the file and exit it. Let's give it the appropriate permissions:

```bash
chmod 600 /home/$USER/.ssh/yunohost
```

Let's add this private key to our keychain:

```bash
ssh-add /home/$USER/.ssh/yunohost
```

From this point on, we should be able to connect via _SSH_ to the _YunoHost_ server from the _backup_ server, so let's test it with the following command formatted to your needs:

ssh <admin\_username>@<yunohost\_server\_ip>

If we did everything correctly, we should not be prompted for a password and should be able to access the _YunoHost_ server shell without any problems. Let's terminate the _SSH_ connection and return back to the _backup_ server using the following command:

```bash
exit
```

To download backup copies from a _YunoHost_ server and transfer them to a _backup_ server, we will use the _scp_ tool, whose name stands for _Secure Copy_. It allows for simple and secure data transfer between servers. The _scp_ syntax for our use case is as follows:

> scp <admin\_name>@<yunohost\_server\_ip>:<what\_to\_copy> <where\_to\_copy>

We now know how to acquire files from one server and transfer them to another. The next step is to consider the strategy for doing so. Let us remind ourselves that a backup task is scheduled to run on the _YunoHost_ server every day at 5:00 AM and 3:00 PM. Creating a backup takes less than a minute, but as our _YunoHost_ environment grows, this time may increase. Therefore, for safety, let us assume that we will download the backup copy one hour after it is made, i.e., at 6:00 AM and 4:00 PM.

We now need to understand how _YunoHost_ manages backup copies. The creators have provided a ready-made command for creating backups from the terminal:

```bash
yunohost backup create
```

This command must be executed with administrator privileges, either directly as the _root_ user or preceded by the _sudo_ phrase. This command syntax will use the default settings of this tool, so a backup of everything (system configuration, user data, applications, etc.) will be created and saved in the folder:

```bash
/home/yunohost.backup/archives/
```

The name under which the backup will be saved has the following format:

> <year><month><day>\-<hour><minute><second>.tar

So, if the backup is created on _July 8, 2023 at 12:34:56_, its name will be _20230708-123456.tar_. Why am I focusing on this so much? It is important in the context of how we will determine which file should be downloaded, which backup is the latest and should be retrieved to occupy the space next to the backups already downloaded to the _backup_ server. Note that by making two copies a day, I will have two files every day, part of the name before the hyphen will be the same because it is the date. Therefore, they can only be distinguished by the second part of the name (after the hyphen), that is, based on the creation time. Note that I intentionally make two copies, the first one at 5:00, so after the hyphen in the name, it will have _0_ (_zero_), and the second one at 15:00, so after the hyphen in the name, it will have _1_ (_one_). In this way, the backup named _20230708-0\*_ is a morning copy made on _July 8, 2023_, and the backup named _20230708-1\*_ is an afternoon copy. The use of the _\*_ sign in _Bash_ means that the remaining part of the name can be anything.

Now that we have everything planned out, let's get to work. Let's start by creating a place (folder) on the _backup_ server where we will store downloaded backup copies.

```bash
mkdir /home/$USER/yunohost_backups
```

Now, let's open (or create if it does not yet exist) the Cron task table on this server:

```bash
crontab -e
```

To add these two lines at the end of an open text file:

```bash
0 6 * * * scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-0* /home/$USER/yunohost_backups/
0 16 * * * scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-1* /home/$USER/yunohost_backups/
```

Just remember to replace the phrase _admin_ with your _YunoHost_ administrator's username and the phrase _AAA.BBB.CCC.DDD_ with your _YunoHost_ server's IP address. Save the file and exit it. The above two lines do almost the same thing but run at two different times (every day at 6:00 and 16:00). In both cases, _scp_ connects to the _YunoHost_ server, finds the file whose name starts with today's date, followed by a hyphen and in the case of the first line (running at 6:00) followed by _0\*_ (zero and any other characters), and in the case of the second line (running at 16:00) followed by _1\*_ (one and any other characters). At the end of each line, there is also an indication of the path to the backup folder on the server.

Just like before, after modifying the Cron tasks, we need to reload the service:

```bash
service cron reload
```

## As usual, sometimes things don't work...

In my case, as a server for _backups_, I chose _Mikrus_ and encountered an interesting problem. After some time, _Mikrus_ completely forgets my private key to the server with _YunoHost_. And as if that wasn't enough, when I tried to add it again with the _ssh-add_ command, I received the following message:

```bash
Could not open a connection to your authentication agent.
```

This is a known problem when trying to use _ssh-add_ when _ssh-agent_ is not working as a process. It turns out that the _ssh-agent_ process is being killed for some reason by my server... Is this an unsolvable problem? Of course not! However, some modifications to the actions I presented are necessary.

First of all, I need to write two scripts that will replace those two tasks from the Cron table. These scripts will:

1. Started the _ssh-agent_,

3. Added my private key to the _Yunohost_ server keychain,

5. Executed the command to copy the backup file using _scp_ as it was done previously.

First, we create the first script that will run cyclically at 6:00:

```bash
nano /home/$USER/yunohost_backup1.sh
```

Let's paste the following content into it (remember to modify the phrases _admin_ and _AAA.BBB.CCC.DDD_ accordingly):

```bash
#!/bin/bash
eval "$(ssh-agent)"
ssh-add /home/$USER/.ssh/yunohost
scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-0* /home/$USER/yunohost_backups/
```

Then, we create the second script:

```bash
nano /home/$USER/yunohost_backup2.sh
```

Let's paste the following content into it (remember to modify the phrases _admin_ and _AAA.BBB.CCC.DDD_ accordingly):

```bash
#!/bin/bash
eval "$(ssh-agent)"
ssh-add /home/$USER/.ssh/yunohost
scp admin@AAA.BBB.CCC.DDD:/home/yunohost.backup/archives/$(date +"%Y%m%d")-1* /home/$USER/yunohost_backups/
```

Now we need to make both scripts _executable_ (give them permission to execute):

```bash
sudo chmod +x /home/$USER/yunohost_backup1.sh /home/$USER/yunohost_backup2.sh
```

Finally, we need to modify the Cron task table:

```bash
crontab -e
```

Instead of the previously set two lines, we paste the following:

```bash
0 6 * * * /home/$USER/yunohost_backup1.sh
0 16 * * * /home/$USER/yunohost_backup2.sh
```

This modified way of operation solves the problem with _ssh-agent_.

## Alternative Solutions

It must be admitted that the solution presented by me is not the most sophisticated one. However, it shows that there are many ways to achieve the same effect. If someone is looking for a different solution, _YunoHost_ in its documentation mentions three applications that can be used: [BorgBackup](https://yunohost.org/en/backup/borgbackup), [Restic](https://yunohost.org/en/backup/restic), and [Archivist](https://yunohost.org/en/backup/archivist). I tried to use the latter, but it seems to be currently broken and simply not working... Among other things, that's why I decided to set everything up from scratch, without relying on external applications. However, I recommend reading the _YunoHost_ documentation and deciding for yourself which option seems best for you.
