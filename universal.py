#!/usr/bin/python3
import os
import subprocess
import platform
import pexpect
import time
import sys

os = platform.system()

if os == "Windows":
	print("Windows is detected")
#Enter WIndows API here
elif os == "Linux":
	print("Linux is detected")
	print("Ensure you have the mac address of the device you wish to connect to")
	print("Enter the mac address")
	mac = input("")
	print("Enter the number")
	number = input("")
	print("gatttool is starting up")
	child = pexpect.spawn("gatttool -I")
	child.sendline("connect {0}".format(mac))
	child.expect("Connection successful"),
	command="char-write-req {0}".format(number)
	time.sleep(5)
	child.sendline(command)
	child.expect("Characteristic value was written successfully", timeout=10)    

else:
	print("Unsure what os is running")
	time.sleep(15)
	sys.exit(0)






