#Fred_The_Chatbot
#Ethan Wodrich

import random
from textblob import TextBlob

def greeting_response(userInput):
    user_greetings = ["hi","hello","hey","sup","greetings","what's up"]
    bots_greetings = ["wassuuuuup","ayeeee","what's up?\nplanes!"]
    stop_greetings = ["Three is enough.","Please stop.","NO"]
    for word in userInput.words:
        if word.lower() in user_greetings:
            if step < 3:
                return bots_greetings[step]
            elif step < 6:
                return stop_greetings[step-3]
            elif step = 6:
                return "Business hours are from 0 to 6 greetings."
            return "\n"

def 

def quit_chatbot(userInput):
    if userInput == "quit".lower():
        exit
    
def main():
    print("I am Fred the chatbot. Type 'quit' to exit.")
    step = -1
    while userInput != "quit".lower():
        userInput = TextBlob(input("\n").correct())
        step += 1
        
        inputhistory = []
        inputhistory.append(userInput)
        
        print(greeting_response(userInput))
        
        
        quit_chatbot(userInput)

main()
