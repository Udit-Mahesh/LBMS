<<<<<<< HEAD
from sql_connection import get_sql_connection
from datetime import date

def get_all_members(conn,search):
    cursor=conn.cursor()
    if not search or search.strip() == '':
        cursor.execute('SELECT * FROM members')
    else:
        cursor.execute("SELECT * FROM members WHERE member_name LIKE %s", ('%' + search.strip() + '%',))
    response=[]
    for (member_id,member_name,email,phone_no,membership_date) in cursor:
        response.append({
            'member_id':member_id,
            'member_name':member_name,
            'email':email,
            'phone_no':phone_no,
            'membership_date':membership_date
        })

    cursor.close()

    return response

def insert_member(conn,member):
    cursor=conn.cursor()
    cursor.execute('insert into members(member_name,email,phone_no,membership_date) values (%s,%s,%s,%s)',(member['member_name'],member['email'],member['phone_no'],date.today()))
    conn.commit()

    return cursor.lastrowid

def remove_member(conn,member):
    cursor=conn.cursor()
    if member['member_id']:
        cursor.execute('delete from members where member_id=%s',(member['member_id'],))
    elif member['member_name']:
        cursor.execute('delete from members where member_name=%s',(member['member_name'],))
    conn.commit()
    return cursor.lastrowid

if __name__=='__main__':
    conn=get_sql_connection()
=======
from sql_connection import get_sql_connection
from datetime import date

def get_all_members(conn,search):
    cursor=conn.cursor()
    if not search or search.strip() == '':
        cursor.execute('SELECT * FROM members')
    else:
        cursor.execute("SELECT * FROM members WHERE member_name LIKE %s", ('%' + search.strip() + '%',))
    response=[]
    for (member_id,member_name,email,phone_no,membership_date) in cursor:
        response.append({
            'member_id':member_id,
            'member_name':member_name,
            'email':email,
            'phone_no':phone_no,
            'membership_date':membership_date
        })

    cursor.close()

    return response

def insert_member(conn,member):
    cursor=conn.cursor()
    cursor.execute('insert into members(member_name,email,phone_no,membership_date) values (%s,%s,%s,%s)',(member['member_name'],member['email'],member['phone_no'],date.today()))
    conn.commit()

    return cursor.lastrowid

def remove_member(conn,member):
    cursor=conn.cursor()
    if member['member_id']:
        cursor.execute('delete from members where member_id=%s',(member['member_id'],))
    elif member['member_name']:
        cursor.execute('delete from members where member_name=%s',(member['member_name'],))
    conn.commit()
    return cursor.lastrowid

if __name__=='__main__':
    conn=get_sql_connection()
>>>>>>> 021fdf591c973b00f047735ae9a78bf0621bacba
    # print(get_all_members())