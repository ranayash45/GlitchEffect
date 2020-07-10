import cv2
import random
import os
import numpy as np
img = cv2.imread('demo.jpg')
frame = cv2.resize(img,(512,512))
isLine = False
while True:
    data = frame.copy()
    noiseM1 = bytearray(os.urandom(675))
    noiseM1 = np.array(noiseM1,np.ubyte)
    noiseM1 = noiseM1.reshape(15,15,3)
    noiseM1 = cv2.resize(noiseM1,(512,512))
    box = np.zeros((512,512,3),dtype=np.ubyte)
    if isLine:
        for i in range(0,100):
            line = random.randint(0,frame.shape[0] - 1)    
            data[line,:,:] = noiseM1[line,:,:]
    else:
        box[:,:,2] = (data[:,:,0] + noiseM1[:,:,1]) / 2
        box = np.asarray((np.asarray(box,np.int)  + np.asarray(frame,np.int)) / 2 , np.ubyte)
        
    cv2.imshow('demo',box)
    cv2.waitKey(50)