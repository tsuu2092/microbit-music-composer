input.onButtonPressed(Button.A, function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
})
input.onGesture(Gesture.Shake, function () {
    music.playTone(294, music.beat(BeatFraction.Whole))
})
basic.forever(function () {
	
})
