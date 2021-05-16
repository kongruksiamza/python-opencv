#แสดง Threshold ใน Matplotlib
import cv2
import matplotlib.pyplot as plt
gray_img = cv2.imread("image/gradient.png")

thresh,th1 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY)
thresh,th2 = cv2.threshold(gray_img,128,255,cv2.THRESH_BINARY_INV)
thresh,th3 = cv2.threshold(gray_img,128,255,cv2.THRESH_TRUNC)
thresh,th4 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO)
thresh,th5 = cv2.threshold(gray_img,128,255,cv2.THRESH_TOZERO_INV)

images = [gray_img,th1,th2,th3,th4,th5]
titles = ["ORIGINAL","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()