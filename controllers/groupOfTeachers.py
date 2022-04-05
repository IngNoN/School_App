from flask import Blueprint, redirect, render_template

from forms.addGroupOfTeachersForm import AddGroupOfTeachersForm
from models import DepartmentManager, GroupOfTeacher, db

group_of_teachers_blueprint = Blueprint("group_of_teachers_blueprint", __name__)

@group_of_teachers_blueprint.route("/groupOfTeachers", methods=["get", "post"])
def group_of_teachers():
    group_of_teachers = db.session.query(GroupOfTeacher).all()
    addGroupOfTeachersData = AddGroupOfTeachersForm()

    return render_template("groupOfTeachers/groupOfTeachers.html",
    group_of_teachers = group_of_teachers,
    form = addGroupOfTeachersData)

add_group_of_teachers_blueprint = Blueprint("add_group_of_teachers_blueprint", __name__)

@add_group_of_teachers_blueprint.route("/groupOfTeachers/add", methods=["get", "post"])
def add_group_of_teachers():
    addGroupOfTeachersData = AddGroupOfTeachersForm()
    teachers = db.session.query(GroupOfTeacher).all()
    department_managers = db.session.query(DepartmentManager).order_by(DepartmentManager.departmentManager_Id).all()
    if True: #request.method == "POST":
        if addGroupOfTeachersData.validate_on_submit():
            groupOfTeachersData = GroupOfTeacher()
            groupOfTeachersData.title = addGroupOfTeachersData.title.data
            groupOfTeachersData.description = addGroupOfTeachersData.description.data
            groupOfTeachersData.subject = addGroupOfTeachersData.subject.data
            #groupOfTeachersData.teacher_in_group_Id = addTeacherFormData.teacher_in_group_Id.data

            db.session.add(groupOfTeachersData)
            db.session.commit()
        
            return redirect("/groupOfTeachers")

        else:
            return render_template("groupOfTeachers/addGroupOfTeachersForm.html", form = addGroupOfTeachersData, department_managers = department_managers)