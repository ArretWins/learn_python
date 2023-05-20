import cv2


def main():
    img = cv2.imread('img/p.jpg')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    img = cv2.cvtColor(img, cv2.COLOR_LAB2RGB)

    r, g, b = cv2.split(img)

    img = cv2.merge([b, g, r])

    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
