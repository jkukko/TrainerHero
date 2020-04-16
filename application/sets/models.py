from application import db
from application.models import Base

class Set(Base):

    __tablename__ = "sets"

    reps = db.Column(db.Integer)
    weigth = db.Column(db.Float, nullable=False)

    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'), nullable=False)


    def __init__(self, reps, weigth, movement_id):
        self.reps = reps
        self.weigth = weigth
        self.movement_id = movement_id 