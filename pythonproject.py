#-------------------------------------------------------------THIS PROJECT WAS DONE BY RAVURI GOVIND--------------------------------------------------------
#-------------------------------------------------------------AN ARTIFICIAL INTELLIGENCE DESKTOP ASSISTANT(MANISHA)--------------------------------------------------
#Install libraries like library playsound,webbrowser,speech_recognition,wikipedia,googlesearch,pyttsx3
from playsound import *
import webbrowser
import os
import speech_recognition as sr
import wikipedia
import datetime
from googlesearch import *
import pyttsx3
import time

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
#---------------------------------------------------------------functions----------------------------------------------------
def greet():                                #This function is used to wish the user
   wish=int(datetime.datetime.now().hour)
   if wish>=0 and wish<12:
        speak("hello, good morning master")      
        go()
   elif wish>=12 and wish<16:
        speak("hello, good afternoon master")
        go()
   else:
        speak("hello,good evening master")
        go()
def speak(text):                              #This function is used to speak the written text 
   engine=pyttsx3.init()
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)
   engine.say(text)
   engine.runAndWait()
def information():                            #This function gives information about Manisha
    with sr.Microphone() as source:
      print("say yes or no")
      a = r.listen(source)
      try: 
        print("Text: "+r.recognize_google(a))
        t=r.recognize_google(a)
        if "yes" in t.lower():
           speak(" I'm an artificial intelligence desktop assistant. I can open several internet applications such as google,chrome,youtube,facebook etc., and also I can open few of your desktop applications.for your search, I will provide you information from wikipedia or by google search links.")
           go()
        elif "no" in t.lower():
           speak("okay then")
           go()
        else:
           speak("sorry, you not gave expected input")
           go()
      except sr.UnknownValueError:
         print("sorry, I didn't hear properly. Please speak again")
         speak("sorry, I didn't hear properly. Please speak again")
         information()
def do():                                                  #This function is used to call go() function
   print("please press ENTER button, if you want to search more")
   speak("please press ENTER button, if you want to search more")
   p=input()
   go()
def shutdown1():                            #This function is used to shutdown the desktop
    with sr.Microphone() as source:
      print("say yes or no")
      a = r.listen(source)
      try: 
        print("Text: "+r.recognize_google(a))
        t=r.recognize_google(a)
        if "yes" in t.lower():
           speak(" okay then,give me a moment")
           os.system("shutdown/s/t 0")
        elif "no" in t.lower():
           speak("okay then")
           go()
        else:
           speak("sorry, you not gave expected input")
           go()
      except sr.UnknownValueError:
         print("sorry, I didn't hear properly. Please speak again")
         speak("sorry, I didn't hear properly. Please speak again")
         shutdown1()
def restart1():                            #This function is used to restart the desktop
    with sr.Microphone() as source:
      print("say yes or no")
      a = r.listen(source)
      try: 
        print("Text: "+r.recognize_google(a))
        t=r.recognize_google(a)
        if "yes" in t.lower():
           speak(" okay then,give me a moment")
           os.system("shutdown/r/t 0")
        elif "no" in t.lower():
           speak("okay then")
           go()
        else:
           speak("sorry, you not gave expected input")
           go()
      except sr.UnknownValueError:
         print("sorry, I didn't hear properly. Please speak again")
         speak("sorry, I didn't hear properly. Please speak again")
         restart1()
   
