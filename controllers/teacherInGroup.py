from flask import Blueprint, redirect, render_template
from forms.addTeacherInGroupForm import AddTeacherInGroupForm
from models import TeacherInGroup, db

teacher_in_group_blueprint = Blueprint("teacher_in_group_blueprint", __name__)

@teacher_in_group_blueprint.route("/teacher_in_group", methods=["get", "post"])
def teacher_in_group():
    teacher_in_group = db.session.query(TeacherInGroup).all()

    return render_template("teacherInGroup/teacherInGroup.html",
    teacher_in_group = teacher_in_group)

add_teacher_in_group_blueprint = Blueprint("add_teacher_in_group_blueprint", __name__)
@add_teacher_in_group_blueprint.route("/teacher_in_group/add", methods=["get", "post"])
def add_teacher_in_group():
    addTeacherInGroupFormData = AddTeacherInGroupForm()
    teacher_in_group = db.session.query(TeacherInGroup).all()
    if True: #request.method == "POST":
        if addTeacherInGroupFormData.validate_on_submit():
            teacherInGroupData = TeacherInGroup()
            teacherInGroupData.teacher_Id = addTeacherInGroupFormData.teacher_id.data
            teacherInGroupData.group_of_teachers_Id = addTeacherInGroupFormData.group_of_teachers_Id.data

            db.session.add(teacherInGroupData)
            db.session.commit()
        
            return redirect("/teacher_in_group")

        else:
            return render_template("teacherInGroup/addTeacherInGroupForm.html",
            form = addTeacherInGroupFormData)
