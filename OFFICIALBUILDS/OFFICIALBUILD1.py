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


print("BLOOD & POWDER")
print("\nRest in Peace Eric Harris, Dylan Klebolds. The only ones brave enough to say the truth to everyone\n")
time.sleep(0.5); print("Copyright Void Studios 2026")
time.sleep(0.5); print("ENJOY...\n")
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


time.sleep(0.5); print("1. Go to the Rooftop")
time.sleep(0.5); print("2. Shoot through the windows")
time.sleep(0.5); print("3. Don't attack the police")
choice4 = input("[INPUT] ").upper()


#--START OF CHOICE SET 4---
if choice4 == "E":
	sys.exit()

if choice4 == "1":
	print("You go to the roof, your partner stays at the bottom. Firing off the roof, you hit 4 cops, and 2 SWAT officers. They return fire, but miss the shots, you laugh, deciding to go return to your partner")

if choice4 == "2":
	print("You and your partner shoots through the windows. A brave yet dumb student grabs you, your partner pressing the barrel into their neck. They back off of you and your partner shoots them in the throat...")

if choice4 == "3":
	print("You and your partner decides not to attack the police, focusing on those stuck inside with you...")
#--END OF CHOICE SET 4---


time.sleep(0.5); print("1. Push corpses off the roof")
time.sleep(0.5); print("2. Smash corpses into the windows")
time.sleep(0.5); print("3. Push corpses out of the windows")
time.sleep(0.5); print("4. END IT ALL")
choice5 = input("[INPUT] ").upper()


#---START OF CHOICE SET 5
if choice5 == "E":
	sys.exit()

if choice5 == "1":
	print("You drag 3 corpses to the roof, throwing them off. Everyone screams in fear and disgust.")

if choice5 == "2":
	print("You smash corpses into the window, hard as you can, until blood splatters onto the windows.. [Fun right?]")

if choice5 == "3":
	print("You break windows using the stock of the gun. Pushing corpses out.")

if choice5 == "4":
	print("You point the gun at your temple. The gun goes off...")
	sys.exit()
#--END OF CHOICE SET 5---


time.sleep(0.5); print("1. Surrender")
time.sleep(0.5); print("2. Escape")
time.sleep(0.5); print("3. END IT ALL")
choice6 = input("[INPUT] ").upper()


#---START OF CHOICE SET 6---
if choice6 == "E":
	sys.exit()

if choice6 == "1":
	print("You throw the gun down. Your partner argues with you not to exit.. You leave, the police grabs and forces you to the ground, and handcuffs you... [How pathetic..]")
	sys.exit()

if choice6 == "2":
	print("You and your partner runs out the back into the woods, police chases you, but as you go deeper into the woods.. The police loosese you and your partner")
	sys.exit()

if choice6 == "3":
	print("You and your partner decide that is time... You and your partner pulls out the homemade poisions... 'Farewell...' you say to your partner...")
	print("THE CANON ENDING")
	print("UNLOCKED: https://shorturl.at/rrB0q | DEVELOPER'S JOURNAL")
	
print("This game is dedicated to Dylan Klebolds, the Abandoned Shepherd of Truth. Eric Harris, the Showman of Truth.”)
