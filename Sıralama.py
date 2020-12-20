import numpy as np
import pandas as pd 
import cv2
import pytesseract
from PIL import ImageGrab
import time
from numpy import savetxt
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
img = cv2.imread('bir.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


boxes= pytesseract.image_to_data(img)

# print(boxes)


  #b  listeliyerek b sütün boxes.splitlines yaparak ise liste içerisinde ki satırları parçalıyoruz a da sayaç işlevinde 
for a,b in enumerate(boxes.splitlines()):
        # print(b)
        if a!=0:
            b = b.split()
            if len(b)==12:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                c=print(b[11])
                c=cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
                
                
                




cv2.imshow('img', img)
cv2.waitKey(0)




# boxes=pytesseract.image_to_data(img)

#Harf harf tespit
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b=b.split()
#         print(b)
#         if len(b)==12:
#               x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
# # hImg, wImg,_ = img.shape
# # boxes = pytesseract.image_to_boxes(img)
# # for b in boxes.splitlines():
# #     print(b)
# #     b = b.split(' ')
# #     print(b)
# #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
# #     cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 1)
# #     cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

