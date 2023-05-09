## Lab 3: Cryptography, Malware, and Ransomware

In this lab, we will learn more about malware; specifically, we will learn some of the main defenses against malware, as well as study the design of ransomware, one of the most problematic types of malware. Both topics – defense against malware and design of ransomware – make extensive use of Cryptography, so, this will also provide a way for us to introduce a bit of cryptography. 

Cryptography is central to cybersecurity, and covered extensively in several courses, beginning with CSE3400. Cryptography is mostly used to defend against attacks; for example, in the first part of the lab, we use cryptography against malware. We will use first a cryptographic hash function and then digital signatures, to ensure the integrity of software, to prevent the installation of malware.

In the second part of the lab, we will see the use of cryptography by malware, specifically, by Ransomware. Ransomware uses a cryptosystem to encrypt files in the computer’s storage (disk); then, the ransomware requires the user to pay the attacker in order to receive the decryption key. We will explore the use of public key cryptosystem, shared key cryptosystem and obfuscation. 

As in all labs, each group’s VM is connected on a dedicated Internet Protocol address (IP address), of the form 172.16.50.x, where 172.16 identifies a block of IP addresses allocated to UConn, 50 identifies (part of) the Altschuler lab dedicated network, and, finally, x is a number, between 0 and 255, which identifies the VM for your group. If you are in team t of section s, then use x=s*20+t. For example, team 3 of section 2 will use IP 172.16.50.43. The VMs are always initialized with user cse and default password cse3140; change the password when you begin the lab. 
