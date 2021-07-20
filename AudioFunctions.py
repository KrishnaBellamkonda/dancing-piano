# Essential modules
import pygame as pg
import numpy as np
import threading 
import winsound
import time


# Mean function 
def mean_int(list_item):
    return int(round(sum(list_item)/len(list_item)))
# Initializing sounds
pg.init()
pg.display.set_mode((200, 100))
pg.mixer.init()
pg.mixer.set_num_channels(50)


a1Note = pg.mixer.Sound("audio/PianoKeys/piano_C.mp3")
a2Note = pg.mixer.Sound("audio/PianoKeys/piano_D.mp3")
a3Note = pg.mixer.Sound("audio/PianoKeys/piano_E.mp3")
a4Note = pg.mixer.Sound("audio/PianoKeys/piano_F.mp3")
a5Note = pg.mixer.Sound("audio/PianoKeys/piano_G.mp3")
a6Note = pg.mixer.Sound("audio/PianoKeys/piano_A.mp3")
a7Note = pg.mixer.Sound("audio/PianoKeys/piano_B.mp3")
notes = [a1Note,a2Note,a3Note,a4Note,a5Note,a6Note,a7Note]
# Playing sounds 

#time.sleep(1)
#print("Played the note!")

# Trying to simulate the detection process

# Function to play 
# function for iteration 
def play_note(category_number):
    notes[category_number].play()
    time.sleep(0.10)

def category_generator(max_number):
    global category_number
    time.sleep(0.50)
    c = np.random.randint(0, 4)
    category_number = c

t1 = time.perf_counter()

# Using threads to handle the function 
category_number = 1
threads = []
for i in range(10):
    thread1 = threading.Thread(target=category_generator, args=[4])
    thread2 = threading.Thread(target=play_note, args =[category_number])
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

t2 = time.perf_counter()
print("The total elapsed time is ", int(t2-t1), "second(s)")
# Threading reduces the time by half