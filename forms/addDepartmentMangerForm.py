from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators
from wtforms.fields import EmailField


class addDepartmentMangerForm(FlaskForm):
    first_name = StringField("first_name")
    last_name = StringField("last_name", validators=[
                            validators.InputRequired()])
    email_adress = EmailField("email_adress")
    department = StringField("department")
