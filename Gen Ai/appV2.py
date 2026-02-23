# pip install speechrecognition pyttsx3
import webbrowser
from datetime import datetime
import requests
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",178)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = rec.listen(source)
    try:
        query = rec.recognize_google(audio)
        print("You :",query)
        return query.lower() 
    except:
        print("Can't catch that")
        return""   
def get_news():
    URL="https://newsapi.org/v2/top-headlines?country=us&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = requests.get(URL)
    data = response.json()
    articles = data['articles']
    for i in range(len(articles)):
        print(articles[i]['title'])


#corpous = ["hi", "hello", "hey", "hi there", "greetings"]and many more
greet_messages = ["hi", "hello", "hey", "hi there", "greetings"]
date_msg = ["what is the date", "current date", "today's date"]
time_msg = ["what is the time", "current time", "time", "now"]
chat = True
while chat:
    user_msg=listen()
    # user_msg = input("Enter your mgs: ").lower()
    # user_msg = input("Enter your message: ").lower()
    if user_msg in greet_messages:
        speak("Hello! How can I help you?")
    elif user_msg in time_msg:
        current_time = datetime.now().strftime("%I:%M:%S %p") # formatting time to 12-hour format with AM/PM
        print(f"The current time is {current_time}")
    elif user_msg in date_msg:
        current_date = datetime.now().strftime("%B %d, %Y")   # can use datetim.now().date() for only date
        print(f"Today's date is {current_date}")
    elif "open" in user_msg:
        msg = user_msg.split()
        site = msg[1]
        url = f"https://www.{site}.com"
        webbrowser.open(url)
        print(f"Opening {site}...")
    elif "calculate" in user_msg:
        msg = user_msg.split()
        expression = msg[-1]
        print(f"The result is: {eval(expression)}")
    elif "news" in user_msg or "headlines" in user_msg:
        get_news()
        speak("Here are the latest news headlines...")
    elif user_msg == "bye":
        print("Goodbye! Have a great day!")
        chat = False

    else:
        print("I cannot understand your message.")