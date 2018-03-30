#
# street craps dice roller
# github/nate_han
#


import random
import time

def roll(amount, sides):

	rolls = 0
	total = 0
	
	dice1 = "\n+-------+\n|       |\n|   0   |\n|       |\n+-------+"
	dice2 = "\n+-------+\n|     0 |\n|       |\n| 0     |\n+-------+"
	dice3 = "\n+-------+\n|     0 |\n|   0   |\n| 0     |\n+-------+"
	dice4 = "\n+-------+\n| 0   0 |\n|       |\n| 0   0 |\n+-------+"
	dice5 = "\n+-------+\n| 0   0 |\n|   0   |\n| 0   0 |\n+-------+"
	dice6 = "\n+-------+\n| 0   0 |\n| 0   0 |\n| 0   0 |\n+-------+"
	
	while rolls < amount:
		
		result = random.randint(1, sides)
		total = total + result
		rolls = rolls + 1
		
		if result == 1:
		
			print(dice1)
			
		elif result == 2:
		
			print(dice2)
			
		elif result == 3:
		
			print(dice3)
			
		elif result == 4:
		
			print(dice4)
			
		elif result == 5:
		
			print(dice5)
			
		elif result == 6:
		
			print(dice6)
		
		
	return total
	
def sideBetch(point):
	
	sidebet = 0

	if point == 5:
	
		sidebet = 9
		
	elif point == 9:
	
		sidebet = 5
		
	elif point == 6:
		
		sidebet = 8

	elif point == 8:
	
		sidebet = 6
		
	elif point == 10:
	
		sidebet = 4
		
	elif point == 4:
	
		sidebet = 10
		
	return sidebet
	
def crapsFirst():

	point = roll(2, 6)
	print("\n########")
	loop = True
	cont = True
	
	while loop:
	
		if point == 2 or point == 3 or point == 12:
			
			print("\nYou crapped out.")
			cont = False
			break
					
		elif point == 7 or point == 11:
				
			print("\nYou win.")
			cont = False
			break
			
		else:
		
			cont = True
			time.sleep(5)
			
		loop = False
				
	return cont, point
		
def crapsRolling(point):
	
	print("\n########")
	pls = roll(2, 6)
	total = pls
	yo = sideBetch(point)
	sidebet = yo
	loop = True
	
	while loop:
	
			
		if total == point:
					
			print("\nYou won")
			break
						
		elif total == 7:
					
			print("\nYou lost")
			break
			
		elif total == sidebet:
					
				print("\n[($)] - Sidebet")
			
		while total != point or total != 7:
				
			print("\n########")
			total = roll(2, 6)
			
			if total == point:
					
				print("\nYou won")
				break
						
			elif total == 7:
					
				print("\nYou lost")
				break
				
			elif total == sidebet:
					
				print("\n[($)] - Sidebet")
					
			time.sleep(5)
		
		loop = False

def craps():
	
	rolling = True
	point = 0
	total = 0
	
	cont, point = crapsFirst()
			
	if cont:
	
		while rolling:
		
			crapsRolling(point)
		
			rolling = False

def main():

	craps()
	
main()