#!/usr/bin/env python
import random

class Mind_game(object):
	"""docstring for Mind_game"""
	def __init__(self):
		self.challenge_key_possoble = 8	# The number of diffrent numbers that can be used as a key
		self.challenge_key_size = 5 	# The length of the guess size
		self.board_size = 12

		self.prev_guesses = []

		self.challenge_key = []

		self.main()

	def draw_board(self):
		print '_____________'
		for empty_cells in range(self.board_size - len(self.prev_guesses)):
			print '|     |     |'
		for guesses in reversed(self.prev_guesses):
			print '|' + ''.join(guesses[0]) + '|%dB %dW|' % (guesses[1][0], guesses[1][1])
		print '`````````````'

	def check_guess(self, guess):
		#print self.challenge_key
		common =  list(set(self.challenge_key) & set(guess))
		correct_spot = 0

		for index, elem in enumerate(guess):
			if self.challenge_key[index] == guess[index]:
				correct_spot +=1
		return (correct_spot, len(common)-correct_spot)

	def setup(self):
		
		print "Welcome to Console MasterMind"
		res = 'y' if raw_input("Play with custom rules?[y/N]:") in ('y', 'Y') else 'n'

		if res != 'n': #Change Options To Custom Options
			test='a'
			while not test.strip().isdigit() and test.strip() != '':
				test = raw_input("Max possoble number [%d]:" % self.challenge_key_possoble)
			self.challenge_key_possoble = int(test.strip()) if int(test.strip()) else self.challenge_key_possoble
			test='a'
			while not test.strip().isdigit() and test.strip() != '':
				test = raw_input("Max number of possoble Numbers [%d]:"% self.challenge_key_size)
			self.challenge_key_size = int(test.strip()) if int(test.strip()) else self.challenge_key_size	
			test='a'
			while not test.strip().isdigit() and test.strip() != '':
				test = raw_input("Max board size [%d]:"% self.board_size)
			self.board_size = int(test.strip()) if int(test.strip()) else self.board_size	

	def main(self):
		self.setup()
		rand_list = range(1, self.challenge_key_possoble+1)
		for x in range(self.challenge_key_size):
			test = random.choice(rand_list)
			self.challenge_key.append(str(test))
			rand_list.remove(test)

		for x in range(self.board_size):
			self.draw_board()
			print self.challenge_key 
			test = raw_input("Guess %d intagers between 1 and %d:ex 1,2,3,4..." % (self.challenge_key_size, self.challenge_key_possoble))
			test = test.split(',')
			if self.check_guess(test)[0] == self.challenge_key_size:
				print "You Win"
				break
			self.prev_guesses.append([test, self.check_guess(test)])
		print self.challenge_key

g = Mind_game()
