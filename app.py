import logging

import flask

import forms

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def front_page():
    form = forms.ScheduledEmailForm()
    return flask.render_template('index.html', form=form)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
