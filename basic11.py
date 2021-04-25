import cv2

#อ่านภาพ
img = cv2.imread("image/cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))


#วาดสี่เหลี่ยม
# rectangle(ภาพ,มุมที่ 1 (บนซ้าย),มุมที่ 2 (ล่างขวา),สี,ความหนา)

cv2.rectangle(imgresize,(100,100),(500,500),(0,0,255),-1)

cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()