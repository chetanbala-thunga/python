import random

game_on = False
guess = False

secret = None

def easy():
     global secret
     global game_on
     secret = float(random.randrange(0,100))
     while game_on == True:
     	guess = int(raw_input('Guess a number. '))
	if guess > secret:
		print('Too High! Try Again. ')
	elif guess < secret:
		print('Too Low! Try Again. ')
	elif guess == secret:
		print('YOU WIN! ')
		play_again()	

# function for hard version

def start():
     global game_on
     game_on = True
     level = raw_input('Welcome, easy, medium, hard or quit. ' )
     if level == 'easy':
	easy()
     elif level == 'medium':
	medium()
     elif level == 'hard':
	hard()
     elif level == 'quit':
	game_on = False

def play_again():
     global game_on
     game_on = True
     play = raw_input('Play again? Yes or No. ')
     if play == 'Yes':
	start()
     else:
	game_on = 'False'
	print('Thanks for playing')

start()
# function to stop game

# function calls go here
