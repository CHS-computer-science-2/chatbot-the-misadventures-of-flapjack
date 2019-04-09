from textblob import TextBlob
greetings = ["hi","hello","hey","sup"]
userinput = input()

def greeting_response(use):
    if userinput.lower() in greetings:
        return print(input_classify(greetings))

def input_classify():
    userinputT = TextBlob(userinput)
    UIC = userinputT.classify()
    if UIC is 'pos':
        return 
    return 
    
def main():
     while True:
        userinput = input()
        greeting_response()

input_classify()

