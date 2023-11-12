// Change input type between password and text 
function ChangePasswordInputType() {
    
    var eyeSvgType = $('#password').attr('type');
    if (eyeSvgType == 'password'){
        $('#password').attr('type', 'text')
    }else if (eyeSvgType == 'text') {
        $('#password').attr('type', 'password')
    }

}

// Checks if a string contains only numbers
function containsOnlyNumbers(str) {
    return /^\d+$/.test(str);
}


function login_button() {
    var phonenumber = document.getElementById("phoneNumber").value;
    var password = document.getElementById("password").value;
    if (containsOnlyNumbers(phonenumber) == true && phonenumber.length == 10) {
        if (password != '') {
            const data = {
                'phonenumber':phonenumber,
                'password':password,
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
                url : '/v1/adminstrator/login/valvalidation/' ,
                type : "POST" ,
                data : {
                    'getdata' : JSON.stringify(data)
                } ,
                dataType : 'json' ,
                success : function (res , status) {
                    console.log(res.status);
                    if (res.status == 200){
                        console.log(res.msg)
                        var alert = '<div class="alert alert-outline-success mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">تبریک!</strong> ' + res.msg + '</div>'
                        $('#validation_msg').append(alert);
                        window.location.href = "/v1/adminstrator/dashboard/";
                    }if (res.status == 500) {
                        console.log(res.msg)
                        var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + res.msg + '</div>'
                        $('#validation_msg').append(alert);
                    }
                    
                    
        
                } ,
                error : function () {
                    console.log('er')
                    
                } ,
            })
        }else{
            var msg = 'مقدار رمز عبور نمی توانند خالی باشد .'
            var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + msg + '</div>'
            $('#validation_msg').append(alert);
        }
        

    }else{
        var msg = 'شماره تلفن وارد شده صحیح نمی باشد .' 
        var alert = '<div class="alert alert-outline-danger mb-4" role="alert"> <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x close" data-dismiss="alert"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg></button><i class="flaticon-cancel-12 close" data-dismiss="alert"></i> <strong id="msg">خطا!</strong> ' + msg + '</div>'
        $('#validation_msg').append(alert);
    }
    
}
