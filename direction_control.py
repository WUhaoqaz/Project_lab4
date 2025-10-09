import tinybit
from microbit import display, Image, sleep

def direction_sequence_demo():
    MOVEMENT_SEQUENCE = [
        (tinybit.car_run, 180, Image.ARROW_S, 1500),
        (tinybit.car_back, 180, Image.ARROW_N, 1500),
        (tinybit.car_left, 150, Image.ARROW_E, 1000),
        (tinybit.car_right, 150, Image.ARROW_W, 1000),
        (tinybit.car_spinleft, 200, Image.ARROW_E, 1200),
        (tinybit.car_spinright, 200, Image.ARROW_W, 1200),
    ]

    for round in range(3):
        display.scroll("R" + str(round + 1))

        for move_func, speed, arrow, duration in MOVEMENT_SEQUENCE:
            display.show(arrow)
            move_func(speed)
            sleep(duration)
            tinybit.car_stop()
            sleep(300)

        display.show(Image.HEART)
        sleep(1000)

    display.scroll("DONE")

direction_sequence_demo()

