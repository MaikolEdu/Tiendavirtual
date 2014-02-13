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

    function inicio(){
        $("#suscribirse").on('click',suscribete);
    }

        function suscribete(){
            var info = $('#miemail').val();
            var nom = $('#text_nombre').val();

            $.ajax({
            url: "ajax/suscribirse/",
            type: "POST",
            data:{'email':info,'nombre':nom},
             success: function(data) {
                //$('#ventana-mensaje').html("<div class='app_margen1'>Gracias Porsu Registro </div>");
                 alert("Felicidades gracias por suscribirse");
                 
             },
 
             error: function(data){
                     console.log("Verifica su email o usuario");
             }
           });
         }