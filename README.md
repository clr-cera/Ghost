# Ghost
 This is Ghost, a virtual assistant for my machines.
---

# 💭 Proposal

- I want to understand better how I can make a virtual assistant, for this I will start building Ghost, a prototype of a virtual assistant.


---

# Algorithm

### Listen

- Speech Recognition + PyAudio.
- recognition.py has the parsing funcion which returns the query (speech).

### Understand

- main loop checks for which type of command should be evaluated and calls the actions.py structure for this type of command.

### Execute

- os + multiprocessing (multiprocessing was chosen because it can be simpler to deal with but later on changing to subprocess should be better).
- The structure use the rest of the query to execute an action.

# Actions

- Speak → uses espeak to speak something
- Open → runs any script which is found in $PATH
- Search → search any text in google search engine
