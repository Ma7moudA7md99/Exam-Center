create database exam_center
use exam_center


create table doctor (
	username varchar(20),
	passkey varchar(20)
);

create table student (
	username varchar(20),
	passkey varchar(20)
);
--- execute this line to get your server name
select @@SERVERNAME
insert into doctor (username, passkey) values ('ahmed', 'ahmed123')

insert into student(username, passkey) values ('mohamed', 'mohamed456')

select passkey from doctor where username = 'mohamed'
select * from doctor
select * from student