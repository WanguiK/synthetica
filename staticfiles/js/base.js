$( document ).ready(function() {

    $('#id_project_name, #id_description, #id_records').addClass('form-control lato form-control-lg');
    $('label').addClass('label');
    $('#id_description').prop({
        'rows':3
    });

    var add_icon = '<span class="fa-stack fa-1x"><i class="far fa-circle fa-stack-2x"></i><i class="fas fa-plus fa-stack-1x"></i></span> Add Field / Attribute';

    $('.formset_row').formset({
        addText: add_icon,
        deleteText: 'remove',
        prefix: 'generate_set'
    });

    $('.add-row').addClass('muli');

});