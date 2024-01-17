from tkinter import filedialog as fd
import tkinter as tk
import os
import cv2
import numpy as np;
from Sombras import Sombras
from matplotlib import pyplot as plt
from UI import UI
from Seleciona import Seleciona
op = None
while(op != 0):
  op = Seleciona().img
  if op == 0:
    break
  image = cv2.imread(op)#Le a imagem
  kernel = np.ones((5, 5), np.uint8)
  tipo_de_img = UI().tipo_de_img
  if tipo_de_img == 2:
    Sombras(image)
    imagem = cv2.imread('Sample.jpg')
  if tipo_de_img == 1:
    imagem = image
  imgray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
  img = cv2.erode(imgray , kernel, iterations=1)#Cria erosao na imagem
  img = cv2.dilate(img, kernel, iterations=1)#dilata a imagem	
  ret,img = cv2.threshold(img,175,255,cv2.THRESH_BINARY)#Converte o Cinza para preto
  height = 200
  width = 200
  x = 50
  y = 70
  img = img[y:y+height, x:x+width]
  dim=(300,300)#Dimencao da imagem
  img = cv2.resize(img,dim,interpolation = cv2.INTER_AREA)
  area_preta = np.sum(img == 0)
  area = int(area_preta * 0.00100)
  area = "Area:"+str(area)+"cm2"
  imagem = cv2.putText(imagem, area, (25,30), cv2.FONT_ITALIC, 1 ,(0,0,255), 2)
  imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
  # Plotar a imagem original
  plt.subplot(1, 2, 1)
  plt.imshow(imagem_rgb)
  plt.title('Imagem original')

  # Plotar a imagem convoluída
  plt.subplot(1, 2, 2)
  plt.imshow(img, cmap='gray')
  plt.title('Imagem Com os Processos')

  # Exibir os gráficos
  plt.show()
  op = 1