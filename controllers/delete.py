from flask import Blueprint, redirect
from forms.deleteForm import DeleteItemForm
from models import Teacher, db


delete_blueprint = Blueprint("delete_blueprint", __name__)

@delete_blueprint.route("/delete", methods=["post"])
def deleteItem():
    print("Hello World")
    DeleteItemFormObj = DeleteItemForm()
    if DeleteItemFormObj.validate_on_submit:
        print("gültig")
        #db objekt holen
        #delete command ausführen

        teacher_Id_to_delete = DeleteItemFormObj.teacher_Id.data

        teacher_to_delte = db.session.query(Teacher).filter(Teacher.teacher_Id == teacher_Id_to_delete)
        teacher_to_delte.delete()
        db.session.commit()
        
    else:
        print("Fatal Error")

    return redirect("/teachers")