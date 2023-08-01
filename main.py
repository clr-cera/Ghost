import pyaudio as pa
import actions
import recognition as rec

name = 'ghost' #Hi Ghost!

pa.PyAudio()

processList = [] #This stores all processes opened by openStructure

# Main Loop

if __name__ == '__main__':
    #speak('All systems nominal.')

    while True:
        # Parse as a list
        command = ''
        query = rec.parseCommand().lower().split()

        if query[0] == name:
            query.pop(0)

            if  len(query)!=0:
                if query[0] == "please":
                    query.pop(0)

            if  len(query) > 1:
                command = query[0] 
                query.pop(0)
            
                #Output production
                if command == 'say':
                    actions.speakStructure(query=query)

                if command == 'open':
                    for i in actions.openStructure(query=query):
                        processList.append(i)

                if command == 'search':
                    actions.searchStructure(query=query)

else:
    print("p-p-p-problem")
