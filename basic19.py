import cv2 
import numpy

while True :
    img=cv2.imread("image/ball2d.jpg")
    img=cv2.resize(img,(400,400))

    #ช่วงของสี BGR
    lower = numpy.array([5,111,10])
    upper = numpy.array([124,255,133])

    mask=cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    if cv2.waitKey(0) & 0xFF == ord("e"):
        break

    cv2.imshow("Original",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)

cv2.destroyAllWindows()