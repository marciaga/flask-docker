from app import db

class Caretaker(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String)
  cats = db.relationship("Cat", back_populates="caretaker")