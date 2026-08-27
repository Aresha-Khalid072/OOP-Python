# Python Number Guessing Game

A simple command-line game where you try to guess a randomly generated number within a set range.

## How It Works

1. The program picks a random number between **1 and 100**.
2. You enter guesses until you find the correct number.
3. After each guess, the game tells you if your guess was:
   - **Too low**
   - **Too high**
   - **Out of range** (not between 1 and 100)
   - **Invalid** (not a number)
4. Once you guess correctly, the game prints the answer and the total number of guesses you took.

## Requirements

- Python 3.x (no external libraries needed — uses the built-in `random` module)

## Usage

Run the script from your terminal:

```bash
python randomNumbers.py
```

Then follow the prompts:

```
Python Number Guessing Game
Select a number between 1 and 100
Enter your guess: 50
Too high! Try Again...
Enter your guess: 25
Too low! Try Again...
Enter your guess: 37
CORRECT! The answer was 37
Number of guesses are 3
```

## Customization

You can change the range of numbers by editing these lines at the top of the script:

```python
lowest_num=1
highest_num=100
```

## Notes

- Input is validated with `.isdigit()`, so non-numeric input (like letters or symbols) will prompt you to try again.
- Negative numbers won't be accepted by `.isdigit()`, so only positive whole numbers can be entered.