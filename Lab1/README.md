## Lab 1: Passwords and Hashing

Passwords are the most well-known and widely used method for user authentication and have many advantages. Passwords are simple to use and implement; do not require hardware; are versatile; and more. Passwords are strings of characters. The number of potential passwords is large; for example, there 64^8=2^64passwords using eight characters chosen from the set of 52 alphabetic characters, ten numerals and two special symbols. Trying all these would be very challenging; a few more characters or options, and it would exceed the capacity of supercomputers. And typically, the login process introduces delays and limits to a reasonable, relatively small number of guesses. 

However, passwords are often vulnerable. Many people choose passwords which are easily guessed, such as 123456. Large sets of commonly-used passwords are available, and referred to as a dictionary; research has repeatedly found that a very large percentage of the passwords in use, can be found in such dictionary of common passwords, e.g., half of the passwords in a dictionary of the hundred-thousand most common passwords. 

In this lab we will experiment with different ways for attackers to guess passwords – and with some of the basic defense mechanisms. The defenses we will learn will involve cryptographic hash functions. A cryptographic hash function receives a string of arbitrary length as input, and outputs a fixed length string.  In this lab we’ll focus on the SHA-2 standard hash function, with 256-bit length outputs; the input strings are usually much longer. 
The two main security requirements from cryptographic hash functions are the one-way and collision-resistant properties. Basically:
	
  A hash function h is one-way when an attacker provided with the hash h(x) of some random input x, cannot, in reasonable time, find x, or any other input x’ such that h(x’)=h(x). 
  
  A hash function h is collision-resistant if it is infeasible to find two different inputs x, x’ such that h(x)=h(x’). 
Cryptographic hash functions are a very important and widely used cybersecurity tool, and, as we will see, very important for password security. This application uses the one-way property; in the next lab, we will use collision-resistance. 
In this lab, use the SHA-256 hash function, which can be found in (1) the PyCryptodome library, which should be installed on the VM, (2) the hashlib library, or (3) the cryptography library. Use one or more of these crypto libraries for all relevant questions in this lab. See in LabGen. 
