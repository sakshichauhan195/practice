import mysql.connector
from tabulate import tabulate
from datetime import date
mydb=mysql.connector.connect(host="localhost",user="root",password="dps123", charset="utf8")
cur=mydb.cursor()
cur.execute("create database if not exists dps12")
cur.execute("use dps12")
cur.execute("create table if not exists emp(Empno varchar(6),\
Ename varchar(20), Hiredate date,Salary integer(7))")

def add():
    eno=input("Enter Employee Number")
    ename=input("Enter Employee Name")
    hdate=input("Enter Hiredate")
    sal=int(input("Enter Employee Salary"))
    sal=str(sal)
    cur.execute("insert into emp values('"+eno+"','"+ename+"','"+hdate+"','"+sal+"')")
    mydb.commit()

def delEmp():
    eno=input("Enter Employee Number")
    cur.execute("Delete from emp where empno='"+eno+"'")
    mydb.commit()
    for i in cur:
        print(i)

def updEmp():
    eno=input("Enter Employee Number")
    ename=input("Enter Employee Name")
    hdate=input("Enter Hiredate")
    sal=int(input("Enter Employee Salary"))
    sal=str(sal)
    cur.execute("update emp set ename='"+ename+"',hiredate='"+hdate+"',salary='"+sal+"' where\
    empno='"+eno+"'")
    mydb.commit()

def viewAll():
    cur.execute("Select * from emp")
    data=cur.fetchall()
    print(tabulate(data,headers=["Empno","Ename","Hiredate","Salary"],tablefmt="psql"))

def search():
    eno=input("Enter Employee number to be search : ")
    cur.execute("Select * from emp where empno='"+eno+"'")
    data=cur.fetchall()
    print(tabulate(data,headers=["Empno","Ename","Hiredate","Salary"],tablefmt="psql"))

    
while True:
    print("1. Add Employee Details")
    print("2. Update")
    print("3. Delete Employee Details")
    print("4. View all")
    print("5. Search")
    print("6. Exit")    
    ch=int(input("Enter your choice from 1/2/3/4/5/6"))
    if ch==1:
        add()
    elif ch==2:
        updEmp()
    elif ch==3:
        delEmp()
    elif ch==4:
        viewAll()
    elif ch==5:
        search()
    elif ch==6:
        print("Application shutdown................")
        break
    else:
        print("You have to select the options from 1/2/3/4/5/6 only")
