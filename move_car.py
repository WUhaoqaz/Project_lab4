 import tinybit
from microbit import display, Image, sleep

def basic_movement_demo():
    display.show(Image.HAPPY)
    sleep(1000)

    display.show(Image.ARROW_S)
    tinybit.car_run(150)
    sleep(2000)
    tinybit.car_stop()

    display.show(Image.ARROW_N)
    tinybit.car_back(150)
    sleep(2000)
    tinybit.car_stop()

    display.show(Image.ARROW_E)
    tinybit.car_left(150)
    sleep(1000)
    tinybit.car_stop()

    display.show(Image.ARROW_W)
    tinybit.car_right(150)
    sleep(1000)
    tinybit.car_stop()

    display.show(Image.YES)
    sleep(1000)
    display.clear()

basic_movement_demo()

