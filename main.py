import cv2 as cv
import mss
import numpy as np
from utils.config import region, obstacle


def main():
    with mss.mss() as sct:
        while True:
            screenshot = sct.grab(region)
            img = np.array(screenshot)
            img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

            cv.rectangle(img, (obstacle["left"], obstacle["top"]), (
                obstacle["left"]+obstacle["width"], obstacle["top"]+obstacle["height"]),(0,255,0),1)
            cv.imshow("Screenshot", img)
            if cv.waitKey(1) & 0xFF == ord('q'):
                cv.destroyAllWindows()
                break


if __name__ == '__main__':
    main()
