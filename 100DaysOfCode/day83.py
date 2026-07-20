# Exercise 9- Shout out

import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")


names = [
    "Hitendra",
    "Rahul",
    "Amit",
    "Rohit",
    "Ankit",
    "Vikas",
    "Suresh",
    "Mohit",
    "Deepak",
    "Karan"
]
for i in range(0,len(names)):
    speak.Speak(f" Shout out {names[i]}")
