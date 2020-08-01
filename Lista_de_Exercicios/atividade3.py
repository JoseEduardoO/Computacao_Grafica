import cv2
import numpy as np
from matplotlib import pyplot as plt

# lendo a imagem
img = cv2.imread("imagem.jpg")

#Ajustando a imagem
h,w = img.shape[:2]
totalPixel = h*w

# Imagem em Cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculando o Histograma
hist = cv2.calcHist([imgCinza],[0],None,[256],[0,256])

#Probabilidade das cores,definindo as variaveis
maxProb = 0
limiar = 0

for i in range(256):
    prob = hist[i]/totalPixel
    if prob > maxProb:
        maxProb = prob
        limiar = i
print(limiar)

#aplicando o limiar
imgNova = np.zeros((h,w), np.uint8)
for i in range(h):
    for j in range(w):
        if img[i,j,0] >= limiar:
            imgNova[i,j] = 255

# Exibi as imagens
cv2.imshow("Imagem Original", img)
cv2.imshow("Limiar", imgNova)
plt.plot(hist,color = 'b')
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)