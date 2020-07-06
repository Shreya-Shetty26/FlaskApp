from flask import Flask , render_template,request
from models import *


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/lecture4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html",flights=flights)

@app.route("/book",methods=["POST"])
def book():
    """Book a flight """

    #Get the name of passenger
    name = request.form.get(name)

    #Get the flight id from drop down

    try:
        flight_id = int(request.form.get(flight_id))
    except ValueError:
        return render_template("error.html",message="Invalid Flight number")

    #Check if the flight id is valid
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with id")

    #Add passenger.
    flight.add_passenger(name)
    return render_template("success.html")

@app.route("/flights")
def flights():
    """List of all flights"""

    flights = Flght.query.all()
    return render_template("flight.html",flights=flights)

@app.route("/flights/<int:flight_id>")
def flight():
    """List details about single flight"""

    #Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html",message="No such Flight")

    #Get allpassengers in taht flight
    #passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    passengers = flight.passengers()
    return render_template("flight.html",flight=flight,passengers=passengers)