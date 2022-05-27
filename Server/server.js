var express = require("express");
var app = express();
var server = require("http").Server(app);
var io = require("socket.io")(server);

var posicion = 0; //Posicion en decimal para los 5 dedos de la mano

var posanterior = 100;

app.use(express.static("public"));

io.on("connection", function (socket) {
  console.log("Alguien se ha conectado con Sockets");
  socket.emit("cambio_posicion", posicion);

  socket.on("pythonEmisor", function (data) {
    console.log(data);
    posicion = data;
    if(posanterior != posicion)
    {
      io.sockets.emit("cambio_posicion", posicion); 
      posanterior = posicion;
    }    
      
  });
  
});

server.listen(5000, function () {
  console.log("Servidor corriendo en http://localhost:5000");
});

