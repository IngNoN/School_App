from flask import Blueprint, redirect, render_template, request
from forms.addDepartmentMangerForm import addDepartmentMangerForm
from models import DepartmentManager, db, GroupOfTeacher
from forms.editForm import EditDepartmentManagersForm

import csv
import os

ROWS_PER_PAGE = 5

department_managers_blueprint = Blueprint(
    "department_managers_blueprint", __name__)


@department_managers_blueprint.route("/department_managers", methods=["get", "post"])
def department_managers():
    department_managers = db.session.query(DepartmentManager).all()

    page = request.args.get('page', 1, type=int)

    department_managers = DepartmentManager.query.paginate(
        page=page, per_page=ROWS_PER_PAGE)

    addDepartmentMangerFormData = addDepartmentMangerForm()
    return render_template("departmentManagers/departmentManager.html",
                           department_managers=department_managers,
                           form=addDepartmentMangerFormData)


add_department_manager_blueprint = Blueprint(
    "add_department_manager_blueprint", __name__)


@add_department_manager_blueprint.route("/department_managers/add", methods=["get", "post"])
def add_department_manager():
    addDepartmentMangerFormData = addDepartmentMangerForm()

    group_of_teacher = db.session.query(GroupOfTeacher).order_by(
        GroupOfTeacher.title).all()
    group_of_teacher_list = [(gt.group_of_teachers_Id, gt.title)
                             for gt in group_of_teacher]
    addDepartmentMangerFormData.department.choices = group_of_teacher_list
    if request.method == "POST":
        if addDepartmentMangerFormData.validate_on_submit():
            DepartmentManagerData = DepartmentManager()
            DepartmentManagerData.first_name = addDepartmentMangerFormData.first_name.data
            DepartmentManagerData.last_name = addDepartmentMangerFormData.last_name.data
            DepartmentManagerData.email_adress = addDepartmentMangerFormData.email_adress.data
            DepartmentManagerData.department = addDepartmentMangerFormData.department.data

            db.session.add(DepartmentManagerData)
            db.session.commit()

            return redirect("/department_managers")

        else:
            return render_template("departmentManagers/addDepartmentManagerForm.html",
                                   form=addDepartmentMangerFormData)
    else:
        return render_template("departmentManagers/addDepartmentManagerForm.html",
                               form=addDepartmentMangerFormData)


show_edit_department_manager_blueprint = Blueprint(
    "show_edit_department_manager_blueprint", __name__)


@show_edit_department_manager_blueprint.route("/department_managers/edit")
def show_edit_department_manager():
    global current_data
    editDepartmentManagerData = EditDepartmentManagersForm()
    current_data = editDepartmentManagerData
    # itemId auslesen
    departmentManager_Id = request.args["departmentManager_Id"]
    # Item laden
    teacher_to_edit = db.session.query(DepartmentManager).filter(
        DepartmentManager.departmentManager_Id == departmentManager_Id).first()
    # Form befüllen
    editDepartmentManagerData.departmentManager_Id.data = departmentManager_Id
    editDepartmentManagerData.first_name.data = teacher_to_edit.first_name
    editDepartmentManagerData.last_name.data = teacher_to_edit.last_name
    editDepartmentManagerData.email_adress.data = teacher_to_edit.email_adress
    editDepartmentManagerData.department.data = teacher_to_edit.department

    return render_template("/departmentManagers/editDepartmentManagerForm.html",
                           form=editDepartmentManagerData)


submit_edit_department_manager_blueprint = Blueprint(
    "submit_edit_department_manager_blueprint", __name__)


@submit_edit_department_manager_blueprint.route("/department_managers/edit", methods=["post"])
def submit_edit_department_manager():
    editDepartmentManagerData = EditDepartmentManagersForm()
    create_report_file(editDepartmentManagerData)
    if editDepartmentManagerData.validate_on_submit():
        # daten aus Form auslesen
        departmentManager_Id = editDepartmentManagerData.departmentManager_Id.data
        depaertment_manager_to_edit = db.session.query(DepartmentManager).filter(
            DepartmentManager.departmentManager_Id == departmentManager_Id).first()
        # daten mit update in DB speichern
        depaertment_manager_to_edit.first_name = editDepartmentManagerData.first_name.data
        depaertment_manager_to_edit.last_name = editDepartmentManagerData.last_name.data
        depaertment_manager_to_edit.email_adress = editDepartmentManagerData.email_adress.data
        depaertment_manager_to_edit.department = editDepartmentManagerData.department.data

        db.session.commit()

        return redirect("/department_managers")

    else:
        raise("Fatal Error")


def create_report_file(teacher_data):
    header = ["Data", "Previous Data", "New Data"]
    department_manager_id = [
        "Department Manager ID", current_data.departmentManager_Id.data,
        teacher_data.departmentManager_Id.data]
    first_name = ["First Name", current_data.first_name.data,
                  teacher_data.first_name.data]
    last_name = ["Last Name", current_data.last_name.data,
                 teacher_data.last_name.data]
    department = ["Department", current_data.department.data,
                  teacher_data.department.data]
    email_adress = ["E-Mail Adress", current_data.email_adress.data,
                    teacher_data.email_adress.data]

    i = 0
    while os.path.exists("DepartmentManagerEdit%s.csv" % i):
        i += 1
    f = open(f"DepartmentManagerEdit{i}.csv", "w")

    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerow(department_manager_id)
    writer.writerow(first_name)
    writer.writerow(last_name)
    writer.writerow(email_adress)
    writer.writerow(department)
