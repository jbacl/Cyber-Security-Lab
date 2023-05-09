## Lab 2: Malware

Malicious software, aka Malware, is the most serious threat for most users and organizations. Malware is any software that is designed to benefits its `owner’, by running without authorization on a victim’s machine (a phone, computer, server or other device). Malware can be distributed for different goals, such as Denial-of-Service attacks, exposure of sensitive information, unauthorized use of computing resources (e.g., for mining bitcoins), and many other nefarious goals; the functionality of the malware designed to meet these nefarious goals is called the payload. 

Most malware also have functionality for distributing the malware, which we refer to as infection or propagation. 
Malware is often categorized by its method of infection/propagation; the categories include:

•	Virus: malware which searches the storage to identify other programs, and then changes them so they will contain a copy of the virus and execute it, in addition to their `real’ function. Viruses often infect a specific type of program, such as binary executables, macro files (e.g., of Office), or programs written in a specific language. In this lab you’ll write a very simple virus that will infect Python source-code programs. 

•	Worm: malware that searches a network to identify vulnerable machines, and then uses the vulnerability to copy itself to these machines (and run also from there). 

•	USB-Transmitted Malware (UTM): malware which is injected by connecting a rogue device to the USB interface of computer. The rogue device can appear to be a USB memory stick, a USB cable or a USB charger. After being injected by the USB interface, the malware may further propagate as a worm and/or virus. In fact, many USB memory sticks on the market may be modified to become such rogue devices, using software on a computer to which the USB is connected. In this way, USB-port malware can also propagate on other USB sticks. UTM is therefore a bit like STD; maybe that’s why we refer to USB connectors as `male’ and `female’? 

•	Trojan (horse): malware, which is distributed disguised as a desirable application, relying on users to innocently install them. In a sense, this is the simplest type of malware, as it depends on the user installing it. However, this simple strategy is surprisingly effective. In fact, many smartphone apps, as well as different programs and utilities for computers, are Trojans!

You can find more information about different kinds of malware online, e.g., in this link.

In this lab, we will learn about malware by writing simple versions of a Virus, a Worm and a UTM.  

As in all labs, each group’s VM is connected on a dedicated Internet Protocol address (IP address), of the form 172.16.51.x, where 172.16 identifies a block of IP addresses allocated to UConn, 51 identifies the subnet, i.e., a (part of) the Altschuller lab dedicated network, and, finally, x is a number, between 0 and 255, which identifies the VM for your group. If you are in team t of section s, then use x=s*20+t. For example, team 3 of section 2 will use IP 172.16.51.43. The VMs are always initialized with user cse and default password cse3140; change the password when you begin the lab. Also, we include in the VM the scripts we used to generate the lab, in case you will find them helpful, e.g., if something is unclear. Notice that we’re using subnet 51 in this lab rather than subnet 50 as in previous labs. 
