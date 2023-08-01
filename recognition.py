import speech_recognition as sr
#This parses the command from input
def parseCommand(): 
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone(sample_rate= 48000,chunk_size=8192) as source: 
        print('Started listening')
        listener.pause_threshold = 2
        listener.energy_threshold = 34099 #Had severe trouble with the source but after setting its energy treshold it works well!
        listener.dynamic_energy_threshold = True 
        input_speech = listener.listen(source) 
        print('Stopped listening')

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_US')
        print(f'the input speech was: {query}')

    except Exception as exception:
        print('I did not quite catch that')
        return 'None'

    return query
