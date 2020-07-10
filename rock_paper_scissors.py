import random
import os


class RockPaperScissors:
    win_dict = {'rock': 'paper',
                'paper': 'scissors',
                'scissors': 'rock'}

    def play(self):
        self.say_hello()
        self.read_options()

    def read_action(self):
        self.choice = input()
        if self.choice not in ['rock', 'paper', 'scissors',
                               '!exit', '!rating']:
            print('Invalid input')
            self.read_action()
        elif self.choice == '!exit':
            self.exit_game()
        elif self.choice == '!rating':
            self.show_rating()
            self.read_action()
        else:
            self.status()

    def status(self):
        self.computer = random.choice(['rock', 'paper', 'scissors'])
        if self.choice == self.computer:
            self.draw()
            self.read_action()
        elif RockPaperScissors.win_dict[self.computer] == self.choice:
            self.win()
            self.read_action()
        else:
            self.lose()
            self.read_action()

    def custom_read_action(self):
        self.choice = input()
        if self.choice not in self.options + ['!rating', '!exit']:
            print('Invalid input')
            self.custom_read_action()
        elif self.choice == '!exit':
            self.exit_game()
        elif self.choice == '!rating':
            self.show_rating()
            self.custom_read_action()
        else:
            self.custom_status()

    def custom_status(self):
        self.computer = random.choice(self.options)
        if self.choice == self.computer:
            self.draw()
            self.custom_read_action()
        else:
            self.choice_index = self.options.index(self.choice)
            self.half_list = range(0, round(len(self.options) / 2))
            self.win_options = [(x + self.choice_index) % len(self.options) for x in self.half_list]
            if  self.options.index(self.computer) in self.win_options:
                # print(self.win_options)
                self.lose()
                self.custom_read_action()
            else:
                # print(self.win_options)
                self.win()
                self.custom_read_action()

    def lose(self):
        print(f'Sorry, but computer chose {self.computer}')

    def win(self):
        print(f'Well done. Computer chose {self.computer} and failed')
        self.user_score += 100

    def draw(self):
        print(f'There is a draw ({self.choice})')
        self.user_score += 50

    def show_rating(self):
        print('Your rating:', self.user_score)

    def exit_game(self):
        print('Bye!')
        self.rating_file = open('rating.txt', 'w')
        self.rating[self.username] = str(self.user_score)
        self.rating_lines = [f'{list(self.rating.keys())[i]} {list(self.rating.values())[i]}\n' for
                             i in range(len(list(self.rating.keys())))]
        self.rating_file.writelines(self.rating_lines)
        self.rating_file.close()
        exit()

    def say_hello(self):
        self.username = input('Enter your name: ')
        print('Hello,', self.username)
        if os.path.exists("rating.txt"):
            self.rating_file = open("rating.txt", "r+")
        else:
            self.rating_file = open("rating.txt", "w")
        self.rating_lines = self.rating_file.readlines()
        self.rating_file.close()
        self.rating = {}
        self.user_list = []
        for line in self.rating_lines:
            user, score = line.split()
            self.user_list.append(user)
            self.rating[user] = score
        if self.username not in self.user_list:
            self.rating[self.username] = '0'
        self.user_score = int(self.rating[self.username])

    def read_options(self):
        self.options = input()
        if self.options == '':
            print("Okay, let's start")
            self.read_action()
        else:
            self.options = self.options.split(",")
            print("Okay, let's start")
            self.custom_read_action()



game = RockPaperScissors()
game.play()
