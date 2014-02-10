var nav = $('#navi');
var nav_offset = nav.offset();

$(window).on('scroll', function() {


    if($(window).scrollTop() > nav_offset.top) {
      nav.addClass('navi');
      nav.css({'top':'20px'});
    } 
    else{
      nav.removeClass('navi');      
    }
});


/*------- Funcionalidades para el Nav-Aside -> Jhon Medina -------*/
//Aun falta optimizarlo

$(".list_hija").eq(0).show();

if($('.list_hija').eq(0).height()<=184){
  $(".list_hija").eq(0).removeClass('scrollando');
  console.log("hata las patas");
}

else{
  $(".list_hija").eq(0).addClass('scrollando');
  console.log("jpder");
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




