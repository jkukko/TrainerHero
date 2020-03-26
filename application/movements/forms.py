from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MovementForm(FlaskForm):
    name = StringField("Movement name", [validators.Length(min=4)])
    muscleGroup = StringField("Muscle Group", [validators.Length(min=4)])
 
    class Meta:
        csrf = False