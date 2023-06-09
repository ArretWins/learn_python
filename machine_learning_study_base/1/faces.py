import cv2

def main():
    img = cv2.imread('img/tanya2.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier('faces.xml')

    results = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for(x, y, w, h) in results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 230), thickness=2)

    cv2.imshow('Result', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
