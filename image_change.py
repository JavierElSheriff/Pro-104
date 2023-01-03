import cv2
import numpy as np

green = np.zeros([600,600])
print(green)

green[200:400,200:400] = 225
print(green)

cv2.imshow("En verde",green)
cv2.waitKey(0)