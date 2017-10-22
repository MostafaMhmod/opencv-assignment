#---------------------------------------------------------
#-----------------------IMPORTS---------------------------
#---------------------------------------------------------
import numpy as np
import cv2
#---------------------------------------------------------
#----------------Handling GUC image-----------------------
#---------------------------------------------------------
img = cv2.imread('images/GUC.png')  # load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert it to hsv
h, s, v = cv2.split(hsv)
v = np.where(v < 50, 0, v - 50)
final_hsv = cv2.merge((h, s, v))
newImg = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("GUC_after.jpg", newImg)
cv2.imshow('Image1_Before', img)
cv2.imshow('Image1_After', newImg)
#---------------------------------------------------------
#----------------Handling Calculator Image----------------
#---------------------------------------------------------
img = cv2.imread('images/calculator.png')  # load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert it to hsv
h, s, v = cv2.split(hsv)
v = np.where(v > 155, 255, v + 100)
v = np.where(v < 100, 0, v - 100)
final_hsv = cv2.merge((h, s, v))
newImg = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("calculator_after.jpg", newImg)
cv2.imshow('Image2_Before', img)
cv2.imshow('Image2_After', newImg)
#---------------------------------------------------------
#----------------Handling cameraman.png-------------------
#---------------------------------------------------------
img = cv2.imread('images/cameraman.png')  # load rgb image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert it to hsv
h, s, v = cv2.split(hsv)
v = np.where(v < 25, v * 3, v)
final_hsv = cv2.merge((h, s, v))
newImg = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("cameraman_after.jpg", newImg)
cv2.imshow('Image3_Before', img)
cv2.imshow('Image3_After', newImg)
#---------------------------------------------------------
#-----------------Handling lake.png----------------------
#---------------------------------------------------------
lake1Img = cv2.imread('images/lake.png', 0)  # load image
lake1Img1 = cv2.adaptiveThreshold(
    lake1Img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, -14)
lake1Img2 = cv2.adaptiveThreshold(
    lake1Img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 8)
lake1ImgFinal = cv2.add(lake1Img, lake1Img2)
lake1ImgFinal = np.where(lake1Img2 == 0, 0, lake1Img)
cv2.imshow("lake_after1.png", lake1ImgFinal)
cv2.imwrite("lake_after1.png", lake1ImgFinal)
#---------------------------------------------------------
#-----------------Handling james.png----------------------
#---------------------------------------------------------
london1Img = cv2.imread('images/london1.png')  # load image
london2Img = cv2.imread('images/london2.png')  # load image
img = cv2.imread('images/james.png', 0)  # load image
newImg = cv2.imread('images/james.png', 0)  # load image
newImg = np.where(newImg < 242, newImg + 1, 60)
newImgFlipped = cv2.flip(newImg, 1)
M = np.float32([[1, 0, -180], [0, 1, 0]])
newImg = cv2.warpAffine(newImg, M, (img.shape[1], img.shape[0]))
bgra = cv2.cvtColor(newImg, cv2.COLOR_GRAY2BGRA)  # convert it to bgra
bgraFlipped = cv2.cvtColor(
    newImgFlipped, cv2.COLOR_GRAY2BGRA)  # convert it to bgra
london1Img = cv2.cvtColor(london1Img, cv2.COLOR_BGR2BGRA)  # convert it to bgra
london2Img = cv2.cvtColor(london2Img, cv2.COLOR_BGR2BGRA)  # convert it to bgra

(b1, g1, r1, a1) = cv2.split(bgra)
(b2, g2, r2, a2) = cv2.split(london1Img)
(b3, g3, r3, a3) = cv2.split(bgraFlipped)
(b4, g4, r4, a4) = cv2.split(london2Img)

for i in range(len(b1)):
    for j in range(len(b1[i])):
        if (b1[i][j] == 60 or b1[i][j] == 0 or g1[i][j] == 60 or g1[i][j] == 60 or r1[i][j] == 60 or r1[i][j] == 0):
            a1[i][j] = 0
            a2[i][j] = 255
            b1[i][j] = 0
            g1[i][j] = 0
            r1[i][j] = 0

        else:
            a1[i][j] = 255
            a3[i][j] = 255
            a2[i][j] = 0
            b2[i][j] = 0
            g2[i][j] = 0
            r2[i][j] = 0


for i in range(len(b3)):
    for j in range(len(b3[i])):
        if (b3[i][j] == 60 or b3[i][j] == 0 or g3[i][j] == 60 or g3[i][j] == 60 or r3[i][j] == 60 or r3[i][j] == 0):
            b3[i][j] = 0
            g3[i][j] = 0
            r3[i][j] = 0
            a4[i][j] = 255
        else:
            a3[i][j] = 255
            a4[i][j] = 0
            b4[i][j] = 25
            g4[i][j] = 25
            r4[i][j] = 25


james_bgra = cv2.merge((b1, g1, r1, a1))
james_bgraFlipped = cv2.merge((b3, g3, r3, a3))
london1Img_bgra = cv2.merge((b2, g2, r2, a2))
london2Img_bgra = cv2.merge((b4, g4, r4, a4))
finalImg = np.where(james_bgra + london1Img_bgra > 255,
                    london1Img_bgra, james_bgra + london1Img_bgra)
finalImgFilpped = np.where(james_bgraFlipped + london2Img_bgra > 255,
                           london2Img_bgra, james_bgraFlipped + london2Img_bgra)
cv2.imshow("jamesInLondon1.png", finalImg)
cv2.imshow("jamesInLondon2.png", finalImgFilpped)
cv2.imwrite("jamesInLondon2.png", finalImg)
cv2.imwrite("jamesInLondon2.png", finalImgFilpped)

#---------------------------------------------------------
#------------Handling img showing and closing-------------
#---------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
