
function removephoto(imageid) {
    const data = {
        'imageid':imageid,
    }
    console.log(data)
            
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            // if not safe, set csrftoken
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken",  getCookie('csrftoken'));
            }
        }
    });
            // Sending data from validation
    $.ajax({
        url : '/v1/adminstrator/dashboard/removepic/' ,
        type : "POST" ,
        data : {
            'getdata' : JSON.stringify(data)
        } ,
        dataType : 'json' ,
        success : function (res , status) {
        if (res.status == 200) {
            document.getElementById('image--' + res.image_id).remove();
        }            

        } ,
        error : function () {
            console.log('er')
            
        } ,
    })
}

function remove_inputs(num) {
    
    // remove div 
    document.getElementById("id_divInputs-"+ num).remove();

// objwehave mean id of the feild now we have 
    var objwehave = document.getElementById('objwehave').value;
    
// for updated objwehave 
    var objupdate = ''

// update obj we now we have prossecc 
    var idlist = objwehave.split('');
    for (let index = 0; index < idlist.length; index++) {
        const element = idlist[index];
        console.log(element);
        if (element !== num) {
            objupdate = objupdate + element
        }
    }

    // update hidden input 
    document.getElementById('objwehave').value = objupdate;
    document.getElementById('counter').value = document.getElementById('counter').value - 1;
}

function add_inputs(num) {
// objwehave mean id of the feild now we have 
    var objwehave = document.getElementById('objwehave').value;

// proccess for finding last feature.id 
    // conver str to list and reverse this array
    var idlist = objwehave.split('').reverse();
    var lastid = idlist[0]

// for updated objwehave 
    var objupdate = ''

// proccess for insert inputs

    var key_input = document.getElementById('id_keyInput' + '-' + lastid.toString()).value;    
    var value_input = document.getElementById('id_valueInput' + '-' + lastid.toString()).value;

    // if status equal true its mean inputs are not empty
    var status = false;
    if (key_input != '' && value_input != ''){
        status = true;
    }

    if (status == true) {
        const selectbox = document.getElementById('select_options-' + idlist[0]).innerHTML;
        new_number = parseInt(lastid) + 1 ;
        var features = '<div class="form-row mb-4 col-12" id="id_divInputs-'+ new_number +'">' +
                            '<div class="form-group mt-2" id="important-'+ new_number +'">'+
                                '<label class="switch s-icons s-outline  s-outline-primary mr-2">'+
                                    '<input name="important-'+ new_number +'" type="checkbox" >'+
                                    '<span class="slider round"></span>'+
                                '</label>'+
                            '</div>'+
                            '<div class="form-group col-md-3">' +
                                '<select name="FeatureCats-'+ new_number +'" id="select_options-'+ new_number +'" class=" form-control">'+
                                    selectbox+
                                '</select>'+
                            '</div>'+
                            '<div class="form-group col-md-3">' +
                                '<input type="text" id="id_keyInput-'+ new_number +'" name="key-'+ new_number +'" class="form-control"  placeholder=" کلیدواژه ">'+
                            '</div>'+
                            '<div class="form-group col-md-3">'+
                                '<input type="text" id="id_valueInput-'+ new_number +'" name="value-'+ new_number +'"  class="form-control"  placeholder=" مقدار ">'+
                            '</div>'+
                            '<span onclick="add_inputs('+ "'" +  new_number + "'" +')" class="btn btn-primary mb-2 ml-2 rounded-circle">'+
                                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-plus"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>'+
                            '</span>'+
                            '<span onclick="remove_inputs('+ "'" +  new_number + "'" +')" class="btn btn-danger mb-2 ml-2 rounded-circle">'+
                                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-minus"><line x1="5" y1="12" x2="19" y2="12"></line></svg>'+
                            '</span>'+
                        '</div>'
        $('#id_features').append(features);
        console.log('added');

        // update values in HTML
        counter = document.getElementById('counter').value ;
        document.getElementById('counter').value = parseInt(counter) + 1;
        idlist = idlist.reverse();
        idlist.push(new_number);
        for (let index = 0; index < idlist.length; index++) {
            const element = idlist[index];
            if (element >! num) {
                objupdate = objupdate + element
            }
            
        }
        document.getElementById('objwehave').value = objupdate;
    }

}