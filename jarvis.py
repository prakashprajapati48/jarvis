import speech_recognition as sr
import pyttsx3 
import datetime
import webbrowser
# import 
from googlesearch import search
u = sr.Recognizer()

web = webbrowser

date = datetime.datetime.today()
week = date.strftime('%A')
time = date.time()
date1 = date.date()

# with mic as source:
#    audio1 = u.listen()

def speechtext(speechtext):
    engine = pyttsx3.init()
    engine.say(speechtext)
    engine.runAndWait()

def audio(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def start():
   hour = int(datetime.datetime.now().hour)
   if hour >0 and hour < 12:
      speechtext("Goodmorning sir")
      speechtext("Can I help you")
      print("Goodmorning sir")
      print("Can I help you")
   
   elif hour > 12 and hour <18:
      speechtext("Good afternoon sir")
      speechtext("Can I help you")
      print("Good afternoon sir")
      print("Can I help you")
      
   elif hour > 18 and hour <24:
      speechtext("Good evening sir")
      speechtext("Can I help you")
      print("Good Evening sir")
      print("Can I help you")

start()

while True:
   
   try: 
     with sr.Microphone() as source2:

         u.adjust_for_ambient_noise(source2,duration=0.4)
 
         print("Listening....")
         speechtext = u.listen(source2)
 
         mytext = u.recognize_google(speechtext)
         mytext2 = mytext.lower()
         
         # for mytext3,cor in mytext2.list():
         #    print(mytext3,cor)

         if "open google" in mytext2:
            webbrowser.open_new("www.google.com")  
            print("Opening google")
            ans = "Opening google"
            audio(ans)
 
         elif "open whatsapp" in mytext2:
            webbrowser.open_new("www.whatsapp.com")
            print("Opening Whatsapp")
            ans = "Opening Whatsapp"
            audio(ans)
         
         elif "today which day" in mytext2:
            week
            # webbrowser.open_new("www.whatsapp.com")
            print(f"Today is: {week}")
            ans = f"today is: {week}"
            audio(ans)
        
         elif "today which date" in mytext2:
          ans = (f"Did you say: {mytext} and answer is: {date1}")
          print(f"Did you say: {mytext} and answer is: {date1}")
          audio(ans)
         
         elif "today time" in mytext2:
          ans = (f"Did you say: {mytext} and answer is: {time}")
          print(f"Did you say: {mytext} and answer is: {time}")
          audio(ans)

         elif "open wikipedia" in mytext2:
          webbrowser.open_new("www.wikipedia.com")
          print("Opening Wikipedia")
          ans = "Opening Wikipedia"
          audio(ans)
         
         elif "open youtube" in mytext2:
          webbrowser.open_new("www.youtube.com")
          print("Opening YouTube")
          ans = "Opening YouTube"
          audio(ans)

         elif "ok google search : "" "in mytext2:
          for it,cor in mytext2.list():
            print(cor)
            # webbrowser.open_new("www.google.com")

         elif "exit program" in mytext2:
            print("Program is exit")
            break

         elif mytext2:
            serc = search(mytext2,stop=1)
            for i in serc:
               print(i)            
               # audio(i)
      
         print(f"Did you say: {mytext2}")
         audio(mytext2)
      
   except sr.RequestError as e:
      print(f"Cloud not request; {0}".format(e))

   except sr.UnknownValueError:
      print(f"unknow valueerror: {ValueError}") 

