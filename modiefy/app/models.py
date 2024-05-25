from . import db

class USER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(60))
    summary = db.Column(db.String(600))
