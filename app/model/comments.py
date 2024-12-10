from enum import Enum
from app import db
from datetime import datetime
from app.model.articles import Articles

class StatusEnum(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class Comments(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_article = db.Column(db.BigInteger, db.ForeignKey('articles.id', ondelete='CASCADE'), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    comment = db.Column(db.Text, nullable=False)
    is_approved = db.Column(db.Boolean, nullable=True)
    status = db.Column(db.Enum(StatusEnum), default=StatusEnum.PENDING, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    article = db.relationship('Articles', backref=db.backref('comments', lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return '<Comments {}>'.format(self.username)