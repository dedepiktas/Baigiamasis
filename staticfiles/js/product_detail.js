$(document).on('click', '#add-button', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: add_to_cart_url,
        data: {
            product_id: $('#add-button').val(),
            product_quantity: $('#select option:selected').text(),
            csrfmiddlewaretoken: csrf_token,
            action: 'post'
        },
        success: function(json){
            document.getElementById("cart-qty").textContent = json.qty;
        },
        error: function(xhr, errmsg, err){
            // Handle error
        }
    });
});

// Initialize the carousel
$(document).ready(function(){
    $('#comments-carousel').carousel({
        interval: 2000
    });
});
