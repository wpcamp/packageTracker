from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .config import Config
from .shipping_form import ShippingForm
from .models import db, Package

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
#ran into NameError = db not defined, we forgot to import
migrate = Migrate(app, db)

@app.route("/")
def index():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)


@app.route("/new_package", methods=["GET", "POST"])
def new_package_route():
    form = ShippingForm()
    # print("new package route")
    # print(form.data)
    if form.validate_on_submit():
        # print("This worked")
        data = form.data
        new_package = Package(sender=data["sender"],
                              recipient=data["recipient"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')
    return render_template('shipping_request.html', form=form)
