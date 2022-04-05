from flask import Blueprint, redirect
from forms.deleteForm import DeleteItemForm
from models import DepartmentManager, GroupOfTeacher, Teacher, TeacherInGroup, db


delete_teacher_blueprint = Blueprint("delete_teacher_blueprint", __name__)

@delete_teacher_blueprint.route("/teachers/delete", methods=["post"])
def delete_teacher():
    print("Hello World")
    DeleteItemData = DeleteItemForm()
    if DeleteItemData.validate_on_submit:
        print("gültig")
        #db objekt holen
        #delete command ausführen

        teacher_Id_to_delete = DeleteItemData.teacher_Id.data

        teacher_to_delte = db.session.query(Teacher).filter(Teacher.teacher_Id == teacher_Id_to_delete)
        teacher_to_delte.delete()
        db.session.commit()
        
    else:
        print("Fatal Error")

    return redirect("/teachers")

delete_department_manager_blueprint = Blueprint("delete_department_manager_blueprint", __name__)

@delete_department_manager_blueprint.route("/department_managers/delete", methods=["post"])
def delete_department_manager():
    DeleteItemData = DeleteItemForm()
    if DeleteItemData.validate_on_submit:
        print("gültig")
        #db objekt holen
        #delete command ausführen

        department_manager_Id_to_delete = DeleteItemData.departmentManager_Id.data

        department_manager_to_delte = db.session.query(DepartmentManager).filter(DepartmentManager.departmentManager_Id == department_manager_Id_to_delete)
        department_manager_to_delte.delete()
        db.session.commit()
        
    else:
        print("Fatal Error")

    return redirect("/department_managers")

delete_group_of_teachers_blueprint = Blueprint("delete_group_of_teachers_blueprint", __name__)

@delete_group_of_teachers_blueprint.route("/groupOfTeachers/delete", methods=["post"])
def delete_group_of_teachers():
    DeleteItemData = DeleteItemForm()
    if DeleteItemData.validate_on_submit:
        print("gültig")
        #db objekt holen
        #delete command ausführen

        group_of_teachers_Id_to_delete = DeleteItemData.group_of_teachers_Id.data

        group_of_teachers_to_delte = db.session.query(GroupOfTeacher).filter(GroupOfTeacher.group_of_teachers_Id == group_of_teachers_Id_to_delete)
        group_of_teachers_to_delte.delete()
        db.session.commit()
        
    else:
        print("Fatal Error")

    return redirect("/groupOfTeachers")

delete_teacher_in_group_blueprint = Blueprint("delete_teacher_in_group_blueprint", __name__)

@delete_teacher_in_group_blueprint.route("/teacher_in_group/delete", methods=["post"])
def delete_teacher_in_group():
    DeleteItemData = DeleteItemForm()
    if DeleteItemData.validate_on_submit:
        print("gültig")
        #db objekt holen
        #delete command ausführen

        teacher_in_group_Id_to_delete = DeleteItemData.teacher_in_group_Id.data

        teacher_in_group_to_delete = db.session.query(TeacherInGroup).filter(TeacherInGroup.teacher_in_group_Id == teacher_in_group_Id_to_delete)
        teacher_in_group_to_delete.delete()
        db.session.commit()
        
    else:
        print("Fatal Error")

    return redirect("/teacher_in_group")