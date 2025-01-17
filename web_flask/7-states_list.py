#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    calls storage.close() method
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    displays all states
    """
    states_dict = storage.all(State)
    list_states = []
    for state in states_dict.values():
        list_states.append(state)
    sorted_states = sorted(list_states, key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
