$( document ).ready(function() {

    setTimeout(function(){
        window.location.href = 'http://127.0.0.1:8000/synthetica/workspace/';
    }, 5000);

    $('input[type=text]:nth-child(2)').addClass('form-control');
    $('input[type=text]:nth-child(3)').addClass('form-control');
    $('textarea:nth-child(1)').addClass('form-control');

});