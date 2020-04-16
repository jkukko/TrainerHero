from application import db

#workout_movement = db.Table(
#    'workout_movement', 
#    db.Column('Workout.id', db.Integer, db.ForeignKey('Workout.id', ondelete='CASCADE'), primary_key=True),
#    db.Column('Movement.id', db.Integer, db.ForeignKey('Movement.id'), primary_key=True)
#)