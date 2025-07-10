from sql_connection import get_sql_connection
from datetime import date

def get_all_staff(conn,search):
    cursor=conn.cursor()
    if not search or search.strip() == '':
        cursor.execute('SELECT * FROM staff')
    else:
        cursor.execute("SELECT * FROM staff WHERE staff_name LIKE %s", ('%' + search.strip() + '%',))
    response=[]
    for (staff_id,staff_name,role,email,password,phone_no,entry_date) in cursor:
        response.append({
            'staff_id':staff_id,
            'staff_name':staff_name,
            'role':role,
            'email':email,
            'password':password,
            'phone_no':phone_no,
            'entry_date':entry_date
        })

    cursor.close()

    return response

def insert_staff(conn,staff):
    cursor=conn.cursor()
    cursor.execute('insert into staff(staff_name,role,email,password,phone_no,entry_date) values (%s,%s,%s,%s,%s,%s)',(staff['staff_name'],staff['role'],staff['email'],staff['password'],staff['phone_no'],date.today()))
    conn.commit()
    return cursor.lastrowid

def remove_staff(conn,staff):
    cursor=conn.cursor()
    if staff['staff_id']:
        cursor.execute('delete from staff where staff_id=%s',(staff['staff_id'],))
    elif staff['staff_name']:
        cursor.execute('delete from staff where staff_name=%s',(staff['staff_name'],))
    conn.commit()
    return cursor.lastrowid

if __name__=='__main__':
    conn=get_sql_connection()
    # print(get_all_staff())