import cv2
import numpy as np

img = cv2.imread('husky.jpg')

h,w = img.shape[:2] # aLtura e largura

imgCopy = img.copy()
imgCopy = imgCopy/255
imgCMYK = np.zeros((h, w, 4), np.float)

for i in range(h):
    for j in range(w):
        black = np.min([imgCopy[i, j, 0],imgCopy[i, j, 1],imgCopy[i, j, 2]])
        if (1-black) == 0:
            black = 0.99999

        blue = imgCopy[i, j, 0]
        green = imgCopy[i, j, 1]
        red = imgCopy[i, j, 2]

        imgCMYK[i, j, 0] = (1-red-black)/(1-black)                  # 0=C
        imgCMYK[i, j, 1] = (1 - green - black) / (1 - black)        # 1=M
        imgCMYK[i, j, 2] = (1 - blue - black) / (1 - black)         # 2=Y
        imgCMYK[i, j, 3] = black                                    # 3=K

imgCMYK = (imgCMYK * 255).astype('uint8')

cv2.imshow("Imagem Ciano", imgCMYK[:, :, 0])
cv2.imshow("Imagem Magenta", imgCMYK[:, :, 1])
cv2.imshow("Imagem Amarelo", imgCMYK[:, :, 2])
cv2.imshow("Imagem Preto", imgCMYK[:, :, 3])
cv2.waitKey(0)

