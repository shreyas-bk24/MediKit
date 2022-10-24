var csrf_token ="{{ csrf_token() }}";

$(document).ready(function(){
    $('.add-to-cart').on('click',function(csrf_token){
        var id=$(this).attr('value');
        var qty=1;
        
        req=$.ajax({
            url : '/addCart',
            type : 'POST',
            headers: {
                'X-CSRF-Token': csrf_token, 
           },
            data : {
                pro_id : id,
                quantity : qty,
            }
        });
        alert("Item is added to cart")
    });
});
// to change the color of the button after a click
// var change=()=>{
//     alert('linked')
// document.getElementById('add-to-cart').onclick=function() {
//     document.getElementById('add-to-cart').style.backgroundColor = "green"; 
//     document.cookie = "pressed=true";
//   };
// }
