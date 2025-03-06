from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"User('{self.name}', {self.points} points)"
    
class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    points_required = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Reward('{self.name}', {self.points_required} points)"