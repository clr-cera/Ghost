import os
import multiprocessing

APPLICATIONS = [
    'spotify',
    'discord',
    'steam',
    'vivaldi',
    'notion',
    'code'

]

#This open an app if this app has a command in any $ROOT directories
def openApp(app):
    os.system(f"{app}")

#Function to search information on Google
def search(info):
    os.system(f"xdg-open https://www.google.com/search?q={info}&sourceid=chrome&ie=UTF-8")

#Function to speak a text
def speak(text):
    print(text)
    os.system(f"espeak '{text}' -v en+f5") #The voice can be tweaked using espeak manual on github

#Structures that check query to choose output 
def openStructure(query):
    processList = []

    for i in query:
        if i in APPLICATIONS:
            processList.append(multiprocessing.Process(target=openApp, args=(i,)))
            processList[-1].start()

    return(processList)

def searchStructure(query):
    if query[0] =="for":
        query.pop(0)
                    
    if len(query) !=0: #After removing "for" there could be no more words and nothing should be searched
        info = '+'.join(query)
        print(f"will search for {info}")

        procSearch = multiprocessing.Process(target=search, args=(info,))
        procSearch.start()

def speakStructure(query):
    speech = ' '.join(query)
    speak(speech)

def shutdownStructure(query):
    os.system("shutdown now")