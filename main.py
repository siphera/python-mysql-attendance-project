import mysql.connector
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='hospital', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


'''sql = 'insert into login values(%s, %s)'

username = input("enter new username: ")
password = input("enter password: ")

val = (username, password)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
xy = mycursor.execute('Select * from login')
for i in mycursor:
    print(i)'''

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