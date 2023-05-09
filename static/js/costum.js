function add_comment(articleId) {
    let message = $('#message').val()
    let parent_id = $("#parent_id").val()
    $.get('/article/add_comment/', {
        message: message,
        article_id: articleId,
        parent_id: parent_id,
    }).then(res => {
        $("#message_box").html(res)
        $("#message").val('')
        if (parent_id !== null && parent_id !== '') {
            document.getElementById("parent_comment_" + parent_id).scrollIntoView({behavior: 'smooth'});
        } else {
            document.getElementById("message_box").scrollIntoView({behavior: 'smooth'});
        }
    })
}


function get_parent(parentId) {
    document.getElementById("comment_box").scrollIntoView({behavior: 'smooth'});
    $("#parent_id").val(parentId)
}


function filter_product() {
    const filter_price = $("#sl2").val().split(',')
    const start_price = filter_price[0]
    const end_price = filter_price[1]
    $("#start_price").val(start_price)
    $("#end_price").val(end_price)
    $("#form_filter").submit()
}

function change_page(page) {
    $("#page_filter").val(page)
    $("#form_filter").submit()
}

function changeImage(src) {
    $("#product_image_gallery").attr('src', src)
}


function addToOrder(productId) {
    const count = $("#product_count").val();

    $.get('/order/add-to-order?productId=' + productId + '&count=' + count).then(res => {
        const status = res.status
        Swal.fire({
                text: res.text,
                icon: res.icon,
                confirmButtonText: res.button
            }
        ).then((result) => {
            if (status === 'not_auth') {
                if (result.isConfirmed===true) {
                    window.location.href = '/login'
                }
            }
        })
    })
}

function remove_order(id){
    $.get('/order/remove_basket?id='+id).then(res=>{
        $("#basket_content").html(res.body)
    })
}
function decrease_order(id){
    $.get('/order/decrease?id='+id).then(res=>{
        $("#basket_content").html(res.body)
    })
}
function increase_order(id){
    $.get('/order/increase?id='+id).then(res=>{
        $("#basket_content").html(res.body)
    })
}