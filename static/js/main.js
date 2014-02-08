
/*------- Funcionalidades para el Nav-Aside -> Jhon Medina -------*/
//Aun falta optimizarlo

$(".list_hija").eq(0).show();

$(".mi").eq(0).on("click", {id:0}, mostrar);
$(".mi").eq(1).on("click", {id:1}, mostrar);
$(".mi").eq(2).on("click", {id:2}, mostrar);


function mostrar(event){
   if(event.data.id==0){
      $(".list_hija").eq(0).toggle(250);
      $(".list_hija").eq(1).hide(250);
      $(".list_hija").eq(2).hide(250);
   }

   if(event.data.id==1){
      $(".list_hija").eq(1).toggle(250);
      $(".list_hija").eq(0).hide(250);
      $(".list_hija").eq(2).hide(250);
   }

   if(event.data.id==2){
      $(".list_hija").eq(2).toggle(250);
      $(".list_hija").eq(1).hide(250);
      $(".list_hija").eq(0).hide(250);
   }
};


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
$('#modal_content').on('mouseleave', {fuera:1}, fueraDentro);
$('#modal_content').on('mouseenter', {dentro:0}, fueraDentro);

function fueraDentro(valor){
   if(valor.data.fuera==1){                      //Fuera del modal
      $('#modal').click(function(){              //Al hacer click fuera del modal
         $(this).hide()                          //Ocultar modal
         $('body').css({'overflow':'visible'});  //Dejar visible el scroll del navegador
      });
   }

   if(valor.data.dentro==0){                     //Dentro del modal
      $('#modal').click(function(){              //Al hacer click dentro del modal
          $(this).show();                        //Dejar mostrado el modal                 
          $('body').css({'overflow':'hidden'});  //Ocultar el scroll del navegador
      });
   }
   
}
/*---------------------------------------------------------------------*/







