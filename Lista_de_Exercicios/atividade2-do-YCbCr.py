import cv2
import numpy as np

# Lendo a imagem
img = cv2.imread("paisagem.jpg")

#Ajustando a imagem
h,w = img.shape[:2]
hnew = int(h/2)
wnew = int(w/2)

#Matriz YCbCr
ycbcrImg = np.zeros((h,w,3), np.float)

#Convertendo RGB para YCbCr
ycbcrImg[:,:,0] = img[:,:,2]*0.2568 + 0.5041*img[:,:,1] + 0.097*img[:,:,0] +16
ycbcrImg[:,:,1] = -img[:,:,2]*0.1482 - 0.2910*img[:,:,1] + 0.4392*img[:,:,0] +128
ycbcrImg[:,:,2] = img[:,:,2]*0.4392 - 0.3678*img[:,:,1] - 0.0714*img[:,:,0] +16

#Y entre 0 e 1
Ymax = np.max(ycbcrImg[:,:,0])
Ymin = np.min(ycbcrImg[:,:,0])
ycbcrImg[:,:,0] = (ycbcrImg[:,:,0] - Ymin)/(Ymax - Ymin)

#Cb entre 0 e 1
Cbmax = np.max(ycbcrImg[:,:,1])
Cbmin = np.min(ycbcrImg[:,:,1])
ycbcrImg[:,:,1] = (ycbcrImg[:,:,1] - Cbmin)/(Cbmax - Cbmin)

#Cr entre 0 e 1
Crmax = np.max(ycbcrImg[:,:,2])
Crmin = np.min(ycbcrImg[:,:,2])
ycbcrImg[:,:,2] = (ycbcrImg[:,:,2] - Crmin)/(Crmax - Crmin)

# Conversão YCbCr
ycbcrImg = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

#Ajustando a imagem
resizedImagem = cv2.resize(img, (wnew, hnew), interpolation=cv2.INTER_AREA)
resizedImagem2 = cv2.resize(ycbcrImg, (wnew, hnew), interpolation=cv2.INTER_AREA)
resizedImagem3 = cv2.resize(ycbcrImg, (wnew, hnew), interpolation=cv2.INTER_AREA)


#Exibir as Imaagem
cv2.imshow("Imagem Original", resizedImagem)
cv2.imshow("Imagem YCbCr do opencv", resizedImagem2)
cv2.imshow("Imagem YCbCr", resizedImagem3)
cv2.waitKey(0)