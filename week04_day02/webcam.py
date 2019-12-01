import numpy as np
import cv2
import time


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        shape = np.shape(img)

        stime = time.time()
        """
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    img[i, j, k] *= 2
                    if img[i, j, k] > 255:
                        img[i, j, k] = 255
        # """

        # """
        img *= 2
        img = np.where(img > 255, 255, img)  
        # """

        print('Time', time.time() - stime, 's')

        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == ord('q'):
            break  # esc to quit
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_webcam()
