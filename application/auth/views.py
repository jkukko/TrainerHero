from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, CreateAccount

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/newuser", methods = ["GET", "POST"])
def auth_create_user():
    if request.method == "GET":
        return render_template("auth/register.html", form = CreateAccount())
    
    form = CreateAccount(request.form)

    u = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if u:
        return render_template("auth/register.html", form=form, error="User already exists")


    new_user = User(form.name.data, form.username.data, form.password.data)
    db.session().add(new_user)
    db.session().commit()

    return redirect(url_for("index"))
