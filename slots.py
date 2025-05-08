import random

MAX_LINES = 3 #This variabe will not be changed(its a constant) also called a global constant
MAX_BET = 120
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine( columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end="|")
            else:
                print(column[row], end='')

        print()

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: €")
        if amount.isdigit(): #isdigit() is a function that enables you to check if an input is a number
            amount = int(amount) #if it is a number we will parse it into an integer since its a string
            if amount > 0:
                break
            else:
                print("The amount deposited must be greater than 0")
        else:
            print("Please enter a number.")

    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The number of lines must be (1-"+str(MAX_LINES)+") ")
        else:
            print("Please enter a number from (1-"+str(MAX_LINES)+").")

    return lines

def get_bet():
    while True:
        amount = input("Enter the amount you want to bet on each line: €")
        if amount.isdigit(): #isdigit() is a function that enables you to check if an input is a number
            amount = int(amount) #if it is a number we will parse it into an integer since its a string
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("The amount of bet must be beteen (€"+str(MIN_BET)+"-€"+str(MAX_BET)+").")
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money in you deposit to bet that amount, your current balance is €{balance}")
        else:
            break
    #balance = total_bet - balance
    print(f"You are betting €{bet} on {lines} lines. Total bet is equal to €{total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won €{winnings}.")
    print(f"You won on lines: ",*winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is €{balance}")
        answer = input("press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with €{balance}")

main()