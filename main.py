select = 0

def on_gesture_shake():
    global select
    select = Math.random_range(1, 5)
    if select == 1:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif select == 2:
        basic.show_icon(IconNames.SQUARE)
    elif select == 3:
        basic.show_icon(IconNames.SCISSORS)
    elif select == 4:
        basic.show_icon(IconNames.GHOST)
    elif select == 4:
        basic.show_icon(IconNames.SMALL_DIAMOND)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
