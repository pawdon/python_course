import cv2
import numpy as np
import contextlib


def triangle(h: int, a: int, char='*'):
    for i in range(1, h + 1):
        x = round(i * a / h)
        if x == 0:
            x = 1
        print(char * x)


def fib(n: int) -> int:
    if n < 0:
        raise ValueError('n < 0')
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def get_date_of_birth(pesel: str):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    century_offset, month = divmod(month, 20)
    if not (1 <= month <= 12):
        raise ValueError('Month should be in range <1, 12>')
    if not (1 <= day <= 31):
        raise ValueError('Day should be in range <1, 31>')
    # century = 1900 + 100 * century_offset if century_offset < 4 else 1800
    century = {4: 1800, 0: 1900, 1: 2000, 2: 2100, 3: 2200}.get(century_offset)
    year += century
    return year, month, day


def format_result(year, month, day, sex):
    month = str(month).rjust(2, '0')
    day = str(day).rjust(2, '0')
    return f'{year}.{month}.{day}-{sex}'


def check_correctness(pesel):
    assert len(pesel) == 11, 'Pesel length should be 11'

    try:
        int(pesel)
    except Exception:
        raise ValueError('Pesel should contain only numbers')

    multipliers = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7]
    expected_checksum = sum([int(p) * m for p, m in zip(pesel, multipliers)]) % 10
    real_checksum = int(pesel[10])
    assert expected_checksum == real_checksum, f'Checksum incorrect (should be {expected_checksum})'


def analyse_pesel(pesel: str):
    try:
        check_correctness(pesel)
        year, month, day = get_date_of_birth(pesel)
        sex = 'M' if int(pesel[9]) % 2 == 1 else 'F'
        return format_result(year, month, day, sex)
    except Exception as e:
        raise ValueError(f'Pesel not correct: {e}')


# print(analyse_pesel('04211725639'))

@contextlib.contextmanager
def open_stream(name):
    # odpala sie w linijce
    # with open_stream(0) as cam
    print('Open stream')
    camera = cv2.VideoCapture(name)
    try:
        yield camera  # to camera trafia do cam z linijki as cam
    finally:
        # to sie wykonuje po wyjsciu z with, czyli kiedy konczy sie wciecie
        print('Close stream')
        camera.release()
        cv2.destroyAllWindows()


def get_frames(cam):
    while True:
        ret_val, img = cam.read()
        if ret_val:
            yield img
        else:
            print('BREAK FROM GENERATOR')
            break


def show_img(img, window_name='image', wait_key=0):
    cv2.imshow(window_name, img)
    return cv2.waitKey(wait_key)


def get_frames_from_cam(name):
    with open_stream(name) as cam:
        for frame in get_frames(cam):
            yield frame


def webcam():
    with open_stream(0) as cam:
        for frame in get_frames(cam):
            key = show_img(frame, wait_key=1)
            if key == ord('q'):
                break


def webcam2():
    for frame in get_frames_from_cam(0):
        key = show_img(frame, wait_key=1)
        if key == ord('q'):
            break


webcam()
