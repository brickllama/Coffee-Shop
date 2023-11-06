class Menu:
    hot_coffees = [
        ('Americano', 3.95),
        ('Brewed Coffee', 4.30),
        ('Cappuccino', 5.50),
        ('Espresso', 6.20),
        ('Flat White', 3.40),
        ('Latte', 6.10),
        ('Macchiato', 6.40),
        ('Mocha', 6.45)
    ]
    teas = [
        ('Black Tea', 3.75),
        ('Earl Grey', 4.00),
        ('Peppermint', 4.25),
        ('Chai Tea', 5.00)
    ]
    cold_coffees = [
        ('Cold Brew', 4.40),
        ('Iced Americano', 4.05),
        ('Iced Coffee', 3.85),
        ('Iced Shaken Espresso', 6.30),
        ('Iced Flat White', 4.00),
        ('Iced Latte', 6.30),
        ('Iced Macchiato', 6.50),
        ('Iced Mocha', 6.65)
    ]
    seasonal_beverages = [
        'Christmas Drink or something'
    ]
    shopping_cart = []

    def select_items(prompt, options):
        for i, (name, price) in enumerate(options):
            print(f'{i + 1}\t{name:<20} {price:.2f}')
        print('Q for quit. ')
        choice = input(f'Which {prompt} would you like? ')
        try:
            choice = int(choice) - 1
            Menu.shopping_cart.append(options[choice])
            print(Menu.shopping_cart)
        except ValueError:
            if 'q' in choice.lower():
                return False
            print('It has to be a number')

    def payments():
        pass

    def menu():
        try:
            answer = int(input('1) Drinks\n2) Food\n3) Merchandise\n4) Quit\nChoice: '))
            if answer == 1:
                try:
                    answer = int(input('1) Hot Beverages\n2) Cold Beverages\nChoice: '))
                    if answer == 1:
                        print('Our hot beverages are:')
                        if Menu.select_items('hot beverage', Menu.hot_coffees + Menu.teas) is False:
                            return False
                    elif answer == 2:
                        print('Our cold beverages are:')
                        Menu.select_items('cold beverage', Menu.cold_coffees)
                    else:
                        print('You must choose between 1 and 2')
                except ValueError:
                    print('You must enter a number!')
            elif answer == 2:
                print('Our food items are:')
                Menu.select_items('food item', Menu.cold_coffees)
            elif answer == 3:
                Menu.seasonal_drinks()
            elif answer == 4:
                Menu.payments()
            else:
                print('You must enter a value between 1 and 4!')
        except ValueError:
            print('You must enter a number!')

        Menu.menu()
