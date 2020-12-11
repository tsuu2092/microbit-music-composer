def delete_last_note():
    song.pop()
    basic.show_icon(IconNames.NO)
    basic.pause(100)
    basic.show_icon(IconNames.EIGTH_NOTE)

def on_button_pressed_a():
    lower_note()
input.on_button_pressed(Button.A, on_button_pressed_a)

def lower_note():
    global current_note
    if current_note > 0:
        current_note = current_note - 1
    play_current_note()

def on_pin_pressed_p2():
    delete_last_note()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def save_current_note():
    song.append(notes[current_note])
    play_current_note()

def on_button_pressed_ab():
    save_current_note()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    higher_note()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    add_rest()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def play_current_note():
    music.play_tone(notes[current_note], music.beat(BeatFraction.QUARTER))

def on_gesture_shake():
    play_song()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def add_rest():
    song.append(0)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.pause(100)
    basic.show_icon(IconNames.EIGTH_NOTE)
def play_song():
    for value in song:
        music.play_tone(value, music.beat(BeatFraction.HALF))
def higher_note():
    global current_note
    if current_note < len(notes) - 1:
        current_note = current_note + 1
    play_current_note()
song: List[number] = []
current_note = 0
notes: List[number] = []
basic.show_icon(IconNames.EIGTH_NOTE)
music.set_volume(255)
music.set_tempo(120)
notes = [131,
    139,
    147,
    156,
    165,
    175,
    185,
    196,
    208,
    220,
    233,
    247,
    262,
    277,
    294,
    311,
    330,
    349,
    370,
    392,
    415,
    440,
    466,
    494,
    523,
    554,
    587,
    622,
    659,
    698,
    740,
    784,
    831,
    880,
    932,
    988,
    1046]
current_note = 12
song = []