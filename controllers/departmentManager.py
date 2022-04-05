from flask import Blueprint, redirect, render_template, request
from forms.addDepartmentMangerForm import addDepartmentMangerForm
from models import DepartmentManager, GroupOfTeacher, db
from forms.editForm import EditDepartmentManagersForm

department_managers_blueprint = Blueprint("department_managers_blueprint", __name__)

@department_managers_blueprint.route("/department_managers", methods=["get", "post"])
def department_managers():
    department_managers = db.session.query(DepartmentManager).all()
    addDepartmentMangerFormData = addDepartmentMangerForm()
    return render_template("departmentManagers/departmentManager.html",
    department_managers = department_managers,
    form = addDepartmentMangerFormData)


add_department_manager_blueprint = Blueprint("add_department_manager_blueprint", __name__)

@add_department_manager_blueprint.route("/department_managers/add", methods=["get", "post"])
def add_department_manager():
    addDepartmentMangerFormData = addDepartmentMangerForm()
    department_managers = db.session.query(DepartmentManager).all()
    if True: #request.method == "POST":
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
            return render_template("departmentManagers/addDepartmentManagerForm.html", form = addDepartmentMangerFormData)


show_edit_department_manager_blueprint = Blueprint("show_edit_department_manager_blueprint", __name__)

@show_edit_department_manager_blueprint.route("/department_managers/edit")
def show_edit_department_manager():
    editDepartmentManagerData = EditDepartmentManagersForm()
    #itemId auslesen
    departmentManager_Id = request.args["departmentManager_Id"]
    #Item laden
    teacher_to_edit = db.session.query(DepartmentManager).filter(DepartmentManager.departmentManager_Id == departmentManager_Id).first()
    #Form befüllen
    editDepartmentManagerData.departmentManager_Id.data = departmentManager_Id 
    editDepartmentManagerData.first_name.data = teacher_to_edit.first_name
    editDepartmentManagerData.last_name.data = teacher_to_edit.last_name
    editDepartmentManagerData.email_adress.data = teacher_to_edit.email_adress
    editDepartmentManagerData.department.data = teacher_to_edit.department

    return render_template("/departmentManagers/editDepartmentManagerForm.html", form = editDepartmentManagerData)

submit_edit_department_manager_blueprint = Blueprint("submit_edit_department_manager_blueprint", __name__)

@submit_edit_department_manager_blueprint.route("/department_managers/edit", methods=["post"])
def submit_edit_department_manager():
    editDepartmentManagerData = EditDepartmentManagersForm()

    if editDepartmentManagerData.validate_on_submit():
        #daten aus Form auslesen
        departmentManager_Id = editDepartmentManagerData.departmentManager_Id.data
        depaertment_manager_to_edit = db.session.query(DepartmentManager).filter(DepartmentManager.departmentManager_Id == departmentManager_Id).first()
        #daten mit update in DB speichern
        depaertment_manager_to_edit.first_name = editDepartmentManagerData.first_name.data
        depaertment_manager_to_edit.last_name = editDepartmentManagerData.last_name.data
        depaertment_manager_to_edit.email_adress = editDepartmentManagerData.email_adress.data
        depaertment_manager_to_edit.department = editDepartmentManagerData.department.data

        db.session.commit()

        return redirect("/department_managers")
    
    else:
        raise("Fatal Error")