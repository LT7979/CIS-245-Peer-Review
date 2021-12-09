# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Samuel Ford
# Creation Date: 12/5/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
#	print('''You are in a land full of dragons. In front of you,
#	you see two caves. In one cave, the dragon is friendly
#	and will share his treasure with you. The other dragon
#	is greedy and hungry, and will eat you on sight.''')
	print('''You are in a land full of dragons. In front of you,\n\
you see two caves. In one cave, the dragon is friendly\n\
and will share his treasure with you. The other dragon\n\
is greedy and hungry, and will eat you on sight.''')
#formating issue, need to add \n for new lines and \ to continue print statement on next line
	print()

def chooseCave():
    #cave = ''
	cave = ''
	#need to tab instead of using space to indent
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	#return caves
	return cave
	#remove s, variable cave is needed, not caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#time.sleep(3)
	time.sleep(2)
	#sleep time needs changed to 2 seconds
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print ('Gobbles you down in one bite!')
		#syntax error, need to add parentheses for print statement

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
#syntax error, there needs to be two equal signs
	displayIntro()
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	#capitalize the C in cave to coorespond with the chooseCave function
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	#if playAgain == "no":
	if playAgain == "no" or playAgain == "n":
	#added or statement to match beginning of program
		#print("Thanks for planing")
		print("Thanks for playing")
		#misspell of the word "playing"

