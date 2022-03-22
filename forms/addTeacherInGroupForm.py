from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms import validators
from wtforms.fields import DecimalField

class AddTeacherInGroupForm(FlaskForm):
    teacher_id = DecimalField("teacher_id")
    group_of_teachers_Id = DecimalField("group_of_teachers_Id")
