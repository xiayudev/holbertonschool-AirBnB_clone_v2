#!/usr/bin/python3
"""Module to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def cities_by_states():
    cities = None
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = storage.all(City)
        cities = [v for v in cities.values()]
    else:
        cities = State.cities
    data = {
        "states": storage.all(State),
        "cities": cities,
        "amenities": storage.all(Amenity)
    }
    return render_template("10-hbnb_filters.html", data=data)


@app.teardown_appcontext
def remove_current_sql_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
