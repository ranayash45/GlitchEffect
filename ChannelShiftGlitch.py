import cv2
import time
import random
img = cv2.imread(r'demo.jpg')
width = 500
height = round(width / img.shape[1] * img.shape[0])
img = cv2.resize(img,(width,height))
frame = img.copy()
n = 5
m = 5
start = time.time()
while True:
    end = time.time()
    elapsedtime = end - start
    if elapsedtime > 0.4:
        n = random.randint(0,25)
        m = random.randint(0,25)
        start = time.time()
    
    frame[:frame.shape[0] - n,:frame.shape[1] - m,0] = img[n:,m:,0] 
    frame[:frame.shape[0] - m,:frame.shape[1] - n,1] = img[m:,n:,1] 
    
    cv2.imshow('demo',frame)
    cv2.imwrite('ChannelShiftGlitch.jpg',frame)
    cv2.waitKey(100)