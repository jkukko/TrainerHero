from application import db
from application.models import Base
#from application.associations import workout_movement


class Workout(Base):
    name = db.Column(db.String(144), nullable=False)
    
    #movenent = db.relationship('Movement', secondary='workout_movement', back_populates='workouts', cascade="all, delete-orphan", lazy=True, single_parent=True)


    def __init__(self, name):
        self.name = name
