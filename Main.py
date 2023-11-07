import random as rd
from Menu import Menu
from datetime import datetime

# date and time
date = datetime.today()
Menu.date = date.strftime("%m/%d/%y")
time = datetime.now()
Menu.time = time.strftime("%H:%M")

# card details
digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
payment_network = ['VISA', 'MasterCard', 'AMEX', 'Discover']
credit_card = ''
for d in range(16):
    credit_card += str(rd.choice(digit))
Menu.blurred_card = f"{'X' * 4} {'X' * 4} {'X' * 4} {credit_card[12:16]}"
Menu.payment_network = rd.choice(payment_network)

Menu.menu()
