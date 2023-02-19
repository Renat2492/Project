select = 0

def on_gesture_shake():
    global select
    select = Math.random_range(1, 3)
    if select == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif select == 2:
        basic.show_icon(IconNames.SQUARE)
    elif select == 3:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
