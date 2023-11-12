        
window.onload = function() {
    var tagid = $('#tagid').attr('data-value');
    $('#'+tagid).attr('data-active','true');
    $('#'+tagid).attr('data-toggle','collapse');
    $('#'+tagid).attr('aria-expanded','true');

    var submenu = $('#submenu').attr('data-value');
    if (submenu == 'true') {
        $('.catandtype').addClass('show');
        var active = $('#whichone').attr('data-value');
        $('#'+active).addClass('active');
    }
    
    
};
