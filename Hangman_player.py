import Hangman

hangman = Hangman.Hangman('c:\\wordlist.txt')
hangman.choose_the_word()
hangman.fill_the_word_status()

while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if(hangman.lives == 0):
        print("Out of attempts. \n |||GAME OVER||| \n The word was: ",format(hangman.chosen_word))
        break

    elif (hangman.chosen_word == ''.join(hangman.word_status)):
        print("Hurray! You've guessed the word correctly.", format(hangman.chosen_word))
        break
        