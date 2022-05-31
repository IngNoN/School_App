from flask_wtf import FlaskForm
from wtforms.fields import SelectField


class AddTeacherInGroupForm(FlaskForm):
    teacher_id = SelectField("teacher_id")
    group_of_teachers_Id = SelectField("group_of_teachers_Id")
