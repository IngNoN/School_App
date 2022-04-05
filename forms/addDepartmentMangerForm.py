from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms import validators
from wtforms.fields import EmailField
from controllers.groupOfTeachers import group_of_teachers

class addDepartmentMangerForm(FlaskForm):
    first_name = StringField("first_name")
    last_name = StringField("last_name", validators=[validators.InputRequired()])
    email_adress = EmailField("email_adress")
    department = StringField("department")