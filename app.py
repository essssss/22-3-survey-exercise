from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey 
app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


responses = []
 
@app.route("/")
def show_survey_intro():
    """Display intro to survey"""
    return render_template("intro.html", survey=survey)

@app.route("/begin", methods=["POST"])
def start_survey():
    """Clear responses and start survey"""
    responses=[]
    return redirect("question/0")

@app.route("/question/<int:question_id>")
def show_question(question_id):
    """Show question"""
    question=survey.questions[question_id]
    return render_template("question.html", survey=survey, question=question)

@app.route("/answer", methods=["POST"])
def show_next_question():
    """handle response and show next question"""

    # get response choice
    choice = request.form['answer']

    # add to responses
    responses.append(choice)

    if(len(responses)== len(survey.questions)):
        return redirect("/complete")

    return redirect(f"question/{len(responses)}")


@app.route("/complete")
def complete():
    """Survey complete. Show completion page."""

    return render_template("completion.html")

