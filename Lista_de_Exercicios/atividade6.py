import cv2
import numpy as np

#Lendo a imagem
img = cv2.imread("pet.jpg")

#Aplicando os filtros
filtro1 = np.array([[0,1,0],[1,1,1],[0,1,0]])/5
media1 = cv2.filter2D(img, -1, filtro1)

filtro2 = np.array([[1,1,1],[1,1,1],[1,1,1]])/9
media2 = cv2.filter2D(img, -1, filtro2)

filtro3 = np.array([[1,1,1],[1,2,1],[1,1,1]])/10
media3 = cv2.filter2D(img, -1, filtro3)

filtro4 = np.array([[1,2,1],[2,4,2],[1,2,1]])/12
media4 = cv2.filter2D(img, -1, filtro4)

#Exibir as Imagens
cv2.imshow("Imagem original", img)
cv2.imshow("Media do F1 3x3", media1)
cv2.imshow("Media do F2 3x3", media2)
cv2.imshow("Media do F3 3x3", media3)
cv2.imshow("Media do F4 3x3", media4)
cv2.waitKey()
