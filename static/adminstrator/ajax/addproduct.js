function checkvalue(key_input, value_input) {
    var status = false;    

    if (key_input != '' && value_input != ''){
        status = true;
    }

    return status;
}



function add_inputs(number) {
    
    var key_input = document.getElementById('id_keyInput' + '-' + number.toString()).value;    
    var value_input = document.getElementById('id_valueInput' + '-' + number.toString()).value;
    
    var status = checkvalue(key_input, value_input);
    if (status == true) {
        const selectbox = document.getElementById('inputFeatureCats-1').innerHTML;
        console.log(selectbox)
        new_number = number + 1 ;
        var features = '<div class="form-row mb-4 col-12" id="id_divInputs-'+ new_number +'">' +
                            '<div class="form-group mt-2" id="important-'+ new_number +'">'+
                                '<label class="switch s-icons s-outline  s-outline-primary mr-2">'+
                                    '<input name="important-'+ new_number +'" type="checkbox">'+
                                    '<span class="slider round"></span>'+
                                '</label>'+
                            '</div>'+
                            '<div class="form-group col-md-3" id="FeatureCats">' +
                                '<select name="FeatureCats-'+ new_number +'" id="inputFeatureCats-'+ new_number +'" class="selectpicker form-control"  data-live-search="true">'+
                                    selectbox +
                                '</select>'+
                            '</div>'+
                            '<div class="form-group col-md-3">' +
                                '<input type="text" id="id_keyInput-'+ new_number +'" name="key-'+ new_number +'" class="form-control"  placeholder=" کلیدواژه ">'+
                            '</div>'+
                            '<div class="form-group col-md-3">'+
                                '<input type="text" id="id_valueInput-'+ new_number +'" name="value-'+ new_number +'"  class="form-control"  placeholder=" مقدار ">'+
                            '</div>'+
                            '<span onclick="add_inputs('+ new_number +')" class="btn btn-primary mb-2 ml-2 rounded-circle">'+
                                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-plus"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>'+
                            '</span>'+
                            '<span onclick="remove_inputs('+ new_number +')" class="btn btn-danger mb-2 ml-2 rounded-circle">'+
                                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-minus"><line x1="5" y1="12" x2="19" y2="12"></line></svg>'+
                            '</span>'+
                        '</div>'
        $('#id_features').append(features);
        console.log('added');
        document.getElementById('counter').value = new_number;

    }

}


function remove_inputs(number) {

    $('#id_divInputs-'+ number).remove()
    document.getElementById("id_divInputs-"+ number).remove();

}