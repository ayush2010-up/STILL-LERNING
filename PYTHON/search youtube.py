name=input("Enter your name: ")
if (name=="ayush"):
    print("Hello Ayush") 
    print("Welcome to the world of programming")
else:
    print("Hello Stranger")
    message= input("Enter a message: ")
    
    if message == "bye":
       print("hai chadi where are you going 🩲🩲")

if  name=="ayush":
    query=input("What's your query:")   # Searh query

import webbrowser
url = f"https://www.youtube.com/results?search_query={query}" #Youtube search URL with the query

webbrowser.open(url)  # Open the URL in the default web browser
