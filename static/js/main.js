$(".list_hija").eq(0).show();


$("p").eq(0).on("click", {id:0}, mostrar);
$("p").eq(1).on("click", {id:1}, mostrar);
$("p").eq(2).on("click", {id:2}, mostrar);
$("p").eq(3).on("click", {id:3}, mostrar);


function mostrar(event){
	if(event.data.id==0){
		$(".list_hija").eq(0).toggle(500);
	}

	if(event.data.id==1){
		$(".list_hija").eq(1).toggle(500);
	}

	if(event.data.id==2){
		$(".list_hija").eq(2).toggle(500);
	}

	if(event.data.id==3){
		$(".list_hija").eq(3).toggle(500);
	}
};


$('.carousel').carousel({
	interval:3000
});

