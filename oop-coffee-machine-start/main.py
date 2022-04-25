from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_on = True

# TODO: Print our current resources
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_maker.report()
money_machine.report()

# TODO: Use while loop to have the program end when user inserts "off".
while coffee_machine_on:
    # TODO: Create object for each menu item
    espresso = MenuItem("espresso", 50, 0, 18, 1.5)
    latte = MenuItem("latte", 200, 150, 24, 2.5)
    cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

    # TODO: Ask user what they would like to order.
    menu = Menu()
    menu_items = menu.get_items()

    drink_choice = input(f"What would you like to drink Sir/Ma\'m? ({menu_items}): ")
    if drink_choice == "off":
        coffee_machine_on = False
    # TODO: Has program print current resources if user inserts "report".
    elif drink_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # TODO: Use method to find the drink chosen by user and return the drink name, ingredients, and cost.
        chosen_drink = menu.find_drink(drink_choice)
        # TODO: Use method to check and see if there is enough resources to make the drink
        if coffee_maker.is_resource_sufficient(chosen_drink):
            if money_machine.make_payment(chosen_drink.cost):
                coffee_maker.make_coffee(chosen_drink)










