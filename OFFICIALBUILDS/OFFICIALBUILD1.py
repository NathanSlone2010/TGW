import time
import os
import sys
import platform
#These are the required modules


time.sleep(1); print("NO ERRORS\n")
#If users sees this, there is no issues


os = platform.system()
if os == "Windows":
	print("OPERATING SYSTEM OWNER: MICROSOFT | WINDOWS-OS\n")
elif os == "Darwin":
	print("OPERATING SYSTEM OWNER: APPLE COMPUTER, INC. | MACOS\n")
elif os == "Linux":
	print("OPERATING SYSTEM OWNER: OPEN SOURCE OS | LINUX KERNEL\n")
elif os in ["FreeBSD", "OpenBSD", "NetBSD"]:
	print("OPERATING SYSTEM OWNER: OPEN SOURCE OS | BSD")
elif os == "iOS":
	print("OPERATING SYSTEM OWNER: APPLE COMPUTER, INC. | iOS\n")
elif os not in ["Windows", "Darwin", "Linux", "iOS", "FreeBSD", "OpenBSD", "NetBSD"]:
      print("UNKNOWN OPERATING SYSTEM || REPORT YOUR OPERATING SYSTEM TO DEVELOPER FOR INTEGRATION.\n")
#OS-recognition of users


print("THE GOLD WAY")
print("Copyright Void Studios 2026")
print("ENJOY...\n")
#The introduction


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


time.sleep(0.5); print("1. Execute the Staff")
time.sleep(0.5); print("2. Execute the Students")
time.sleep(0.5); print("3. Force Students to execute the Staff")
time.sleep(0.5); print("4. Force Staff to execute the Students")
choice3 = input("[INPUT] ").upper()


#---START OF CHOICE SET 3---
if choice3 == "E":
	sys.exit()

if choice3 == "1":
	print("You point the gun at the staff.. They beg, they plea.. You pull the trigger, the gun fires off... Bodies fall..")

if choice3 == "2":
	print("You point the gun at the staff. They cry, scream.. Laughing, you open fire, killing them all...")

if choice3 == "3":
	print("You grab a student with a cross tattoo, forcing the gun in their hand and forcing their finger on the trigger. Your partner point the gun at the cross tattoo, 'Shoot them or suffer in front of your god' he says to them. They cry, refusing. Your partner pulls the trigger, shooting the student... You shoot the rest of the staff.")

if choice3 == "4":
	print("You grab the science teacher, forcing the gun in their hand, and forcing their finger on the trigger. You press their finger down causing it to go off, killing one of the students.. You shoot the rest while your partner uses a knife to execute the students..")
#---END OF CHOICE SET 3---
