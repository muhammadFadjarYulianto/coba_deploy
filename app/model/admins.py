from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Admins(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    gender = db.Column(db.Enum('Laki-Laki', 'Perempuan'), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Admins {}>'.format(self.name)
    
    def setPassword(self,password):
        self.password = generate_password_hash(password)

    def checkPassword(self,password):
        return check_password_hash(self.password,password)