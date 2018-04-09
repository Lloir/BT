#!/usr/bin/python2.7
# No Licence
# https://mcuoneclipse.com/2016/12/29/using-python-gatttool-and-bluetooth-low-energy-with-hexiwear/
# https://extr3metech.wordpress.com/2014/09/14/simple-text-menu-in-python/

import os
import subprocess
import pexpect
import time
vibrate_giant_dildo="50:8C:B1:44:8A:AB" #Hard code this for now


def print_menu():
    print 30 * "-", "Verge Attack", 30 * "-"
    print "1. Slow"
    print "2. Medium"
    print "3. Stupid"
    print "4. Exit"
    print 67 * "-"


loop = True

while loop:
    print_menu()
    choice = input("Enter your choice [1-4]: ")

    if choice == 1:
        print "Slow"
        print("gatttool is starting up")
        child = pexpect.spawn("gatttool -I")
        print("I see the ")
        print( vibrate_giant_dildo),
        child.sendline("connect {0}".format(vibrate_giant_dildo))
        child.expect("Connection successful", timeout=5)
        print(" So far so good!")
        command="char-write-req 0x25 0F01"
        time.sleep(5)
        child.sendline(command)
        child.expect("Characteristic value was written successfully", timeout=10)

    elif choice == 2:
        print("gatttool is starting up")
        child = pexpect.spawn("gatttool -I")
        print("I see the ")
        print( vibrate_giant_dildo),
        child.sendline("connect {0}".format(vibrate_giant_dildo))
        child.expect("Connection successful", timeout=5)
        print(" So far so good!")
        command="char-write-req 0x25 0F03"
        time.sleep(5)
        child.sendline(command)
        child.expect("Characteristic value was written successfully", timeout=10)

    elif choice == 3:
        print "Menu 3 has been selected"
        print("gatttool is starting up")
        child = pexpect.spawn("gatttool -I")
        print("I see the ")
        print( vibrate_giant_dildo),
        child.sendline("connect {0}".format(vibrate_giant_dildo))
        child.expect("Connection successful", timeout=5)
        print(" So far so good!")
        command="char-write-req 0x25 0F10"
        time.sleep(5)
        child.sendline(command)
        child.expect("Characteristic value was written successfully", timeout=10)
        command="char-write-req 0x25 0F13"
        time.sleep(5)
        child.sendline(command)
        child.expect("Characteristic value was written successfully", timeout=10)
        command="char-write-req 0x25 0F06"
        time.sleep(5)
        child.sendline(command)
        child.expect("Characteristic value was written successfully", timeout=10)

    elif choice == 4:
        print "Quitting"
        loop = False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
