import random

class Hangman:

    def play(self):
        self.action = input('Type "play" to play the game, "exit" to quit: ')
        if self.action == 'play':
            self.start()
        elif self.action == 'exit':
            exit()
        else:
            self.play()

    def start(self):
        print('H A N G M A N')
        self.choices = ['python', 'java', 'kotlin', 'javascript']
        self.word = random.choice(self.choices)
        self.word_set = set(self.word)
        self.word_list = list(self.word)
        self.guessed = list()
        self.all_inputs = list()
        self.take_input()

    def print_state(self):
        self.guessed_set = set(self.guessed)
        self.state_list = ['-' if x not in self.guessed_set else x for x in self.word_list]
        if '-' in self.state_list:
            print('\n', *self.state_list, sep='')

    def take_input(self):
        i = 8
        while i > 0:
            self.print_state()
            if '-' not in self.state_list:
                break
            self.letter = input('Input a letter: ')
            if self.letter in self.word_set:
                if self.letter not in self.guessed:
                    self.guessed += self.letter
                else:
                    print('You already typed this letter')
            elif self.letter in self.all_inputs:
                print('You already typed this letter')
            elif len(self.letter) != 1:
                print('You should input a single letter')
            elif not (self.letter.isascii() and self.letter.islower()):
                print('It is not an ASCII lowercase letter')
            else:
                print('No such letter in the word')
                self.all_inputs += self.letter
                i -= 1
        if '-' in self.state_list:
            print('You are hanged!\n')
            self.play()
        else:
            print(f"""You guessed the word {self.word}!\nYou survived!\n""")
            self.play()


game = Hangman()
game.play()
