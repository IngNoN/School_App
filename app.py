from flask import Flask, render_template
from models import Teacher, db

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/todoItemApp"
db.init_app(app)


@app.route("/", methods=["get", "post"])
def index():
    return render_template("index.html")

@app.route("/teachers")
def teachers():
    teachers = db.session.query(Teacher).all()
    return render_template("teachers.html",
    teachers = teachers)

app.run(debug=True)