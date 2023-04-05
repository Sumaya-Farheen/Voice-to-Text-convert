
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    import speech_recognition as sr
#initialization
r = sr.Recognizer()
#Convert Speech to text

while True:
    with sr.Microphone() as source:
        #to clear the background noise
        r.adjust_for_ambient_noise(source, duration=0.3)
        print(input("speak now"))
        #capture the audio
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # break
            print("speak:", text)
            if text == 'quit':
                break
                # sys.exit()
                
               #return 0
        except Exception as e:
            print("say again") 
        

