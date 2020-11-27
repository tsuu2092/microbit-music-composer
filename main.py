def on_button_pressed_a():
    music.set_volume(255)
    music.change_tempo_by(140)
input.on_button_pressed(Button.A, on_button_pressed_a)

def noteToFrequency(text: str):
    if text == "A4":
        return 440
    return invalid_note
invalid_note = 0
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
    988]
invalid_note = -1
current_note = 0