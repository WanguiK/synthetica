$( document ).ready(function() {

    $('#id_project_name, #id_description, #id_records').addClass('form-control lato form-control-lg');
    $('label').addClass('label');
    $('#id_description').prop({
        'rows':5
    });

    var add_icon = '<span class="fa-stack fa-2x"><i class="far gradient fa-circle fa-stack-2x"></i><i class="fas gradient fa-plus fa-stack-1x"></i></span> Add Field / Attribute';

    var delete_icon = '<i class="far fa-3x gradient fa-times-circle text-center"></i>';

    $('.formset_row').formset({
        addText: add_icon,
        deleteText: delete_icon,
        prefix: 'generate_set'
    });

    $('.add-row').addClass('muli');

});