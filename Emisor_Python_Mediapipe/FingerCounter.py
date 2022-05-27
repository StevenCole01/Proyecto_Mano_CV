import cv2
import time
import os
import HandTrackingModule as htm

import socketio

##################################################################################
sio = socketio.Client() #Creacion del socket

@sio.event
def connect():
    print("Conexion establecida")

@sio.event
def disconnect():
    print('disconnected from server')

#Definicion de las variables necesarias
PUERTOSERIE = "COM7"
BAUDIOS = 9600
IPSERVER = "187.250.90.30" #IP del server
PUERTOSERVER = "5000"
    
sio.connect('http://' + IPSERVER + ':' + PUERTOSERVER)
time.sleep(1) #Tiempo de retardo
##################################################################################          

wCam, hCam = 640, 480
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
 
detector = htm.handDetector(detectionCon=0.75)
 
tipIds = [4, 8, 12, 16, 20]

flag = True
 
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)
 
    if len(lmList) != 0:
        fingers = []
 
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
 
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
 
        print(fingers)
        totalFingers = fingers.count(1)
        #print(totalFingers)

        mov = 0
    
        dedos = fingers
        if dedos[0] == 1:
            mov += 1
        if dedos[1] == 1:
            mov += 2
        if dedos[2] == 1:
            mov += 4
        if dedos[3] == 1:
            mov += 8
        if dedos[4] == 1:
            mov += 16
        sio.emit('pythonEmisor', mov)
        print(mov) #Imprime lo recibido por el puerto serie
 
        #cv2.rectangle(img, (5, 225), (85, 212), (0, 255, 0), cv2.FILLED)
        #cv2.putText(img, str(totalFingers), (10, 375), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 25)
 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
 
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)