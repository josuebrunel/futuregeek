Title: Backing up your wireless networks data on linux 
Date: 2013-10-17 
Tags: linux, wifi
Category: Linux
Author: Josue Kouka 
Summary: Backing up your wireless networks data on linux 


Hey guys.
I'm sure that almost all of us, one day, have wondered how we could backup our Wireless Networks Settings
on Linux to be able to use it for another linux freshly installed. There's a really easy and natural way to do so.

	:::console 
	yosuke@loking:~$ cd /etc/NetworkManager/
	yosuke@loking:/etc/NetworkManager$ sudo tar czvf WirelessNetworksBackup.tar.gz system-connections/
	system-connections/
	system-connections/eth0
	system-connections/ALICE_SANDRA_68
	system-connections/FreeWifi
	system-connections/Freebox-ACF055
	system-connections/anafree
	system-connections/FBX_QUERNEL
	system-connections/Cheval de Troie
	system-connections/Bbox-00F72CC0
	system-connections/freebox
	system-connections/elchero
	system-connections/HPC410a.FCBFE6
	system-connections/Molaka
	system-connections/Bbox_min
	system-connections/Freebox-4883FA
	system-connections/SFR WiFi Public
	yosuke@loking:/etc/NetworkManager$

You've noticed the interesting folder here is ***system-connections*** . This directory contains the description of each
network you connected to or you've tried to connect to. You can open each one of them and see the password (if there's one) in **plain text** of network.

To restore those data on a freshly installed or another computer, just untar the archive into ***/etc/NetworkManager/*** .

That's all. 
