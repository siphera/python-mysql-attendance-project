import mysql.connector
'''mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='hospital', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def insert():
    sql = 'insert into login values(%s, %s)'

    username = input("enter new username: ")
    password = input("enter password: ")

    val = (username, password)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")
    xy = mycursor.execute('Select * from login')
    for i in mycursor:
        print(i)

insert()


def verify():
    username = input("enter new username: ")
    password = input("enter password: ")

    sql = "select * from login where username = %s and password =%s"
    mycursor.execute(sql, [(username), (password)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            print("you have logged in successfully")
            break;
    else:
        print("Login have failed")


verify()

# insert into users(name, surname, contact, email, department, password) values('siphe', 'salman', '0734229818', 'salman@gmail.com', 'academy', 'siphera8');

'''
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


def register():


    # sql = 'insert into users values(id, name, surname, contact, email, department, password)'

    # sql = 'insert into users values(%s, %s, %s, %s, %s, %s)'
    name = input("please enter name: ")
    surname = input("please enter surname: ")
    contact = input("please enter contact: ")
    email = input("please enter email: ")
    department = input("please enter department: ")
    password = input("please enter password: ")
    add_user = """INSERT INTO Lifechoicesonline.users 
                  (name, surname, contact, email, department, password) 
                  VALUES (%s, %s, %s, %s, %s, %s)"""
    val = (name, surname, contact, email, department, password)
    mycursor.execute(add_user, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")
    xy = mycursor.execute('Select * from users')
    for i in mycursor:
        print(i)


register()


