var csrf_token ="{{ csrf_token() }}";

$(document).ready(function(){
    $('.qty').on('change',function(csrf_token){
        var id=$(this).attr('pro_id');
        var qty=$(this).val();
        // var price=$(this).attr('price');
        console.log(qty)
        req=$.ajax({
            url : '/updateCart',
            type : 'POST',
            headers: {
                'X-CSRF-Token': csrf_token, 
           },
            data : {
                pro_id : id,
                quantity : qty,
            }
        });
        updateTotal(this)
        alert("cart is updated"+qty);
    });
});

// remove item from cart
$(document).ready(function(){
    $('.remove').on('click',function(csrf_token){
        var id=$(this).attr('value');
        req=$.ajax({
            url : '/removeFromCart',
            type : 'POST',
            headers: {
                'X-CSRF-Token': csrf_token, 
           },
            data : {
                pro_id : id,
            }
        });
        // access the parent element of the item clicked
        var pro_div=$(this).parent().parent();
        pro_div.remove();
        alert("item is removed")
        });
        
    });

fadeTime=10;

    function updateTotal(qty){
        var productRow = $(qty).parent().parent();
        // var price = productRow.children().last().children('.price').text();
        var price = $(qty).attr('price')
        var quantity = $(qty).val();
        var linePrice = price * quantity;
        console.log(price,quantity,linePrice)

// update the total price
        productRow.children().last().children('.price').each(function () {
            $(this).fadeOut(fadeTime, function () {
              $(this).text(linePrice.toFixed(2));
              recalculateCart();
              $(this).fadeIn(fadeTime),function(){
                 $(this).text==total;
              };
            });
          });
    }

// update the checkout total

function recalculateCart() {
    var subtotal = 0;
  
    /* Sum up row totals */
    $(".price").each(function () {
      subtotal +=parseFloat($(this).parent().parent().children().last().children('.price').text())
    });
  
    /* Calculate totals */
    var shipping = 40;
    var total = subtotal + shipping;
  
    /* Update totals display */
    $("#g_total").fadeOut(fadeTime, function () {
        $('#g_total').fadeIn(fadeTime,function(){
            $(this).html(total.toFixed(2))
        })
      $("#total").html(subtotal.toFixed(2));
      $(this).html(total.toFixed(2));
      if(subtotal==0){
        total=0
      }
    });
  }
