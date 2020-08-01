import cv2
import numpy as np

# Lendo a imagem
img = cv2.imread("animal.jpg")
img2 = cv2.imread("animal.jpg")

#ajustando a imagem
h,w = img.shape[:2]
hnew = int(h/1)
wnew = int(w/1)
resizedImagem = cv2.resize(img2, (wnew, hnew), interpolation=cv2.INTER_AREA)

# Imagem Cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resizedImagem2 = cv2.resize(imgCinza, (wnew, hnew), interpolation=cv2.INTER_AREA)

# Pegando os pixeis RGB
bp = img[:,:,0]
gp = img[:,:,1]
rp = img[:,:,2]

# Realizando a média entre os três canais.
media = ((bp + gp + rp)/3)

# Colocado os pixeis feito da media , e assim fazendo a media cinza
img[:,:, 0] = media
img[:,:, 1] = media
img[:,:, 2] = media
resizedImagem3 = cv2.resize(img, (wnew, hnew), interpolation=cv2.INTER_AREA)

# Exibir as imagens
cv2.imshow("Imagem Original", resizedImagem)
cv2.imshow("Imagem Cinza ", resizedImagem2)
cv2.imshow("Imagem Cinza Media dos 3 canais", resizedImagem3)
cv2.waitKey(0)