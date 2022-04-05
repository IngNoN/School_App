from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField

class DeleteItemForm(FlaskForm):
    teacher_Id = HiddenField("teacher_Id")
    departmentManager_Id = HiddenField("departmentManager_Id")
    group_of_teachers_Id = HiddenField("group_of_teachers_Id")
    teacher_in_group_Id = HiddenField("teacher_in_group_Id")
