from flask import Blueprint, redirect, render_template, request
from forms.addTeacherInGroupForm import AddTeacherInGroupForm
from models import GroupOfTeacher, TeacherInGroup, db, Teacher
from forms.editForm import EditTeacherInGroupForm

teacher_in_group_blueprint = Blueprint("teacher_in_group_blueprint", __name__)


@teacher_in_group_blueprint.route("/teacher_in_group", methods=["get", "post"])
def teacher_in_group():
    teacher_in_group = db.session.query(TeacherInGroup).all()

    return render_template("teacherInGroup/teacherInGroup.html",
                           teacher_in_group=teacher_in_group)


add_teacher_in_group_blueprint = Blueprint(
    "add_teacher_in_group_blueprint", __name__)


@add_teacher_in_group_blueprint.route("/teacher_in_group/add", methods=["get", "post"])
def add_teacher_in_group():
    addTeacherInGroupFormData = AddTeacherInGroupForm()
    teacher = db.session.query(Teacher).order_by(Teacher.teacher_Id).all()
    teacher_list = [(t.teacher_Id, t.first_name + " " + t.last_name)
                    for t in teacher]
    addTeacherInGroupFormData.teacher_id.choices = teacher_list

    group_of_teacher = db.session.query(GroupOfTeacher).order_by(
        GroupOfTeacher.group_of_teachers_Id).all()
    group_of_teacher_list = [(gt.group_of_teachers_Id, gt.title)
                             for gt in group_of_teacher]
    addTeacherInGroupFormData.group_of_teachers_Id.choices = group_of_teacher_list
    # teacher_in_group = db.session.query(TeacherInGroup).all()
    if True:  # request.method == "POST":
        if addTeacherInGroupFormData.validate_on_submit():
            teacherInGroupData = TeacherInGroup()
            teacherInGroupData.teacher_Id = addTeacherInGroupFormData.teacher_id.data
            teacherInGroupData.group_of_teachers_Id = \
                addTeacherInGroupFormData.group_of_teachers_Id.data

            db.session.add(teacherInGroupData)
            db.session.commit()

            return redirect("/teacher_in_group")

        else:
            return render_template("teacherInGroup/addTeacherInGroupForm.html",
                                   form=addTeacherInGroupFormData)


show_edit_teacher_in_group_blueprint = Blueprint(
    "show_edit_teacher_in_group_blueprint", __name__)


@show_edit_teacher_in_group_blueprint.route("/teacher_in_group/edit")
def show_edit_group_of_teachers():
    editTeacherInGroupData = EditTeacherInGroupForm()
    teacher = db.session.query(Teacher).order_by(Teacher.teacher_Id).all()
    teacher_list = [(t.teacher_Id, t.first_name + " " + t.last_name)
                    for t in teacher]
    editTeacherInGroupData.teacher_id.choices = teacher_list

    group_of_teacher = db.session.query(GroupOfTeacher).order_by(
        GroupOfTeacher.group_of_teachers_Id).all()
    group_of_teacher_list = [(gt.group_of_teachers_Id, gt.title)
                             for gt in group_of_teacher]
    editTeacherInGroupData.group_of_teachers_Id.choices = group_of_teacher_list
    # teacher_in_group = \
    # db.session.query(TeacherInGroup).order_by(TeacherInGroup.teacher_in_group_Id).all()
    # itemId auslesen
    teacher_in_group_Id = request.args["teacher_in_group_Id"]
    # Item laden
    teacher_in_group_to_edit = db.session.query(TeacherInGroup).filter(
        TeacherInGroup.teacher_in_group_Id == teacher_in_group_Id).first()
    # Form befüllen
    editTeacherInGroupData.teacher_in_group_Id.data = teacher_in_group_Id
    editTeacherInGroupData.teacher_id.data = teacher_in_group_to_edit.teacher_Id
    editTeacherInGroupData.group_of_teachers_Id.data = teacher_in_group_to_edit.group_of_teachers_Id

    return render_template("/teacherInGroup/editTeacherInGroup.html", form=editTeacherInGroupData)


submit_edit_teacher_in_group_blueprint = Blueprint(
    "submit_edit_teacher_in_group_blueprint", __name__)


@submit_edit_teacher_in_group_blueprint.route("/teacher_in_group/edit", methods=["post"])
def submit_edit_teacher_in_group():
    editTeacherInGroupData = EditTeacherInGroupForm()

    teacher = db.session.query(Teacher).order_by(Teacher.teacher_Id).all()
    teacher_list = [(t.teacher_Id, t.first_name + " " + t.last_name)
                    for t in teacher]
    editTeacherInGroupData.teacher_id.choices = teacher_list

    group_of_teacher = db.session.query(GroupOfTeacher).order_by(
        GroupOfTeacher.group_of_teachers_Id).all()
    group_of_teacher_list = [(gt.group_of_teachers_Id, gt.title)
                             for gt in group_of_teacher]
    editTeacherInGroupData.group_of_teachers_Id.choices = group_of_teacher_list

    if editTeacherInGroupData.validate_on_submit():
        # daten aus Form auslesen
        teacher_in_group_Id = editTeacherInGroupData.teacher_in_group_Id.data
        teacher_in_group_to_edit = db.session.query(TeacherInGroup).filter(
            TeacherInGroup.teacher_in_group_Id == teacher_in_group_Id).first()
        # daten mit update in DB speichern
        teacher_in_group_to_edit.teacher_Id = editTeacherInGroupData.teacher_id.data
        teacher_in_group_to_edit.group_of_teacher_Id =\
            editTeacherInGroupData.group_of_teachers_Id.data

        db.session.commit()

        return redirect("/teacher_in_group")

    else:
        raise("Fatal Error")
