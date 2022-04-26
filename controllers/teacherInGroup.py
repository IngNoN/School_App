from flask import Blueprint, redirect, render_template, request
from forms.addTeacherInGroupForm import AddTeacherInGroupForm
from models import Teacher, TeacherInGroup, db
from forms.editForm import EditTeacherInGroupForm

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

show_edit_teacher_in_group_blueprint = Blueprint("show_edit_teacher_in_group_blueprint", __name__)

@show_edit_teacher_in_group_blueprint.route("/teacher_in_group/edit")
def show_edit_group_of_teachers():
    editTeacherInGroupData = EditTeacherInGroupForm()
    #teacher_in_group = db.session.query(TeacherInGroup).order_by(TeacherInGroup.teacher_in_group_Id).all()
    #itemId auslesen
    teacher_in_group_Id = request.args["teacher_in_group_Id"]
    #Item laden
    teacher_in_group_to_edit = db.session.query(TeacherInGroup).filter(TeacherInGroup.teacher_in_group_Id == teacher_in_group_Id).first()
    #Form befüllen
    editTeacherInGroupData.teacher_in_group_Id.data = teacher_in_group_Id 
    editTeacherInGroupData.teacher_id.data = teacher_in_group_to_edit.teacher_Id
    editTeacherInGroupData.group_of_teachers_Id.data = teacher_in_group_to_edit.group_of_teachers_Id

    return render_template("/teacherInGroup/editTeacherInGroup.html", form = editTeacherInGroupData)

submit_edit_teacher_in_group_blueprint  = Blueprint("submit_edit_teacher_in_group_blueprint", __name__)

@submit_edit_teacher_in_group_blueprint.route("/teacher_in_group/edit", methods=["post"])
def submit_edit_teacher_in_group():
    editTeacherInGroupData = EditTeacherInGroupForm()

    if editTeacherInGroupData.validate_on_submit():
        #daten aus Form auslesen
        teacher_in_group_Id = editTeacherInGroupData.teacher_in_group_Id.data
        teacher_in_group_to_edit = db.session.query(TeacherInGroup).filter(TeacherInGroup.teacher_in_group_Id == teacher_in_group_Id).first()
        #daten mit update in DB speichern
        teacher_in_group_to_edit.teacher_Id = editTeacherInGroupData.teacher_id.data
        teacher_in_group_to_edit.group_of_teacher_Id = editTeacherInGroupData.group_of_teachers_Id.data

        db.session.commit()

        return redirect("/teacher_in_group")
    
    else:
        raise("Fatal Error")