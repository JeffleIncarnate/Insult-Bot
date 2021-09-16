# Imports
import pyttsx3
import random

# Variables
Insults = ["Lol short", "You suck", "You don't have a nice head", "You are VERY short", "You legit are so damn short its unreal", "You are ok"]
n = 0

# While Loop
while n <= 100000000000000:
    # Start-up
    engine = pyttsx3.init()

    # voices
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)

    # Talking
    engine.say(random.choice(Insults))
    engine.runAndWait()

    n += 1
