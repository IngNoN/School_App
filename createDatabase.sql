create database if not exists school_app;
use school_app;

create table if not exists department_manager
(
departmentManager_Id int auto_increment unique key primary key,
first_name varchar(64) not null,
last_name varchar(64) not null,
email_adress varchar(64) not null,
department varchar(64)
);

create table if not exists group_of_teachers
(
group_of_teachers_Id int auto_increment unique key primary key,
title varchar(32) not null,
description text,
subject varchar(32),
teacher_in_group_Id int
);

create table if not exists teacher
(
teacher_Id int auto_increment unique key primary key,
first_name varchar(64) not null,
last_name varchar(64) not null,
birthdate date,
teacher_in_group_Id int
);

create table if not exists teacher_in_group
(
teacher_in_group_Id int auto_increment unique key primary key,
teacher_Id int,
group_of_teachers_Id int, 
constraint teacher_id_foreign_key foreign key (teacher_Id) references teacher (teacher_Id),
constraint group_of_teachers_id_foreign_key foreign key (group_of_teachers_Id) references group_of_teachers (group_of_teachers_Id)
);

alter table group_of_teachers add constraint teacher_in_group_foreign_key foreign key (teacher_in_group_Id) references teacher_in_group (teacher_in_group_id);
alter table teacher add constraint teacher_teacher_in_group_foreign_key foreign key (teacher_in_group_Id) references teacher_in_group (teacher_in_group_Id);

alter table teacher_in_group drop constraint teacher_in_group_foreign_group_of_teachers_Id;
alter table teacher_in_group drop constraint teacher_in_group_freign_teacher_Id;
alter table teacher drop column email_adress;
alter table group_of_teachers drop constraint group_teacher_in_group_foreign_key;

drop table department_manager;
drop table group_of_teachers;
drop table teacher;
drop table teacher_in_group;