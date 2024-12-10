from app import db
from datetime import datetime
from app.model.admins import Admins

class Articles(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_by = db.Column(db.BigInteger, db.ForeignKey('admins.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    img_file = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=True)
    views = db.Column(db.Integer, default=0, nullable=False)
    author = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    admin = db.relationship('Admins', backref=db.backref('articles', lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return '<Articles {}>'.format(self.title)