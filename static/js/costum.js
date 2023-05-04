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


function filter_product(){
    const filter_price = $("#sl2").val().split(',')
    const start_price = filter_price[0]
    const end_price = filter_price[1]
    $("#start_price").val(start_price)
    $("#end_price").val(end_price)
    $("#form_filter").submit()
}

function change_page(page){
    $("#page_filter").val(page)
    $("#form_filter").submit()
}

function changeImage(src){
    $("#product_image_gallery").attr('src',src)
}