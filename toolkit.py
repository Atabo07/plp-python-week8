# toolkit.py
# Personal Mini-Toolkit - Week 8 Final Project
# A menu-driven program with four tools:
#   1. Number Guessing Game   2. To-Do List
#   3. Simple Calculator      4. Name Formatter

import random

# The to-do list lives OUTSIDE the main loop so tasks are remembered
# even when the user leaves the To-Do tool and comes back later.
tasks = []

print("Welcome to the Personal Mini-Toolkit!")
print("Pick a tool from the menu and have fun.")

running = True

# ---------------------------------------------------------------
# MAIN MENU LOOP - keeps showing the menu until the user quits
# ---------------------------------------------------------------
while running:
    print()
    print("========== MAIN MENU ==========")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Name Formatter")
    print("5. Quit")
    print("===============================")
    choice = input("Choose a tool (1-5): ").strip()

    # -----------------------------------------------------------
    # TOOL 1: Number Guessing Game
    # The computer picks a number from 1 to 20. The player has 6
    # tries and gets "too high" / "too low" hints after each guess.
    # Uses: while loop, conditionals, try/except, f-strings.
    # -----------------------------------------------------------
    if choice == "1":
        print()
        print("--- Number Guessing Game ---")
        secret = random.randint(1, 20)
        tries_left = 6
        won = False
        print("I'm thinking of a number between 1 and 20.")
        print(f"You have {tries_left} tries. Good luck!")

        while tries_left > 0:
            guess_text = input("Your guess: ").strip()

            try:
                guess = int(guess_text)
            except ValueError:
                print(f'"{guess_text}" is not a whole number. Try again (no try used).')
                continue

            if guess < 1 or guess > 20:
                print("Please guess a number between 1 and 20 (no try used).")
                continue

            tries_left = tries_left - 1

            if guess == secret:
                won = True
                break
            elif guess < secret:
                print(f"Too low! Tries left: {tries_left}")
            else:
                print(f"Too high! Tries left: {tries_left}")

        if won:
            tries_used = 6 - tries_left
            print(f"Correct! The number was {secret}. You got it in {tries_used} tries!")
        else:
            print(f"Out of tries! The number was {secret}. Better luck next time.")

    # -----------------------------------------------------------
    # TOOL 2: To-Do List
    # Add tasks, view them, mark one as done, or clear them all.
    # Uses: a list that changes while the program runs (append,
    # pop, clear), while loop, for loop, conditionals, f-strings.
    # -----------------------------------------------------------
    elif choice == "2":
        print()
        print("--- To-Do List ---")
        in_todo = True

        while in_todo:
            print()
            print("a) Add a task")
            print("v) View tasks")
            print("d) Mark a task as done")
            print("c) Clear all tasks")
            print("b) Back to main menu")
            action = input("What would you like to do? ").strip().lower()

            if action == "a":
                new_task = input("Task to add: ").strip()
                if new_task == "":
                    print("A task can't be empty. Nothing was added.")
                else:
                    tasks.append(new_task)
                    print(f'Added "{new_task}". You now have {len(tasks)} task(s).')

            elif action == "v":
                if len(tasks) == 0:
                    print("Your to-do list is empty. Nice and clear!")
                else:
                    print(f"You have {len(tasks)} task(s):")
                    for number, task in enumerate(tasks, start=1):
                        print(f"  {number}. {task}")

            elif action == "d":
                if len(tasks) == 0:
                    print("There is nothing to mark as done yet.")
                else:
                    for number, task in enumerate(tasks, start=1):
                        print(f"  {number}. {task}")
                    number_text = input("Number of the finished task: ").strip()
                    try:
                        number = int(number_text)
                    except ValueError:
                        number = 0
                    if number >= 1 and number <= len(tasks):
                        finished = tasks.pop(number - 1)
                        print(f'Well done! "{finished}" is complete. {len(tasks)} left.')
                    else:
                        print(f'"{number_text}" is not a task number on the list.')

            elif action == "c":
                if len(tasks) == 0:
                    print("The list is already empty.")
                else:
                    count = len(tasks)
                    tasks.clear()
                    print(f"Cleared {count} task(s). Fresh start!")

            elif action == "b":
                in_todo = False
                print("Leaving the To-Do List. Your tasks are saved while the program runs.")

            else:
                print(f'"{action}" is not an option. Please type a, v, d, c or b.')

    # -----------------------------------------------------------
    # TOOL 3: Simple Calculator
    # Takes two numbers and an operator (+, -, *, /) and prints
    # the answer. Uses: conditionals (if/elif/else), try/except,
    # a divide-by-zero check, f-strings.
    # -----------------------------------------------------------
    elif choice == "3":
        print()
        print("--- Simple Calculator ---")
        first_text = input("First number: ").strip()
        operator = input("Operator (+, -, *, /): ").strip()
        second_text = input("Second number: ").strip()

        try:
            first = float(first_text)
            second = float(second_text)
        except ValueError:
            print("Those weren't both valid numbers, so I can't calculate. Try again!")
        else:
            if operator == "+":
                print(f"{first:g} + {second:g} = {first + second:g}")
            elif operator == "-":
                print(f"{first:g} - {second:g} = {first - second:g}")
            elif operator == "*":
                print(f"{first:g} * {second:g} = {first * second:g}")
            elif operator == "/":
                if second == 0:
                    print("Oops! You can't divide by zero.")
                else:
                    print(f"{first:g} / {second:g} = {first / second:g}")
            else:
                print(f'"{operator}" is not a supported operator. Use +, -, * or /.')

    # -----------------------------------------------------------
    # TOOL 4: Name Formatter
    # Cleans up messy capitalisation and shows the user's initials.
    # Uses: variables, string methods, conditionals, f-strings.
    # -----------------------------------------------------------
    elif choice == "4":
        print()
        print("--- Name Formatter ---")
        first_name = input("First name: ").strip()
        last_name = input("Last name: ").strip()

        if first_name == "" or last_name == "":
            print("I need both a first and a last name. Please try again.")
        else:
            first_name = first_name.title()
            last_name = last_name.title()
            initials = first_name[0] + last_name[0]
            print(f"Formatted name: {first_name} {last_name}")
            print(f"Surname first:  {last_name.upper()}, {first_name}")
            print(f"Your initials:  {initials}")

    # -----------------------------------------------------------
    # QUIT: stop the main loop
    # -----------------------------------------------------------
    elif choice == "5":
        running = False

    # -----------------------------------------------------------
    # ANYTHING ELSE: polite message, then the menu comes back
    # -----------------------------------------------------------
    else:
        print(f'Oops! "{choice}" is not on the menu. Please type a number from 1 to 5.')

print()
print("Thanks for using the Personal Mini-Toolkit. See you next time!")
