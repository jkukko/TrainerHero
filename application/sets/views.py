from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.sets.models import Set
from application.movements.models import Movement
from application.sets.forms import SetForm

@app.route("/sets", methods=["GET"])
@login_required
def sets_index():
    return render_template("sets/list.html", sets=set.query.all())

@app.route("/sets/new", methods=["GET"])
@login_required
def set_form():
    m = Movement.query.all()
    names = [(i.id, i.name) for i in m]
    form = SetForm()
    form.movement.choices = names
    return render_template("sets/new.html", form=form)

@app.route("/sets/", methods=["POST"])
@login_required
def set_create():
    m = Movement.query.all()
    names = [(i.id, i.name) for i in m]
    form = SetForm(request.form)
    form.movement.choices = names

    #if not form.validate():
    #    return render_template("sets/new.html", form=form)

    S = Set(form.reps.data, form.weigth.data, form.movement.data)
    db.session().add(S)
    db.session().commit()

    return redirect(url_for("set_form"))

    