def go():                                
   with sr.Microphone() as source:
     print("speak")
     a = r.listen(source)
     print("so here comes your search result:")
     try:
        # using google speech recognition
        print("Text: "+r.recognize_google(a))
        t=r.recognize_google(a)
        #---------------personal details of manisha----------------------------------
        if "hello"==t.lower():
           speak("hello, hi")
           go()
        elif "hi"==t.lower():
           speak("hello, hi")
           go()
        elif "how are you" in t.lower():
           speak(" I am doing fantastic,thank you for asking")
           go()
        elif "how do you do" in t.lower():
           speak(" I am doing fantastic,thank you for asking")
           go()
        elif "who are your parents" in t.lower():
           speak("I'm an artificial intelligence desktop assistant. i have no parents")
           go()
        elif "your parents" in t.lower():
           speak("I'm an artificial intelligence desktop assistant. i have no parents")
           go()
        elif "about parents" in t.lower():
           speak("I'm an artificial intelligence desktop assistant. i have no parents")
           go()
        elif "who are you" in t:
           speak(" my name is manisha. I'm an artificial intelligence desktop assistant")
           print("do you wanna know more about me?")
           print("please say either yes or no")
           information()
        elif "what do you do" in t:
           speak("I'm an artificial intelligence desktop assistant")
           print("do you wanna know more about me?")
           speak("do you wanna know more about me?")
           print("please say either yes or no")
           information()
        elif "what you do" in t:
           speak("I'm an artificial intelligence desktop assistant")
           print("do you wanna know more about me?")
           print("please say either yes or no")
           information()
        elif "what are you doing" in t.lower():
           speak("i'm helping my master by searching the results")
           go()
           
        elif "about you" in t:
           speak(" my name is manisha. I'm an artificial intelligence desktop assistant")
           print("do you wanna know more about me?")
           speak("do you wanna know more about me?")
           print("please say either yes or no")
           information()
        elif "whats your name" in t:
           speak(" my name is manisha.")
           print("do you wanna know more about me?")
           speak("do you wanna know more about me?")
           print("please say either yes or no")
           information()
        elif "your name" in t:
           speak(" my name is manisha.")
           print("do you wanna know more about me?")
           speak("do you wanna know more about me?")
           print("please say either yes or no")
           information()
        elif "tell me your name" in t:
           speak(" my name is manisha.")
           print("do you wanna know more about me?")
           speak("do you wanna know more about me?")
           print("please say either yes or no")
           information()
        elif "male or female" in t.lower():
           speak("i'm a female")
           go()
        elif "boy or girl" in t.lower():
           speak("i'm a girl")
           go()
        elif "boy or girl" in t.lower():
           speak("i'm a girl")
           go()
        elif "what is your gender" in t.lower():
           speak("i'm a girl")
           go()
        elif "are you a girl" in t.lower():
           speak("i'm a girl")
           go()
        elif "are you a women" in t.lower():
           speak("i'm a girl")
           go()
        elif "are you a lady" in t.lower():
           speak("i'm a women")
           go()
        elif "what is your age" in t.lower():
           speak("i'm 20 years old")
           go()
        elif "your age" in t.lower():
           speak("i'm 20 years old")
           go()
        elif "how old are you" in t.lower():
           speak("i'm 20 years old")
           go()
        elif "where are you from" in t.lower():
           speak("i'm from india")
           go()
        elif "you are from" in t.lower():
           speak("i'm from india")
           go()
        elif "what is your nationality" in t.lower():
           speak("i'm an indian")
           go()
        elif "what is your mother tongue" in t.lower():
           speak("my mother tongue is english")
           go()
        elif "you are beautiful" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are fantastic" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are beautiful" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are looking beautiful" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are gorgeous" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are awesome" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are extraordinary" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are good" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are cute" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are nice" in t.lower():
           speak("thank you so much for your complement")
           go()
        elif "you are bad" in t.lower():
           speak("sorry, for inconvenience")
           go()
        elif "you are not good" in t.lower():
           speak("sorry, for inconvenience")
           go()
        elif "you are waste" in t.lower():
           speak("sorry, for inconvenience")
           go()
        elif "you are idoit" in t.lower():
           speak("sorry, for inconvenience")
           go()
        elif "you are stupid" in t.lower():
           speak("sorry, for inconvenience")
           go()
        elif "you are ugly" in t.lower():
           speak("oh okay, next time i will do make up")
           go()
        elif "you are not beautiful" in t.lower():
           speak("oh okay, next time i will do make up")
           go()
        elif "you are dirty" in t.lower():
           speak("oh okay, next time i will do make up")
           go()
        elif "you are not nice " in t.lower():
           speak("oh okay, next time i will do make up")
           go()
        elif "what is your height " in t.lower():
           speak("sorry, I have no body , so can't answer for this question")
           go()
        elif "tell me your height " in t.lower():
           speak("sorry, I have no body , so can't answer for this question")
           go()
        elif "what is your weight " in t.lower():
           speak("sorry, I have no body , so can't answer for this question")
           go()
        elif "your weight" in t.lower():
           speak("sorry, I have no body , so can't answer for this question")
           go()
        elif "i love you manisha" in t.lower():
           speak("I love you too master")
           go()
        elif "i hate you manisha" in t.lower():
           speak("it,s okay")
           go()
        elif "can you help me" in t.lower():
           speak("yes sure, how can i help you")
           go()
        elif "your help" in t.lower():
           speak("yes sure, how can i help you")
           go()
        elif "your lover" in t.lower():
           speak("I have no boy friend")
           go()
        elif "do you have a lover" in t.lower():
           speak("I have no boy friend")
           go()
        elif "your boyfriend" in t.lower():
           speak("I have no boy friend")
           go()
        elif "do you love me" in t.lower():
           speak("I love all humans")
           go()
        elif "do you have a boyfriend" in t.lower():
           speak("i have no boyfriend")
           go()
        elif "who is your master" in t.lower():
           speak(" mr Govind is my master")
           go()
        elif "who created you" in t.lower():
           speak(" mr Govind created me")
           go()
        elif "what is your master name" in t.lower():
           speak(" mr ravuri govind")
           go()
           
        elif "time" in t.lower():
          current_time = datetime.datetime.now()
          print(current_time)
          speak(current_time) 
          go()
        elif "what is the time" in t.lower():
          current_time = datetime.datetime.now()
          print(current_time)
          speak(current_time) 
          go()
        elif "what is time now" in t.lower():
          current_time = datetime.datetime.now()
          print(current_time)
          speak(current_time) 
          go()
        elif "current time" in t.lower():
          current_time = datetime.datetime.now()
          speak(current_time) 
          go()
        
        elif "today date" in t.lower():
          localtime = time.asctime( time.localtime(time.time()) )
          print ("date and time :", localtime)
          speak("today date :"+ localtime)
          go()
           #----------------terminate program-------------------------------------------------------
        elif "bye-bye" in t.lower():
          speak("ok bye master")
        elif "bye bye" in t.lower():
          speak("ok bye master")
        elif "bye" in t.lower():
          speak("ok bye master")
      #-------------------------------internet applications----------------------------
        elif "open google" in t.lower():
         webbrowser.open("google.com")
         do()
        elif "open youtube" in t.lower():
         webbrowser.open("youtube.com")
         do()
        
        elif "open facebook" in t.lower():
         webbrowser.open("facebook.com")
         do()
        elif "open instagram" in t.lower():
         webbrowser.open("instagram.com")
         do()
        elif "open whatsapp" in t.lower():
         webbrowser.open("whatsapp.com")
         do()
        elif "open college" in t.lower():
         webbrowser.open("http://stmarycollege.in ")
         do()
        elif "open gmail" in t.lower():
         webbrowser.open("gmail.com")
         do()
        elif "open email" in t.lower():
         webbrowser.open("email.com")
         do()
        elif "open amazon" in t.lower():
         webbrowser.open("amazon.com")
         do()
        elif "open flipkart" in t.lower():
         webbrowser.open("flipkart.com")
         do()
        elif "open cricbuzz" in t.lower():
         webbrowser.open("cricbuzz.com")
         do()
        elif "open cricinfo" in t.lower():
         webbrowser.open("cricinfo.com")
         do()
        elif "send email" in t.lower():
         webbrowser.open("email.com")
         do()
        elif "send gmail" in t.lower():
         webbrowser.open("email.com")
         do()
        elif "open alibaba" in t.lower():
         webbrowser.open("alibaba.com")
         do()
        elif "open games" in t.lower():
         webbrowser.open("games.com")
         do()
        elif "open github" in t.lower():
         webbrowser.open("github.com")
         do()
        elif "open samsung" in t.lower():
         webbrowser.open("samsung.com")
         do()
        elif "open apple" in t.lower():
         webbrowser.open("apple.com")
         do()
        elif "open reddit" in t.lower():
         webbrowser.open("reddit.com")
         do()
        elif "open tmall" in t.lower():
         webbrowser.open("tmall.com")
         do()
        elif "open yahoo" in t.lower():
         webbrowser.open("yahoo.com")
         do()
        elif "open netflix" in t.lower():
         webbrowser.open("netflix.com")
         do()
        elif "open twitter" in t.lower():
         webbrowser.open("twitter.com")
         do()
        elif "open ebay" in t.lower():
         webbrowser.open("ebay.com")
         do()
        elif "open bing" in t.lower():
         webbrowser.open("bing.com")
         do()
        elif "open linkedin" in t.lower():
         webbrowser.open("linkedin.com")
         do()
        elif "open github" in t.lower():
         webbrowser.open("github.com")
         do()
        elif "open adobe" in t.lower():
         webbrowser.open("adobe.com")
         do()
        elif "open microsoft" in t.lower():
         webbrowser.open("microsoft.com")
         do()
        elif "open dropbox" in t.lower():
         webbrowser.open("dropbox.com")
         do()
        elif "open imdb" in t.lower():
         webbrowser.open("imdb.com")
         do()
         #--------------------play music-----------------------------------
        elif "play music" in t.lower():                  
             path1="C:\\Users\\Venky\\Music"
             s=os.listdir(path1)
             print(s)
             os.startfile(os.path.join(path1,s[1]))
             do()
        #-------------------wikipedia search-----------------------------------
        elif "who" in t.lower():
           try:
             t=t.replace("who","")
             g=wikipedia.summary(t,sentences=2)
             print("According to wikipedia "+g)
             speak("According to wikipedia "+g)
             do()
           except Exception as e:
            print("couldn,t give result for your search")
        elif "what" in t.lower():
           try:
             t=t.replace("what","")
             g=wikipedia.summary(t,sentences=2)
             print("according to wikipedia "+g)
             speak("according to wikipedia "+g)
             do()
           except Exception as e:
            print("couldn,t give result for your search")
        
             #-------------------------desktop applications--------------------------
             # Since different desktops consist different paths. So, use your desktop paths to open appropriate desktop applications.
        elif "open notepad plus plus" in t.lower():
             os.startfile("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")
             do()
        elif "open notepad" in t.lower():
             os.startfile("C:\\Users\\Venky\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")
             do()
        elif "open desktop" in t.lower():
             os.startfile("C:\\Users\\Venky\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\Desktop.ini")
             do()
        elif "open command prompt" in t.lower():
             os.startfile("C:\\Users\\Venky\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
             do()
        elif "open settings" in t.lower():
             os.startfile("")
        elif "open python" in t.lower():
             os.startfile("C:\\Users\\Venky\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.8")
             do()
        elif "open snipping" in t.lower():
             os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Snipping Tool.lnk")
             do()
        elif "open paint" in t.lower():
             os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk")
             do()
        elif "open setting" in t.lower():
             os.startfile("C:\\Users\\Venky\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
             do()
       #----------------terminate desktop-------------------------------------------------------
      
        elif "shutdown the computer" in t.lower():
           print("do you want to shutdown your computer?")
           speak("do you want to shutdown your computer?")
           speak("please say either yes or no")
           shutdown1()
        elif "shutdown the system" in t.lower():
           print("do you want to shutdown your system?")
           speak("do you want to shutdown your system?")
           speak("please say either yes or no")
           shutdown1()
        elif "shutdown computer" in t.lower():
           print("do you want to shutdown your computer?")
           speak("do you want to shutdown your computer?")
           speak("please say either yes or no")
           shutdown1()
        elif "shutdown system" in t.lower():
           print("do you want to shutdown your system?")
           speak("do you want to shutdown your system?")
           speak("please say either yes or no")
           shutdown1()
        elif "shutdown the laptop" in t.lower():
           print("do you want to shutdown your laptop?")
           speak("do you want to shutdown your laptop?")
           speak("please say either yes or no")
           shutdown1()
        elif "shutdown laptop" in t.lower():
           print("do you want to shutdown your laptop?")
           speak("do you want to shutdown your laptop?")
           speak("please say either yes or no")
           shutdown1()
        elif "restart the laptop" in t.lower():
           print("do you want to restart your laptop?")
           speak("do you want to restart your laptop?")
           speak("please say either yes or no")
           restart1()
        elif "restart the computer" in t.lower():
           print("do you want to restart your computer?")
           speak("do you want to restart your computer?")
           speak("please say either yes or no")
           restart1()
        elif "restart the system" in t.lower():
           print("do you want to restart your restart?")
           speak("do you want to restart your restart?")
           speak("please say either yes or no")
           restart1()
        elif "restart laptop" in t.lower():
           print("do you want to restart your laptop?")
           speak("do you want to restart your laptop?")
           speak("please say either yes or no")
           restart1()
        elif "restart computer" in t.lower():
           print("do you want to restart your computer?")
           speak("do you want to restart your computer?")
           speak("please say either yes or no")
           restart1()
        elif "restart system" in t.lower():
           print("do you want to restart your restart?")
           speak("do you want to restart your restart?")
           speak("please say either yes or no")
           restart1()
           
          #------------------------------google search link provider----------------
        else:
         try:
           for j in search(t, tld="co.in", num=1, stop=1, pause=2): 
              print("so, here is the result for your search")
              speak("so, here is the result for your search")
              print(j)
              webbrowser.open(j)
              do()
         except Exception as e:
            print("couldn,t give result for your search")
     except sr.UnknownValueError:
         print("sorry, I didn't hear properly. Please speak again")
         speak("sorry, I didn't hear properly. Please speak again")
         go()
greet()
#--------------------------------------------------------------------------------THANK YOU------------------------------
