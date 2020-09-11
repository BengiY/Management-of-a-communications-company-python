create database pythonDB
go
use pythonDB
go
create table customer
(
CustomerCode  int primary key identity(0,10),
CustomerId varchar(9),
CustomerName varchar(20),
CustomerLast varchar(20),
CustomerAdress varchar(40),
CustomerCountry varchar(20)
)
create table cRoute
(
RouteCode int primary key identity(1,1),
RouteName varchar(25),
RouteCost int,
MinitRouteHere int,
MinitRouteBroad int
)
create table line
(
LineCode  int identity(100,10)primary key,
CustomerCode int foreign key references customer(CustomerCode),
RouteCode int foreign key references cRoute(RouteCode),
LineFone varchar(10) unique
)
create table talking(
TalkinCode int primary key identity(1,1),
StartDate date,
EndDate date,
OneFhone varchar(10) foreign key references line(LineFone),
SecondFhone varchar(10) foreign key references line(LineFone)
)
use pythonDB
INSERT INTO cRoute(RouteName,RouteCost,MinitRouteHere,MinitRouteBroad) VALUES('kosher',54,2000,1000)
INSERT INTO cRoute(RouteName,RouteCost,MinitRouteHere,MinitRouteBroad) VALUES('busy',20,2000,1000)
INSERT INTO cRoute(RouteName,RouteCost,MinitRouteHere,MinitRouteBroad) VALUES('tocman',5,1,2)
INSERT INTO cRoute(RouteName,RouteCost,MinitRouteHere,MinitRouteBroad) VALUES('govine',21,2,1)

INSERT INTO line(CustomerCode,RouteCode,LineFone) VALUES(10,1,'0548466119')
INSERT INTO line(CustomerCode,RouteCode,LineFone) VALUES(20,2,'0542558966')
INSERT INTO line(CustomerCode,RouteCode,LineFone) VALUES(30,2,'0522235689')
INSERT INTO line(CustomerCode,RouteCode,LineFone) VALUES(30,1,'0528896598')

INSERT INTO talking(StartDate,EndDate,OneFhone,SecondFhone) VALUES('12-10-2000','12-10-2000','0548466119','0542558966')
INSERT INTO talking(StartDate,EndDate,OneFhone,SecondFhone) VALUES('12/13/2000','12/12/2000','0542558966','0522235689')
INSERT INTO talking(StartDate,EndDate,OneFhone,SecondFhone) VALUES('12-25-2000','12-26-2000','0528896598','0542558966')
INSERT INTO talking(StartDate,EndDate,OneFhone,SecondFhone) VALUES('10-01-2000','10-02-2000','0548466119','0522235689')