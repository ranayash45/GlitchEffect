import cv2
import random
img = cv2.imread('demo.jpg')
img = cv2.resize(img,(512,512))
frame = img.copy()
while True:
    for i in range(0,100):
        n = random.randint(0,img.shape[0] - 1)
        shift_n = random.randint(0,20)
        color_channel = random.randint(0,2)
        frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
    cv2.imshow('demo',frame)
    cv2.waitKey(50)