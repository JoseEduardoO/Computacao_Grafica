import cv2
import numpy as np
import math


def filterImage(image):
    k = np.ones((3, 3))
    k[1][1] = np.sum(k)
    h, w = image.shape[:2]
    filtro = np.zeros((h, w))

    for i in range(h-1):
        for j in range(w-1):
            filtro[i][j] = (image[i-1][j-1] * k[0][0] + image[i-1][j] * k[0][1] + image[i-1][j+1] * k[0][2] +\
                              image[i][j-1] * k[1][0] + image[i][j] * k[1][1] + image[i][j+1] * k[1][2] +\
                              image[i+1][j-1] * k[2][0] + image[i+1][j] * k[2][1] + image[i+1][j+1] * k[2][2]) / 17

    return filtro.astype("uint8")


image = cv2.imread("passaro.jpg", 0)

filtered = filterImage(image)
cv2.imshow("Imagem Original", image)
cv2.imshow("Imagem Filtrada", filtered)
cv2.waitKey(0)
