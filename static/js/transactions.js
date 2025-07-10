<<<<<<< HEAD
$('#borrow-book-save').click(()=>{
    let data=$('#borrowForm').serializeArray();
    let requestPayload={
        book_id:data[0].value,
        member_id:data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/borrowBook',JSON.stringify(requestPayload));
});

$('#return-book-save').click(()=>{
    let data=$('#returnForm').serializeArray();
    let requestPayload={
        book_id : data[0].value,
        member_id : data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/returnBook',JSON.stringify(requestPayload));
=======
$('#borrow-book-save').click(()=>{
    let data=$('#borrowForm').serializeArray();
    let requestPayload={
        book_id:data[0].value,
        member_id:data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/borrowBook',JSON.stringify(requestPayload));
});

$('#return-book-save').click(()=>{
    let data=$('#returnForm').serializeArray();
    let requestPayload={
        book_id : data[0].value,
        member_id : data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/returnBook',JSON.stringify(requestPayload));
>>>>>>> 021fdf591c973b00f047735ae9a78bf0621bacba
})