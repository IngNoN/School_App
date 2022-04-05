from flask_wtf import FlaskForm
from wtforms.fields import DecimalField

class AddTeacherInGroupForm(FlaskForm):
    teacher_id = DecimalField("teacher_id")
    group_of_teachers_Id = DecimalField("group_of_teachers_Id")
