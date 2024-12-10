from app import db
from datetime import datetime
from app.model.admins import Admins
from app.model.categories import Categories

class Products(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_by = db.Column(db.BigInteger, db.ForeignKey('admins.id', ondelete='CASCADE'), nullable=False)
    category_id = db.Column(db.BigInteger, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    product_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    contact = db.Column(db.String(100), nullable=True)
    img_file = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    admin = db.relationship('Admins', backref=db.backref('products', lazy=True, cascade="all, delete-orphan"))
    category = db.relationship('Categories', backref=db.backref('products', lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return '<Products {}>'.format(self.product_name)