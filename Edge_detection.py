import cv2 as cv
import numpy as np

I=cv.imread('img/a03-011-00-00.png');
image = cv.cvtColor(I, cv.COLOR_BGR2GRAY)


Gx = np.array([(-1, 0, 1), (-2, 0, 2), (-1, 0, 1)])
Gy = np.array([(-1, -2, -1), (0, 0, 0), (1, 2, 1)])
ligne=image.shape[0];
colonne=image.shape[1];
imgX=image.copy();
imgY=image.copy();
imgFin = image.copy();
for i in range(1, ligne-1 ):
    for j in range(1,colonne-1):
        x_sum = (Gx.item(0, 0) * image.item(i-1, j-1)) + (Gx.item(0, 2) * image.item(i-1, j+1)) + (Gx.item(1, 0) * image.item(i, j-1)) + (Gx.item(1, 2) * image.item(i, j+1)) + (Gx.item(2, 0) * image.item(i+1, j-1)) + (Gx.item(2, 2) * image.item(i+1, j+1))
        y_sum = (Gy.item(0, 0) * image.item(i-1, j-1)) + (Gy.item(0, 1) * image.item(i-1, j)) + (Gy.item(0, 2) * image.item(i-1, j+1)) + (Gy.item(2, 0) * image.item(i+1, j-1)) + (Gy.item(2, 1) * image.item(i+1, j)) + (Gy.item(2, 2) * image.item(i+1, j+1))
        imgX.itemset((i-1, j-1), x_sum)
        imgY.itemset((i-1, j-1), y_sum)
        imgFin.itemset((i-1,j-1),np.sqrt(x_sum ** 2 +y_sum ** 2))
cv.imshow('gray',imgFin);
cv.waitKey(0);
        