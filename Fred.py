from textblob import TextBlob

def response(userinput):
    
    greetings = ["hi","hello","hey","how are you","whats up","its good to see you"]
    aQue = ["how are you doing","how are you","are you doing well","whats been good"]
    aAdj = ["good","bad","well","terrible","horrible","great","fine","ok","excelent","swell"]


    
    return TextBlob(userinput)

def main():

    greetings = ["hi","hello","hey","how are you","whats up","its good to see you"]
    aQue = ["how are you doing","how are you","are you doing well","whats been good"]
    aAdj = ["good","bad","well","terrible","horrible","great","fine","ok","excelent","swell"]
    
    while True:
        userInput = input(" ")
        print(response(userInput))
main()
