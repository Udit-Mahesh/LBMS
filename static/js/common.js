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

