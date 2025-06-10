from sql_connection import get_sql_connection
from datetime import date,timedelta
import mysql.connector
from flask import jsonify


def get_all_transactions(conn,book,member):
    cursor=conn.cursor()
    if (book and member) and (book.strip()!='' and member.strip()!=''):
        cursor.execute('select * from transact where book_name like %s and member_name like %s',('%'+book.strip()+'%','%'+member.strip()+'%'))
    elif book and book.strip()!='':
        cursor.execute('select * from transact where book_name like %s',('%'+book.strip()+'%',))
    elif member and member.strip()!='':
        cursor.execute('select * from transact where member_name like %s',('%'+member.strip()+'%',))
    else:
        cursor.execute('select * from transact')
    response=[]
    for (transaction_id,book_name,member_name,issue_date,due_date,return_date) in cursor:
        response.append({
            'transaction_id':transaction_id,
            'book_name':book_name,
            'member_name':member_name,
            'issue_date':issue_date,
            'due_date':due_date,
            'return_date':return_date
        })

    conn.commit()

    return response

    
def borrowing(conn,transact):
    cursor=conn.cursor()
    try:
        cursor.execute('insert into transactions(book_id,member_id,issue_date,due_date) values (%s,%s,%s,%s)',(transact['book_id'],transact['member_id'],date.today(),date.today()+timedelta(days=14)))
        cursor.execute("update books set borrowed='y' where book_id=%s",(transact['book_id'],))
        conn.commit()
        return jsonify({'success': True,'message':'Transaction was success'})
    except mysql.connector.IntegrityError as e:
        conn.rollback()
        if e.errno==1452:
            return jsonify({'success':False,'message':'Enter valid book or member ID'}),400
        return jsonify({'success':False,'message':str(e)}),500
    
def returning(conn,transact):
    cursor=conn.cursor()
    try:
        cursor.execute('update transactions set return_date=%s where book_id=%s and member_id=%s',(date.today(),transact['book_id'],transact['member_id']))
        cursor.execute("update books set borrowed='n' where book_id=%s",(transact['book_id'],))
        conn.commit()
        return jsonify({'success':True,'message':'Transaction was success'})
    except mysql.connector.IntegrityError as e:
        conn.rollback()
        if e.errno==1452:
            return jsonify({'success':False,'message':'Enter valid book or member ID'}),400
        return jsonify({'success':False,'message':str(e)}),500
    

if __name__=='__main__':
    conn=get_sql_connection()
    # print(get_all_transactions())