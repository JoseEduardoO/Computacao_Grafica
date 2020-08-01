import cv2
from math import log2

def otsu():
    img = cv2.imread("ilha.jpg", 0) #
    h, w = img.shape[:2]
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    l = 256
    mediaTotal = 0.0
    varTotal = 0.00001
    media_t = 0.0
    w0 = 0.00000000001
    n = -1
    max = -1
    pos = -1

    for t in range(l):
        for i in range(t):
            Pi = hist[i] / (h * w)
            w0 = w0 + Pi
            media_t = media_t + i * Pi
        Pi = hist[t] / (h * w)
        mediaTotal = mediaTotal + t * Pi
        w1 = 1 - w0
        u0 = media_t / w0
        u1 = mediaTotal - media_t / (1 - u0)
        varClasses = w0 * w1 * pow((u1 * u0), 2)
        n = varClasses / varTotal
        if n > max:
            max = n
            pos = t
    return mediaTotal

#Lendo a imamem
imgagem = cv2.imread("ilha.jpg")
img = cv2.imread("ilha.jpg", 0)

#Ajustando a imagem
h,w = img.shape[:2]
otsuTh = otsu()

th, imagem2 = cv2.threshold(img, otsuTh, 255, cv2.THRESH_BINARY)
th, imagem3 = cv2.threshold(img,0,255, cv2.THRESH_OTSU)

# Exibir as imagens
cv2.imshow(" Imagem Original", imgagem)
cv2.imshow("Imaagem Otsu", imagem2)
cv2.imshow(" Imagem Otsu Threshold Binary", imagem3)
cv2.waitKey(0)  
