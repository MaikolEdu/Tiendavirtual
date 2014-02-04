
/*********************************/
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







