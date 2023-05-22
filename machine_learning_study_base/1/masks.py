import cv2
import numpy as np

def main():

    photo = cv2.imread('img/p.jpg')
    img = np.zeros(photo.shape[:2], dtype='uint8') #даведацца аб размерах фота(срэз толькі 2 элементаў без слаёў"

    circle = cv2.circle(img.copy(), (200, 300), 120, 255, -1)
    square = cv2.rectangle(img.copy(), (25 , 25), (250, 350), 255, -1)

    img = cv2.bitwise_and(photo, photo, mask=circle) #отображает аднолькавыя часткі
    # img = cv2.bitwise_or(circle, square) #отображает усе часткі
    # img = cv2.bitwise_xor(circle, square) #отображает усе часткі, акрамя аднолькавых
    # img = cv2.bitwise_not(circle) #інверсія


    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
