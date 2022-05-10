from email.headerregistry import Group
from flask import Blueprint, redirect, render_template, request


from forms.addGroupOfTeachersForm import AddGroupOfTeachersForm
from models import DepartmentManager, GroupOfTeacher, db
from forms.editForm import EditGroupOfTeachersForm

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
            groupOfTeachersData.departmentManager_Id = addGroupOfTeachersData.department_managers_Id.data
            #groupOfTeachersData.teacher_in_group_Id = addTeacherFormData.teacher_in_group_Id.data

            db.session.add(groupOfTeachersData)
            db.session.commit()
        
            return redirect("/groupOfTeachers")

        else:
            return render_template("groupOfTeachers/addGroupOfTeachersForm.html", form = addGroupOfTeachersData, department_managers = department_managers)


show_edit_group_of_teachers_blueprint = Blueprint("show_edit_group_of_teachers_blueprint", __name__)

@show_edit_group_of_teachers_blueprint.route("/groupOfTeachers/edit")
def show_edit_group_of_teachers():
    editGroupOfTeachersData = EditGroupOfTeachersForm()
    department_managers = db.session.query(DepartmentManager).order_by(DepartmentManager.departmentManager_Id).all()
    #itemId auslesen
    group_of_teachers_Id = request.args["group_of_teachers_Id"]
    #Item laden
    group_of_teachers_to_edit = db.session.query(GroupOfTeacher).filter(GroupOfTeacher.group_of_teachers_Id == group_of_teachers_Id).first()
    #Form befüllen
    editGroupOfTeachersData.group_of_teachers_Id.data = group_of_teachers_Id 
    editGroupOfTeachersData.title.data = group_of_teachers_to_edit.title
    editGroupOfTeachersData.description.data = group_of_teachers_to_edit.description
    editGroupOfTeachersData.subject.data = group_of_teachers_to_edit.subject
    #editGroupOfTeachersData.teacher_in_group_Id.data = group_of_teachers_to_edit.teacher_in_group_Id
    editGroupOfTeachersData.department_manager_Id.data = group_of_teachers_to_edit.departmentManager_Id

    return render_template("/groupOfTeachers/editGroupOfTeacher.html", form = editGroupOfTeachersData, department_managers = department_managers)

submit_edit_group_of_teachers_blueprint  = Blueprint("submit_edit_group_of_teachers_blueprint", __name__)

@submit_edit_group_of_teachers_blueprint.route("/groupOfTeachers/edit", methods=["post"])
def submit_edit_group_of_teachers():
    editGroupOfTeachersData = EditGroupOfTeachersForm()

    if editGroupOfTeachersData.validate_on_submit():
        #daten aus Form auslesen
        group_of_teachers_Id = editGroupOfTeachersData.group_of_teachers_Id.data
        group_of_teachers_to_edit = db.session.query(GroupOfTeacher).filter(GroupOfTeacher.group_of_teachers_Id == group_of_teachers_Id).first()
        #daten mit update in DB speichern
        group_of_teachers_to_edit.title = editGroupOfTeachersData.title.data
        group_of_teachers_to_edit.description = editGroupOfTeachersData.description.data
        group_of_teachers_to_edit.subject = editGroupOfTeachersData.subject.data
        #group_of_teachers_to_edit.teacher_in_group_Id = editGroupOfTeachersData.teacher_in_group_Id
        group_of_teachers_to_edit.departmentManager_Id = editGroupOfTeachersData.department_manager_Id.data

        db.session.commit()

        return redirect("/groupOfTeachers")
    
    else:
        raise("Fatal Error")