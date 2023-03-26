# If your application requires a database, define 
# your database models and their relationships in 
# models.py using an ORM like SQLAlchemy.
from application import db
from datetime import datetime

class DailyTemperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
#    date = db.Column(db.Date, nullable=False, unique=False)
    timestamp = db.Column(db.DateTime, nullable=True, unique=False)
    temperature = db.Column(db.Float, nullable=False)

    def __repr__(self):
#        return f'<DailyTemperature {self.date} {self.temperature}>'
        return f'<DailyTemperature {self.timestamp} {self.temperature}>'
  
