# Replace youremail@gmail.com to sender's mail id
# Replace youremailPassword to sender's mail Password 
# Replace recieveremail@gmail.com to reciever's mail id


# Note : This code is designed for Windows machine only 

from playsound import playsound
from pygame import mixer
from datetime import datetime
from time import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyowm
# import re
from pygame import mixer
import json
import requests
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        speak(f"It's {strTime} a m")
        print(f"It's {strTime} a m")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
        speak(f"It's {strTime}")
        print(f"It's {strTime}")
    else:
        speak("Good Evening Sir")
        speak(f"It's {strTime} p m")
        print(f"It's {strTime} p m")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','youremailPassword')
    server.sendmail('recieveremail@gmail.com',to,content)
    server.close()

def headlines(str):
    from  win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.headlines(str)
def musiconloop(file , stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
        return "None"
    return query

def log_now(msg):
    with open("mylogs.txt","a") as f:
     f.write(f"{msg} {datetime.now()}\n ")


if __name__ == '__main__':
    print(voices)
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

    #logic for executing task on quary
        if 'wikipedia' in query:
            speak("Searching Wikipedia ")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'good evening' in query:
            speak("Very good evening")
        elif 'good morning' in query:
            speak("Very good morning")
        elif 'who owns you' in query:
            speak("I belongs to Mayank , He created me.")
        elif 'who are you'in query:
            speak("I am Jarvis ,a personal assistant based on Artificial Intelligence")
        elif 'good night' in query:
            speak("good night dear , sweet dreams")
            exit()
        elif 'Okay' in query:
            speak("Okay")
            exit()
        elif 'ok' in query:
            speak("OK.Let me know if there's anything else I can help you with.")
            exit()
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open whatsapp ' in query:
            speak("Opening Whatsapp")
            webbrowser.open("web.whatsapp.com")
        elif 'play some music' in query:
            speak("playing music")
            music_dir = 'E:\\musicz'
             # Provide full path to music
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open pycharm' in query:
            speak("Opening pycharm")
            codePath = "E:\PyCharm Community Edition 2020.2\bin\pycharm64.exe"
            # Provide full path to pycharm
            os.startfile(codePath)
        elif 'email to my friend':
             try:
                 speak("What should i say ?")
                 content = takeCommand()
                 to = "myfriend@gmail.com" # or "myfriend@icloud.com"
                 sendEmail(to, content)
                 speak("I have sent the email")
             except Exception as e:
                 print(e)
            musiconloop("physical.mp3", "stop")
        elif 'activate' in query:
            init_water = time()
            init_eyes = time()
            init_exercise = time()
            watersecs = 5
            eyessecs = 10
            exesecs = 20
            while True:
                try:
                    if time() - init_water > watersecs:
                        print("Water drinking time. 'drank' to stop the alarm")
                        musiconloop('water1.mp3', 'drank')
                        init_water = time()
                        log_now("Drank water at ")

                    if time() - init_eyes > eyessecs:
                        print("Eye exercise time. 'done' to stop the alarm")
                        musiconloop('eyes.mp3', 'done')
                        init_eyes = time()
                        log_now("Eye exercise done at ")

                    if time() - init_exercise > exesecs:
                        print("Physical activity done time. 'donephy' to stop the alarm.")
                        musiconloop('physical.mp3', 'donephy')
                        init_exercise = time()
                        log_now("Physical activity done at ")
                except Exception as e:
                    continue
        elif 'quit' in query:
            speak("okay")
            exit()
        elif 'what is the weather'  in query:
            owm = pyowm.OWM('91546b1d5987cba39fabba05fe611a5a')
            location = owm.weather_at_place('New Delhi')
            weather = location.get_weather()
            temp = weather.get_temperature('celsius')
            humidity = weather.get_humidity()
            cloud = weather.get_clouds()
            wind = weather.get_wind()
            speak(f"The weather is {temp['temp']} degrees with {cloud} percent of sky covered with clouds")
            speak(f"humidity level is {humidity} grams of water vapor per kilogram of air")
            speak(f"The wind speed is {wind['speed']} meter per seconds")
        elif 'are you there' in query:
            speak("For you,sir,always.")
        elif 'headlines' in query:
            speak("News for today")
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=10d1ffedf6804024ab0aa29db8ac2d6e"
            news = requests.get(url).text
            news = json.loads(news)
            print(news["articles"])
            arts = news['articles']
            for articles in arts:
                speak(articles['title'])
                speak("Moving on the next headline ...")
        elif 'hey Jarvis' in query:
            speak("I am listening")
            print("I am listening")
        elif 'I love you' in query:
            speak("After a careful study of most of the romantic songs,"
                  "I have come to the conclusion that love can be quite complicated,So I'd rather pass.")

        elif 'calculate my age' in query:
            print("Enter your age or year of birth : ")
            speak("Enter your age or year of birth")
            age = input(int())
            if int(age) >= 1900 and int(age) <= 2020:
                    print("You entered year of birth")
                    speak("You entered year of birth")
                    age1 = int(age) + (100)
                    print(f"You will become 100 years old in {age1} ")
                    speak(f"You will become 100 years old in {age1}")
                    age = 2020 - int(age)
                    print(f"Your current age is : {age}")
                    speak(f"Your current age is : {age}")

            elif int(age) >= 0 and int(age) <= 150:
                    print("You entered your current age")
                    speak("You entered your current age")
                    age1 = (2020 - int(age)) + (100)
                    print(f"You will become 100 years old in {age1} ")
                    speak(f"You will become 100 years old in {age1} ")

            elif int(age) > 2020:
                    print("You are not yet born !")
                    speak("You are not yet born ")

            else:  # int(age)>=151 and int(age) >= 200 :
                    print("I think you are the oldest living human on the earth.")
                    speak("I think you are the oldest living human on the earth.")
        elif 'alarm' in query:
            alarmH = int(input("What hour do you want the alarm to ring? "))
            speak("What hour do you want the alarm to ring?")
            alarmM = int(input("What minute do you want the alarm to ring? "))
            amPm = str(input("am or pm? "))
            speak("What minute do you want the alarm to ring? ")
            print(f"Waiting for alarm {alarmH}:{alarmM} {amPm}")
            speak("Waiting for alarm")
            if (amPm == "pm"):
                alarmH = alarmH + 12
            while (1 == 1):
                if (alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute):
                    print("Time to wake up")
                    speak("Time to wake up")
                    musiconloop('physical.mp3')
                    # playsound('/Users/HOME/Downloads/beep-06')
                    # # Provide  full path to "beep-06"
                    break
        elif'shutdown' in query:
            os.system("shutdown/s/t1")
            exit()




