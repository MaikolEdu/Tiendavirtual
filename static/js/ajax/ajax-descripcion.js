$(document).on("ready", inicio);

function inicio()
{
   $(".carrito").on("click",añadircarrito);
}
function añadircarrito()
{
    var cantidad = $("#cantidad").val();
    var producto_id=$(this).val();
    
    console.log(cantidad)
    console.log(producto_id)

      $.ajax({
        data:{'producto_id':producto_id,'cantidad':cantidad},
        type:"post",
        url:'/ajax_carrito/',
        success: function (data)
        {
         console.log(" "+data["nombre"]+" "+data["precio"]);
        }
      });
    
}