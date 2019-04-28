# Example by Anas
import cv2

camera = cv2.VideoCapture(0)
raw = ('Press enter to continue')
return_value, image = camera.read()
cv2.imwrite('img1.png',image)
del(camera)