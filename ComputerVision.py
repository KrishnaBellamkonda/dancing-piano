# This code detects the face of a human 
import dlib 
import cv2
import numpy as np
import pygame as pg
import time
import threading

# Pygame initialization 
pg.init()
pg.mixer.init()
pg.display.set_mode((200, 100))
pg.mixer.set_num_channels(50)


a1Note = pg.mixer.Sound("audio/PianoKeys/piano_C.mp3")
a2Note = pg.mixer.Sound("audio/PianoKeys/piano_D.mp3")
a3Note = pg.mixer.Sound("audio/PianoKeys/piano_E.mp3")
a4Note = pg.mixer.Sound("audio/PianoKeys/piano_F.mp3")
a5Note = pg.mixer.Sound("audio/PianoKeys/piano_G.mp3")
a6Note = pg.mixer.Sound("audio/PianoKeys/piano_A.mp3")
a7Note = pg.mixer.Sound("audio/PianoKeys/piano_B.mp3")
notes = [a1Note,a2Note,a3Note,a4Note,a5Note,a6Note,a7Note]
pg.mixer.set_num_channels(50)



def decide_category(center,frame, no_keys):
    width = frame.shape[1]
    threshold = np.linspace(0, width, no_keys+1)
    result = (center)>threshold
    category = result.sum()
    return category

def mean_int(list_item):
    return int(round(sum(list_item)/len(list_item)))

def tracking_function(frame):
    tracker.update(frame)
    pos = tracker.get_position()
    cv2.rectangle(frame, (int(pos.left()), int(pos.top())), (int(pos.right()), int(pos.bottom())), (0, 255, 0), 3)
    center = mean_int([pos.left(), pos.right()]) 
    Category= decide_category(center, frame, 5)
    categories.append(Category)

def play_note(category_number):
    notes[category_number].play()
    time.sleep(0.1)

# Face Tracking initialization 
face_detector = dlib.get_frontal_face_detector()
tracker = dlib.correlation_tracker()
capture = cv2.VideoCapture(0)
Category = 1
# Initial Controls
tracking = False
it = 0
categories = []
while True:
    it+= 1
    ret, frame = capture.read()
    if tracking == False:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = face_detector(gray)
        if len(rects) > 0:    
            tracker.start_track(frame,rects[0]) 
            tracking = True
            
    
    if tracking == True:
        if it != 5:
            tracker.update(frame)
            pos = tracker.get_position()
            cv2.rectangle(frame, (int(pos.left()), int(pos.top())), (int(pos.right()), int(pos.bottom())), (0, 255, 0), 3)
            center = mean_int([pos.left(), pos.right()]) 
            Category= decide_category(center, frame, 6)
            categories.append(Category)
        else:
            FinalCat = mean_int(categories)
            thread1 = threading.Thread(target=tracking_function, args=[frame])
            thread2 = threading.Thread(target=play_note, args=[FinalCat])

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()
            it = 0
            categories = []

    # Wait Keys
    key = 0xFF & cv2.waitKey(1)
    if key == 27:
        break
    if key == ord("1"):
        tracking = False
    
    cv2.imshow("Face Tracking",frame)

capture.release()
cv2.destroyAllWindows()