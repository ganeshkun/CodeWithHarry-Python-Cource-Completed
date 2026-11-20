import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
# import gettext
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    pass 

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" == c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    else:
        return speak(False)
        # output = aiprocess()
        # speak(output)


if __name__ == "__main__":
    speak("Initializing friday...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
      
       
        # recognize speech using google
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "friday"):
                speak("Yessss")     
                with sr.Microphone() as source:
                    print("friday Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
