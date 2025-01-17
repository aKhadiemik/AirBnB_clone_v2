#!/usr/bin/python3
"""
Flask application with route to states list
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


#Route for listing states
@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order
        
       Returns:
            str: Rendered HTML content.
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown
       
       Args:
            exception (Exception): An exception, if any, that occurred during
            processing.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
