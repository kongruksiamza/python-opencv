#Canny Method
import cv2 

img = cv2.imread("image/currency.jpg",0)
canny = cv2.Canny(img,50,200)

cv2.imshow("Original",img)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()