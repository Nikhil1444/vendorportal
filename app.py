from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# LOGIN PAGE

@app.route('/')
def login():
    return render_template('login.html')


# DASHBOARD

@app.route('/dashboard', methods=['POST'])
def dashboard():

    username = request.form['username']
    password = request.form['password']

    # LOGIN CHECK

    if username == "admin" and password == "1234":

        # READ EXCEL FILE

        df = pd.read_excel('data/Order.xlsx')

        # CONVERT TO LIST

        orders = df.to_dict(orient='records')

        return render_template(
            'dashboard.html',
            orders=orders
        )

    error = "Invalid Username or Password"

    return render_template(
        'login.html',
        error=error
    )


# LOGOUT

@app.route('/logout')
def logout():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)