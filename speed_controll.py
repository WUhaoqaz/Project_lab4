
import tinybit
from microbit import display, Image, sleep

def speed_control_demo():
    display.show(Image.HAPPY)
    sleep(1000)

    SPEED_CONFIGS = [
        (50, 50, 2000, "SLOW"),
        (120, 120, 2000, "MEDIUM"),
        (200, 200, 2000, "FAST"),
        (255, 255, 2000, "MAX"),
        (0, 0, 1000, "STOP"),
        (100, 200, 1500, "LEFT"),
        (200, 100, 1500, "RIGHT"),
    ]

    for left_speed, right_speed, duration, desc in SPEED_CONFIGS:
        display.scroll(desc)

        if left_speed == 0 and right_speed == 0:
            tinybit.car_stop()
        else:
            tinybit.car_run(left_speed, right_speed)

        sleep(duration)

    display.show(Image.YES)
    sleep(1000)

speed_control_demo()
