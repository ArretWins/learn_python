import cv2
import numpy as np

photo = np.zeros((450,450, 3), dtype = 'uint8')


#photo[100:150, 200:280] = 150 , 120 , 55

cv2.rectangle(photo, (50, 50), (150, 150), (128, 0, 128), thickness = 3)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (128, 0, 128), thickness = 3)

cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 60, (128, 0, 128), thickness = cv2.FILLED)

cv2.putText(photo, 'Prohor', (100, 150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (250, 0 , 0), thickness = 1)
#print(photo)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
`