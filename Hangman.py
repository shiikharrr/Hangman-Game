import random
import re

class Hangman:

    def __init__(self,wordlist):

        self.wordlist = wordlist
        self.lives = 6
        self.current_letter = ''
        self.chosen_word = ''
        self.guessed_letters = []

    def choose_the_word(self):

        file = open(self.wordlist)
        words = file.read().split('\n')
        word_count = len(words)
        self.chosen_word = words[random.randrange(0,word_count)]
        self.word_status = ['-' for i in range(len(self.chosen_word))]

    def fill_the_word_status(self):

        nos = random.randrange(1,3)
        for i in range(nos):
            position = random.randrange(0,len(self.chosen_word))
            self.word_status[position] = self.chosen_word[position]

    def guess_the_letter(self):

        letter = input("Guess the letter:")

        if(letter in self.guessed_letters):
            print("You've already guessed that letter. Your guess : ", format(self.guessed_letters))
            return

        self.guessed_letters.append(letter)

        occurences = []
        occurence = re.finditer(letter,self.chosen_word)

        for m in occurence:
            occurences.append(m.start())

        if (len(occurences)) == 0:
            self.lives -= 1
            print("Oops! Your guess was wrong. Lives remaining ", format(self.lives))
        else:
            for position in occurences:
                self.word_status[position] = self.chosen_word[position]
                print("Correct word!")


    def get_word_status(self):

            print("Current status:  () \n",format(''.join(self.word_status)))