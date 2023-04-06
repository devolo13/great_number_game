import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Harry Potter was mid'
guessed_integer = None


@app.route('/', methods=["GET"])
def landing_page():
    session['number'] = random.randint(1, 100)
    return render_template('index.html', number=session['number'], guess=guessed_integer)


@app.route('/guess', methods=["GET", "POST"])
def guess():
    # USER HAS SUBMITTED A GUESS
    if not request.form['user_guess'].isdigit():
        # IF USER INPUTS NOT AN INTEGER
        guessed_integer = 'Not an integer'
    else:
        # USER SUBMITTED AN INTEGER. PARSE IT
        guessed_integer = int(request.form['user_guess'])
    return render_template('index.html', number=session['number'], guess=guessed_integer)


@app.route('/destroy_session')
def reset_session():
    # RESET SESSION COOKIES AND REDIRECT TO '/'
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
