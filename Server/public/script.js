var socket = io.connect("http://187.250.90.30:5000", { forceNew: true });



socket.on("cambio_posicion", function (data) {

    x =  Number(data)
    envio = x.toString(2).split("");
    if (envio.length !=5){
      while(envio.length !=5 ){
        envio.unshift("0")
      }
    } 
    if (envio[4] == 1){ //Pulgar
      $("#dedo0").addClass("ani")
      $("#rcorners2").addClass("ani")
    }else{
      $("#dedo0").removeClass("ani")
      $("#rcorners2").removeClass("ani")
    }
    if (envio[3] == 1){ //Indice
      $("#dedo1").addClass("ani")
    }else{
      $("#dedo1").removeClass("ani")
    }
    if (envio[2] == 1){ //Medio
      $("#dedo2").addClass("ani")
    }else{
      $("#dedo2").removeClass("ani")
    }
    if (envio[1] == 1){ //Anular
      $("#dedo3").addClass("ani")
    }else{
      $("#dedo3").removeClass("ani")
    }
    if (envio[0] == 1){ //Meniq
      $("#dedo4").addClass("ani")
    }else{
      $("#dedo4").removeClass("ani")
    }
    if ( x == 31 ){
      $("#rcorners1").addClass("ani")
    }else{
      $("#rcorners1").removeClass("ani")
    }





    
    console.log(envio); // '101010'
});
