import cv2
import numpy as np
import math

# Lendo a imagem
img = np.float32(cv2.imread("paisagem.jpg"))/255
img2 = cv2.imread("paisagem.jpg")

#Ajustando a imagem
h,w = img.shape[:2]
hnew = int(h/2)
wnew = int(w/2)

# Pegar os pixeis RGB
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

# Calculando a Intensidade dos 3 canais
intensidade = ((r + g + b)/3)
# Calcular Saturação
minimo = np.minimum(np.minimum(r, g), b)
saturacao = 1 - (3 / (r + g + b + 0.001)* minimo)

# Calcular Matriz
with np.errstate(divide='ignore', invalid='ignore'):
    matriz = np.copy(r)
    for i in range(0, b.shape[0]):
        for j in range(0, b.shape[1]):
            matriz[i][j] = 0.5 * ((r[i][j] - g[i][j]) + (r[i][j] - b[i][j])) / \
                    math.sqrt((r[i][j] - g[i][j])**2 +
                     ((r[i][j] - b[i][j]) * (g[i][j] - b[i][j])))
            matriz[i][j] = math.acos(matriz[i][j])
            if b[i][j] <= g[i][j]:
                matriz[i][j] = matriz[i][j]
            else:
                matriz[i][j] = ((360 * math.pi) / 180.0) - matriz[i][j]

# juntando os canais na imagem
img[:,:, 0] = matriz
img[:,:, 1] = saturacao
img[:,:, 2] = intensidade
Imagem = cv2.cvtColor(img2, cv2.COLOR_RGB2HLS)

# Ajustando a imagem
resizedImagem = cv2.resize(img, (wnew, hnew), interpolation=cv2.INTER_AREA)
resizedImagem2 = cv2.resize(Imagem, (wnew, hnew), interpolation=cv2.INTER_AREA)
resizedImagem3 = cv2.resize(img2, (wnew, hnew), interpolation=cv2.INTER_AREA)

# Exibir a Imagem
cv2.imshow("Imagem HSI", resizedImagem)
cv2.imshow("Imagem HSL ", resizedImagem2)
cv2.imshow("Imagem Original ", resizedImagem3)
cv2.waitKey(0)