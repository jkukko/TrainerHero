from application import db
from application.models import Base

class muscleGroup(Base):

    __tablename__= "muscleGroup"

    name = db.Column(db.String(144), nullable=False)

    movement = db.relationship("Movement", backref="muscleGroup", lazy=True)

    def __init__(self, name):
        self.name = name
