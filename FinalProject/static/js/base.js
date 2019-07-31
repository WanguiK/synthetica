$(document).ready(function () {

    $('#id_project_name, #id_description, #id_records').addClass('form-control lato form-control-lg');
    $('label').addClass('label');
    $('#id_description').prop({
        'rows': 5
    });

    var add_icon = '<span class="fa-stack fa-2x"><i class="far gradient fa-circle fa-stack-2x"></i><i class="fas gradient fa-plus fa-stack-1x"></i></span> Add Field / Attribute';

    var delete_icon = '<i class="far fa-3x gradient fa-times-circle text-center"></i>';

    $('.formset_row').formset({
        addText: add_icon,
        deleteText: delete_icon,
        prefix: 'generate_set'
    });

    $('.add-row').addClass('muli');

    var instruction = '<p class="instruction lato"><span><strong>Guide:<br></strong></span>Textual input is expected</p>';
    $('table tbody tr:nth-child(1) td textarea').after(instruction);

    var child = $('tbody .formset_row').length;
    console.log('Initially we have '+child+' number of rows');
    $('.add-row').click(function(){
        child ++;
        console.log('There are '+child+' table rows now');
        addGuide(child);
    });
    function addGuide(c) {
        $('tbody tr:nth-child('+c+') td textarea').after(instruction);
    }

    var data_type, title, guide, which;
    var randint = ['age', 'medu', 'fedu', 'famrel', 'traveltime', 'studytime', 'failures', 'freetime', 'walc', 'dalc', 'health', 'absences', 'g1', 'g2', 'g3'];
    var choices = ['sex', 'address', 'pstatus', 'mjob', 'fjob','guardian', 'famsize', 'reason', 'schoolsup', 'famsup','activities', 'paidclass', 'internet'];

    $('tbody').on('change', 'tr td select', function() { 
        // title = $(this).find('option:selected').text();
        data_type = $(this).find('option:selected').val();
        $(this).parent().parent().find('input[type=text]').val(data_type);
        if (choices.includes(data_type)) {
            guide = 'Input text values separated by commas<br><span>Example:<strong> yes,no,maybe</strong></span>';
            $(this).parent().parent().find('.instruction').html(guide);
        } else if (randint.includes(data_type)) {
            guide = 'Input number range values (digits) separated by commas<br><span>Example:<strong> 15,22</strong></span>';
            $(this).parent().parent().find('.instruction').html(guide);
        }
    });

    // Tour
    var tour = new Trip([
        { 
            sel : $('#id_project_name'), 
            content : 'Create a project with a custom project name', 
            position : 's'
        },
        { 
            sel : $('#id_description'), 
            content : 'Add a project description for the project', 
            position : 'n' 
        },
        { 
            sel : $('#id_records'), 
            content : 'Specify the number of records required in the artificial dataset', 
            position : 'n' 
        },
        { 
            sel : $('#id_generate_set-0-data_type'), 
            content : 'Select the type of data you want to generate.', 
            position : 's' 
        },
        { 
            sel : $('#id_generate_set-0-field_name'), 
            content : 'Add a field name. This will also be used as a header.', 
            position : 's' 
        },
        { 
            sel : $('#id_generate_set-0-options'), 
            content : 'Specify the data options or range of values to be used in generating the dataset.', 
            position : 's' 
        },
        { 
            sel : $('.delete-row'), 
            content : 'Click to delete this field.', 
            position : 's' 
        },
        { 
            sel : $('.add-row'), 
            content : 'Click to add a field', 
            position : 'n' 
        },
        { 
            sel : $('input[type=submit]'), 
            content : 'Click to generate the dataset', 
            position : 'n' 
        }
    ], {
        delay: -1,
        showNavigation : true,
        showCloseBox : true,
        tripTheme: 'white',
        showHeader: true,
    });
      
    $('#help').on('click', function() {
        tour.start();
    });

    // tour.start();


});