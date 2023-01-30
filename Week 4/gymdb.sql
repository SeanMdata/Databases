set global local_infile = 1;
drop database if exists gymdb ;
create database gymdb ;
use gymdb ;

Select 'Create Members table' as ' ' ;

create table Members (
  memberID int NOT NULL,
  name varchar (20) NOT NULL,
  phone varchar (12) ,
  email varchar (35),
  membershipstatus varchar(20),
  Primary Key (memberID) ) ;
show warnings ;

Select 'Create Locations Table' as ' ' ;

create table Locations (
  locationID int NOt NULL,
  memberID int,
  streetnum varchar (50),
  city varchar (20),
  state varchar (20),
  Primary Key (locationID),
  Foreign Key (memberID) References Members(memberID) ) ;

Select 'Create Classes table' as ' ' ;

create table Classes (
  classID int,
  memberID int,
  dayofweek varchar (20),
  duration int,
  targetgroup varchar (20),
  Primary Key (classID),
  Foreign Key (memberID) References Members(memberID) ) ;

Select 'Create equipment table' as ' ' ;

create table Equipment (
  equipmentID int,
  locationID int,
  manufacturer varchar (20),
  datelastserviced date,
  Primary Key (equipmentID),
  Foreign Key (locationID) References Locations(locationID) ) ;
show warnings ;

Select 'Create Hold relation' as ' ' ;
create table Hold (
  classID int,
  locationID int,
  Foreign Key (classID) References Classes(classID),
  Foreign Key (locationID) References Locations(locationID) ) ;

Select 'Create Own relation' as ' ' ;
create table Own (
  locationID int,
  equipmentID int,
  Foreign Key (locationID) References Locations(locationID),
  Foreign Key (equipmentID) References Equipment(equipmentID) ) ;

Select 'Loads into Members' as  ' ' ;

load data local infile '/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/members_data.csv' into table Members
fields terminated by ','
lines terminated by '\n';
show warnings ;

Select 'Loads into Locations' as  ' ' ;

load data local infile '/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/location_data.csv' into table Locations
fields terminated by ','
lines terminated by '\n';
show warnings ;

Select 'Loads into Classes' as  ' ' ;

load data local infile '/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/classes_data.csv' into table Classes
fields terminated by ','
lines terminated by '\n';
show warnings ;
Select 'Loads into Equipment' as  ' ' ;

load data local infile '/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/equipment_data.csv' into table Equipment
fields terminated by ','
lines terminated by '\n';
show warnings ;

Select 'Loads into Hold' as  ' ' ;

load data local infile '/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/hold_data.csv' into table Hold
fields terminated by ','
lines terminated by '\n';
show warnings ;

Select 'Loads into Own' as  ' ' ;

load data local infile '/Users/sean/Documents/University_of_denver/comp_3421/Assignment_4/Own_data.csv' into table Own
fields terminated by ','
lines terminated by '\n';
show warnings ;

show tables ;

describe Members ;

describe Locations ;

describe Classes ;

describe equipment ;

describe Hold ;

describe Own ;

Select Count(*) From Members ;

Select Count(*) From Locations ;

Select Count(*) From Equipment ;

Select Count(*) From Classes ;

Select Count(*) From Hold ;

Select Count(*) From Own;

Select * From members m where m.memberID < 10;

Select * From locations where locationID < 10 ;

Select * From Classes Where classID < 10 ;

Select * From equipment where equipmentID < 10 ;

Select * From Hold where locationID < 5 ;

Select * From Own where locationID < 1 ;
