import cv2
import numpy as np

img = cv2.imread('husky.jpg')

h,w = img.shape[:2]
imgCopy = img.copy()
imgCopy = imgCopy/255
imgyCbCr = np.zeros((h, w, 3), np.float)

imgyCbCr[:, :, 0] = (0.2568 * img[:, :, 2]) + (0.5041 * img[:, :, 1]) + (0.097 * img[:, :, 0]) + 16        # 0 Y
imgyCbCr[:, :, 1] = (-0.1482 * img[:, :, 2]) - (0.2910 * img[:, :, 1]) + (0.4392 * img[:, :, 0]) + 128     # 1 Cb
imgyCbCr[:, :, 2] = (0.4392 * img[:, :, 2]) - (0.3678 * img[:, :, 1]) - (0.0714 * img[:, :, 0]) + 128      # 2 Cr

yMax = np.max(imgyCbCr[:, :, 0])
yMin = np.min(imgyCbCr[:, :, 0])

imgyCbCr[:, :, 0] = (imgyCbCr[:, :, 0] - yMin)/(yMax - yMin) #Y entre 0 e 1

CbMax = np.max(imgyCbCr[:, :, 1])
CbMin = np.min(imgyCbCr[:, :, 1])

imgyCbCr[:, :, 1] = (imgyCbCr[:, :, 1] - CbMin) / (CbMax - CbMin) #Cb entre 0 e 1

CrMax = np.max(imgyCbCr[:, :, 2])
CrMin = np.min(imgyCbCr[:, :, 2])

imgyCbCr[:, :, 2] = (imgyCbCr[:, :, 2] - CrMin) / (CrMax - CrMin) #Cr entre 0 e 1

yCbCr = np.zeros((h, w, 3), np.uint8)
yCbCr = (imgyCbCr * 255).astype('uint8')

cv2.imshow("Imagem y - Luminancia", yCbCr[:, :, 0])
cv2.imshow("Imagem Cb - Azul", yCbCr[:, :, 1])
cv2.imshow("Imagem Cr - Vermelho", yCbCr[:, :, 2])

novaImg = np.zeros((h, w, 3), np.uint8)
novaImg[:, :, 0] = yCbCr[:, :, 1] #B
novaImg[:, :, 1] = yCbCr[:, :, 0] #G
novaImg[:, :, 2] = yCbCr[:, :, 2] #R
cv2.imshow("Imagem yCbCr - G B R", novaImg)
cv2.imshow("Imagem RGB", img)
cv2.waitKey(0)

