$( document ).ready(function() {

    setTimeout(function(){
        // window.location.href = 'http://127.0.0.1:8000/synthetica/workspace/';
        window.location.href = 'http://syntheticaa.herokuapp.com/synthetica/workspace/';
    }, 10000);

    $('input[type=text]:nth-child(2)').addClass('form-control');
    $('input[type=text]:nth-child(3)').addClass('form-control');
    $('textarea:nth-child(1)').addClass('form-control');

});