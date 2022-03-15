from flask import Blueprint, Flask, render_template

index_blueprint = Blueprint("index_blueprint", __name__)


@index_blueprint.route("/", methods=["get", "post"])
def index():
    return render_template("index.html")
