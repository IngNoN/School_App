from flask import Blueprint, redirect, render_template
from forms.addDepartmentMangerForm import addDepartmentMangerForm
from models import DepartmentManager, db

department_managers_blueprint = Blueprint("department_managers_blueprint", __name__)

@department_managers_blueprint.route("/department_managers", methods=["get", "post"])
def department_managers():
    department_managers = db.session.query(DepartmentManager).all()
    return render_template("departmentManagers.html",
    department_managers = department_managers)


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
            return render_template("addDepartmentManagerForm.html", form = addDepartmentMangerFormData)

    return render_template("addTeacherForm.html",
        form = addTeacherFormData,
        teacher = teachers)
            