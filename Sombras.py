import cv2
import numpy as np


class Sombras:
    def __init__(self,src):
       # src = "21.jpg"
        dim=(300,300)#Dimencao da imagem
        imagem = cv2.resize(src,dim,interpolation = cv2.INTER_AREA)#Troca a dimencao da imagem
        rgb_planes = cv2.split(imagem)
        result_planes = []
        result_norm_planes = []
        for plane in rgb_planes:
            dilated_img = cv2.dilate(plane, np.ones((100,100), np.uint8))
            bg_img = cv2.medianBlur(dilated_img, 21)
            diff_img = 255 - cv2.absdiff(plane, bg_img)
            norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
            result_planes.append(diff_img)
            result_norm_planes.append(norm_img)
        result_norm = cv2.merge(result_norm_planes)
        cv2.imwrite('Sample.jpg',result_norm)