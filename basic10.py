import cv2

#อ่านภาพ
img = cv2.imread("image/cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))


#วาดเส้นตรง
# line (ภาพ , จุดเริ่มต้น (x,y) , จุดสุดท้าย (x,y), สี (BGR) ,ความหนา)
cv2.arrowedLine(imgresize,(100,100),(500,200),(255,0,0),10)
cv2.arrowedLine(imgresize,(20,0),(400,400),(0,255,0),10)
cv2.arrowedLine(imgresize,(0,0),(600,400),(0,0,255),10)

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()