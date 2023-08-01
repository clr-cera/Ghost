# Ghost
 This is Ghost, a virtual assistant for my machines.
 
# Description

### Listen

- Speech Recognition + PyAudio.
- recognition.py has the parsing funcion which returns the query (speech).

### Understand

- main loop checks for which type of command should be evaluated and calls the actions.py structure for this type of command.

### Execute

- os + multiprocessing (multiprocessing was chosen because it can be simpler to deal with but later on changing to subprocess should be better).
- The structure use the rest of the query to execute an action.

# Actions

- ### Speak - uses espeak to say something
- ### Open - open any application that has a script in path and is listed in APPLICATIONS list. 
- ### Search - search any text in google search engine
