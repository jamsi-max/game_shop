$(function() {
    $(".basket-list, input[type=number]").change(function(event){
        console.log(1)
       let target = event.target;
       $.ajax({
           url:"/basket/update/" + target.name + "/" + target.value + "/",
           
           success: function(data) {
            //    console.log(data)
               $('.basket-list').html(data.result);
           },
       });

    //    event.preventDefault();
    });
});

// window.onload = function() {
//     $(".basket-list").on("change", "input[type=number]", function(event){
//        let target = event.target;
//        $.ajax({
//            url:"/basket/update/" + target.name + "/" + target.value + "/",
           
//            success: function(data) {
//                $('.basket-list').html(data.result);
//            },
//        });
//       event.preventDefault();
//     });
// }