from ext import create_app, db
from models import User, Feedback

app = create_app()

with app.app_context():
    
    db.create_all()
