from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'secret'

toolbar = DebugToolbarExtension(app)

responses = []

@app.route("/")
def show_survey_intro():
    return render_template("intro.html")
