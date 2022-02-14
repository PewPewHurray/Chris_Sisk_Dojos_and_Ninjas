from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route("/")
def index():

    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", all_dojos = dojos)

@app.route("/dojos/add", methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["dojo_name"]
    }
    Dojo.create(data)

    return redirect("/dojos")

@app.route("/dojos/<int:dojo_id>")
def dojo_profile(dojo_id):
    data = {
        "id": dojo_id
    }
    one_dojo_with_ninjas = Dojo.dojo_with_ninjas(data)
    print(one_dojo_with_ninjas)
    return render_template("dojo_ninjas.html", one_dojo = one_dojo_with_ninjas)