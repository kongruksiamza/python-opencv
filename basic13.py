import cv2

#อ่านภาพ
img = cv2.imread("image/cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))

#วาดข้อความบนภาพ
# putText(ภาพ,ข้อความ,พิกัดที่จะแสดงข้อความ (x,y),font,ขนาดข้อความ,สี,ความหนา)

cv2.putText(imgresize,"KONGRUKSIAM",(100,600),cv2.FONT_HERSHEY_SIMPLEX,1.8,(0,0,255),cv2.LINE_4)

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()