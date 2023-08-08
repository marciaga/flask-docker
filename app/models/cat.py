from app import db


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    personality = db.Column(db.String)
    pet_count = db.Column(db.Integer, nullable=False, default=0)
    caretaker = db.relationship("Caretaker", back_populates="cats")
    caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))

    @classmethod
    def from_dict(cls, data_dict, caretaker=None):
        new_cat = cls(
            name=data_dict["name"],
            color=data_dict["color"],
            personality=data_dict["personality"],
            caretaker=caretaker
        )
        if "pet_count" in data_dict:
            new_cat.pet_count = data_dict["pet_count"]

        return new_cat

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            color=self.color,
            personality=self.personality,
            pet_count=self.pet_count,
            caretaker=self.caretaker.name if self.caretaker else ""
        )
        
    
