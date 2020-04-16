from application import db
from application.models import Base

class Movement(Base):
    name = db.Column(db.String(144), nullable=False)
    isTemplate = db.Column(db.Boolean, nullable=False)

    musclegroup_id = db.Column(db.Integer, db.ForeignKey('muscleGroup.id'), nullable=False)
    sets = db.relationship('Set', backref='movement', lazy=True)
    

    def __init__(self, name, m):
        self.name = name
        self.musclegroup_id = m
        self.isTemplate = False


