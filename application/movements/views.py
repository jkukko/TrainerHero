from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.movements.models import Movement
from application.movements.forms import MovementForm
from application.muscleGroup.models import muscleGroup


@app.route("/movements", methods=["GET"])
@login_required
def movements_index():
    return render_template("movements/list.html", movements = Movement.query.all())

@app.route("/movements/new/", methods =["GET"])
@login_required
def movement_form():
    m = muscleGroup.query.all()
    names = [(i.id, i.name) for i in m]
    form = MovementForm()
    form.muscleGroup.choices = names
    return render_template("movements/new.html", form = form)



@app.route("/movements/delete/<movement_id>", methods=["POST"])
@login_required
def remove_movement(movement_id):
    m = Movement.query.get(movement_id)
    
    db.session().delete(m)
    db.session().commit()

    return redirect(url_for("movements_index"))
    
@app.route("/movements/<movement_id>", methods=["POST"])
@login_required
def add_movement_template(movement_id):
    m = Movement.query.get(movement_id)
    if m.isTemplate == True:
        m.isTemplate = False
    else:
        m.isTemplate = True
    db.session().commit()
    return redirect(url_for("movements_index"))


@app.route("/movements/", methods=["POST"])
@login_required
def movement_create():
    m = muscleGroup.query.all()
    names = [(i.id, i.name) for i in m]
    form = MovementForm(request.form)
    form.muscleGroup.choices = names

    if not form.validate():
        return render_template("movements/new.html", form = form)
    mg = form.muscleGroup.data
    M = Movement(form.name.data, form.muscleGroup.data)

    db.session().add(M)
    db.session().commit()
  
    return redirect(url_for("movements_index"))