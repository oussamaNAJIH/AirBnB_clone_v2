#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    calls storage.close() method
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    displays all statesn amenties and places
    """
    list_states = storage.all(State).values()
    list_amenities = storage.all(Amenity).values()
    list_places = storage.all(Place).values()
    return render_template("100-hbnb.html", states=list_states,
                           amenities=list_amenities, places=list_places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)