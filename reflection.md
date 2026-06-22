# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1.the hints were backwards
  2. the seeting stated that Range: 1 to 100, but it's currently able to enter 1000 (out of range)

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 1000 | notice player that the entered number is out of range | hint: GO LOWER| none|
| 50| hint: GO HIGHER | hint: GO LOWER | none|
| 6 | hint: GO HIGHER| hint: GO Higher and "Out of attempts! The secret was 21. Score: 5" at the 7th attempt| none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code (Claude AI). Used for debugging, refactoring, writing tests, and fixing bugs throughout the project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Correct Suggestion: High/Low Message Bug Fix
    - What the AI suggested: The AI identified that in the `check_guess()` function, the hint messages were backwards. When the guess was too high (guess > secret), it showed "📈 Go HIGHER!" when it should say "Go LOWER!" And vice versa for too low guesses. The AI swapped the messages to fix this logic error.
    - How I verified: 
      1. Tested the game manually - when I guessed a number higher than the secret, it now correctly says "Go LOWER!"
      2. Created and ran pytest tests (`test_guess_too_high_message_correct()` and `test_guess_too_low_message_correct()`) that specifically verify the message text matches the outcome
      3. All tests passed, confirming the fix is correct

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Incorrect/Misleading Suggestion: Removing Conditional Logi
    - What the AI suggested: When attempting to fix the FIXME comment on line 142, the AI suggested removing the if-else block (lines 146-149) that conditionally converts the secret to a string on even attempts. The AI wanted to simplify it to just `secret = st.session_state.secret`.
    - Why it was misleading: I rejected this suggestion because I wanted to investigate more carefully first. Upon closer inspection of the actual code, both branches of the conditional do the exact same thing (both assign `st.session_state.secret`), so the conditional is dead code but not actually causing a bug. The AI's suggestion was to delete code without fully understanding that it wasn't actually broken.
    - How I verified: I examined the code on lines 146-149 and confirmed that both the `if` and `else` branches contain identical statements. This meant the conditional logic was pointless and the AI's fix was technically correct but missed the nuance that the bug was already neutralized by dead code.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I used a combination of manual gameplay testing and automated pytest tests. For the high/low message bug, I would guess a number higher than the secret and check if the hint said "Go LOWER!" instead of "Go HIGHER!" For the range validation bug, I tried entering 1000 and verified the game rejected it with an error message. Both approaches confirmed the fixes worked as intended.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Manual Testing - High/Low Message Bug: I played the game with Normal difficulty (secret range 1-100) and deliberately guessed a number higher than the secret (e.g., guessing 80 when secret was 50). The game correctly displayed "📉 Go LOWER!" instead of the backwards "Go HIGHER!" This proved the message swap fix was working.
  
  Pytest Testing - Range Validation: I ran `pytest tests/test_range_validation.py` which verified that Easy difficulty returns range 1-20, Normal difficulty returns range 1-100, Hard difficulty returns range 1-50, guesses within range are acceptable, and guesses outside range (0, 101, 1000) are rejected. All tests passed, confirming the range validation was properly enforced.

- Did AI help you design or understand any tests? How?
  Yes, the AI helped significantly. When the initial tests failed because they expected just outcome strings but `check_guess()` returns tuples, the AI fixed the old tests to unpack both `(outcome, message)`. The AI also designed the new test cases (`test_guess_too_high_message_correct()` and `test_guess_too_low_message_correct()`) to specifically check that the message text matched the bug fix. For range validation, the AI created all 5 test cases in `test_range_validation.py` that comprehensively test each difficulty level and edge cases (guesses above, below, and within range).

---

## 4. What did you learn about Streamlit and state?

  Streamlit reruns the entire script from top to bottom every time a button is clicked or input changes. Without session state, variables reset to their initial values on each rerun—so our secret number kept regenerating instead of staying the same. Session state is like a "memory" that persists across reruns. By storing the secret in `st.session_state.secret`, we tell Streamlit "keep this value even when you rerun the script." It's the difference between writing on a whiteboard (resets each rerun) and a ledger (persists).

---

## 5. Looking ahead: your developer habits

-> Habit/Strategy to Reuse:
 1.two-layer testing approach. I combined manual gameplay testing (playing the game to verify the fix actually works) with automated pytest tests (catching edge cases systematically).
 2.documented bugs clearly in that Bug Reproduction Log before fixing them

 -> Changes: 
  1.ask the AI why it's suggesting a change and have it explain the logic before accepting it

-> Thoughts:
1.AI is a tool that accelerates development, but human judgment about testing and verification is non-negotiable