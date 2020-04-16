from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SelectField, validators
from application.movements.models import Movement

class SetForm(FlaskForm):
    movement = SelectField('Movement', coerce=int)
    reps = IntegerField('Reps', [validators.required()])
    weigth = FloatField('Weigth', [validators.required()])