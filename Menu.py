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
        ('Black tea', 3.75),
        ('Earl Grey', 4.00),
        ('Peppermint', 4.25),
        ('Chai Tea', 5.00)
    ]
    cold_beverages = [
        'Cold Brew', 'Iced Americano', 'Iced Coffee',
        'Iced Shaken Espresso', 'Iced Flat White', 'Iced Latte',
        'Iced Macchiato', 'Iced Mocha'
    ]
    seasonal_beverages = [
        'Christmas Drink or something'
    ]

    def hot_drinks():
        options = Menu.hot_coffees
        options += Menu.teas
        print('Our hot beverages are:')
        for i, (name, price) in enumerate(options):
            print(f'{i + 1}\t{name}\t{price}')
        try:
            choice = int(input('Which drink would you like? '))
            choice = choice - 1
            print(choice)
        except ValueError:
            print('It has to be a number')

    def cold_drinks():
        pass

    def seasonal_drinks():
        pass

    def payments():
        pass

    def menu():
        answer = input('1) Drinks\n2) Food\n3) Merchandise\n4) Quit\nChoice: ')
        if answer.isnumeric():
            answer = int(answer)
            if answer == 1:
                Menu.hot_drinks()
            elif answer == 2:
                Menu.cold_drinks()
            elif answer == 3:
                Menu.seasonal_drinks()
            elif answer == 4:
                Menu.payments()
            else:
                print('You must enter a value between 1 and 4!')
                Menu.menu()
        else:
            print('You must enter a number!')
            Menu.menu()
