import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')#getting details of current voice
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

"""What is sapi5?
    ----Microsoft developed speech API
    ----Helps in synthesis and recognition of voice.
What Is Voiced?
    ----Voice id helps us to select different voices.
    ----voice[0].id = Male voice 
    ----voice[1].id = Female voice"""


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  #Without this command, speech will not be audible to us.

def WishMe():
    hour = int(datetime.datetime.now().hour)

   # Here, we have stored the current hour or time integer value into a variable named hour. Now, we will use this hour value inside an if-else loop.

 
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")
    speak("Hey this is Jarvis , Say how can i help you") 


"""The next most important thing for our A.I. assistant is that it should take command 
     with the help of the microphone of the user's system. So, now we will make a takeCommand() function.  
     With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the user.
    Before defining the takeCommand() function, we need to install a module called speechRecognition. Install this module by: """


def takeCommand():
    #it take microphone input from the user and returne string output
    r = sr.Recognizer()     #to detect the audio 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   #second of non  speaking audio before we consider that conservation is stop    
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

        
         

               
     
if __name__ == "__main__":
    WishMe()
    while True:
        # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)  # how many line of sentances you want from jarvis
            speak("According to Wikipedia")
            print(results)
            speak(results)  

            """To open any website, we need to import a module called webbrowser.
             It is an in-built module, and we do not need to install it with a pip statement"""

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google 'in query:
            webbrowser.open("google.com") 
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")       
        elif 'play music' in query:
            music_dir = "C:\\Users\\Sandhya yadav\\Desktop\\SY programming world\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Didi, the time is {strTime}")    