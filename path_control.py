from microbit import sleep, display, Image, button_a, button_b
import tinybit

LETTER_IMAGES = {
    "S": Image("99999:90009:90909:90009:99999"),
    "+": Image("00900:00900:99999:00900:00900"),
    "T": Image("00900:09090:90009:09090:00900"),
}

LETTER_MOVEMENTS = {
    "S": [
        ("run", 100, 1000),
        ("spinleft", 200, 380),
        ("run", 100, 1000),
        ("spinleft", 200, 380),
        ("run", 100, 1000),
        ("spinleft", 200, 380),
        ("run", 100, 1000),
        ("stop", 0, 500)
    ],
    "+": [
        ("run", 100, 1000),
        ("backward", 100, 2000),
        ("run", 100, 1000),
        ("spinleft", 200, 380),
        ("run", 100, 800),
        ("backward", 100, 1600),
        ("run", 100, 800),
        ("stop", 0, 500)
    ],
    "T": [
        ("run", 100, 1200),
        ("spinleft", 200, 500),
        ("run", 100, 1200),
        ("spinleft", 200, 500),
        ("run", 100, 1200),
        ("stop", 0, 500)
    ]
}

def execute_movement_sequence(letter):
    if letter in LETTER_MOVEMENTS:
        movements = LETTER_MOVEMENTS[letter]
        for action, speed, duration in movements:
            if action == "run":
                tinybit.car_run(speed)
            elif action == "backward":
                tinybit.car_back(speed)
            elif action == "spinleft":
                tinybit.car_spinleft(speed)
            elif action == "spinright":
                tinybit.car_spinright(speed)
            elif action == "stop":
                tinybit.car_stop()

            sleep(duration)

current_letter = 0
letter_keys = list(LETTER_IMAGES.keys())
execute_flag = False

display.show(LETTER_IMAGES[letter_keys[current_letter]])

while True:
    if button_a.was_pressed():
        current_letter = (current_letter + 1) % len(letter_keys)
        display.show(LETTER_IMAGES[letter_keys[current_letter]])

    if button_b.was_pressed():
        execute_flag = True

    if execute_flag:
        execute_movement_sequence(letter_keys[current_letter])
        execute_flag = False
        display.clear()
        sleep(1000)
        display.show(LETTER_IMAGES[letter_keys[current_letter]])

    sleep(100)

