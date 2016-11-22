import logging

import flask

import forms
from repositories import emails

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def front_page():
    if flask.request.method == 'GET':
        form = forms.ScheduledEmailForm()
        return flask.render_template('index.html', form=form)

    logging.info(flask.request.form)
    form = forms.ScheduledEmailForm(flask.request.form)
    logging.info(form.validate())
    if form.validate():
        logging.info("Form is valid!")
        logging.info(form.data)
        emails.save_email(form.data)

    logging.info(form.errors)
    return flask.redirect('/')

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
