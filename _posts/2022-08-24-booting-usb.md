--- 
layout: page
title: Creating a bootable USB to install or try out Linux distros
category: notes
tags: [productivity,life]
excerpt: My own recipe for creating and booting to USB drives.
---

# Choosing a distribution and desktop environment. 

I have an old (2018) version of Ubunbtu with the KDE Plasma desktop environment, and I need a change. 
My impression is that other distributions are more friendly to programmers. 
I was also recommended Manjaro, which is billed as an easier-to-use offshoot of Arch Linux. 
A major advantage of that is the updates are rolling, so you always have the most up-to-date version of things. 

## Ubuntu

I've been using this for a long time, primarily because I assumed it had the best support for random everyday life things that I might want to do. 
For example, plugging in a peripheral device or running a GUI. 
A problem with it is it tends to release huge updates infrequently, and it's kind of a hassle to deal with those. 
It also doesn't have [Environment Modules](http://modules.sourceforge.net) (`modules`) preinstalled, which I know other distros do have. 
Ubuntu probably enjoys the widest third-party, proprietary support of any distribution. 

## Fedora

One nice thing about Fedora: it has a more frequent and easier release cycle. 
It's not as widely supported as Ubuntu, but it is probably second place.
There seems to be a general impression that Fedora is better than Ubuntu for software development, I'm not 100% sure where this comes from.
Perhaps experience will tell.
I do know that Environment Modules is preinstalled on Fedora, maybe that is one example of why.
Perhaps there are also most extra features in Ubuntu that aren't really useful for programming, at least that seems to be the unsaid assumption online. 

Often you need third-party proprietary drivers for all your hardware features to work. 
Apparently, Fedora does not make installing these simple, sticking to purely open-sources packages for it's software suite. 
This seems like a problem, since a graphics card or a certain microphone or some other pluggable hardware might not work without some proprietary software. 

## Majaro

Apparently, Manjaro is Linus' (from *Linus Tech Tips*) favorite Linux OS. 
Apparently, it is because it is the most compatible with windows programs.
This is supported by [this blog post comparing Fedora and Majaro](https://linuxhint.com/manjaro-vs-fedora/#:~:text=Considering%20the%20major%20difference%20between,compatibility%20with%20the%20latest%20software.). 
That seems like a significant boon to me. 
It also has rolling updates, so software will be kept up-to-date with minimal interference in my work.

## My decision 

I get the impression that Manjaro is more interesting, but possibly less functional, while Fedora is more functional, but possibly less interesting. 
So, I decided to go Manjaro first, and if it becomes annoying, switch to Fedora. 

# Creating the bootable USB

I like to use [GParted](https://gparted.org/) to format disks, and I usually reformat the USB I'm going to use before I use it to install an OS. 
This is probably out of paranoia, but if a virus happens to be on the USB, then reformatting should wipe it right out. 
Also, it ensures there's no problems from files or formatting issues on the USB before you start trying to boot from it.
Booting from USB is always tricky, and it's better to remove any possible complications to simplify debugging it. 

I choose EXT4 for Linux-bootable disks and FAT32 for Windows bootable disks. 
I don't remember why. I'm sure there is a reason on Google somewhere. 

Once it is formatted, and the `.iso` or `.img` file is downloaded (make sure to verify the checksum, for safety and to eliminate possible complications again), unmount the USB drive and use 
```
sudo dd if=/path/to/your.iso of=/dev/sda bs=4M status=progress conv=fdatasync
```
`conv=fdatasyunc` apparently will make sure all caches are flushed before `dd` exits. 
Be sure to use an address of the form `/dev/sda`, *not* `/dev/sda1`! 
Doing the latter (which puts the boot data in a certain partition on the USB disk) will not make a bootable USB drive, as I found out. 

`/dev/sda` might be different for you, depending on how many external drives are plugged in, and in what order. 
I use GParted to figure it out, usually, but there are command-line options out there on Google.


# Booting to the USB.

Warning: this step is always a huge pain-in-the-ass.

The best way to boot to the USB is to use a one-time boot menu, which turned out to be achieved by pressing `F12` when booting my Dell XPS. 
`F2` will bring up the BIOS settings, which also might be important for debugging. 

The idea is to select the USB drive from the one-time boot menu when booting the computer. 
If it works will, your USB will start blinking happily, and whatever OS you put on the USB will pop up after a much longer boot duration than normal (assuming you have a reasonable hard drive). 

If it doesn't do that, then you need to trouble shoot (I always have to troubleshoot at least a little when I do this). 
Here are some things to check:
- [x] Is the ISO or IMG file burned correctly? Check that the `of` argument of `dd` is not `/dev/sda1` when it should be `/dev/sda` or something else incorrect. 
- [x] Did you choose the correct ISO, or did you do what I did and click a random one that doesn't match your system? 
- [x] Is the boot menu on a different key? Try searching Google for the boot menu keys for your computer model.
- [x] Try deactivating secure boot. 
- [x] If you have some sort of fast-boot option on, turn it off. 
- [x] Try checking the boot order and putting the USB first. 
- [x] Try enabling legacy boot. You probably shouldn't have to do this if you're using a recent ISO and USB stick. 
- [x] Try using the USB on a different computer, that will tell you if the USB is at fault or your computer is not willing to boot from a working USB yet. 
- [x] Try a different USB. Sometimes the USB is just damaged and it causes a problem. 
- [x] Try formatting the USB differently. Try a different file format for it. Make sure there's no other partitions on it. 
- [x] Google desperately.

Once things are working, usually the bootable USB OS will guide you through any decision making you'll need to do.
