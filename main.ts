let select = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    select = Math.randomRange(1, 5)
    if (select == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (select == 2) {
        basic.showIcon(IconNames.Square)
    } else if (select == 3) {
        basic.showIcon(IconNames.Scissors)
    } else if (select == 4) {
        basic.showIcon(IconNames.Ghost)
    } else if (select == 4) {
        basic.showIcon(IconNames.SmallDiamond)
    }
    
})
