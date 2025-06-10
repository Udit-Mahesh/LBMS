$('#add-book-save').click(()=>{
    let data=$('#addBookForm').serializeArray();
    let requestPayload={
        book_name : data[0].value,
        author : data[1].value,
        publisher : data[2].value
    };
    callApi('POST','http://127.0.0.1:5000/addBook',JSON.stringify(requestPayload));
});

$('#delete-book-save').click(()=>{
    let data=$('#deleteBookForm').serializeArray();
    let requestPayload={
        book_id:data[0].value,
        book_name:data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/deleteBook',JSON.stringify(requestPayload));
});

