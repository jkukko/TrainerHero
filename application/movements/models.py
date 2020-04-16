from application import db
from application.models import Base
#from application.associations import workout_movement

class Movement(Base):
    name = db.Column(db.String(144), nullable=False)
    isTemplate = db.Column(db.Boolean, nullable=False)

    musclegroup_id = db.Column(db.Integer, db.ForeignKey('muscleGroup.id'), nullable=False)
    sets = db.relationship('Set', backref='movement', lazy=True)
    #workout = db.relationship('Workout', secondary='workout_movement', back_populates='movement', lazy=True, single_parent=True)
    

    def __init__(self, name, m):
        self.name = name
        self.musclegroup_id = m
        self.isTemplate = False


