#!/usr/bin/python3
"""Module to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state_list():
    data = {
            "storage": storage.all(State),
            "id": None
            }
    return render_template("9-states.html", data=data)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_states(id):
    cities = None
    name = None
    id_found = None  # Flag to check if id exists
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = storage.all(City)
        cities = [v for v in cities.values()]
    else:
        cities = State.cities

    if id in [v.id for v in storage.all(State).values()]:  # Check if id exists
        # Save name of the state
        name = {"n": v.name for v in storage.all(State).values() if v.id == id}
        id_found = "found!"
    else:
        id_found = None
    data = {
            "storage": storage.all(State),
            "cities": cities,
            "id": id,
            "id_found": id_found,
            "name": name
            }
    return render_template("9-states.html", data=data)


@app.teardown_appcontext
def remove_current_sql_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
