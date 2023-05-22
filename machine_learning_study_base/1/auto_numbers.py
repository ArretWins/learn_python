import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

def main():
    img = cv2.imread('img/car1.webp')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_filter = cv2.bilateralFilter(gray, 11, 15, 15) #уменьшение шума
    edges = cv2.Canny(img_filter, 100, 200) #края

    cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #контуры
    cont = imutils.grab_contours(cont)
    cont = sorted(cont, key = cv2.contourArea, reverse = True)[:8]

    pos = None
    for c in cont:
        approx = cv2.approxPolyDP(c, 10, True)
        if len(approx) == 4:
            pos = approx
            break

    mask = np.zeros(gray.shape, np.uint8)
    new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
    bitwise_img = cv2.bitwise_and(img, img, mask = mask)

    #print(pos)

    pl.imshow(cv2.cvtColor(bitwise_img, cv2.COLOR_BGR2RGB))
    pl.show()


if __name__ == '__main__':
    main()
