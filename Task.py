#Functions
import datetime
from Speak import say
from Listen import Listen
import requests
import random
import os

#1. Non Input functionalities
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        time = datetime.datetime.now().strftime('%I:%M %p')
        say(f"Good Morning sir.. It's {time}.")
    elif hour>12 and hour<18:
        time = datetime.datetime.now().strftime('%I:%M %p')
        say(f"Good Afternoon  sir...it's {time}")
    else:
        time = datetime.datetime.now().strftime('%I:%M %p')
        say(f"Good Evening sir...it's {time}")

def Time():
      time = datetime.datetime.now().strftime("%I:%M %p")
      say(f"The time is {time}")

def Date():
      date = datetime.date.today()
      say(date)

def Day():
      day = datetime.datetime.now().strftime("%A")
      say(day)

def  news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=628bef6b78ae4ddbb9d05eb86f0db45d'

    main_page = requests.get(main_url).json()
    #print (main_page)
    articles = main_page["articles"]
    #print(articles)
    head = []
    day = ["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's{day[i]} news is: {head[i]}")
        say(f"today's {day[i]} news is: {head[i]}")

 

def NonInputExecution(query):
      query = str(query)

      if "time" in query:
            Time()
      
      elif "date" in query:
            Date()

      elif "day" in query:
            Day()            
      elif "news" in query:
            news()
def battery():
      import psutil

      battery = psutil.sensors_battery()
      percentage  =battery.percent
      say(f"sir our system have {percentage} percent battery")
      if percentage>=75:
            say("we have enough power to continue our work")
      elif percentage>=40 and percentage<=75:
            say("we should connect our system to charge our battery")
      elif percentage>=15 and percentage<=40:
            say("we don't have enough power to work, please connect to charging")
      elif percentage<=15:
            say("we have very low power, please connect the charger or the system will shutdown soon")

battery()

#2.  Input functionalities


def InputExecution(tag,query):

      if "wikipedia" in tag:
            import wikipedia

            say("searching wikipedia...")
            name = str(query).replace("","")          
            name = str(query).replace("according","")          
            result = wikipedia.summary(name, sentences=1)
            say("according to wikipedia...")
            say(result)

      if "google" in tag:
            query = str(query).replace("google","")
            query = query.replace("search","")
            query = query.replace("about","")
            import pywhatkit as kit
            kit.search(query)

      if "music" in tag:
            import pywhatkit as kit
            
            say("tell me the name of the song!")
            query = str(query).replace("music","")
            query = query.replace("youtube","")
            query=Listen()
            # musicName = Listen()
            kit.playonyt(query)

      if "temperature" in tag:
            import requests      
            from bs4 import BeautifulSoup
            search = "temperature in karnataka"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            say(f"The Temperature Outside Is {temperature} celcius")

            say("Do I Have To Tell You Another Place Temperature ?")
            query = Listen()

            if 'yes' in query:
                  say("Tell Me The Name Of tHE Place ")
                  query = Listen()
                  search = f"temperature in {query}"
                  url = f"https://www.google.com/search?q={search}"
                  r = requests.get(url)
                  data = BeautifulSoup(r.text,"html.parser")
                  temperature = data.find("div",class_ = "BNeawe").text
                  say(f"The Temperature in {query} is {temperature} celcius")

            else:
                  say("no problem sir")

      if "shutdown" in tag:
                say("wait a sec! sir shuting down...")
                os.system("shutdown /s /t 5")
            
      if "restart" in tag:
                say("restarting....")
                os.system("shutdown /r /t 5")

      if "sleep" in tag:
                say("sleeping...")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
      

      if "close" in tag:
            from time import sleep

            import pyautogui
            sleep(0.5)
            pyautogui.hotkey('alt', 'f4')
            sleep(0.5)
            query = str(query).replace("close","")
            say("closing.."+query)

            TaskExe = str(query).lower()
            TaskExe = TaskExe.replace(' ','')
      
      if "play music" in tag:
            music_dir = " "
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))

      if 'switch window' in tag: 
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            sleep(1)
            pyautogui.keyUp("alt")

      
      if 'email' in tag:
            import smtplib
            # from email import encoders
            # from email.mime.base import MIMEBase
            # from email.mime.multipart import MIMEMultipart
            # from email.mime.text import MIMEText

            email = 'madhanhk2911@gmail.com'
            password = 'hsaujyvbdflggiim'
            
            say("Sir what should i say")
            query = Listen().lower()

            send_to_email = input('enter the reciver`s email: ')
            message = query

            server = smtplib.SMTP('smtp.gmail.com', 587) #connect to the server
            server.starttls() #use TLS
            server.login(email, password)
            server.sendmail(email, send_to_email, message)
            server.quit()
            say("email has been sent")

      if "set alarm" in tag:
            # nn= int (datetime.datetime.now().hour)
            # if nn==int(take_command()):
            #     music_dir = "C:\\Users\\Madhan\\Music\\play"
            #     songs = os.listdir(music_dir)
            #     os.startfile(os.path.join(music_dir, songs[2]))


            say("Enter the time ")
            time = input(": Enter the Time : ")

            while True:
                Time_ac = datetime.datetime.now()
                now = Time_ac.strftime("%H:%M:%S")

                if now == time:
                    say("time to wake up sir")
                    music_dir = " "
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[2]))
                
                elif now>time:
                    break
       