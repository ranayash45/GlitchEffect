import cv2
import random
import os
import numpy as np
img = cv2.imread('demo.jpg')
width = 500
height = round(width / img.shape[1] * img.shape[0])
frame = cv2.resize(img,(width,height))
isLine = False
noisex = 125
noisey = 125
noisechannel = 3
while True:
    data = frame.copy()
    noiseM1 = bytearray(os.urandom(noisex * noisey * noisechannel))
    noiseM1 = np.array(noiseM1,np.ubyte)
    noiseM1 = noiseM1.reshape(noisey,noisex,noisechannel)
    noiseM1 = cv2.resize(noiseM1,(width,height))
    box = np.zeros((width,height,3),dtype=np.ubyte)
    #print(box.shape,frame.shape)
    if isLine:
        for i in range(0,100):
            line = random.randint(0,frame.shape[0] - 1)    
            data[line,:,:] = noiseM1[line,:,:]
    else:
        box = np.asarray((np.asarray(noiseM1,np.int) + np.asarray(frame,np.int) * 2) / 3, np.ubyte)
        
    cv2.imwrite('MatrixGlitch.jpg',box)
    cv2.imshow('demo',box)
    cv2.waitKey(50)