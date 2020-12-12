import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12 :
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("hello I am jarvis. How may I help you")    


def takeCommand():
     #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . . ")
        r.pause_threshold = 1 
        audio = r.listen(source)



    try:
        print("Recognizing . . . ")
        query = r.recognize_google(audio, language='en-in') #using for the voice Recognition
        print("User said : {query}\n")    #User query will be printed.


    except Exception as e:
        
        print("say that again please...")  #Say that again will be printed in case of improper voice 
        return "None"
    return query

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('makeyurwebsite@gmail.com','Bg@123456')
        server.sendmail('makeyurwebsite@gmail.com', to, content)
        server.close()

if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:    
        query = takeCommand().lower()
    # logic for executing tasks

        if wikipedia in query:
            speak('searcing wikipedia . . . ')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "E:\\mobile\\New Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is {strTime}")    
#open any program from your system
        elif 'open vs code' in query:
            codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)    

        elif 'send email ' in query:
                try:
                  speak("What should I say?")
                  content = takeCommand()
                  to = "makeyurwebsite@gmail.com"
                  sendEmail(to,content)
                  speak("Email has been sent!")
              
                except expression as e:
                   print(e)
                   speak("Sorry! Bijay. I am not able to send the email")
