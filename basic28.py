#ฟังก์ชั่น Threshold ใน OpenCV
import cv2
gray_img = cv2.imread("image/gradient.png")

thresh,th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh,th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh,th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
thresh,th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
thresh,th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("Orignal",gray_img)
cv2.imshow("BINARY",th1)
cv2.imshow("BINARY_INV",th2)
cv2.imshow("TRUNC",th3)
cv2.imshow("TOZERO",th4)
cv2.imshow("TOZERO_INV",th5)
cv2.waitKey(0)
cv2.destroyAllWindows()