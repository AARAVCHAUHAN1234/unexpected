import pyttsx3
import random
import speech_recognition as sr # type: ignore
import datetime
import csv
import pyaudio # type: ignore


engine=pyttsx3.init()                
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)  
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
def speak(q):
    engine.say(q)
    engine.runAndWait()
    
r = sr.Recognizer()
with sr.Microphone() as source:
        
    print("how can i help you...")
    speak("how can i help you...")
    r.adjust_for_ambient_noise(source)      #use???????????????????????????????
    audio = r.listen(source)
    
  
    try:
        text = r.recognize_google(audio)
        print("listening")
        query="You said: {}".format(text)
        print(query)
        q=str(query)


    
        if 'hey' in query or 'hello' in query:
            ans="hi master, how are you"
            speak(ans)
        elif 'head' in query:
            if random.randrange(1,1000000)%2==0:
                ans="head ,give it a try."
            else:
                ans="tail master, leave it. "
            print(ans)
            speak(ans)
        elif "introduce " in query:
            ans="hi boss, so, i am KELET. i am the first human interface created by master Aarav. Currently i am in developing stage. i am able to play games, answer some of the basic question,and write your feedabck and boss will work on it."
            print(ans)
            speak(ans)

        elif 'feedback' in query:
            ans="please type your feedback"
            print(ans)
            speak(ans)
            name=input("enter your name")
            feedback=input("enter your feedback")
            l1=[name,feedback]
            a=open("feedback.csv","a",newline="")
            dev=csv.writer(a)
            dev.writerow(l1)
            a.flush()
            a.close()
            ans="thanks for your feedback"
            print(ans)
            speak(ans)
        #elif 'change language' in query or 'could you speak' in query:

        elif "time" in query or 'date' in query:    
            if "time" in query and "now" in query :
                from datetime import datetime
                now=datetime.now().time()
                print(now)
                speak(now)    
            elif "date" in query and "today" in query :
                from datetime import date
                now=date.today()
                print(now)
                speak(now)
            elif "time" in query and 'date' in query:
                from datetime import datetime
                now=datetime.now()
                print(now)
                speak(now)    
        elif query== "play game":
            aws=input("enter the name of game")
            speak("enter the game name")
            speak('i can play guessing the number game and tic tac toe')
            if aws=="guessing the number":
                a=random.randrange(0,100)
                ans=input("enter your guess")
                for i in range(0,3):
                    if ans==a:
                        print("you win")
                        break
                    elif ans>a:
                        print("big number,thiink low")
                    elif ans<a:
                        print("small number,thiink big")
                print("well played,but you lose")
            elif aws== 'tic tac toe':
                for i in range(0,3):
                    for j in range(0,3):
                        a=chr(65+i)
                        b=j+1
                        print(a,b,end="   ")
                    print() 
                print("the above is the grid now choose the code according to it")
                            
                def randome():
                    first=65+random.randint(0,2)
                    second=random.randint(1,3)
                    return chr(first),second  
                list=[]
                sace=randome()
                print("i choose this",sace)
                list.append(sace)       
                user_choice=str(input("your chance,you choose"))
                list.append(user_choice)
                sace2=str(randome())
                while sace2 in list:
                    sace2=str(randome())
                print("i choose this",sace2)
                list.append(sace2)       
                user_choice2=str(input("your chance,you choose"))
                list.append(user_choice2)
                sace3=str(randome())
                while sace3 in list:
                    sace3=str(randome())
                print("i choose this",sace3)
                list.append(sace3)       
                user_choice3=str(input("your chance,you choose"))
                list.append(user_choice3)
                sace4=str(randome())
                while sace4 in list:
                    sace4=str(randome())
                print("i choose this",sace4)
                list.append(sace4)       
                user_choice4=str(input("your chance,you choose"))
                list.append(user_choice4)
                sace5=str(randome())
                while sace5 in list:
                    sace5=str(randome())
                og_list= ['A1', 'A2', 'A3','B1', 'B2', 'B3','C1', 'C2', 'C3']
                list_user=[user_choice,user_choice2,user_choice3]
                list_bot=[sace,sace5,sace2,sace3,sace4,]
                if 'A1' in list_user and 'A2' in list_user and 'A3' in list_user:
                    print("you win")
                elif 'B1' in list_user and 'B2' in list_user and 'B3' in list_user:
                    print("you win")
                elif 'C1' in list_user and 'C2' in list_user and 'C3' in list_user:
                    print("you win")
                elif 'A1' in list_user and 'B1' in list_user and 'C1' in list_user:
                    print("you win")
                elif 'A2' in list_user and 'B2' in list_user and 'C2' in list_user:
                    print("you win")
                elif 'A3' in list_user and 'B3' in list_user and 'C3' in list_user:
                    print("you win")
                elif 'A1' in list_user and 'B2' in list_user and 'C3' in list_user:
                    print("you win")    
                elif 'A3' in list_user and 'B2' in list_user and 'C1' in list_user:
                    print("you win")
                else:
                    print("you lose")
        elif "exit"in query or "break" in query or "stop" in query:
            ans="nice play sir... \n good bye"
            print(ans)
            speak(ans)
            

        else:
            ans="sorrry try again"
            print(ans)
            speak(ans)
            
        
    
    except: 
       print("Could not understand audio")
    
