from flask import Flask, render_template
from .config import Config
from .shipping_form import ShippingForm


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"


@app.route("/new_package", methods=["GET", "POST"])
def new_package_route():
    form = ShippingForm()
    return render_template('shipping_request.html', form=form)