import random

def reverse_number(number):
    return int(str(number)[::-1])

def calculator():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back to Main Menu")
        
        choice = input("Please select an option (1/2/3/4/5): ")
        
        if choice == '5':
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option.")
            continue
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")

def gambling_game():
    print("\nWelcome to the Gambling Game!")
    print("You have $100. You can bet any amount (minimum $1) to guess the correct number (1-5).")
    print("If you guess right, you double your bet; otherwise, you lose your bet.")
    
    money = 100
    
    while money > 0:
        print(f"\nYour current balance: ${money}")
        bet = input("Place your bet (1-$100): ")
        
        if not bet.isdigit() or int(bet) < 1 or int(bet) > money:
            print("Invalid bet. Please enter a valid bet.")
            continue
        
        bet = int(bet)
        
        guess = int(input("Guess a number (1-5): "))
        if guess < 1 or guess > 5:
            print("Invalid guess. Please guess a number between 1 and 5.")
            continue
        
        result = random.randint(1, 5)
        print(f"The correct number was: {result}")
        
        if guess == result:
            print(f"Congratulations! You guessed right and won ${bet}!")
            money += bet
        else:
            print(f"Sorry, you guessed wrong and lost ${bet}.")
            money -= bet

    print("You have run out of money. Thank you for playing!")

while True:
    print("\nMain Menu:")
    print("1. Reverse a Number")
    print("2. Calculator")
    print("3. Play Gambling Game")
    print("4. Exit")
    
    option = input("Please select an option (1/2/3/4): ")
    
    if option == '4':
        break
    
    if option not in ['1', '2', '3']:
        print("Invalid choice. Please select a valid option.")
        continue
    
    if option == '1':
        number = int(input("Please enter a number to reverse: "))
        reversed_num = reverse_number(number)
        print(f"Reversed Number: {reversed_num}")
    elif option == '2':
        calculator()
    elif option == '3':
        gambling_game()
