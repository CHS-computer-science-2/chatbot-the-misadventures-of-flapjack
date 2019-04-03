from textblob import TextBlob

def response(userinput):
    
    greetings = ["hi","hello","hey","how are you","whats up","its good to see you"]
    aQue = ["how are you doing","how are you","are you doing well","whats been good"]
    aAdj = ["good","bad","well","terrible","great","horrible","excellent","fine","swell","ok"]

    
    
    return TextBlob(userinput)

def main():

     while True:
        userInput = input(" ")
        input(response(userInput))
        
main()
