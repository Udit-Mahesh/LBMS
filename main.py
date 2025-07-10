from flask import Flask,render_template,request,jsonify

from sql_connection import get_sql_connection
import homepage
import manage_members
import manage_transactions
import manage_staff


app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    conn=get_sql_connection()
    search=request.args.get('input-value')
    books=homepage.get_all_books(conn,search)
    return render_template('index.html',books=books)

@app.route('/manageMembers',methods=['GET'])
def members_page():
    conn=get_sql_connection()
    search=request.args.get('input-value')
    members=manage_members.get_all_members(conn,search)
    return render_template('members.html',members=members)

@app.route('/manageTransactions',methods=['GET'])
def transactions_page():
    conn=get_sql_connection()
    book=request.args.get('book-name')
    member=request.args.get('member-name')
    transactions=manage_transactions.get_all_transactions(conn,book,member)
    return render_template('transactions.html',transactions=transactions)

@app.route('/manageStaff',methods=['GET'])
def staff_page():
    conn=get_sql_connection()
    search=request.args.get('input-value')
    staff=manage_staff.get_all_staff(conn,search)
    return render_template('staff.html',staff=staff)

@app.route('/addBook',methods=['POST'])
def insert_new_book():
    conn=get_sql_connection()
    request_payload=request.get_json()
    book_id=homepage.insert_new_book(conn,request_payload)
    response=jsonify({'book_id':book_id})
    return response

@app.route('/deleteBook',methods=['POST'])
def delete_book():
    conn=get_sql_connection()
    request_payload=request.get_json()
    book_id=homepage.delete_book(conn,request_payload)
    response=jsonify({'book_id':book_id})
    return response

@app.route('/addMember',methods=['POST'])
def add_member():
    conn=get_sql_connection()
    request_payload=request.get_json()
    member_id=manage_members.insert_member(conn,request_payload)
    return jsonify({'member_id':member_id})

@app.route('/deleteMember',methods=['POST'])
def delete_member():
    conn=get_sql_connection()
    request_payload=request.get_json()
    member_id=manage_members.remove_member(conn,request_payload)
    return jsonify({'member_id':member_id})

@app.route('/addStaff',methods=['POST'])
def add_staff():
    conn=get_sql_connection()
    request_payload=request.get_json()
    staff_id=manage_staff.insert_staff(conn,request_payload)
    return jsonify({'staff_id':staff_id})

@app.route('/deleteStaff',methods=['POST'])
def delete_staff():
    conn=get_sql_connection()
    request_payload=request.get_json()
    staff_id=manage_staff.remove_staff(conn,request_payload)
    return jsonify({'staff_id':staff_id})

@app.route('/borrowBook',methods=['POST'])
def borrow_book():
    conn=get_sql_connection()
    request_payload=request.get_json()
    result=manage_transactions.borrowing(conn,request_payload)
    return result
    
    
@app.route('/returnBook',methods=['POST'])
def return_book():
    conn=get_sql_connection()
    request_payload=request.get_json()
    result=manage_transactions.returning(conn,request_payload)
    return result
    
    

if __name__=='__main__':
    app.run(port=5000)