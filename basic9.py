#การบันทึกวิดีโอ
import cv2 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame

    if check == True :
        cv2.imshow("Output",frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break

result.release()
cap.release()
cv2.destroyAllWindows()

