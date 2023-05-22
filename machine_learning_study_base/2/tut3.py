import cv2

# Захватываем видео с первой доступной камеры
cap = cv2.VideoCapture(0)

while True:
    # Читаем кадр из видео потока
    ret, frame = cap.read()

    # Отображаем кадр
    cv2.imshow('frame', frame)

    # Если пользователь нажимает клавишу 'q', выходим из цикла
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем захват камеры и закрываем окна
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
