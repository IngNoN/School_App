from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms import validators
from wtforms.fields import DecimalField

class AddTeacherForm(FlaskForm):
    first_name = StringField("first_name")
    last_name = StringField("last_name", validators=[validators.InputRequired()])
    birthdate = DateField("birthdate")
    teacher_in_group_Id = DecimalField("teacher_in_group_Id")