
/*------- Funcionalidades para el Nav-Aside -> Jhon Medina -------*/

//--> Funcionalidad para poder mantener el Nav-aside fixed
var nav = $('#navi');                               //Seleccionando elemento de id #navi
var nav_offset = nav.offset();                      //Obteniendo las cordenadas, left y top del elemento

$(window).on('scroll', function() {                 //Disparando evento scroll a nuestra ventana

    if($(window).scrollTop() > nav_offset.top)      //Comparando la posión del scroll con, la coordenada top
    {                                               //... del nav_offset en pixeles, si ...
      nav.addClass('navi');                         //Le agregamos la clase .navi al elemento de id #navi
      nav.css({'top':'20px'});                      //Ubicamos ese mismo elemento con top de 20px
    } 
    else{                                           //si no ...
      nav.removeClass('navi');                      //Quitarle la clase .navi al elemento de id #navi
    }
});

//--> Mostrando por Defecto en Nav-Aside
var selecc_defecto = $(".list_hija").eq(0);         //Seleccionando la primera .list_hija
var tam_list = selecc_defecto.height();             //Obtener el tamaño del elemento seleccionado

selecc_defecto.show();                              //La primera .list_hija se mostrará por defecto

if(tam_list<=184){                                  //Si el tamaño de .list_hija es menor/igual que 184
  $(".list_hija").eq(0).removeClass('scrollando');  //A esta primera .list_hija, le removemos la clase
}                                                   //... scrollando, y no mostrara scroll para esa seccion  
else{                                               //Si no ...
  $(".list_hija").eq(0).addClass('scrollando');     //Le agregamos la clase scrollando
}





$(".mi").eq(0).on("mouseover", {id:0}, mostraricono);
$(".mi").eq(1).on("mouseover", {id:1}, mostraricono);
$(".mi").eq(2).on("mouseover", {id:2}, mostraricono);

function mostraricono(event){
   if(event.data.id==0){
      $(".sh").eq(0).show(250);
      $(".sh").eq(1).hide(250);
      $(".sh").eq(2).hide(250);
   }

   if(event.data.id==1){
      $(".sh").eq(1).show(250);
      $(".sh").eq(2).hide(250);
      $(".sh").eq(0).hide(250);
   }

   if(event.data.id==2){
      $(".sh").eq(2).show(250);
      $(".sh").eq(1).hide(250);
      $(".sh").eq(0).hide(250);
   }
}
/*------------------------------------------------------------------------*/

/*------------ Funcionalidades para el Modal -> Jhon Medina ------------*/

//--> Mostrar el Modal para el carrito
$('#enlace_modal').on('click', mostrarModal);    //Click sobre el enlace, llama a función mostrarModal

function mostrarModal(){
   $('#modal').show();                           //Muestra el modal primera vez
   $('body').css({'overflow-y':'hidden'});       //Oculta el scroll del navegador
}

//--> Ocultar el Modal para el carrito
$('#modal').click(function(){                    //por defecto ocultar al hacer click en modal
   $(this).hide(); 
   $('body').css({'overflow':'visible'});
}); 

$('#modal_content').on('mouseleave', {id:1}, fueraDentro);
$('#modal_content').on('mouseup', {id:0}, fueraDentro);

function fueraDentro(valor){
   if(valor.data.id==1){                         //Fuera del modal
      console.log(valor.data.id);
      $('#modal').click(function(){              //Al hacer click fuera del modal
         $(this).hide()                          //Ocultar modal
         $('body').css({'overflow':'visible'});  //Dejar visible el scroll del navegador
      });
   }

   if(valor.data.id==0){                         //Dentro del modal
      console.log(valor.data.id);
      $('#modal').click(function(){              //Al hacer click dentro del modal
          $(this).show();                        //Dejar mostrado el modal                 
          $('body').css({'overflow':'hidden'});  //Ocultar el scroll del navegador
      });
   }
   
}
/*---------------------------------------------------------------------*/


$('#miemail').click(function(){
  $('#text_nombre').show(250);
});




