`use strict`
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
                    let err = Object.keys(data.error)
                    $('.form-login-errors').text(data.error[err[0]]);
                }else{
                    $(".main-menu").html(data.result);
                    $("#modal").prop('checked', false);
                    $('input[name="csrfmiddlewaretoken"]').val(getCookie('csrftoken'));
                    logout();
                    $('.form-login-errors').text('');
                }
            },
        });
    event.preventDefault();
    });

    logout();

    $('.product-category-menu').on('click', ".product-category-menu-item", function(event){
        let elm = document.querySelector(".menu-list-active");
        elm.classList.remove('menu-list-active');
        event.target.classList.add("menu-list-active");
        $.ajax({
            url: $(event.target).data('url'),
            success: function(data){
                if (!data.result){
                    $(".product-items-block").text(' No products ');
                }else{
                    $(".product-items-block").html(data.result);
                }
            },
        });
    event.preventDefault();
    });
   

    $('.product-category-menu').on('click', ".product-category-menu-item", function(event){

        $.ajax({
            url: $(event.target).data('url'),
            success: function(data){
                if (!data.result){
                    $(".product-items-block").text(' No products ');
                }else{
                    $(".product-items-block").html(data.result);
                }
            },
        });
    event.preventDefault();
    });


});