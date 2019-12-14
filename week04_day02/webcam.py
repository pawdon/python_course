import numpy as np
import cv2
import time


def black_rect(img):
    shape = np.shape(img)
    height = shape[0]
    h_start = int(height / 3)
    h_stop = int(height * 2 / 3)

    width = shape[1]
    w_start = int(width / 2)
    w_stop = int(width * 3 / 4)

    img[h_start:h_stop, w_start:w_stop] = 0


def reset_gb(img):
    img[:, :, 0] = 0  # reset B
    img[:, :, 1] = 0  # reset G


def edit01(img):
    img = np.asarray(img, np.float)  # np.int tez by zadzialal
    img[:, :, 2] *= 2  # edit R
    img[:, :, 2] = np.where(img[:, :, 2] > 255, 255, img[:, :, 2])
    img = np.asarray(img, np.uint8)
    return img


def edit02(img):
    img = np.asarray(img, np.float)
    img[:, :, 2] /= 2  # edit R
    img = np.asarray(img, np.uint8)
    return img


def show_image():
    img: np.ndarray = cv2.imread('Lenna.png')  # img jest juz np.ndarray
    print(type(img), np.shape(img), img.dtype)
    reset_gb(img)
    cv2.imshow('original', img)
    # black_rect(img)
    img = edit01(img)
    cv2.imshow('edit', img)  # pokazanie okna o nazwie 'my image' z tym obrazem
    # 1. np.ndarray, dtype=np.uint8, wartosci w przedziale <0, 255>
    # 2. np.ndarray, dtype=np.float, wartosci w przedziale <0, 1>
    cv2.waitKey(0)  # czekaj na nacisniecie jakiegos klawisza przez x ms; x <=0 oznacza nieskonczenie dlugo
    cv2.destroyAllWindows()  # zniszcz okna


def show_webcam():
    cam = cv2.VideoCapture(0)  # jesli wpiszemy nr, to oznacza to kamerke, jesli nazwe pliku, to plik
    while True:
        ret_val, img = cam.read()  # ret_val to bool, ktory mowi, czy sie udalo
        if ret_val:
            cv2.imshow('my webcam', img)
            if cv2.waitKey(1) == ord('q'):  # waitKey zwraca kod przycisku, ktory zostal nacisniety
                break  # esc to quit
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_webcam()
