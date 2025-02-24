from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

# Tables of keyhole database
class Calendar(db.Model):
    __tablename__ = "calendar"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_cal = db.Column(db.Date, nullable=False)
    message = db.Column(db.String(150), nullable=False)
    
class Investments(db.Model):
    __tablename__ = "investments"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String(5), nullable=False)
    name_inv = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    profit = db.Column(db.Integer, nullable=False)

class Objectives(db.Model):
    __tablename__ = "objectives"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    objective = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.SmallInteger, nullable=False)

class Transactions(db.Model):
    __tablename__ = "transactions"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    months = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    trans_type = db.Column(Enum('income', 'expense', name='trans_type'), nullable=False)