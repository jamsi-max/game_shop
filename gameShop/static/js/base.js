let logout = function(){
    $(".auth-logout-link").click(function(event){
        $.ajax({
            url: "/auth/logout/",
            success: function(data){
                if (data.result){
                    $(".main-menu").html(data.result);
                }
            },
        });
    event.preventDefault();
    });
};

$(function() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    $('.auth').on('click', "#loginButton", function(event){
        let csrfSerialaze = $("#loginForm").serialize();
        $.ajax({
            url: $("#loginForm").data('url'),
            type: "post",
            data: csrfSerialaze,
            success: function(data){
                if (!data.result){
                    $('.form-login-errors').text(data.error.__all__[0].split('.')[0])
                }else{
                    $(".main-menu").html(data.result);
                    $("#modal").prop('checked', false);
                    $('input[name="csrfmiddlewaretoken"]').val(getCookie('csrftoken'));
                    logout();
                }
            },
        });
    event.preventDefault();
    });

    logout();
});