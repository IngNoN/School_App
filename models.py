# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class DepartmentManager(db.Model):
    __tablename__ = 'department_manager'

    departmentManager_Id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email_adress = db.Column(db.String(64), nullable=False)
    department = db.Column(db.String(64))



class GroupOfTeacher(db.Model):
    __tablename__ = 'group_of_teachers'

    group_of_teachers_Id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text)
    subject = db.Column(db.String(32))
    #teacher_in_group_Id = db.Column(db.ForeignKey('teacher_in_group.teacher_in_group_Id'), index=True)
    departmentManager_Id = db.Column(db.ForeignKey('department_manager.departmentManager_Id'), index=True)

    department_manager = db.relationship('DepartmentManager', primaryjoin='GroupOfTeacher.departmentManager_Id == DepartmentManager.departmentManager_Id', backref='group_of_teachers')
    #teacher_in_group = db.relationship('TeacherInGroup', primaryjoin='GroupOfTeacher.teacher_in_group_Id == TeacherInGroup.teacher_in_group_Id', backref='group_of_teachers')



class Teacher(db.Model):
    __tablename__ = 'teacher'

    teacher_Id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    birthdate = db.Column(db.Date)
    teacher_in_group_Id = db.Column(db.ForeignKey('teacher_in_group.teacher_in_group_Id'), index=True)

    teacher_in_group = db.relationship('TeacherInGroup', primaryjoin='Teacher.teacher_in_group_Id == TeacherInGroup.teacher_in_group_Id', backref='teachers')



class TeacherInGroup(db.Model):
    __tablename__ = 'teacher_in_group'

    teacher_in_group_Id = db.Column(db.Integer, primary_key=True, unique=True)
    teacher_Id = db.Column(db.ForeignKey('teacher.teacher_Id'), index=True)
    group_of_teachers_Id = db.Column(db.ForeignKey('group_of_teachers.group_of_teachers_Id'), index=True)

    group_of_teacher = db.relationship('GroupOfTeacher', primaryjoin='TeacherInGroup.group_of_teachers_Id == GroupOfTeacher.group_of_teachers_Id', backref='teacher_in_groups')
    teacher = db.relationship('Teacher', primaryjoin='TeacherInGroup.teacher_Id == Teacher.teacher_Id', backref='teacher_in_groups')
