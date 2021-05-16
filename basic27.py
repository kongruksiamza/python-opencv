# แสดงผลภาพด้วย Matplotlib
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("image/girl.jpg")
cv2.imshow("Output",img)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()