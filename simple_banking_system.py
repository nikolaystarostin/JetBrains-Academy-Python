import random
import sqlite3

# Write your code here
class Bank:
    def __init__(self):
        self.choices = {'1': self.create,
                        '2': self.login,
                        '0': self.exit}
        self.choices_menu = {'1': self.balance,
                             '2': self.add,
                             '3': self.transfer,
                             '4': self.close,
                             '5': self.start,
                             '0': self.exit}
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0);''')

    def start(self):
        print('\n1. Create an account\n2. Log into account\n0. Exit')
        choice = input()
        self.choices.get(choice)()

    def create(self):
        card15 = '400000' + str(random.randint(0, 999999999)).zfill(9)
        self.luhn_algorithm(card15)
        self.card = card15 + self.luhn
        self.pin = str(random.randint(0, 9999)).zfill(4)
        print(f'\nYour card has been created\n'
              f'Your card number:\n'
              f'{self.card}\n'
              f'Your card PIN:\n'
              f'{self.pin}')
        self.cur.execute('SELECT number FROM card;')
        if self.card in self.cur.fetchall():
            self.create()
        else:
            self.cur.execute(
                f'INSERT INTO card (number, pin) VALUES ({self.card}, {self.pin});'
            )
            self.conn.commit()
            self.start()

    def luhn_algorithm(self, card15):
        card_list = list(card15)
        card_list = [int(x) for x in card_list]
        card_list = [card_list[x] * 2 if (x + 1) % 2 == 1 else card_list[x] for x in range(0, 15)]
        card_list = [x - 9 if x > 9 else x for x in card_list]
        num_sum = sum(card_list)
        luhn = 0
        while (num_sum + luhn) % 10 != 0:
            luhn += 1
        self.luhn = str(luhn)

    def login(self):
        card_input = input('\nEnter your card number:\n')
        pin_input = input('Enter your PIN\n')
        self.cur.execute(
            f'''
SELECT number, pin, balance 
FROM card 
WHERE number = {card_input} AND pin = {pin_input}''')
        if len(self.cur.fetchall()) != 0:
            print('\nYou have successfully logged in!')
            self.logged_card = card_input
            self.menu()
        else:
            print('\nWrong card number or PIN!')
            self.start()

    def menu(self):
        print('\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')
        choice = input()
        self.choices_menu.get(choice)()

    def balance(self):
        self.cur.execute(f'SELECT balance FROM card WHERE number = {self.logged_card};')
        print(f'\nBalance: {self.cur.fetchone()[0]}')
        self.menu()

    def add(self):
        self.cur.execute(f'SELECT balance FROM card WHERE number = {self.logged_card};')
        new_balance = self.cur.fetchone()[0] + int(input('Enter income:\n'))
        self.cur.execute(f'UPDATE card SET balance = {new_balance} WHERE number = {self.logged_card}')
        self.conn.commit()
        print('Income was added!')
        self.menu()

    def transfer(self):
        print('Transfer')
        transfer_to = input('Enter card number:\n')
        card15 = transfer_to[:-1]
        self.luhn_algorithm(card15)
        if transfer_to != card15 + self.luhn:
            print('Probably you made mistake in the card number. \nPlease try again!')
            self.menu()
        elif transfer_to == self.logged_card:
            self.menu()
        else:
            self.cur.execute('SELECT number FROM card')
            rows = self.cur.fetchall()
            cards_list = [x[0] for x in rows]
            print(cards_list)
            if transfer_to not in cards_list:
                print('Such a card does not exist.')
                self.menu()
            else:
                transfer_amount = int(input('Enter how much money you want to transfer:'))
                self.cur.execute(f'SELECT balance FROM card WHERE number = {self.logged_card};')
                balance = self.cur.fetchone()[0]
                if transfer_amount > balance:
                    print('Not enough money!')
                    self.menu()
                else:
                    self.cur.execute(
                        f'UPDATE card SET balance = {balance - transfer_amount} WHERE number = {self.logged_card};')
                    self.conn.commit()
                    self.cur.execute(f'SELECT balance FROM card WHERE number = {transfer_to};')
                    balance_to = self.cur.fetchone()[0]
                    self.cur.execute(
                        f'UPDATE card SET balance = {balance_to + transfer_amount} WHERE number = {transfer_to};')
                    self.conn.commit()
                    print('Success!')
                    self.menu()

    def close(self):
        self.cur.execute(f'DELETE FROM card WHERE number = {self.logged_card};')
        self.conn.commit()
        print('The account has been closed!')
        self.start()

    def exit(self):
        exit()


user_bank = Bank()
user_bank.start()
