from extension import db  
''' This imports the db object from extension.py, which looks like this:
Why do we use extension.py?

If we import db from app.py, it creates a circular import error.
Keeping db separate allows it to be imported anywhere (e.g., in models.py and routes.py) without issues.'''

class Friend(db.Model):
    '''Friend is a class that represents a table in the database.
db.Model makes this class a SQLAlchemy model.
 This means SQLAlchemy will create a table named friend (by default, table names are lowercase versions of class names).'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "gender": self.gender,
            "image_url": self.image_url
        }
    
    '''Flask returns Python objects by default, but APIs send data in JSON format.'''
