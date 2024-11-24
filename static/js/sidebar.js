$(".menu-bar").on("click", function(){
    $(".sidebar").addClass("active");
})

$(".logo").on("click", function(){
    $(".sidebar").removeClass("active");
})
