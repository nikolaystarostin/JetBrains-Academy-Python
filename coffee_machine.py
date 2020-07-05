class CoffeeMachine:

    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def remaining(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money
''')
        self.action()

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        self.action()

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:'))
        self.milk += int(input('Write how many ml of milk do you want to add:'))
        self.coffee += int(input('Write how many grams of coffee beans do you want to add:'))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add:'))
        self.action()

    def exit(self):
        quit()

    def buy(self):
        drink = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if drink == '1':
            needed_water = 250
            needed_milk = 0
            needed_coffee = 16
            add_money = 4
        elif drink == '2':
            needed_water = 350
            needed_milk = 75
            needed_coffee = 20
            add_money = 7
        elif drink == '3':
            needed_water = 200
            needed_milk = 100
            needed_coffee = 12
            add_money = 6
        elif drink == 'back':
            self.action()
        else:
            print('Wrong input, back to the main menu')
            self.action()
        if self.water - needed_water < 0:
            print('Sorry, not enough water')
            self.action()
        if self.milk - needed_milk < 0:
            print('Sorry, not enough milk')
            self.action()
        if self.coffee - needed_coffee < 0:
            print('Sorry, not enough coffee beans')
            self.action()
        if self.cups <= 0:
            print('Sorry, not enough cups')
            self.action()
        else:
            self.water -= needed_water
            self.milk -= needed_milk
            self.coffee -= needed_coffee
            self.cups -= 1
            self.money += add_money
            print('I have enough resources, making you a coffee!')
            self.action()

    def action(self):
        action = input('Write action (buy, fill, take, remaining, exit):')
        if action == 'remaining':
            self.remaining()
        if action == 'exit':
            self.exit()
        if action == 'buy':
            self.buy()
        if action == 'take':
            self.take()
        if action == 'fill':
            self.fill()
        else:
            print('Wrong input, back to the main menu')
            self.action()


coffee_machine = CoffeeMachine()
coffee_machine.action()
