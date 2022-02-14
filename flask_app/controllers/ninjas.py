from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas/new")
def new_ninja():
    dojos = Dojo.get_all()

    return render_template("new_ninja.html", all_dojos = dojos)

@app.route("/ninjas/add", methods=["POST"])
def app_ninja():
    # data = {
    #     "first_name": request.form["first_name"],
    #     "last_name" : request.form["last_name"],
    #     "age": request.form["age"],
    #     "dojo": request.form["dojo_id"]
    # }
    dojo_id = request.form["dojo_id"]
    Ninja.create(request.form)
    print(request.form)


    return redirect(f"/dojos/{dojo_id}")