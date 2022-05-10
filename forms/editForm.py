from tokenize import String
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField, EmailField, SelectField

class EditTeacherForm(FlaskForm):
    teacher_Id = HiddenField("teacher_Id")
    first_name = StringField("first_name")
    last_name = StringField("last_name")
    birthdate = DateField("birthdate")
    teacher_in_group_Id = DecimalField("teacher_in_group_Id")

class EditDepartmentManagersForm(FlaskForm):
    departmentManager_Id = HiddenField("departmentManager_Id")
    first_name = StringField("first_name")
    last_name = StringField("last_name")
    email_adress = EmailField("email_adress")
    department = StringField("department")

class EditGroupOfTeachersForm(FlaskForm):
    group_of_teachers_Id = HiddenField("group_of_teachers_Id")
    title = StringField("title")
    description = TextAreaField("description")
    subject = StringField("subject")
    teacher_in_group_Id = DecimalField("teacher_in_group_Id")
    department_manager_Id = StringField("department_managers_Id")

class EditTeacherInGroupForm(FlaskForm):
    teacher_in_group_Id = HiddenField("teacher_in_group_Id")
    teacher_id = DecimalField("teacher_id")
    group_of_teachers_Id = DecimalField("group_of_teachers_Id")