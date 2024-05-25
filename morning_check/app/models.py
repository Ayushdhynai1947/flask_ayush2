from . import db

class USER(db.Model):
    __tablename__ = 'summary'
    emp_no = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(14), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)