from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/dashboard', methods=['POST'])
def dashboard():

    username = request.form['username']
    password = request.form['password']

    # LOGIN CHECK

    if username == "admin" and password == "1234":
        return render_template('dashboard.html')

    # INVALID LOGIN

    error = "Invalid Username or Password"

    return render_template('login.html', error=error)


@app.route('/forgot-password')
def forgot_password():
    return """
    <h2>Forgot Password</h2>

    <p>
    Please contact Admin or EPD Team
    to reset your password.
    </p>
    """


@app.route('/logout')
def logout():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)