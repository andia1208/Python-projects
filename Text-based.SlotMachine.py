
#Text based slot machine project
import random  #because we need to generate the random values for the slot machine

MAX_LINES = 3  #It's a constant value, that it will not change
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#create a dictionary for the symbols that the slot machine will have
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


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#create e function that generate what symbols gonna be in each column based on the frequency of symbols that we have. Essentialy, randomly pick the number of rows inside of
# each column
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  #define a list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []  #define a list
    for _ in range(cols):  #for every colon we need to generate a certain number of symbols. this happens 3 times
        column = []
        current_symbols = all_symbols[:]  #it's a list
        for _ in range(rows):
            value = random.choice(current_symbols)  #we can use random because we import the random library. Pick random value
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


#create a function to collect user input and get the deposit from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():   #check that the amount is a number
            amount = int(amount)   #convert it into int because it is a string
            if amount > 0:
                break   #if true, break the while loop and return the amount
            else:
                print("Amount must be greater than 0.")
        else:    #if the amount is not a digit, then:
            print("Please enter a number.")

    return amount

#create a function to collect the bet from users
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

#Create a function to get the amount the user want to bet for each line. Create the max and min value
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:   #check if the user has enough money in balance to bet
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()