#แสดงผลภาพ
import cv2
img = cv2.imread("image/cat.jpg")

#แสดงภาพ
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()