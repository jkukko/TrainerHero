from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SelectField, validators

class SetForm(FlaskForm):
    movement = SelectField('Movement', coerce=int)
    reps = IntegerField('Reps', [validators.required()])
    weigth = FloatField('Weigth', [validators.required()])