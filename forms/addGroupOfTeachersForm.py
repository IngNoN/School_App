from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.fields import DecimalField, SelectField

class AddGroupOfTeachersForm(FlaskForm):
    title = StringField("title")
    description = TextAreaField("description")
    subject = StringField("subject")
    teacher_in_group_Id = DecimalField("teacher_in_group_Id")
    department_managers_Id = StringField("department_managers_Id")