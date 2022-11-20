import cv2
import matplotlib.pyplot as plt
import numpy as np
# Read image
image1 = cv2.imread("image1.jpeg")
image2 = cv2.imread("image2.jpeg")
# Plot Histogram
image1_hist = cv2.calcHist([image1], [0], None, [256], [0, 256])
image2_hist = cv2.calcHist([image2], [0], None, [256], [0, 256])

cv2.imshow("First Image", image1)
plt.plot(image1_hist)
plt.show()
cv2.imshow("Second Image", image2)
plt.plot(image2_hist)
plt.show()
cv2.waitKey(0)