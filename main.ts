function noteToFrequency (text: string) {
    if (text == "A4") {
        return 440
    }
    return invalid_note
}
let invalid_note = 0
invalid_note = -1
let notes = [131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 0, 0, 0, 0, 0]
music.playTone(noteToFrequency("A4"), music.beat(BeatFraction.Whole))
