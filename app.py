from flask import Flask

app = Flask(__name__, static_folder="static", template_folder="template")

app.config['SECRET_KEY'] = "mRV5IOgl62HcXP0lDaUbzzk5zx4316OpGYvF8BHQBsNr41z"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"