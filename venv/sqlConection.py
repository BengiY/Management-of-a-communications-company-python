from Customer import  Customer
from Talking import Talking
from Line import Line
from Croute import Croute
import pyodbc

#connect to pythonDb database in sql server
def Connect():
    database="pythonDB"
    server="DESKTOP-2U2SABC"
    global connection
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';')
    global cursor
    cursor = connection.cursor()

#add customer by input of user
def addCustomerByInput():
    Connect()
    customer = Customer(
        input("enter your id"),
        input("enter your first name"),
        input("enter your last name"),
        input("enter your address"),
        input("enter your country")
    )
    countRow=cursor.execute("INSERT INTO Customer(CustomerId,CustomerName,CustomerLast,CustomerAdress,CustomerCountry) "
                                "VALUES('" + customer.CustomerId + "','" + customer.CustomerName + "','" + customer.CustomerLast + "','" + customer.CustomerAdress + "','" + customer.CustomerCountry + "')").rowcount
    print(str(countRow) +" row effected")
    connection.commit()
    cursor.close()
    connection.close()

# add customer with const parameter
def addCustomer():
    Connect()
    countRow=cursor.execute("INSERT INTO Customer(CustomerId,CustomerName,CustomerLast,CustomerAdress,CustomerCountry)VALUES('123','yosef','cohen','rabi akiva 5','israel')").rowcount
    print(str(countRow) +" row effected")
    connection.commit()
    cursor.close()
    connection.close()

#Increase by 2% the price for a rote that costs less than 30
def updateCost():
    Connect()
    countRow = cursor.execute("UPDATE cRoute set RouteCost=RouteCost*102/100 where RouteCost<30").rowcount
    print(str(countRow) +" row effected")
    connection.commit()
    cursor.close()
    connection.close()

# delete talking of user by number of his phone
def deleteTalking():
  Connect()
  phone=input("enter your fone to delete your's talking")
  countRow = cursor.execute('DELETE FROM talking WHERE OneFhone='+phone).rowcount
  print(str(countRow) + " row deleted")
  connection.commit()
  cursor.close()
  connection.close()

#add new talking
def addTalking():
    Connect()
    talking = Talking(
        input("enter StartDate"),
        input("enter EndDate"),
        input("enter your fhone"),
        input("enter memeber fhone")
    )
    countRow=cursor.execute("INSERT INTO Talking(StartDate,EndDate,OneFhone,SecondFhone)VALUES('" + talking.StartDate + "','" + talking.EndDate + "','" + talking.OneFhone + "','" + talking.SecondFhone +"')").rowcount
    print(str(countRow) +" row effected")
    connection.commit()
    cursor.close()
    connection.close()

#get all talking of user by phone number
def getTalkingByPhone(YourPhone):
    Connect()
    Connect()
    cursor.execute("SELECT StartDate,EndDate,OneFhone,SecondFhone from Talking where OneFhone="+YourPhone)
    all=cursor.fetchall()
    talkingList = []
    for i in all:
        talkingList.append(Talking(i[0], i[1], i[2], i[3]))
    for i in talkingList:
        print(i)
    connection.commit()
    cursor.close()
    connection.close()

#get cost of all talking by customer id
def getcost(yourcode):
    Connect()
    cursor.execute("select SUM(DATEDIFF(MINUTE,StartDate, EndDate))*c.RouteCost s from talking t  join line l  on t.OneFhone =l.LineFone join cRoute c on l.RouteCode= c.RouteCode where  OneFhone like (select LineFone l from line where CustomerCode={})group by c.RouteCost".format(yourcode))
    result=0
    all=cursor.fetchall()
    for i in all:
        result=i[0]
    print("your cost of all your talking is " +str(result)+" NIS")
    connection.commit()
    cursor.close()
    connection.close()

#get num of lines to any route
def getCountLinesOfAnyRoute():
    Connect()
    cursor.execute("select COUNT(LineFone),c.RouteName from line l join cRoute c on l.RouteCode=c.RouteCode group by c.RouteName")
    all = cursor.fetchall()
    for i in all:
        print("rote: "+i[1]+" ,count lines: " +str(i[0]))
    connection.commit()
    cursor.close()
    connection.close()

#Check for a line if it has exceeded the allowable number of minutes
def exceptionCheck(yourPhone):
    Connect()
    cursor.execute("select c.MinitRouteHere -SUM(DATEDIFF(MINUTE,StartDate, EndDate)) from talking t  join line l on t.OneFhone =l.LineFone join cRoute c on l.RouteCode= c.RouteCode where  OneFhone = {} group by c.MinitRouteHere".format(yourPhone))
    result=0
    all = cursor.fetchall()
    for i in all:
        result=i[0]
    if result<0:
        print("was exception")
    else:
        print("was not exception")


