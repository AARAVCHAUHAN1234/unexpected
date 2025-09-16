import random
import mysql.connector as mq

# to make captcha:

def captcha():
    global z
    z = str()
    for i in range(0, 4):
        if i % 2 == 0:
            s = random.randint(65, 92)
            x = chr(s)
            z += x
        else:
            s = random.randint(0, 10)
            d = str(s)
            z += d
    print("your captcha is:", z)

# to insert detail of customer:
def insert():
    db = mq.connect(host="localhost", user="root", passwd="#Vansh*02/08", database="aarav")
    con = db.cursor()
    q = 'select acc_no from bank;'
    con.execute(q)
    data = con.fetchall()
    l = []
    for i in data:
        l.append(i[0])
    acc_id = random.randint(10000, 99999)
    while acc_id in l:
        acc_id = random.randint(10000, 99999)
    print("Your account number is-", acc_id)
    b = input("enter the name: ")
    c = int(input("enter the amount by customer: "))
    d = int(input("any loan?: "))
    ph = int(input('enter the phone number: '))
    address = input("enter your address: ")
    q = "insert into bank values({},'{}',{},{},{},'{}');".format(acc_id, b, c, d, ph, address)
    con.execute(q)
    db.commit()
    db.close()

# to take a loan:
def loan():
    db = mq.connect(host="localhost", user="root", passwd="#Vansh*02/08", database="aarav")
    con = db.cursor()
    m = input("enter your account no.: ")
    p = int(input("enter the principle amount: "))
    t = int(input("enter the time period: "))
    r = 15
    print("rate=15%")
    i = (p * r * t / 100)
    print("interest paid by you will be", i)
    print("Do you still want to take a loan? Type 'yes' or 'no'.")
    d = input("enter your choice: ")
    if d == "Yes" or d == "yes":
        l = i + p
        query = "update bank set loan={} where acc_no={};".format(l, m)
        con.execute(query)
        print("Loan has been provided")
        db.commit()
    else:
        print("Thank You")
    db.close()

# to display record via Account Number:
def display():
    db = mq.connect(host="localhost", user="root", passwd="#Vansh*02/08", database="aarav")
    con = db.cursor()
    c = int(input("enter your account no."))
    query = "select * from bank where acc_no={};".format(c)
    con.execute(query)
    data = con.fetchall()
    captcha()

    g = str(input("enter the captcha"))
    if g == z:
        print("captcha matched")
        print("the information will display in couple of minute.....")
        for i in data:
            print("your account number is:", i[0])
            print("your name is:", i[1])
            print("your amount deposited in bank is:", i[2])
            print("your loan amount is:", i[3])
            print("your phone no. is:", i[4])
            print("your addtress is:", i[5])
        db.close()
    else:
        print("wrong captcha try again")


# to see how many customers have loan:
def Maximum():
    db = mq.connect(host="localhost", user="root", passwd="#Vansh*02/08", database="aarav")
    con = db.cursor()
    query = "select * from bank ;"
    con.execute (query)
    data = con.fetchall()
    for i in data:
        a=i[3]
        if a > 5000  or a == 5000:
            print("your account number is:", i[0])
            print("your name is:", i[1])
            print("your amount deposited in bank is:", i[2])
            print("your loan amount is:", i[3])
            print("your phone no. is:", i[4])
            print("your address is:", i[5])
            print()
    else:
        print("Loan is less than 5000")
   db.close()

# to change details:
def updation():
    db = mq.connect(host="localhost", user="root", passwd="#Vansh*02/08", database="aarav")
    con = db.cursor()
    q = str(input("enter your acc. no."))
    captcha()
    g = str(input("enter the captcha"))
    if g == z:
        print("captcha matched")
        print("the information will display in couple of minute.....")
        for i in range(1, 2):
            print()
            print("if you want change name,press 1")
            print("if you want change phone number,press 2")
            print("if you want change address,press 3")
            print()
            u = int(input("enter your choice: "))
            if u == 1:
                m = input("Enter the new name: ")
                query = "update bank set name='{}' where acc_no={};".format(m, q)
            if u == 2:
                m = input("Enter the new phone number: ")
                query = "update bank set phone_no='{}' where acc_no={};".format(m, q)
            if u == 3:
                m = input("Enter the new address: ")
                query = "update bank set address='{}' where acc_no={};".format(m, q)
            con.execute(query)
            db.commit()
            db.close()
    else:
        print("wrong captcha try again")

# to delete a customer account:
def deletion():
    db = mq.connect(host="localhost", user="root", passwd="#Vansh*02/08", database="aarav")
    con = db.cursor()
    q = input("enter your acc no.")
    query = "delete from bank where acc_no={};".format(q)
    con.execute(query)
    db.close()


# to deposit money:
def deposit():
    db = mq.connect(host="localhost", user="root", passwd="#Vansh*02/08", database="aarav")
    con = db.cursor()
    q = input("enter the acc. no.")
    a = int(input("Enter the amount you want to deposit: "))
    query = "update bank set balance=balance+{} where acc_no={};".format(a, q)
    con.execute(query)
    q1 = ("select * from bank where acc_no={};").format(q)
    con.execute(q1)
    data = con.fetchall()
    for i in data:
        print("Account Number-", i[0])
        print("Account holder Name-", i[1])
        print("Balance after depositing money-", i[2])
    db.commit()
    db.close()

def choice():
    print()
    print("If you want to enter new account, Press 1")
    print("If you want to take a loan, Press 2")
    print("If you want to display a record, Press 3")
    print("If you want to check if someone has more loan than 5000, Press 4")
    print("If you want to update your account, Press 5")
    print("If you want to delete an account, Press 6")
    print("If you want to deposit money, Press 7")
    print("If you want to exit, Press 8")


while True:
    print()
    choice()
    print()

    i = int(input("Enter your choice:"))
    if i == 1:
        insert()
        print("Work Done")
    elif i == 2:
        loan()
    elif i == 3:
        display()
        print("Your asked account detail had been displayed")
    elif i == 4:
        Maximum()
    elif i == 5:
        updation()
        print("Your account has been updated")
    elif i == 6:
        deletion()
        print("Selected account is deleted")
    elif i == 7:
        deposit()
        print("The account has been deposited")
    elif i == 8:
        print("THANK YOU")
        break
    else:
        print("Invalid selection")
