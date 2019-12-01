import numpy as np
import cv2
import time


def show_image():
    img: np.ndarray = cv2.imread('Lenna.png')  # img jest juz np.ndarray
    print(type(img), np.shape(img), img.dtype)
    cv2.imshow('my image', img)  # pokazanie okna o nazwie 'my image' z tym obrazem
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
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_webcam()
