# Exercise -11

import time
import pygame
from plyer import notification

# Initialize pygame only once
pygame.mixer.init()


# Generator
def timer(seconds):
    while True:
        time.sleep(seconds)
        yield "Time's up!"


# Create generator object
gen = timer(10)

print("Timer Started...")

# Runs forever until you stop the program (Ctrl + C)
for message in gen:

    notification.notify(
        title="Break Time!",
        message="You have been working for a while. Take a 5-minute stretch!",
        timeout=5,
    )

    pygame.mixer.music.load("water.mp3")
    pygame.mixer.music.play()

    time.sleep(5)

    pygame.mixer.music.stop()

    print("Alarm Complete. Waiting for next timer...")
