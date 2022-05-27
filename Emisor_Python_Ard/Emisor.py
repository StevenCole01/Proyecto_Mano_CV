import socketio
import time #Importar modulo para el manejo de tiempo
import serial #Importar modulo para comunicacion con puerto serial

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

serialArduino = serial.Serial(PUERTOSERIE, BAUDIOS) #Creacion del objeto serial para la comunicacion con el arduino emisor
time.sleep(1) #Tiempo de retardo
mov = ""
while True:
    mov = int(serialArduino.readline().decode("ascii"))#Lectrura y conversion de lo recivido por el puerto serieo
    sio.emit('pythonEmisor', mov)
    print(mov) #Imprime lo recibido por el puerto serie
    time.sleep(1)
   