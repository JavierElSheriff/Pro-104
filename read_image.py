import cv2

img = cv2.imread("butterfly.jpg")

cv2.imshow("Mostrar imagen",img)

print(img)

cv2.waitKey(0)

