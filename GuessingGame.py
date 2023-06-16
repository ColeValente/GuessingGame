import random

def GameStart():

	while True:
		print("\nIf you would like to exit the game type: exit")
		start = input("Welcome to the Guessing Game!!! To start please roll for a number between 1-99. \nTo roll please type roll: \n\n\t")
		NoG = 1

		if start == "roll":
			num = random.randrange(100)
			print(num)
			
			print("At anytime if you would like to end task type: exit")
			print("Your number is beteen 1-99 (it can be 1 or 99) take a guess:\n\t")
			
			while True:
				
				guess = input(f"Guess #{NoG}: ")

				if guess == "exit":
					break

				else:
					GInt = int(guess)
					if GInt == num:
						print("Your guess is correct!! Congradulations! return to the main menu.\n")
						break

					elif GInt < 1 or GInt > 99:
						print("Your number must be beteen 1 - 99. try again.")

					else:
						print("Wrong number try again.")

				NoG += 1

		elif start == "exit":
			break

		else:
			print("I'm sorry that input is invalid please try again \n")

x = GameStart()




