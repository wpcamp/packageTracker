from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, URL
from map.map import map


def fix_keys(x):
    list = []
    for key in x:
        list.append(key)
    return list

class ShippingForm(FlaskForm):
    sender = StringField("Sender", validators=[DataRequired()])
    recipient = StringField("Recipient", validators=[DataRequired()])
    origin = SelectField("Origin", choices= fix_keys(map.keys()), validators=[DataRequired()])
    destination = SelectField("Destination", choices=fix_keys(map.keys()), validators=[DataRequired()])
    express = BooleanField("Express Shipping")
    submit = SubmitField("Confirm")
