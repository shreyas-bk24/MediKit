//remove item
$(document).ready(function(){
    $('.delete-btn').on('click',function(csrf_token){
        var id=$(this).attr('pro_id');
        req=$.ajax({
            url : '/delete_pro',
            type : 'POST',
            headers: {
                'X-CSRF-Token': csrf_token,
           },
            data : {
                pro_id : id,
            }
        });
        // access the parent element of the item clicked
        var pro_div=$(this).parent().parent().parent();
        pro_div.remove();
        alert("item is removed")
        });

    });

//update vendor
var csrf_token ="{{ csrf_token() }}";

$(document).ready(function(){
    $('.qty').on('change',function(csrf_token){
        var id=$(this).attr('pro_id');
        var qty=$(this).val();
        // var price=$(this).attr('price');
        console.log(qty)
        req=$.ajax({
            url : '/product_update',
            type : 'POST',
            headers: {
                'X-CSRF-Token': csrf_token, 
           },
            data : {
                pro_id : id,
                quantity : qty,
            }
        });
        alert("cart is updated"+qty);
    });
});