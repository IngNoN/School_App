from flask import Flask
from models import db
from controllers.index import index_blueprint
from controllers.teachers import teachers_blueprint, add_teachers_blueprint, show_edit_teachers_blueprint, submit_edit_teachers_blueprint
from controllers.departmentManager import department_managers_blueprint, add_department_manager_blueprint, show_edit_department_manager_blueprint, submit_edit_department_manager_blueprint
from controllers.groupOfTeachers import group_of_teachers_blueprint, add_group_of_teachers_blueprint, show_edit_group_of_teachers_blueprint, submit_edit_group_of_teachers_blueprint
from controllers.teacherInGroup import teacher_in_group_blueprint, add_teacher_in_group_blueprint
from controllers.delete import delete_teacher_blueprint, delete_department_manager_blueprint, delete_group_of_teachers_blueprint, delete_teacher_in_group_blueprint

app = Flask(__name__)

app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/school_app"
db.init_app(app)

app.register_blueprint(index_blueprint)
app.register_blueprint(teachers_blueprint)
app.register_blueprint(add_teachers_blueprint)
app.register_blueprint(department_managers_blueprint)
app.register_blueprint(add_department_manager_blueprint)
app.register_blueprint(group_of_teachers_blueprint)
app.register_blueprint(add_group_of_teachers_blueprint)
app.register_blueprint(teacher_in_group_blueprint)
app.register_blueprint(add_teacher_in_group_blueprint)

app.register_blueprint(delete_teacher_blueprint)
app.register_blueprint(delete_department_manager_blueprint)
app.register_blueprint(delete_group_of_teachers_blueprint)
app.register_blueprint(delete_teacher_in_group_blueprint)

app.register_blueprint(show_edit_teachers_blueprint)
app.register_blueprint(submit_edit_teachers_blueprint)
app.register_blueprint(show_edit_department_manager_blueprint)
app.register_blueprint(submit_edit_department_manager_blueprint)
app.register_blueprint(show_edit_group_of_teachers_blueprint)
app.register_blueprint(submit_edit_group_of_teachers_blueprint)
app.run(debug=True)