import cv2

def main():
    photo = cv2.imread('../1/img/p.jpg', -1)

    photo = cv2.resize(photo, (0, 0), fx = 0.5, fy = 0.5)

    photo = cv2.rotate(photo, cv2.ROTATE_180)

    cv2.imwrite('new.jpg', photo)

    cv2.imshow('Result', photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
