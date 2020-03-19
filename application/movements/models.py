from application import db

class Movement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    muscleGroup = db.Column(db.String(144), nullable=False)
    isTemplate = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, m):
        self.name = name
        self.muscleGroup = m
        self.isTemplate = False


