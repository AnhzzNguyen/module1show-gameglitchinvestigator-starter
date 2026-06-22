# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose: A Streamlit-based number guessing game where players try to guess a secret number and receive hints. Points are earned based on the number of attempts.

- [x] Detail which bugs you found: 
  1. Secret number changed on every button click due to missing session state initialization.
  2. Hint messages were reversed ("Go HIGHER!" when too high).
  3. No range validation—guesses outside the valid range were accepted.

- [x] Explain what fixes you applied:
  1. Fixed session state to persist the secret number throughout gameplay.
  2. Corrected check_guess() logic to display proper hints ("Go LOWER!" for too high,  "Go HIGHER!" for too low).
  3. Added range validation to reject out-of-range guesses.
  4. Refactored logic functions to logic_utils.py with comprehensive test coverage.

## 📸 Demo Walkthrough

1. Game starts:Player sees the number guessing game interface with an input field and submit button. The secret number is set once and remains constant throughout the game.

2. First guess (40):Player enters 40 and clicks Submit. The game displays "Too Low" and shows "Guesses: 1" in the score counter.

3. Second guess (70): Player enters 70 and clicks Submit. The game displays "Too High" and updates the counter to "Guesses: 2".

4. Third guess (55): Player enters 55 and clicks Submit. The game displays "Too Low" and updates to "Guesses: 3".

5. Fourth guess (62): Player enters 62 and clicks Submit. The game displays " You got it! The secret number was 62!" and the counter shows "Guesses: 4".

6. Game completes: A "Play Again" button appears, allowing the player to reset and play another round with a new secret number.

## 🧪 Test Results


 ========================= 10/10 passed =========================

