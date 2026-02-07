---
title: "Terminal with Proxmox - creating VM [ENG 🇬🇧]"
date: 2023-04-01
categories: 
  - "self-hosting-eng"
  - "tutorials"
tags: 
  - "backup"
  - "cpu"
  - "dellwyse"
  - "firewall"
  - "fujitsu"
  - "gui"
  - "intelnuc"
  - "opensource"
  - "proxmox"
  - "ram"
  - "selfhosted"
  - "snapshot"
  - "terminal"
  - "ubuntu"
  - "virtualmachine"
  - "vm"
coverImage: "/images/proxmox_vms.png"
---

[🇵🇱 Przejdź do polskiej wersji tego wpisu / Go to polish version of this post](https://blog.tomaszdunia.pl/proxmox-vm/)

This is a continuation of the [previous post](https://blog.tomaszdunia.pl/terminal-proxmox-eng/) in which I presented a tool called _Proxmox_, which is a virtualization environment. I discussed its installation on a _terminal_, which is a type of _mini PC_. Below, I will describe how to create your first **_virtual machine_** (_VM_) in _Proxmox_.

## Creating virtual machines

When you enter the _Proxmox_ management panel, you will be greeted with a login window. Use the _root_ login and the password that you provided during installation. Next, you will see another popup, this time informing you that you do not have a subscription. _Proxmox_ is an _open-source_ solution, but it also has optional paid subscriptions. As an ordinary private user, simply click _OK_ to close the popup. Unfortunately, you will have to do this every time you log in, which can be a bit annoying.

Getting to the point, I would like to note at the beginning that I do not plan to discuss all of the settings, as it might take me a lifetime. I will only focus on showing you how to start your first _**virtual machine**_. First, we need to download the _ISO_ image of the system that we want to install on this machine. One such system could be Ubuntu Server 22.04 LTS, which can be downloaded from the [official distribution site](https://ubuntu.com/download/server). Image can be uploaded to _Proxmox_ in two ways. The first is to download the image to your computer first and then upload it to the server, and the second is to point the server to the image link and download it directly from the server. Both of these actions can be performed by expanding the tree in the left column, selecting _local volume_, and going to the _ISO Images_ tab. At the top of the menu, two buttons will appear, _Upload_ (for uploading from your computer) and _Download from URL_ (for downloading directly from the distribution site).

Now we can move on to creating a _virtual machine_, and the quickest way to do so is to use the blue _Create VM_ button located at the top right of the interface. _Proxmox_ will open the new virtual machine wizard, so let's go through each step one by one.

1. _**General**_: Here we set basic information about the machine. _Node_ is like a cluster to which it belongs. I assume you are at the beginning of the road, so there is a limited choice - one _Node_ to choose from. _VM ID_ is a very important parameter that will be the unique identifier of this machine. _Name_ is, of course, the name of the machine. It is not very important what we enter here, as long as it helps us later to identify which machine we are dealing with. At the beginning of our journey, it is worth creating some naming system that we will appreciate later when we have many virtual machines. We are not interested in _Resource Pool_ at the moment, as we have not configured it yet.

3. _**OS**_: We leave _Storage_ as _local_, which means that images are searched on the local disk. As for _ISO image_, we indicate the system image downloaded earlier. It is important to correctly specify the _Type_ and _Version_ parameters in the _Guest OS_ section, depending on the system we are installing.

5. _**System**_: We have nothing to change here, I suggest leaving the default values.

7. _**Hard Disk**_: Here we are mainly interested in the _Disk size (GiB)_ parameter, where we specify how much disk space we intend to allocate to this _virtual machine_. However, it is worth remembering that this value can be easily increased later, while reducing it will be a bigger problem, so it is best to start with the smallest value recommended by the specification of the given distribution (system), and then gradually expand it as the need arises.

9. _**CPU**_: Here we set how much computing power we want to assign to this _virtual machine_. _Proxmox_ offers a division into _Sockets_ and _Cores_ that is not entirely clear to me. I read a bit about it on various forums, and if I remember correctly, _Sockets_ are used only for machines that have more than one processor. I also remember seeing a formula for calculating the optimal _Cores_ setting, which involved entering the number of cores and threads of our server processor and relating it to the hardware requirements we intend to set for the _virtual machine_. However, in practice, I only operate the _Cores_ parameter here, and I know that for a 4-core processor, I can set this value in the range of 1-4. However, the good advice here is to do the same as with the disk space _Disk size_ defined in the previous point. It's always best to assign only one core and modify this value later if you notice the need. The difference is that changing the number of assigned cores has no limits, i.e., it can be done easily both up and down. In theory, I see even the possibility of doing this while the machine is running, but common sense tells me not to do so. It's always better to stop the machine, change the settings, and restart it with new resources.

11. _**Memory**_: Here, of course, we have settings related to operating memory (_RAM_). We have one parameter to set, _Memory (MiB)_, which is the amount of assigned _RAM_. This parameter can be changed as easily as the _CPU_ settings, and the value of _2048_ is an excellent starting point.

13. _**Network**_: Nothing more than network settings. For the purposes of this post, let's leave everything default, but I would like to point out that there are many other options here that need to be adapted to the specific solution. We can completely cut off network access to this _virtual machine_. We can separate _virtual machines_ from each other or from the management interface. In general, this is more complex topic, which I don't want to focus on in this post.

15. _**Confirm**_: Summary of all settings that need to be checked and finalized by clicking the _Finish_ button.

Immediately after approval on the list on the left, we should see the newly created _virtual machine_, but it may take a while to start it up and make it usable.

## Virtual machine control panel

After selecting the _machine_ from the list on the left, the control panel for that _machine_ will be displayed in the main window. Let's go through all the tabs just as we did for the installation wizard above.

![](/images/proxmox_screenshot-1024x502.png)
    
![](/images/proxmox_screenshot2-1024x502.png)
    

1. **_Summary_**: All the key statistics regarding the _VM_. CPU, memory and disk usage, as well as network traffic. We can also add notes.

3. **_Console_**: As the name suggests, this is the place from which we can communicate with the server directly from the _Proxmox_ environment. If we installed a system with a graphical interface, we can access it here just as if we physically connected a monitor, keyboard, and mouse. If we chose a system without a _GUI_, a text-based interface (terminal) will be displayed.

5. **_Hardware_**: Here, as well as in the _Options_ tab, we can change what was set up during the creation of the _machine_. Additionally, it is important to note that we can manage data media here, which means simulating connecting a portable memory or inserting a CD-ROM into the machine.

7. **_Cloud-Init_**: A tab for more advanced users who manage the entire virtual machine cloud, and this is just another node in it.

9. **_Options_**: See point 3 above.

11. **_Task History_**: A basic event log that sometimes helps to understand what happened with the machine when, for example, it unexpectedly restarted.

13. **_Monitor_**: Honestly, I have never used this tab and I have no idea what it is for.

15. **_Backup_**: A super important tab where we can make a complete backup of the machine. In my opinion, this way of making backups is one of the biggest advantages of _Proxmox_. You don't have to mess around with any _tar -cvpf_ or similar actions performed on a running system. Here we simply take the entire machine disk, make its clone, and we are ready to move it anywhere.

17. **_Replication_**: A tool for replicating (duplicating) data stores between _Nodes_. This does not apply to us because as I mentioned earlier, we only operate on one _Node_ at the beginner level.

19. **_Snapshots_**: What is the difference between _snapshots_ and _backups_? A _backup_ is a complete copy of a _machine_, which contains all of its data, whereas a _snapshot_ is a restore point of the system, meaning a set of information about the state of the _machine_ at the time it was created. It is a very fast and low-invasive way of protecting yourself from making significant changes to the _machine_ whose effect is not entirely known or predictable. Before making such a change, it is always a good idea to take a _snapshot_, which will allow you to return to that point at any time and either start over or completely abandon those changes.

21. **_Firewall_**: Network firewall settings. I have not yet determined whether this is an additional layer or whether it is at the same level as, for example, _ufw_ running on a _virtual machine_.

23. **_Permissions_**: _Proxmox_ is an environment in which more than one user can work. In this tab, you can assign access to a specific user or group of users for a given machine. An additional option is also to provide access through the _API_ based on _Token_ authentication.

## Summary

As you probably noticed, dear Reader, _Proxmox_ is a truly powerful and very extensive tool. It allows for configuration of an incredible number of parameters and the creation of truly powerful network solutions based on virtualization. What I have shown in my two posts is only a fraction of what can be done with this environment. I am not an expert in this field myself and I must admit honestly that I cannot do much more in it than what I have described. Nevertheless, _Proxmox_ is definitely my number one solution for a home server. It is stable enough to allow me to run really important services with a clear conscience. It can also be used at the same time as a _homelab_, i.e., a home experimental playground, where you can quickly create test _machines_ as well as destroy them when they are no longer needed.
