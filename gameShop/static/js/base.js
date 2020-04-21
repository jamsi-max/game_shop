$(function() {

    $("#loginButton").click(function(event){
        let csrfSerialaze = $("#loginForm").serialize();
        // console.log(csrfSerialaze)
    $.ajax({
        url: $("#loginForm").data('url'),
        type: "post",
        data: csrfSerialaze,
        success: function(data){
            if (!data.result){
                $('.form-login-errors').text(data.error.__all__[0].split('.')[0])
            }else{
                console.log(data.result)
                $(".main-menu").html(data.result);
                $("#modal").prop('checked', false);
            }
        },
    });

    event.preventDefault();
  });
});