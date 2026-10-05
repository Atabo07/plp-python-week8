# Personal Mini-Toolkit

**Week 8 Final Project - PLP Python**

## What my toolkit does

A menu-driven Python program with four tools. The menu comes back after every tool and only stops when you choose Quit. Invalid choices get a polite message instead of crashing the program.

| # | Tool | What it does |
|---|------|--------------|
| 1 | Number Guessing Game | Guess a secret number from 1 to 20 in 6 tries, with "too high / too low" hints. |
| 2 | To-Do List | Add, view, complete and clear tasks stored in a list that changes while the program runs. |
| 3 | Simple Calculator | Does `+`, `-`, `*`, `/` on two numbers and refuses to divide by zero. |
| 4 | Name Formatter | Tidies messy capitalisation and shows "Surname first" and initials. |

Concepts used: variables, `input()`/`print()`, `while` and `for` loops, `if / elif / else`, lists (`append`, `pop`, `clear`), f-strings, and `try / except`.

## How to run it

1. Make sure Python 3 is installed (`python --version`).
2. Download or clone this repository.
3. In a terminal, go to the project folder and run:

```
python toolkit.py
```

(On some systems use `python3 toolkit.py`.)

## Files

- `toolkit_plan.txt` - my plan: tools, exact menu text, concepts and test checklist
- `toolkit.py` - the program
- `screenshots/` - the menu with invalid choices, and each tool running

## Reflection

The hardest part was combining everything into one program, because the menu loop, the to-do sub-menu and the guessing game all contain their own loops and it was easy to lose track of which loop I was in. The bug that took longest to fix was in the guessing game: at first a wrong input like a letter used up one of the player's tries, so I added `try / except` with `continue` so only real guesses are counted. Another small bug was that the to-do list forgot its tasks every time I left the tool, which I fixed by creating the list once before the main loop instead of inside the tool. Writing `toolkit_plan.txt` first really did make building faster, since I already knew the menu text and which concepts each tool needed. Testing every menu path, including quitting and invalid input, helped me catch mistakes like a "1 tries left" message. With one more week I would save the to-do list to a file so it survives after the program closes, add a difficulty setting to the guessing game, and add a countdown timer as a fifth tool.
