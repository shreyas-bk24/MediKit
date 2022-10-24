$(document).ready(function(){
    $('.resolve').on('click',function(csrf_token){
        var id=$(this).attr('comp_id');
        confirm("Marked as resolved");
        req=$.ajax({
            url : '/resolve',
            type : 'POST',
            headers: {
                'X-CSRF-Token': csrf_token, 
           },
            data : {
                comp_id : id,
            }
        });
    });
});