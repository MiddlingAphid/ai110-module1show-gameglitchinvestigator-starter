# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game was extremely basic and felt more like a broken prototype than a finished product.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The most obvious issue was that the feedback was completely reversed; when I guessed a low number like 5, it told me to go lower, and when I guessed 95, it told me to go higher. It made winning impossible unless you ignored the hints entirely.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used GitHub Copilot and Gemini to help manage the project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One correct suggestion from the AI was the initial refactor, where it successfully moved the game logic out of the main app file and into a dedicated utility script.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI was misleading when it suggested a "Hard" mode range of 1-50, which was actually easier than the "Normal" mode range of 1-100. I caught this by reading the code it generated and verified the mistake by looking at the logical inconsistency of the ranges.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed only after it passed an automated test suite, rather than just playing the game manually.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran a specific pytest for the "Hard" difficulty range which confirmed that the game correctly set the target between 1 and 500.

- Did AI help you design or understand any tests? How?

The AI was actually very helpful in designing these tests; it showed me how to use assert statements to check both the logic outcomes and the specific emoji messages the game sends to the player.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I’d tell a friend that Streamlit is like a "Groundhog Day" loop; every time you click a button or change a setting, the entire script runs from the very top all over again. Session state is like a digital backpack that keeps your items (like your score or the secret number) safe so they don't disappear every time the page refreshes. Without that "backpack," the game would forget the secret number every single time you made a guess.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

One strategy I’ll definitely reuse is "test-driven verification" because it’s much faster to run a command and see six green dots than it is to manually play a game over and over to check for bugs.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I’ll be more skeptical of the AI’s "logic" choices—like the scoring system—and double-check the math before I hit save.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project taught me that while AI is a fast "builder," I still need to be the "architect" who double-checks the blueprints for common sense.
