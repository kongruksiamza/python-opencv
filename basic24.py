#ตรวจจับดวงตาและใบหน้า
import cv2

#อ่านภาพ
img = cv2.imread("image/girl.jpg")

#อ่านไฟล์ xml
face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#ตรวจจับใบหน้า
face_detect = face_cascade.detectMultiScale(gray_img,1.1,4)

#ตรวจจับดวงตา
eye_detect = eye_cascade.detectMultiScale(gray_img,1.1,4)

for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
    for (ex,ey,ew,eh) in eye_detect:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),thickness=5)

#แสดงภาพ
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()