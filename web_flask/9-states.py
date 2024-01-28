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


@app.route("/states", strict_slashes=False)
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


@app.route("/states/<id>", strict_slashes=False)
def cities_by_id_state(id):
    """
    displays all cities of the state requested
    """
    state = None
    states_dict = storage.all(State)
    id_str = str(id)
    for s in states_dict.values():
        if s.id == id_str:
            state = s
            break
    return render_template("9-states.html", state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
