from application import app, db
from flask import render_template, request, url_for, redirect
from application.muscle_group.models import muscleGroup

@app.route("/musclegroups", methods=["GET"])
def musclegroup_index():
    return render_template("musclegroups/list.html", musclegroups = muscleGroup.query.all())

@app.route("/musclegroups/new/")
def musclegroup_form():
    return render_template("musclegroups/new.html")


@app.route("/musclegroups/", methods=["POST"])
def musclegourp_create():
    name = request.form.get("name")
    m = muscleGroup(name)
    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("musclegroup_index"))