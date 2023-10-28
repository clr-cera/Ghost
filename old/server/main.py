import pyaudio as pa
import socket
import server.actions as actions
import data.serverData as serverData

NAME = 'ghost' #Hi Ghost!

if __name__ == '__main__':
    #speak('All systems nominal.')


    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM,0)         # Create a socket object
    s.bind((serverData.HOST,serverData.PORT,0,0))

    s.listen(20)                 # Now wait for client connection.



    while True:
        # Parse as a list
        command = ''
        query = s.recv(1024).decode().lower().split()

        if query[0] == NAME:
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
                    
                if command == 'shutdown':
                    actions.shutdownStructure(query=query)
    
    s.close()

else:
    print("p-p-p-problem")

