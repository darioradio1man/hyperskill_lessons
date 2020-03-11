class CoffeeMachine:
    def __init__(self):
        self.available_water = 400
        self.available_milk = 540
        self.available_coffee = 120
        self.available_cups = 9
        self.available_money = 550
        self.active_state = True
        self.current_action = ""
        self.coffee_type = ""

    def get_water(self):
        return self.available_water

    def get_milk(self):
        return self.available_milk

    def get_coffee(self):
        return self.available_coffee

    def get_money(self):
        return self.available_money

    def get_cups(self):
        return self.available_cups

    def get_state(self):
        return self.active_state

    def get_action(self):
        return self.current_action

    def get_type(self):
        return self.coffee_type

    def set_water(self, val):
        self.available_water += val

    def set_milk(self, val):
        self.available_milk += val

    def set_coffee(self, val):
        self.available_coffee += val

    def set_money(self, val):
        self.available_money += val

    def set_cups(self, val):
        self.available_cups += val

    def set_state(self, new_state):
        self.active_state = new_state

    def set_action(self, new_action):
        self.current_action = new_action

    def set_type(self, new_type):
        self.coffee_type = new_type

    def exit_state(self):
        self.set_state(False)

    def state(self):
        print(f"The coffee machine has:")
        print(f"{self.get_water()} of water")
        print(f"{self.get_milk()} of milk")
        print(f"{self.get_coffee()} of coffee beans")
        print(f"{self.get_cups()} of disposable cups")
        print(f"{self.get_money()} of money")
        print("")

    def take_all_money(self):
        print(f"I gave you ${self.get_money()}")
        self.set_money(- self.get_money())

    def fill_resources(self):
        self.set_water(int(input("Write how many ml of water do you want to add: ")))
        self.set_milk(int(input("Write how many ml of milk do you want to add: ")))
        self.set_coffee(int(input("Write how many grams of coffee beans do you want to add: ")))
        self.set_cups(int(input("Write how many disposable cups of coffee do you want to add: ")))

    def choose(self):
        self.set_type(input("What do you want to buy? 1 - espresso, 2 - latte, "
                            "3 - cappuccino: back -  to main menu: "))
        return self.get_type()

    def update_resources(self, water, milk, coffee, money):
        self.set_water(- water)
        self.set_milk(- milk)
        self.set_coffee(- coffee)
        self.set_cups(- 1)
        self.set_money(money)

    def resource_check(self, water, milk, coffee):
        if self.get_water() - water < 0:
            print("Sorry, not enough water!")
            return False
        elif self.get_milk() - milk < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.get_coffee() - coffee < 0:
            print("Sorry, not enough coffee beans!")
            return False
        elif self.get_cups() <= 0:
            print("Sorry, not enough cups!")
            return False

    def coffee(self, coffee_type):
        if coffee_type == "1":
            if self.resource_check(250, 0, 16) is not False:
                self.update_resources(250, 0, 16, 4)
                print("I have enough resources, making you a coffee!")
        elif coffee_type == "2":
            if self.resource_check(350, 75, 20) is not False:
                self.update_resources(350, 75, 20, 7)
                print("I have enough resources, making you a coffee!")
        elif coffee_type == "3":
            if self.resource_check(200, 100, 12) is not False:
                self.update_resources(200, 100, 12, 6)
                print("I have enough resources, making you a coffee!")


the_coffee_machine = CoffeeMachine()
while the_coffee_machine.get_state() is True:
    the_coffee_machine.set_action(input("Write action(buy, fill, take, remaining, exit): "))
    print("")
    if the_coffee_machine.get_action() == "buy":
        the_coffee_type = the_coffee_machine.choose()
        the_coffee_machine.coffee(the_coffee_type)
        print()
    elif the_coffee_machine.get_action() == "fill":
        the_coffee_machine.fill_resources()
    elif the_coffee_machine.get_action() == "take":
        the_coffee_machine.take_all_money()
    elif the_coffee_machine.get_action() == "remaining":
        the_coffee_machine.state()
    elif the_coffee_machine.get_action() == "exit":
        the_coffee_machine.set_state(False)
    else:
        print("Only buy, fill, take, remaining, exit actions can be used")
        print("More carefully, please")
