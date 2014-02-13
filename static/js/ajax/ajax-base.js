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
           
             $(".item").on("click",eliminaritem);

        }
        function eliminaritem()
        {
            var item_id=$(this).val();
            var $this=$(this);
            console.log(item_id)
            $.ajax({
                data:{'item_id':item_id},
                type:"post",
                url:'/ajax_eliminaritem/',
                success: function(data) {
                    console.log(data);
                    var ojo = $this.parent().parent().hide();
                    console.log(ojo);
                },
                error: function(data){
                    console.log(data);
                }
              });
            
        }
