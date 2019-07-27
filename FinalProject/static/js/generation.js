$(document).ready(function () {

    $('table').addClass('table table-bordered table-hover lato');
    $('table thead tr th:first-child').text('#');
    var m = 0;

    $('table tr td:first-child').each(function (index, value) {
        m++;
        $(this).text(m);
    });

    $('#export').click(function () {
        $('table').tableToCSV();
    });

});