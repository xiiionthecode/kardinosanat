function addFields(number) {
    var select = $('#inputFeatureType_'+number).val();
    var inputFeature = $('#inputFeature_'+number).val();
    var inputDescriptions = $('#inputDescriptions_'+number).val();
    if (select != 0 && inputFeature != '' && inputDescriptions != '') {
        var fieldNumber = 0
        fieldNumber = number + 1 ;
        $('#numberOfDetaileFileds').attr('value', fieldNumber)
        var featureTypeDIV = $('#inputFeatureType').html();

        var checkedparent = '<div class="form-group mt-2">'+
                                '<label class="switch s-icons s-outline  s-outline-primary  mb-4 mr-2">'+
                                    '<input type="checkbox"  name="inputImportant_'+fieldNumber+'"  id="inputImportant_'+fieldNumber+'" >'+
                                    '<span class="slider"></span>'+
                                '</label>'+
                            '</div>';

        var featureparent = '<div class="form-group col-md-3" id="featureTypeDIV">'+
                                '<select id="inputFeatureType_'+fieldNumber+'" name="type_'+fieldNumber+'" class="form-control">'+
                                    featureTypeDIV+
                                '</select>'+    
                            '</div>';

        var divhtml =   '<div class="form-row mb-4" id="detaileFieldsChild_'+fieldNumber+'">'+
                            checkedparent+
                            featureparent+
                            '<div class="form-group col-md-3">'+
                                '<input type="text" name="inputFeature_'+fieldNumber+'" class="form-control" id="inputFeature_'+fieldNumber+'" placeholder=" موضوع ">'+
                            '</div>'+
                            '<div class="form-group col-md-3">'+
                                '<input type="text" name="inputDescriptions_'+fieldNumber+'" class="form-control" id="inputDescriptions_'+fieldNumber+'" placeholder=" توضیح ">'+
                            '</div>'+
                            '<span class="btn btn-primary mb-2 ml-2 rounded-circle" onclick="addFields('+fieldNumber+')">'+
                                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-plus"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>'+
                            '</span>'+
                            '<span class="btn btn-danger mb-2 ml-2 rounded-circle" onclick="removeFields('+fieldNumber+')">'+
                                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-minus"><line x1="5" y1="12" x2="19" y2="12"></line></svg>'+
                            '</span>'+
                        '</div>';
        $('#detaileFields').append(divhtml)
    }else{
        alert('ابتدا فیلد های مربوط به توضیحات فنی اول را پر کنید .')
    }
    
    
}

function removeFields(number) {
    var fieldNumber = 0
    var fieldNumber = number - 1 ;
    var featureTypeDIV = $('#inputFeatureType').html();
    
    $('#detaileFieldsChild_'+number).remove()
    $('#numberOfDetaileFileds').attr('value', fieldNumber);

    
    
    
}

