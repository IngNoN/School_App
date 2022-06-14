from flask import Blueprint, redirect, render_template, request


from forms.addGroupOfTeachersForm import AddGroupOfTeachersForm
from models import DepartmentManager, GroupOfTeacher, db
from forms.editForm import EditGroupOfTeachersForm

import csv
import os

ROWS_PER_PAGE = 5


group_of_teachers_blueprint = Blueprint(
    "group_of_teachers_blueprint", __name__)


@group_of_teachers_blueprint.route("/groupOfTeachers", methods=["get", "post"])
def group_of_teachers():
    page = request.args.get('page', 1, type=int)

    group_of_teachers = GroupOfTeacher.query.order_by(GroupOfTeacher.title).\
        paginate(page=page, per_page=ROWS_PER_PAGE)
    addGroupOfTeachersData = AddGroupOfTeachersForm()

    return render_template("groupOfTeachers/groupOfTeachers.html",
                           group_of_teachers=group_of_teachers,
                           form=addGroupOfTeachersData)


add_group_of_teachers_blueprint = Blueprint(
    "add_group_of_teachers_blueprint", __name__)


@add_group_of_teachers_blueprint.route("/groupOfTeachers/add", methods=["get", "post"])
def add_group_of_teachers():
    addGroupOfTeachersData = AddGroupOfTeachersForm()
    department_managers = db.session.query(DepartmentManager).order_by(
        DepartmentManager.last_name).all()
    department_managers_list = [(dm.departmentManager_Id, dm.first_name + " " + dm.last_name)
                                for dm in department_managers]
    addGroupOfTeachersData.department_managers_Id.choices = department_managers_list
    if True:  # request.method == "POST":
        if addGroupOfTeachersData.validate_on_submit():
            groupOfTeachersData = GroupOfTeacher()
            groupOfTeachersData.title = addGroupOfTeachersData.title.data
            groupOfTeachersData.description = addGroupOfTeachersData.description.data
            groupOfTeachersData.subject = addGroupOfTeachersData.subject.data
            groupOfTeachersData.departmentManager_Id = \
                addGroupOfTeachersData.department_managers_Id.data
            # groupOfTeachersData.teacher_in_group_Id = addTeacherFormData.teacher_in_group_Id.data

            db.session.add(groupOfTeachersData)
            db.session.commit()

            return redirect("/groupOfTeachers")

        else:
            return render_template("groupOfTeachers/addGroupOfTeachersForm.html",
                                   form=addGroupOfTeachersData,
                                   department_managers=department_managers)


show_edit_group_of_teachers_blueprint = Blueprint(
    "show_edit_group_of_teachers_blueprint", __name__)


@show_edit_group_of_teachers_blueprint.route("/groupOfTeachers/edit")
def show_edit_group_of_teachers():
    global current_data
    editGroupOfTeachersData = EditGroupOfTeachersForm()
    current_data = editGroupOfTeachersData
    department_managers = db.session.query(DepartmentManager).order_by(
        DepartmentManager.departmentManager_Id).all()
    department_managers_list = [(dm.departmentManager_Id, dm.first_name + " " + dm.last_name)
                                for dm in department_managers]
    editGroupOfTeachersData.department_manager_Id.choices = department_managers_list
    # itemId auslesen
    group_of_teachers_Id = request.args["group_of_teachers_Id"]
    # Item laden
    group_of_teachers_to_edit = db.session.query(GroupOfTeacher).filter(
        GroupOfTeacher.group_of_teachers_Id == group_of_teachers_Id).first()
    # Form befüllen
    editGroupOfTeachersData.group_of_teachers_Id.data = group_of_teachers_Id
    editGroupOfTeachersData.title.data = group_of_teachers_to_edit.title
    editGroupOfTeachersData.description.data = group_of_teachers_to_edit.description
    editGroupOfTeachersData.subject.data = group_of_teachers_to_edit.subject
    # editGroupOfTeachersData.teacher_in_group_Id.data =\
    # group_of_teachers_to_edit.teacher_in_group_Id
    editGroupOfTeachersData.department_manager_Id.data =\
        group_of_teachers_to_edit.departmentManager_Id

    return render_template("/groupOfTeachers/editGroupOfTeacher.html",
                           form=editGroupOfTeachersData,
                           department_managers=department_managers)


submit_edit_group_of_teachers_blueprint = Blueprint(
    "submit_edit_group_of_teachers_blueprint", __name__)


@submit_edit_group_of_teachers_blueprint.route("/groupOfTeachers/edit", methods=["post"])
def submit_edit_group_of_teachers():
    editGroupOfTeachersData = EditGroupOfTeachersForm()
    department_managers = db.session.query(DepartmentManager).order_by(
        DepartmentManager.departmentManager_Id).all()
    department_managers_list = [(dm.departmentManager_Id, dm.first_name + " " + dm.last_name)
                                for dm in department_managers]
    editGroupOfTeachersData.department_manager_Id.choices = department_managers_list
    create_report_file(editGroupOfTeachersData)
    if editGroupOfTeachersData.validate_on_submit():
        # daten aus Form auslesen
        group_of_teachers_Id = editGroupOfTeachersData.group_of_teachers_Id.data
        group_of_teachers_to_edit = db.session.query(GroupOfTeacher).filter(
            GroupOfTeacher.group_of_teachers_Id == group_of_teachers_Id).first()
        # daten mit update in DB speichern
        group_of_teachers_to_edit.title = editGroupOfTeachersData.title.data
        group_of_teachers_to_edit.description = editGroupOfTeachersData.description.data
        group_of_teachers_to_edit.subject = editGroupOfTeachersData.subject.data
        # group_of_teachers_to_edit.teacher_in_group_Id =\
        # editGroupOfTeachersData.teacher_in_group_Id
        group_of_teachers_to_edit.departmentManager_Id =\
            editGroupOfTeachersData.department_manager_Id.data

        db.session.commit()

        return redirect("/groupOfTeachers")

    else:
        raise("Fatal Error")


def create_report_file(teacher_data):
    header = ["Data", "Previous Data", "New Data"]
    group_of_teachers_id = [
        "Group Of Teacher ID", current_data.group_of_teachers_Id.data,
        teacher_data.group_of_teachers_Id.data]
    title = ["Title", current_data.title.data,
             teacher_data.title.data]
    description = ["Description", current_data.description.data,
                   teacher_data.description.data]
    subject = ["Subject", current_data.subject.data,
               teacher_data.subject.data]
    department_manager_Id = ["Department Manager ID", current_data.department_manager_Id.data,
                             teacher_data.department_manager_Id.data]

    i = 0
    while os.path.exists("GroupOfTeacherEdit%s.csv" % i):
        i += 1
    f = open(f"GroupOfTeacherEdit{i}.csv", "w")

    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerow(group_of_teachers_id)
    writer.writerow(title)
    writer.writerow(description)
    writer.writerow(subject)
    writer.writerow(department_manager_Id)
