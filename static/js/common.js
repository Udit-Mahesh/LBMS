<<<<<<< HEAD
function callApi(method,url,data){
    $.ajax({
        type:method,
        url:url,
        data:data,
        contentType:'application/json',
        error:(xhr)=>{
            alert(xhr.responseJSON?.message || 'An unknown error occured');
        }
    }).done(()=>{
        window.location.reload();
    })
}

=======
function callApi(method,url,data){
    $.ajax({
        type:method,
        url:url,
        data:data,
        contentType:'application/json',
        error:(xhr)=>{
            alert(xhr.responseJSON?.message || 'An unknown error occured');
        }
    }).done(()=>{
        window.location.reload();
    })
}

>>>>>>> 021fdf591c973b00f047735ae9a78bf0621bacba
