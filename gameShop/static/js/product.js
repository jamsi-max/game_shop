$(function() {
    $(".product-text-buy").click(function(event){
    let target = event.target;
    $.ajax({
        url: "/basket/add/" + target.name + "/",
        success: function(data){
            if (!data.result){
                $('#modal').prop('checked', true);
                console.log(data.result)
            }else{
                $('.basket-block').html(data.result);
            }
        },
    });
    event.preventDefault();
 });
});
