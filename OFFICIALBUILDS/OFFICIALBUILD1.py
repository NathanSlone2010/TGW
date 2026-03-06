import time
import os
import sys
import platform
#These are the required modules


time.sleep(1); print("NO ERRORS\n")
#If users sees this, there is no issues


os = platform.system()
if os == "Windows":
	print("OPERATING SYSTEM OWNER: MICROSOFT | WINDOWS-OS")
elif os == "Darwin":
	print("OPERATING SYSTEM OWNER: APPLE COMPUTER, INC. | MACOS")
elif os == "Linux":
	print("OPERATING SYSTEM OWNER: OPEN SOURCE OS | LINUX KERNEL")
elif os in ["FreeBSD", "OpenBSD", "NetBSD"]:
	print("OPERATING SYSTEM OWNER: OPEN SOURCE OS | BSD")
elif os == "iOS":
	print("OPERATING SYSTEM OWNER: APPLE COMPUTER, INC. | iOS")
elif os not in ["Windows", "Darwin", "Linux", "iOS", "FreeBSD", "OpenBSD", "NetBSD"]:
      print("UNKNOWN OPERATING SYSTEM || REPORT YOUR OPERATING SYSTEM TO DEVELOPER FOR INTEGRATION.")


print("THE GOLD WAY")
print("Copyright Void Studios 2026")
print("ENJOY...\n")


print("You enter the school. You see three paths.")


time.sleep(0.5); print("1. Library.")
time.sleep(0.5); print("2. Cafeteria")
time.sleep(0.5); print("3. Auditorium")
choice1 = input("[INPUT] ").upper()

#---START OF CHOICE SET 1---
if choice1 == "E":
	sys.exit()

if choice1 == "1":
	print("\nYou enter the library. You fire the rifle, shot after shot ringing out, bodies falling and crying can be heard...")

if choice1 == "2":
	print("\nYou enter the cafeteria... There are many... FIRE")

if choice1 == "3":
	print("\nYou enter the auditorium, opening fire on everyone... Five down so far....")
#---END OF CHOICE SET 1---


time.sleep(0.5); print("1. Clear the Halls")
time.sleep(0.5); print("2. Block the Exits")
time.sleep(0.5); print("3. Grab the hidden rifles from the closet")
time.sleep(0.5); print("4. END IT ALL")
choice2 = input("[INPUT] ").upper()

#---START OF CHOICE SET 2---
if choice2 == "E":
	sys.exit()

if choice2 == "1":
	print("\nYou enter the halls.. You slowly walk down them, gunning down everyone, and checking rooms.. Surprise you scream at a target, who is hiding from you. The bullet hits her head, splashing blood onto your face")

if choice2 == "2":
	print("\nYou grab heavy shelves with your partner, blocking the doors but purposefully leaving the windows unblocked.")

if choice2 == "3":
	print("\nYou enter the closet, breaking open a vent, pulling out two compact rifles, handing one to your partner. LOCK, LOAD, EXIT, FIRE")

if choice2 == "4":
	print("\nYou point the gun at your face, pulling the trigger...")
	time.sleep(1); sys.exit()
#---END OF CHOICE SET 2---