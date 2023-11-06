import random as rd

digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
payment_network = ['VISA', 'MasterCard', 'AMEX', 'Discover']
credit_card = ''
for d in range(16):
    credit_card += str(rd.choice(digit))
blurred_card = f"{'X' * 4} {'X' * 4} {'X' * 4} {credit_card[12:16]}"
print(f"{blurred_card}\t{rd.choice(payment_network)}")
