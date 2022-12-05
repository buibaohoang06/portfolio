from flask import Blueprint, render_template, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import InputRequired
from models import db, Posts, Achievements

#WTForms 
class ContactForm(FlaskForm):
    name = StringField(validators=[InputRequired()], render_kw={"placeholder": "Name"})
    email = EmailField(validators=[InputRequired()], render_kw={"placeholder": "Email"})
    message = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Message"})

#Register Blueprint
indexbp = Blueprint("index", __name__, url_prefix="/")

#Routes
@indexbp.route('/', methods=['GET'])
def mainpage():
    return render_template("index.html")