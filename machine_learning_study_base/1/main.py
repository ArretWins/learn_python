import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 300)


if not cap.isOpened():
    print("Ошибка: камера недоступна")
else:
    while True:
        success, img = cap.read()

        cv2.imshow('Result', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#
#
# img = cv2.imread('img/p.jpg')
#
# #new_img = cv2.resize(img, (500, 500))
# img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
# img = cv2.GaussianBlur(img, (3, 3), 0)      #blur
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# img = cv2.Canny(img, 200, 200)
#
# kernel = np.ones((5, 5), np.uint8)
# img = cv2.dilate(img, kernel, iterations = 1)
#
# img = cv2.erode(img, kernel, iterations = 1)
#
# cv2.imshow("Result", img)
#
# #print(img.shape)    #show size of image


