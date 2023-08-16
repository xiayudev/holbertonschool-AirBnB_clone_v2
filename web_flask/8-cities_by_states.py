#!/usr/bin/python3
"""Module to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    return render_template("7-states_list.html", storages=storage.all(State))


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    cities = None
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = storage.all(City)
        cities = [v for v in cities.values()]
    else:
        cities = State.cities
    data = {
            "storage": storage.all(State),
            "cities": cities
            }
    return render_template("8-cities_by_states.html", data=data)


@app.teardown_appcontext
def remove_current_sql_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
