$(document).on("ready", setup);
    $(document).on("ready", inicio);
    
    function setup(){
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
                    function getCookie(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '') {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++) {
                                var cookie = jQuery.trim(cookies[i]);
                                // Does this cookie string begin with the name we want?
                                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                    break;
                                }
                            }
                        }
                        return cookieValue;
                    }
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                }
                });
            }
    function inicio()
    {   
        $(".sub").on('click', {id:0}, mostrarProductos);
        $(".mi").on('click', {id:1}, mostrarProductos);    
        
    }
 
    function mostrarProductos(valor){

        if(valor.data.id==0){
            var info = $(this);
            var id = info.attr('id');
            console.log(id);

            $.ajax({
            url: "/ajax/ver_subcategoria/",
            type: "POST",
            data:{'id':id},
            success: function(data) {
                html = "";
                //console.log(data);
                for(i=0;i< data.length;i++){
                    html += "<div class='col-xs-3'id ='"+data[i].pk+"'>";
                    html += "<div class='img-thumbnail app_padding app-margenProducto'>";
                    html += "<div class='app_alinear'>";
                    html += "<h5 >"+data[i].fields.nombre+"</h5>";
                    html += "</div>";
                    html += "<div class='caja_imagen'>";
                    html += "<a href='#'><img src='{{MEDIA_URL}}"+data[i].fields.img+"' class='img-responsive img_producto'><span class='info'>Ver</span></a></div>";
                    html += "<div class='app_alinear app_centrar'>";
                    html += "<h5>"+ data[i].fields.precio+"</h5>";
                    html += "<form action=''>";
                    html += "<div class='app-div1'>";
                    html += "<input type='text' name='cantidad' id='cantidad' class='app_cantidad'>";
                    html += "</div>";
                    html += "<div class='app-div2'>";
                    html += "<input type='submit' name='agregar' id='agregar' value='Agregar' class='app_agregar'>"
                    html += "</div>";
                    html += "</form>";
                    html += "</div>";
                    html += "</div>";
                    html += "</div>";
                }
                
            $(".col-xs-9").html(html);
               
            },
            error: function(data){
                    console.log(data);
                    }
            });
        }

        else if(valor.data.id==1){
            var cat = $(this);                          //Seleccionando el mismo elemento de clase .mi
            var id_cat = cat.attr('id');                //Obtener el valor de id, de clase .mi

            $('.list_hija').eq(id_cat-1).toggle(500);   //Desplazando la clase .list_hija

            var tam = $('.list_hija').eq(id_cat-1).height();

            if(tam>184){
                $('.list_hija').eq(id_cat-1).addClass('scrollando');
            }

            else{
                console.log('no lo soy');
            }
        }

        
    }