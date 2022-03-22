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

        itemIdToDelete = DeleteItemFormObj.teacher_Id.data

        itemToDelete = db.session.query(Teacher).filter(Teacher.teacher_Id == itemIdToDelete)
        itemToDelete.delete()
        db.session.commit()
        
    else:
        print("Fatal Error")

    return redirect("/teachers")