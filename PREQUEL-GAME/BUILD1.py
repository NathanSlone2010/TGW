import time
import os
import sys
import platform
#These are the required modules


time.sleep(1); print("NO ERRORS\n")
#If users see this, the program has no issues


os = platform.system()
if os == "Windows":
	print("OPERATING SYSTEM OWNER: MICROSOFT | WINDOWS-OS\n")
elif os == "Darwin":
	print("OPERATING SYSTEM OWNER: APPLE COMPUTERS, INC. | MACOS\n")
elif os == "Linux":
	print("OPERATING SYSTEM OWNER: OPEN SOURCE OS | LINUX KERNEL\n")
elif os in ["FreeBSD", "NetBSD", "OpenBSD"]:
	print("OPERATING SYSTEM OWNER: OPEN SOURCE OS | BSD\n")
elif os == "iOS":
	print("OPERATING SYSTEM OWNER: APPLE COMPUTERS, INC. | iOS\n")
elif os not in ["Windows", "Darwin", "Linux", "OpenBSD", "NetBSD", "FreeBSD"]:
	print("UKNOWN OPERATING SYSTEM || REPORT YOUR OPERATING SYSTEM TO DEVELOPER FOR INTEGRATION.")
#OS-recognition of users


print("BLOOD & POWDER: THE PLAN")
print("\nRest in Peace Eric Harris, Dylan Klebolds.")
time.sleep(0.5); print("Copyright Void Studios 2026")


game = input("START GAME? Y/N: ").upper()
if game == "Y":
	print("STARTING GAME...")
elif game == "N":
	print("COME BACK WHEN YOU ARE READY, DUMB FUCK")
	sys.exit()
elif game not in ["Y", "N"]:
	print("STARTING GAME ANYWAYS, NUMBNUTS.")


#---START OF CHOICE SET 1---
while True:
	print("\n'Yo, bro! You good? Blanked out there, for a second'")
	time.sleep(0.5); print("1. Say 'Yeah. Day dreamed a bit'")
	time.sleep(0.5); print("2. Say 'No...'")
	time.sleep(0.5); print("3. Say nothing")
	choice1 = input("INPUT: ").upper()

	if choice1 == "1":
		print("Alright.. Anything you want to talk about? Y/N")
		inchoice1 = input("[INPUT] ").upper()
		if inchoice1 == "Y":
			print("[YOU] I have been struggling.. Honestly do not know what to do")
			break
		elif inchoice1 == "N":
			print("[YOU] No, thank you, though. You were always nice to me")
			break
		elif inchoice1 not in ["Y", "N"]:
				print("Make a choice when you are ready...")

	elif choice1 == "2":
		print("'Oh... Okay..'")
		break

	elif choice1 == "3":
		print("'Something definetly is wrong... You never ignore me..'")
		break

	elif choice1 not in ["1", "2", "3"]:
		print("Relaunch the game when you are READY? WHY ARE YOU NOT READY IF YOU LAUNCHED THE GAME?????????????")
		print("BE FUCKING READY NEXT TIME " * 5)
		break
#---END OF CHOICE SET 1---


#--START OF CHOICE SET 2---
while True:
	print("\nDay at school goes by slowly. Faraemein High School... School of hell..")
	print("1. Eat in the cafeteria")
	print("2. Eat at the staircase")
	print("3. Don't eat today")
	choice2 = input("INPUT: ").upper()

	if choice2 == "1":
		print("You get your food and sit down at a table. Your friend, Dylan, sits down with you. As you have a conversation a person behind you taps your head hard with a plastic luch tray. You look back and see it is Daniel... 'Dammit, can you stop, Daniel' Dylan says, speaking up to defend you.. Daniel chuckles but walks off.... He backed off.. for now")
		break

	if choice2 == "2":
		print("You go to the staircase, eating your food, Peyton walks by, she waves at you. You wave back but her boyfriend glares at you.. Dylan comes up to you. 'Daniel bothering you?' [Y/N]")
		inchoice2 = input("[INPUT] ").upper()
		if inchoice2 == "Y":
			print("'That damn bastard... One day he'll get what is coming to him...'")
			break
		if inchoice2 == "N":
			print("'You sure..? Alright, I will take your word for it.. Just let me know if he bothers you, bro..'")
			break
		if inchoice not in ["Y", "N"]:
			print("MAKE A CHOICE, BITCH.")

	if choice2 == "3":
		print("While hungry, you don't eat, not willing to take the abuse from other students.. You walk upstairs to your next class ahead of schedule..")
		break
#---END OF CHOICE SET 2---


#---START OF CHOICE SET 3---
while True:
	print("\nIt is the end of the day. Do you and Dylan go to your house? [Y/N]")
	choice3 = input("INPUT: ").upper()

	if choice3 == "Y":
		print("'Thanks for letting me come over, Mrs. Harris... Yo bro, want to order some food? I will pay' [Y/N]")
		inchoice3 = input("[INPUT] ").upper()
		if inchoice3 == "Y":
			print("[YOU] Sure. Thanks for paying. I'll get next time... 'Alright. Only chinese and the pizza place is open..")
			print("1. Chinese")
			print("2. Pizza")
			dchoice3 = input("[[INPUT]] ")
			if dchoice3 == "1":
				print("'Chinese it is!'")
			if dchoice3 == "2":
				print("[YOU] Pizza does sound good right about now")
			if dchoice3 not in ["1", "2"]:
				print("FINE, SKIP DIALOGUE [WHICH IS THE GAME ITSELF DUMBASS]")
		if inchoice3 == "N":
			print("'Alright, but I am hungry. Care if I get a snack?'")
		break
	if choice3 == "N":
		print("You and Dylan goes to the park... Next day arrives quickly")
		break
#---END OF CHOICE SET 3---


#--START OF CHOICE SET 4---
while True:
	print("\nYou and Dylan is in the basement. Playing pool... 'How many rounds should we get from the seller? Since the guns are for the range, we should not need much, right?'")
	print("1. Single Box [CRINGE]")
	print("2. A few Boxes")
	print("3. Enough for a massacre")
	choice4 = input("INPUT: ").upper()

	if choice4 == "1":
		print("[YOU] A single box should be fine. Can't over-do it, ya'know?")
		break

	if choice4 == "2":
		print("[YOU] Just a few. Enough to last a while..")
		break

	if choice4 == "3":
		print("'And how much exactly is that?")
		numchoice4 = input("[INPUT NUMBER] ")
		print(f"Alright, {numchoice4} it is, then'")
		break
#---END OF CHOICE SET 4---
