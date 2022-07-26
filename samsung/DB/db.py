from config import host, username, password, db_name
import psycopg2

try:
    connection = psycopg2.connect(
        host = host,
        user = username,
        password = password,
        database = db_name
    )
    
    connection.autocommit = True
    
    # with connection.cursor() as cursor:
    #     cursor.execute('''
    #         create table mobile(
    #             id serial primary key,
    #             name varchar(50) not null,
    #             model varchar(50) not null
    #         );
    #     ''')
        
    # with connection.cursor() as cursor:
    #     cursor.execute('''
    #         insert into mobile values (1, 'iphone','11'),(2,'samsung','s20');
    #     ''')
        
    with connection.cursor() as cursor:
        cursor.execute('''
            select * from mobile
        ''')
        print(cursor.fetchall())
except Exception as ex:
    print(f"Error: {ex}")
finally:
    if connection:
        connection.close()
        print('connection is closed')