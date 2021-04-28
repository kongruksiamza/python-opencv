#แสดงพิกัดด้วย Mouse Event
import cv2
img = cv2.imread("image/tree.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),cv2.LINE_4)
        cv2.imshow("Output",img)

#แสดงภาพ
cv2.imshow("Output",img)
#ทำงานกับ Mouse
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()