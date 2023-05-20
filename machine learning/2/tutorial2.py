import cv2
import random


def main():
    photo = cv2.imread('../1/img/p.jpg', -1)

    photo = cv2.resize(photo, (0, 0), fx=0.5, fy=0.5)


    for i in range(300):
        for j in range(photo.shape[1]):
            photo[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    cv2.imshow('Result', photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
