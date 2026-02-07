---
title: "Docker - one server, many services [ENG 🇬🇧]"
date: 2023-03-18
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "backup"
  - "container"
  - "docker"
  - "dockerhub"
  - "dockercompose"
  - "dockerio"
  - "opensource"
  - "pihole"
  - "portainer"
  - "raspberrypi"
  - "selfhosted"
  - "tar"
  - "tcp"
  - "termius"
  - "udp"
  - "virtualmachine"
  - "vm"
  - "yaml"
coverImage: "docker.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/docker/)

I've previously written that I'm a huge enthusiast of **self-hosted** solutions, which means running on your own hardware or on a _VPS_ that you manage. [In previous posts](https://blog.tomaszdunia.pl/serwer-domowy-eng/), I've already written about how to create your own home server, so the natural next step is to run services on it. In this post, I'll introduce _**Docker**_, which is the most popular tool for _**virtualization**_, or running many small **_virtual machines_** inside one physical machine (server). These machines are called **_containers_**, and they are controlled environments for running specific applications. _Containers_ can be isolated from each other or connected in a controlled way. The advantage of this solution is that from one main server, you can manage many environments in a **very clear way**, on which many services will be running. An additional advantage of _Docker_ is that there are many **ready-made container images** available on the Internet, which, after quick configuration, usually limited to setting a few parameters, are ready to run.

EDIT: I was rightfully corrected by one of the Readers that **_Docker_ != _virtualization_**, and that **_containers_ are not _virtual machines_**. Indeed, this is true and I admit that I wrongly used a shortcut by referring to _Docker_ as _virtualization_. Why _Docker_ is not virtualization is concisely explained in [this article](https://www.freecodecamp.org/news/docker-vs-vm-key-differences-you-should-know/).

## Installation and basic configuration

I will describe everything as if we were dealing with a clean server, and everyone will adapt the following instructions to their situation. We start with **installing the Docker environment**.

```bash
sudo apt install docker.io docker-compose -y
```

These are packages **normally available in the APT repository**. I'm writing about it because in some Docker tutorials, you may come across the _docker-ce_ package, which in practice is the same, but is located in an external, official _[docker.com](https://docker.com)_ repository, which would require connecting to the server. I don't see the need to take additional steps, so we use the package provided by the default repository. After a successful installation, the service should start immediately, but let's check it with the following command just to be sure:

```bash
sudo systemctl status docker
```

If by some chance we received a response containing the phrase _inactive_, it means that something suspicious went wrong. Sometimes it's enough to manually start the process:

```bash
sudo systemctl enable --now docker
```

Sometimes, however, it may be necessary to restart the entire server. If even that doesn't help, as a result of executing the above command, we should receive some error message. Errors can be various, so I am not able to describe all the possibilities in this post. However, in order not to leave anyone in need, I suggest that you, dear Reader, leave a comment with the copied error message, and I will try to help as much as I can.

After installation, a special group should also be created for users dedicated to working with _Docker_. It is a good practice to make sure that such a group exists, and if not, create it:

```bash
sudo groupadd docker
```

Then, you should add your user to this group:

```bash
sudo usermod -aG docker $USER
```

Now, in order for the changes to take effect, i.e. for our user to actually have new permissions, you need to log out and log back in to the server. From experience, I can also add that sometimes a _reboot_ of the entire machine is necessary.

## Running a sample container

Let's now try to run a sample _container_. For this purpose, I have chosen _pi-hole_, which is a DNS server service that can be used, among other things, to moderate network traffic that we allow through it. That's in a huge nutshell, because I will definitely write a separate post about _pi-hole_, and here it will only serve as an example. _Docker containers_ can be run in many ways, but the most popular ones are:

- _**docker run ...**_ command, which is convenient for quickly running simple containers,

- **docker-compose**, which involves creating an appropriate configuration file in _.yml_ format and its _compilation_ (or _composition_ from _compose_). This is the preferred solution for me,

- using a **GUI tool** that allows managing containers in a more user-friendly way (for some people) because it does not require using the terminal. An example of such a tool is _[Portainer](https://www.portainer.io/)_.

In this post, we will use the method based on using _docker-compose_. We start by creating a folder dedicated to _Docker_ in the home directory of our user and a subfolder for the _container_ that we are creating.

```bash
mkdir -p /home/$USER/docker/pihole
```

Next, let's create the _docker-compose.yml_ configuration file inside which is necessary to create the given _container_ and its subsequent update, because updating the _container_ actually involves deleting it and creating a new one with the appropriate files and settings, but more on the update process later.

```bash
nano /home/$USER/docker/pihole/docker-compose.yml
```

The contents of the basic _pi-hole_ _container_ configuration file should look as follows:

```yaml
version: "3"

services:
  pihole: # working container name (not very important, only for the purpose of this file)
    container_name: pihole # the name by which this container will be identified (must be unique)
    image: pihole/pihole:latest # specifying which image to use
    ports: # section in which server port redirections to container ports are set
      - "53:53/tcp" # DNS using the TCP protocol
      - "53:53/udp" # DNS using the UDP protocol
      - "80:80/tcp" # HTTP
    environment: # section where so-called environmental variables are specified
      TZ: 'Europe/Warsaw' # an example variable specifying the time zone
    volumes: # section in which so-called volumes are defined, i.e., shared folders between the server and the container
      - '/home/$USER/docker/pihole/volumes/etc/pihole:/etc/pihole'
    restart: unless-stopped # the so-called restart policy, e.g., to restart the server or just the Docker process
```

If this isn't your first post you're reading on this blog, you know that my favorite way of describing code is through comments within it. That's what I did this time as well, and comments in _YAML_ files start with the _#_ sign. **_YAML_ files have a structure similar to a tree**, where bigger branches branch out into smaller ones and so on and so forth. In the _services_ section, we have only one _container_, because the example presented above is quite simple and there's no need to overcomplicate things at the beginning. However, it's worth mentioning that through one configuration file, you can start a group of _containers_ that will work together. For example, it can be a service and a necessary _MySQL_ database for it to work properly - like a tandem.

Despite explaining the code through comments, I would like to delve more into certain fragments:

- Line 6, in which we specify **which image we want to use**. The basic repository from which container images are sourced is [_Docker Hub_](https://hub.docker.com/). Custom repositories can also be added, but we will not focus on that here. The format is similar to that used on GitHub, where the first part is the name of the developer behind the image and the second part is the name of the image itself. After the colon, the version to be used is specified. In this case, we used _**latest**_, which means we are instructing the compiler to use the **newest** version.

- Lines 8-10, in which we **redirect server ports to container ports**. The syntax is such that before the colon, we specify the server port we want to redirect, and after the colon, the container port. Additionally, we can specify the _TCP_/_UDP_ protocol after the slash, but I emphasize that it's optional, as if we don't specify anything, the redirection will work for both protocols.

- Line 11, which is the section for **environment variables**. What does this proudly sounding name actually mean? Simplifying the issue to the minimum, it's a set of input data based on which we can easily modify the parameters of the _container_'s operation, provided of course that the developer behind a given image has provided such a possibility.

- Line 14, in which we created a **shared space between the server and the _container_**. This is a folder whose contents are identical on the server and inside the _container_. This is a crucial issue because such a shared folder remains on the server even after the complete annihilation of the _container_. _Volumes_ are essential in the process of updating _containers_, but we'll talk about that in a moment.

- Line 15, which is the **restart policy**, which specifies how the _container_ should behave when it is shut down due to some event. The following values can be set here:
    - **no** - never restart the _container_,
    
    - _**always**_ - restart the _container_ unconditionally until it is completely removed,
    
    - _**on-failure**_ - restart the _container_ if an error status is reported,
    
    - **unless-stopped** - restart the _container_ as long as it is not manually stopped (status _stop_).

We already know everything about the structure of the _docker-compose.yml_ file, so we can save it and exit. Now, we still need to create the _volume_ that we defined in the configuration file and open the ports in the _firewall_ that the container will use.

```bash
mkdir -p /home/$USER/docker/pihole/volumes/etc/pihole
sudo ufw allow 53
sudo ufw allow 80/tcp
```

Finally, we compile and run the container.

```bash
docker-compose -f /home/$USER/docker/pihole/docker-compose.yml up -d
```

## Managing Containers

We've completed the first run, so now we should learn how to manage _containers_. I will go through only the basic commands that are fundamental.

[Listing all running _containers_](https://docs.docker.com/engine/reference/commandline/ps/) (by adding _\-a_ at the end, all _containers_ that exist on our server, not just those that are running, will be shown):

```bash
docker ps
```

[Stopping a container](https://docs.docker.com/engine/reference/commandline/stop/) (example: _pi-hole_):

```bash
docker stop pihole
```

[Starting a stopped container](https://docs.docker.com/engine/reference/commandline/start/) (example: _pi-hole_):

```bash
docker start pihole
```

An alternative way of [running new containers](https://docs.docker.com/engine/reference/commandline/run/) that I use when I need to quickly launch a test container or run a service that is not very complex and does not require many parameters. In the example below, a test container _hello-world_ will be launched, which works by displaying a string of characters and then shutting down:

```bash
docker run hello-world
```

[Removing a container](https://docs.docker.com/engine/reference/commandline/rm/) (after it has been stopped using the _stop_ command):

```bash
docker rm hello-world
```

These are basically all the basic commands you need to know to operate _Docker_ at an acceptable level. For each of the above commands, I also added direct links to their documentation.

## How to access the container

A very useful feature of _Docker_ is the ability to access the shell of the _container_ just as if we were logging into a regular server using _SSH_. This is done using the command (using _pi-hole_ as an example):

```bash
docker exec -it pihole /bin/bash
```

You exit it in the same way as from a server connected via _SSH_, that is, with the _exit_ command. Similarly, you can also execute a specific command inside the _container_ without entering it:

```bash
docker exec -it pihole <command>
```

## Updating Containers

To be honest, when I started my adventure with _Docker_ and learned how to update _containers_, I was initially in a slight shock and even thought it was stupid, but later, after analyzing it, I understood that it is brilliant in its simplicity. As I described above, the process of running a container starts with creating a configuration file _docker-compose.yml_, which contains all the information about how we want that _container_ to look. This file, after compilation and running the _container_, does not disappear anywhere and is still available where we created it. Additionally, we define _volumes_, in which we store all the essential files of the _container_. These _volumes_ remain untouched even if the _container_ is stopped or completely removed. Taking these two things into account, we have all the necessary components that are needed to restart an identical _container_. Alright, but now you might ask - if it will be the same container, where is the update in all this?! Let's go back to the configuration file we created and extract the following line:

> image: pihole/pihole:**latest**

The keyword here is _latest_, which is a parameter telling the compiler that, when creating the _container_, it should take the latest version of the image available at the time of compilation. So in short, updating a _Docker_ container involves stopping it, deleting it, recompiling it with the same parameters but with a newer image version, and finally filling it with files from the _volume_ it was using before the update. Simple and effective. Let's go through such an update process for our example _pi-hole_ container.

1\. Stop the _container_:

```bash
docker stop pihole
```

2\. Remove the _container_:

```bash
docker rm pihole
```

3\. Recompile and run the _container_ again:

```bash
docker-compose -f /home/$USER/docker/pihole/docker-compose.yml up -d
```

4\. Check if it started correctly:

```bash
docker ps
```

Done. I usually handle this with a script that automatically updates all my _containers_. The above instruction may seem trivial and lightning fast, but if you have to repeat it a dozen times, you start wondering how to automate it. In the future, I will definitely share such a script in a separate post.

## Creating backups of containers

Managing _containers_ as I described has a huge advantage. Having all the _containers_ in one place and divided into subfolders, one for each _container_, there is absolutely no problem with making a quick backup. To back up all _containers_, simply copy the entire contents of the _/home/$USER/docker/_ folder. You can use the _tar_ function for this purpose:

```bash
tar -cvpf /home/$USER/$(date +"%FT%H%M")_docker_backup.tar.gz /home/$USER/docker
```

This command will create an archive named _<date>\_docker\_backup.tar.gz_ with the backup inside, in the user's home directory. For safety, it is also a good idea to copy the entire contents of the _/var/lib/docker/_ folder, which contains all Docker files as services installed on our server. However, we need root access to do this.

```bash
sudo su
tar -cvpf /root/$(date +"%FT%H%M")_var_lib_docker_backup.tar.gz /var/lib/docker
```

This command will create an archive named _<date>\_var\_lib\_docker\_backup.tar.gz_ with the backup inside, in the root's home directory.

## That's all for today...

Phew, we made it to the end. Writing this post was not easy, and reading it probably won't be too pleasant either. Nevertheless, I think I managed to pack a lot of informative content that hopefully someone will find useful! The knowledge presented above is rather elementary, but it certainly allows you to recognize the topic and even operate in the _Docker_ environment in terms of basic tasks. That was the goal of this post. Many times I promised on my other blog - [odroid.pl](https://odroid.pl/blog) - that such a post would be created, and I finally managed to sit down and write it. Thank you for today, and if you have any questions, I am available in the comments.
