<<<<<<< HEAD
$('#add-member-save').click(()=>{
    let data=$('#addMemberForm').serializeArray();
    let requestPayload={
        member_name:data[0].value,
        email:data[1].value,
        phone_no:data[2].value
    };
    callApi('POST','http://127.0.0.1:5000/addMember',JSON.stringify(requestPayload));
});

$('#delete-member-save').click(()=>{
    let data=$('#deleteMemberForm').serializeArray();
    let requestPayload={
        member_id:data[0].value,
        member_name:data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/deleteMember',JSON.stringify(requestPayload));
=======
$('#add-member-save').click(()=>{
    let data=$('#addMemberForm').serializeArray();
    let requestPayload={
        member_name:data[0].value,
        email:data[1].value,
        phone_no:data[2].value
    };
    callApi('POST','http://127.0.0.1:5000/addMember',JSON.stringify(requestPayload));
});

$('#delete-member-save').click(()=>{
    let data=$('#deleteMemberForm').serializeArray();
    let requestPayload={
        member_id:data[0].value,
        member_name:data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/deleteMember',JSON.stringify(requestPayload));
>>>>>>> 021fdf591c973b00f047735ae9a78bf0621bacba
})