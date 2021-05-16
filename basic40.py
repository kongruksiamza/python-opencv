#Motion Detection
import cv2 
cap = cv2.VideoCapture("image/Walking.mp4")
check , frame1 = cap.read()
check , frame2 = cap.read()
while (cap.isOpened()):
    if check == True :
        motiondiff= cv2.absdiff(frame1,frame2)
        gray=cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        thresh,result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)
        dilation = cv2.dilate(result,None,iterations=3)
        contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame1,contours,-1,(0,255,0),2)
        cv2.imshow("Output",frame1)
        frame1=frame2
        check,frame2 = cap.read()
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()

