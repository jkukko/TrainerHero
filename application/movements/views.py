from flask import render_template, request, redirect, url_for

from application import app, db
from application.movements.models import Movement
from application.movements.forms import MovementForm

@app.route("/movements", methods=["GET"])
def movements_index():
    return render_template("movements/list.html", movements = Movement.query.all())

@app.route("/movements/new/")
def movement_form():
    return render_template("movements/new_movement.html", form = MovementForm())

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
    form = MovementForm(request.form)

    if not form.validate():
        return render_template("movements/new_movement.html", form = form)

    M = Movement(form.name.data, form.muscleGroup.data)

    db.session().add(M)
    db.session().commit()
  
    return redirect(url_for("movements_index"))