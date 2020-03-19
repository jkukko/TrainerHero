from application import app, db
from flask import render_template, request, url_for, redirect
from application.movements.models import Movement

@app.route("/movements", methods=["GET"])
def movements_index():
    return render_template("movements/list.html", movements = Movement.query.all())

@app.route("/movements/new/")
def movement_form():
    return render_template("movements/new_movement.html")

@app.route("/movements/<movement_id>", methods=["POST"])
def add_movement_template(movement_id):
    m = Movement.query.get(movement_id)
    if m.isTemplate == True:
        m.isTemplate = False
    else:
        m.isTemplate = True
    db.session().commit()
    return redirect(url_for("movements_index"))


@app.route("/movements/", methods=["POST"])
def movement_create():
    name = request.form.get("name")
    muscleGroup = request.form.get("muscleGroup")

    M = Movement(name, muscleGroup) 

    db.session().add(M)
    db.session().commit()
  
    return redirect(url_for("movements_index"))