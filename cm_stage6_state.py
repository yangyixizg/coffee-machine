# stage 6 ###################################
class CoffeeMachine:
    # list of coffee: water/ml, milk/ml, beans/g, cup/1
    ingredients_text = ['water', 'milk', 'beans', 'cup']
    espresso = [250, 0, 16, 1]
    latte = [350, 75, 20, 1]
    cappuccino = [200, 100, 12, 1]
    # coffee price/$: espresso, latte, cappuccino
    cost = [4, 7, 6]
    fill_amount = [0, 0, 0, 0]

    def __init__(self, water, milk, beans, cups, money):
        # ingredients: water, milk, coffee beans, disposable cups
        self.ingredients_total = [water, milk, beans, cups]
        self.money = money
        self.state = "choosing_an_action"
        # self.next_state = "choosing_an_action"

    # def __str__(self):

    def enough_resources(self, coffee_arg):
        for i, v in enumerate(self.ingredients_total):
            if v < coffee_arg[i]:
                print(f"Sorry, not enough {self.ingredients_text[i]}!")
                return False
        return True

    def machine_resources(self):
        print("The coffee machine has:")
        print(f'{self.ingredients_total[0]} of water')
        print(f'{self.ingredients_total[1]} of milk')
        print(f'{self.ingredients_total[2]} of coffee beans')
        print(f'{self.ingredients_total[3]} of disposable cups')
        print(f'{self.money} of money')

    def start(self):
        print("Write action (buy, fill, take, remaining, exit):")

    def user_input(self, in1):
        if self.state == "choosing_an_action":
            if in1 == 'buy':
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu')
                self.state = "choosing_a_type_of_coffee"
            elif in1 == 'fill':
                CoffeeMachine.fill_amount = [0, 0, 0, 0]
                print("Write how many ml of water do you want to add:")
                self.state = "choosing_the_fill_quantity_water"
            elif in1 == 'take':
                print(f'I gave you ${self.money}')
                self.money = 0
                self.state = "choosing_an_action"
            elif in1 == 'remaining':
                self.machine_resources()
                self.state = "choosing_an_action"
            elif in1 == 'exit':
                self.state = "exit"
        elif self.state == "choosing_a_type_of_coffee":
            if in1 == 'back':
                self.state = "choosing_an_action"
            else:
                if in1 == '1':
                    if self.enough_resources(CoffeeMachine.espresso):
                        self.ingredients_total = [i - j for i, j in zip(self.ingredients_total, CoffeeMachine.espresso)]
                        self.money += CoffeeMachine.cost[int(in1) - 1]
                        print("I have enough resources, making you a coffee!")
                elif in1 == '2':
                    if self.enough_resources(CoffeeMachine.latte):
                        self.ingredients_total = [i - j for i, j in zip(self.ingredients_total, CoffeeMachine.latte)]
                        self.money += CoffeeMachine.cost[int(in1) - 1]
                        print("I have enough resources, making you a coffee!")
                elif in1 == '3':
                    if self.enough_resources(CoffeeMachine.cappuccino):
                        self.ingredients_total = [i - j for i, j in zip(self.ingredients_total, CoffeeMachine.cappuccino)]
                        self.money += CoffeeMachine.cost[int(in1) - 1]
                        print("I have enough resources, making you a coffee!")
                self.state = "choosing_an_action"
        elif self.state == "choosing_the_fill_quantity_water":
            CoffeeMachine.fill_amount[0] = int(in1)
            print("Write how many ml of milk do you want to add:")
            self.state = "choosing_the_fill_quantity_milk"
        elif self.state == "choosing_the_fill_quantity_milk":
            CoffeeMachine.fill_amount[1] = int(in1)
            print("Write how many grams of coffee beans do you want to add:")
            self.state = "choosing_the_fill_quantity_beans"
        elif self.state == "choosing_the_fill_quantity_beans":
            CoffeeMachine.fill_amount[2] = int(in1)
            print("Write how many disposable cups of coffee do you want to add:")
            self.state = "choosing_the_fill_quantity_cups"
        elif self.state == "choosing_the_fill_quantity_cups":
            CoffeeMachine.fill_amount[3] = int(in1)
            self.ingredients_total = [i + j for i, j in zip(self.ingredients_total, CoffeeMachine.fill_amount)]
            self.state = "choosing_an_action"


obj_cm = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    if obj_cm.state == 'exit':
        break
    else:
        if obj_cm.state == 'choosing_an_action':
            obj_cm.start()
        obj_cm.user_input(input("> "))
