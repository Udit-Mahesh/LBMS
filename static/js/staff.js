$('#add-staff-save').click(()=>{
    let data=$('#addStaffForm').serializeArray();
    if (data[3].value===data[4].value){
        let requestPayload={
            staff_name : data[0].value,
            role : data[1].value,
            email : data[2].value,
            password : data[3].value,
            phone_no : data[5].value
        };
        callApi('POST','http://127.0.0.1:5000/addStaff',JSON.stringify(requestPayload));
    }else{
        alert('Enter matching passwords');
    }
});

$('#delete-staff-save').click(()=>{
    let data=$('#deleteStaffForm').serializeArray();
    let requestPayload={
        staff_id : data[0].value,
        staff_name : data[1].value
    };
    callApi('POST','http://127.0.0.1:5000/deleteStaff',JSON.stringify(requestPayload));
})