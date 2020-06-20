import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('husky.jpg')
print (img.shape)

h,w,c = img.shape
h2 = int(h/4)
w2 = int(w/4)

resized = cv2.resize(img, (w2,h2))
hR = numpy.zeros(256, numpy.float)  # Vermelho
hG = numpy.zeros(256, numpy.float)  # Verde
hB = numpy.zeros(256, numpy.float)  # Azul

for i in range(h2):
  for j in range(w2):
    pR = resized[i,j,2]
    hR[resized[i,j,2]] = hR[resized[i,j,2]] + 1    # Vermelho

    pG = resized[i,j,1]
    hG[resized[i,j,1]] = hG[resized[i,j,1]] + 1    # Verde

    pB = resized[i,j,0]                             #Azul
    hB[resized[i,j,0]] = hB[resized[i,j,0]] + 1

plt.plot(hR, 'r')
plt.plot(hG, 'g')
plt.plot(hB, 'b')
plt.show()