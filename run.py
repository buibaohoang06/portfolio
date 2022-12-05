from app import app
from index import indexbp
import os
from models import db

app.register_blueprint(indexbp)

#For development only
if __name__ == "__main__":
    if os.path.exists("database.db") == False:
        with app.app_context():
            db.create_all()
    app.run(debug=True, port=80, host="0.0.0.0")