# Writing the audio files 
# Playing the music


def play_note(category_number):
    notes[category_number].play()
    time.sleep(0.15)

def tracking_function(frame):
    global Category
    tracker.update(frame)
    pos = tracker.get_position()
    cv2.rectangle(frame, (int(pos.left()), int(pos.top())), (int(pos.right()), int(pos.bottom())), (0, 255, 0), 3)
    center = mean_int([pos.left(), pos.right()]) 
    Category= decide_category(center, frame, 5)


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
 
# Complete the schedule 
# 