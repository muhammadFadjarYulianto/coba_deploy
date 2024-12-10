from app import db
from datetime import datetime

class Categories(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Categories {}>'.format(self.category_name)