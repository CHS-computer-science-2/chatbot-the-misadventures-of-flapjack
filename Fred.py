from textblob import TextBlob
import random
baby = open("script.txt","r")
greetings = ["hi","hello","hey","how are you","whats up","its good to see you"]
aQue = ["how are you doing","how are you","are you doing well","whats been good"]
aAdj = ["good","bad","well","terrible","great","horrible","excellent","fine","swell","ok"]


def response(userinput):
    if userinput in greetings:
        return TextBlob(closest(greetings))
    
def closest(userinput):
    for 
    
def main():
     while True:
        userInput = input(" ")
        input(response(userInput))
        
        
main()
