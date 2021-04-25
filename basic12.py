import cv2

#อ่านภาพ
img = cv2.imread("image/cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))


#วาดวงกลม
# circle(ภาพ,ตำแหน่งจุดศูนย์กลางวงกลม (x,y),รัศมี,สี,ความหนา)
cv2.circle(imgresize,(200,200),70,(0,0,255),-1)

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()