from flask import Blueprint, redirect, render_template, request
import sqlalchemy
from forms.addTeacherForm import AddTeacherForm
from models import GroupOfTeacher, Teacher, TeacherInGroup, db
from forms.editForm import EditTeacherForm

teachers_blueprint = Blueprint("teachers_blueprint", __name__)


@teachers_blueprint.route("/teachers", methods=["get", "post"])
def teachers():
    teachers = db.session.query(Teacher).all()
    addTeacherFormData = AddTeacherForm()

    return render_template("teachers/teachers.html",
                           teachers=teachers,
                           form=addTeacherFormData)


add_teachers_blueprint = Blueprint("add_teachers_blueprint", __name__)


@add_teachers_blueprint.route("/teachers/add", methods=["get", "post"])
def add_teachers():
    addTeacherFormData = AddTeacherForm()
    # teachers = db.session.query(Teacher).all()
    if True:  # request.method == "POST":
        if addTeacherFormData.validate_on_submit():
            teacherData = Teacher()
            teacherData.first_name = addTeacherFormData.first_name.data
            teacherData.last_name = addTeacherFormData.last_name.data
            teacherData.birthdate = addTeacherFormData.birthdate.data
            # teacherData.teacher_in_group_Id = addTeacherFormData.teacher_in_group_Id.data

            db.session.add(teacherData)
            db.session.commit()

            return redirect("/teachers")

        else:
            return render_template("teachers/addTeacherForm.html",
                                   form=addTeacherFormData)


show_edit_teachers_blueprint = Blueprint(
    "show_edit_teachers_blueprint", __name__)


@show_edit_teachers_blueprint.route("/teachers/edit")
def show_edit_teachers():
    editTeacherFormData = EditTeacherForm()
    global current_data
    current_data = editTeacherFormData
    # itemId auslesen
    teacher_Id = request.args["teacher_Id"]
    # Item laden
    teacher_to_edit = db.session.query(Teacher).filter(
        Teacher.teacher_Id == teacher_Id).first()
    # Form befüllen
    editTeacherFormData.teacher_Id.data = teacher_Id
    editTeacherFormData.first_name.data = teacher_to_edit.first_name
    editTeacherFormData.last_name.data = teacher_to_edit.last_name
    editTeacherFormData.birthdate.data = teacher_to_edit.birthdate
    # editTeacherFormData.teacher_in_group_Id.data = teacher_to_edit.teacher_in_group_Id

    group_of_teachers = db.session.query(GroupOfTeacher).filter(
        sqlalchemy.and_(TeacherInGroup.group_of_teachers_Id == GroupOfTeacher.group_of_teachers_Id,
                    TeacherInGroup.teacher_Id == teacher_Id))

    return render_template("/teachers/editTeacherForm.html", form=editTeacherFormData,
                           group_of_teachers=group_of_teachers)


submit_edit_teachers_blueprint = Blueprint(
    "submit_edit_teachers_blueprint", __name__)


@submit_edit_teachers_blueprint.route("/teachers/edit", methods=["post"])
def submit_edit_teachers():
    editTeacherFormData = EditTeacherForm()
    create_report_file(editTeacherFormData)
    if editTeacherFormData.validate_on_submit():
        # daten aus Form auslesen
        teacher_Id = editTeacherFormData.teacher_Id.data
        teacher_to_edit = db.session.query(Teacher).filter(
            Teacher.teacher_Id == teacher_Id).first()
        # daten mit update in DB speichern
        teacher_to_edit.first_name = editTeacherFormData.first_name.data
        teacher_to_edit.last_name = editTeacherFormData.last_name.data
        teacher_to_edit.birthdate = editTeacherFormData.birthdate.data
        # teacher_to_edit.teacher_in_group_Id = editTeacherFormData.teacher_in_group_Id.data

        db.session.commit()

        return redirect("/teachers")

    else:
        raise("Fatal Error")

import pdfkit


def create_report_file(teacher_data):
    table_html = """<!DOCTYPE html>
    <html>
    <head>
    <style>
    table, th, td {
    border: 1px solid black;
    }
    
    table {
    width: 100%;
    }
    </style>
    </head>
    <body>
    
    <h2>Sample Table</h2>
    
    <table>
    <tr>
        <th>Field 1</th>
        <th>Field 2</th>
    </tr>
    <tr>
        <td>x1</td>
        <td>x2</td>
    </tr>
    <tr>
        <td>x3</td>
        <td>x4</td>
    </tr>
    </table>
    
    </body>
    </html>
    """
    
    pdfkit.from_string(table_html, output_path="sample_table.pdf")
    """f = open("test.txt", 'w')
    f.write("old " + current_data.first_name.data + "\n")
    f.write("\n")
    f.write("new " + teacher_data.first_name.data)
    f.close()"""
