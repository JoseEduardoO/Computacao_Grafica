import cv2

#lendo a imagem
imagem = cv2.imread("animais.jpg")

#Processos de suavização a partir da mediana para janelas 3x3, 5x5 e 7x7.
mediana_3x3 = cv2.medianBlur(imagem, 3)
mediana_5x5 = cv2.medianBlur(imagem, 5)
mediana_7x7 = cv2.medianBlur(imagem, 7)

# Exibir as imagens
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Mediana de 3x3", mediana_3x3)
cv2.imshow("Mediana de 5x5", mediana_5x5)
cv2.imshow("Mediana de 7x7", mediana_7x7)
cv2.waitKey(0)

