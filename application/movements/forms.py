from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField

class MovementForm(FlaskForm):
    name = StringField("Movement name", [validators.Length(min=4)])
    muscleGroup = SelectField("Muscle Group", coerce=int)


    class Meta:
        csrf = False

