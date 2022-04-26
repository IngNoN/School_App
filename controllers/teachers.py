from re import sub
from flask import Blueprint, redirect, render_template, request
from controllers.teacherInGroup import TeacherInGroup
from forms.addTeacherForm import AddTeacherForm
from models import Teacher, db
from forms.editForm import EditTeacherForm

teachers_blueprint = Blueprint("teachers_blueprint", __name__)

@teachers_blueprint.route("/teachers", methods=["get", "post"])
def teachers():
    teachers = db.session.query(Teacher).all()
    addTeacherFormData = AddTeacherForm()

    return render_template("teachers/teachers.html",
    teachers = teachers,
    form = addTeacherFormData)


add_teachers_blueprint = Blueprint("add_teachers_blueprint", __name__)

@add_teachers_blueprint.route("/teachers/add", methods=["get", "post"])
def add_teachers():
    addTeacherFormData = AddTeacherForm()
    teachers = db.session.query(Teacher).all()
    teacher_in_group = db.session.query(TeacherInGroup).all()
    if True: #request.method == "POST":
        if addTeacherFormData.validate_on_submit():
            teacherData = Teacher()
            teacherData.first_name = addTeacherFormData.first_name.data
            teacherData.last_name = addTeacherFormData.last_name.data
            teacherData.birthdate = addTeacherFormData.birthdate.data
            #teacherData.teacher_in_group_Id = addTeacherFormData.teacher_in_group_Id.data

            db.session.add(teacherData)
            db.session.commit()
        
            return redirect("/teachers")

        else:
            return render_template("teachers/addTeacherForm.html", form = addTeacherFormData, teacher_in_group = teacher_in_group)

show_edit_teachers_blueprint = Blueprint("show_edit_teachers_blueprint", __name__)

@show_edit_teachers_blueprint.route("/teachers/edit")
def show_edit_teachers():
    editTeacherFormData = EditTeacherForm()
    #itemId auslesen
    teacher_Id = request.args["teacher_Id"]
    #Item laden
    teacher_to_edit = db.session.query(Teacher).filter(Teacher.teacher_Id == teacher_Id).first()
    #Form befüllen
    editTeacherFormData.teacher_Id.data = teacher_Id
    editTeacherFormData.first_name.data = teacher_to_edit.first_name
    editTeacherFormData.last_name.data = teacher_to_edit.last_name
    editTeacherFormData.birthdate.data = teacher_to_edit.birthdate
    editTeacherFormData.teacher_in_group_Id.data = teacher_to_edit.teacher_in_group_Id

    return render_template("/teachers/editTeacherForm.html", form = editTeacherFormData)


submit_edit_teachers_blueprint = Blueprint("submit_edit_teachers_blueprint", __name__)

@submit_edit_teachers_blueprint.route("/teachers/edit", methods=["post"])
def submit_edit_teachers():
    editTeacherFormData = EditTeacherForm()

    if editTeacherFormData.validate_on_submit():
        #daten aus Form auslesen
        teacher_Id = editTeacherFormData.teacher_Id.data
        teacher_to_edit = db.session.query(Teacher).filter(Teacher.teacher_Id == teacher_Id).first()
        #daten mit update in DB speichern
        teacher_to_edit.first_name = editTeacherFormData.first_name.data
        teacher_to_edit.last_name = editTeacherFormData.last_name.data
        teacher_to_edit.birthdate = editTeacherFormData.birthdate.data
        #teacher_to_edit.teacher_in_group_Id = editTeacherFormData.teacher_in_group_Id.data

        db.session.commit()

        return redirect("/teachers")
    
    else:
        raise("Fatal Error")