from textblob import TextBlob
name = input("Enter your name : ")

while True:
    s = input("Enter Statement : ")
    if s.lower() == "exit":
        print("Bye ...",name)
        break
    p = TextBlob(s).statement.polarity
    if p > 0:
        print("Statement is positive",p)
    elif p < 0 :
        print("Statement is negetive",p)
    else:
        print("Statement is nuterial",p)