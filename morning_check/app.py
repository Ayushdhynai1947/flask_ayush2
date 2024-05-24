from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ayush@localhost/product'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Define the summary model
class Summary(db.Model):
    __tablename__ = 'summary'
    emp_no = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(14), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define a route to fetch all summaries
@app.route('/summaries', methods=['GET'])
def get_summaries():
    summaries = Summary.query.all()
    result = [
        {
            "emp_no": summary.emp_no,
            "product_name": summary.product_name,
            "first_name": summary.first_name,
            "last_name": summary.last_name
        } for summary in summaries
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
