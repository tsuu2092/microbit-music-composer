function delete_last_note () {
    if (song.length > 0) {
        music.playTone(song.pop(), music.beat(BeatFraction.Quarter))
    }
}
input.onButtonPressed(Button.A, function () {
    lower_note()
})
function lower_note () {
    if (current_note > 0) {
        current_note = current_note - 1
    }
    play_current_note()
}
input.onPinPressed(TouchPin.P2, function () {
    delete_last_note()
})
function save_current_note () {
    song.push(notes[current_note])
    play_current_note()
}
input.onButtonPressed(Button.AB, function () {
    save_current_note()
})
input.onButtonPressed(Button.B, function () {
    higher_note()
})
input.onPinPressed(TouchPin.P1, function () {
    add_rest()
})
function play_current_note () {
    music.playTone(notes[current_note], music.beat(BeatFraction.Quarter))
}
input.onGesture(Gesture.Shake, function () {
    play_song()
})
function add_rest () {
    song.push(0)
    basic.showIcon(IconNames.SmallDiamond)
    basic.pause(100)
    basic.showIcon(IconNames.EigthNote)
}
function play_song () {
    for (let value of song) {
        music.playTone(value, music.beat(BeatFraction.Half))
    }
}
function higher_note () {
    if (current_note < notes.length - 1) {
        current_note = current_note + 1
    }
    play_current_note()
}
let current_note = 0
let notes: number[] = []
let song : number[] = []
basic.showIcon(IconNames.EigthNote)
music.setVolume(255)
music.setTempo(120)
notes = [131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247, 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880, 932, 988, 1046]
current_note = 12
song = []
