import socketio
import time #Importar modulo para el manejo de tiempo
import serial #Importar modulo para comunicacion con puerto serial

sio = socketio.Client() #Creacion del socket

pos = 0 #Posicion de la mano

#Definicion de las variables necesarias
PUERTOSERIE = "COM7"
BAUDIOS = 9600
IPSERVER = "187.250.90.30" #IP del server
PUERTOSERVER = "5000"

sio.connect('http://' + IPSERVER + ':' + PUERTOSERVER)

serialArduino = serial.Serial(PUERTOSERIE, BAUDIOS)
time.sleep(1)

@sio.event
def connect():
    print("Conexion establecida")

@sio.on('cambio_posicion')
def on_message(data):
    pos = data
    print("Cambio de posicion recibido: " + str(pos))
    serialArduino.write(pos.encode("ascii"))

@sio.event
def disconnect():
    print('disconnected from server')
  