import cv2
img = cv2.imread('face.jpg')

character = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','|','\\']

width = 100
height = round(width / img.shape[1] * img.shape[0])
img = cv2.resize(img,(width,height))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

chrsrange = 0 
chrerange = len(character)
pfile = open("Pattern.txt","w")
for i in range(0,gray.shape[0]):
    line = ""
    for j in range(0,gray.shape[1]):
        line = line + " " + character[(int((gray[i,j] * (chrerange - chrsrange)/255) + chrsrange))]
    pfile.write(line+"\n")
    print(line)
pfile.close()