from sql_connection import get_sql_connection
from datetime import date

def get_all_books(conn,search):
    cursor=conn.cursor()
    if not search or search.strip() == '':
        cursor.execute('SELECT * FROM books')
    else:
        cursor.execute("SELECT * FROM books WHERE book_name LIKE %s", ('%' + search.strip() + '%',))
    response=[]
    for (book_id,book_name,author,publisher,date_of_entry,borrowed) in cursor:
        response.append({
            'book_id':book_id,
            'book_name':book_name,
            'author':author,
            'publisher':publisher,
            'date_of_entry':date_of_entry,
            'borrowed':borrowed
        })

    cursor.close()

    return response

def insert_new_book(conn, book):
    cursor=conn.cursor()
    print(book)
    cursor.execute('insert into books(book_name,author,publisher,date_of_entry,borrowed) values (%s,%s,%s,%s,%s)',
                   (book['book_name'],book['author'],book['publisher'],date.today(),'n'))
    conn.commit()

    return cursor.lastrowid

def delete_book(conn,book):
    cursor=conn.cursor()
    if book['book_id']:
        cursor.execute('delete from books where book_id='+book['book_id'])
    elif book['book_name']:
        cursor.execute('delete from books where book_name='+book['book_name'])
    conn.commit()
    return cursor.lastrowid

if __name__=='__main__':
    conn=get_sql_connection()
    
