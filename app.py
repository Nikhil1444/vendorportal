from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

FILE_PATH = r'data/Master sheet - Copy.xlsx'


# LOGIN PAGE

@app.route('/')
def login():
    return render_template('login.html')


# DASHBOARD

@app.route('/dashboard', methods=['POST'])
def dashboard():

    username = request.form['username']
    password = request.form['password']

    # ADMIN LOGIN

    if username == 'admin' and password == '1234':

        df = pd.read_excel(
            FILE_PATH,
            engine='openpyxl'
        )

        df.columns = df.columns.str.strip()

        # CONVERT ORDER QTY TO NUMBER

        df['ORDER QTY'] = pd.to_numeric(
            df['ORDER QTY'],
            errors='coerce'
        ).fillna(0)

        orders = df.to_dict(
            orient='records'
        )

        return render_template(
            'dashboard.html',
            orders=orders,
            title='Admin Dashboard'
        )

    return "Invalid Login"


# PENDING ORDERS

@app.route('/pending-orders')
def pending_orders():

    df = pd.read_excel(
        FILE_PATH,
        engine='openpyxl'
    )

    df.columns = df.columns.str.strip()

    df['ORDER QTY'] = pd.to_numeric(
        df['ORDER QTY'],
        errors='coerce'
    ).fillna(0)

    pending = df[
        df['STATUS']
        .astype(str)
        .str.lower()
        == 'pending'
    ]

    orders = pending.to_dict(
        orient='records'
    )

    return render_template(
        'dashboard.html',
        orders=orders,
        title='Pending Orders'
    )


# CURRENT ORDERS

@app.route('/current-orders')
def current_orders():

    df = pd.read_excel(
        FILE_PATH,
        engine='openpyxl'
    )

    df.columns = df.columns.str.strip()

    df['ORDER QTY'] = pd.to_numeric(
        df['ORDER QTY'],
        errors='coerce'
    ).fillna(0)

    current = df[
        df['STATUS']
        .astype(str)
        .str.lower()
        == 'partial'
    ]

    orders = current.to_dict(
        orient='records'
    )

    return render_template(
        'dashboard.html',
        orders=orders,
        title='Current Orders'
    )


# PRIORITY

@app.route('/priority/<level>')
def priority(level):

    df = pd.read_excel(
        FILE_PATH,
        engine='openpyxl'
    )

    df.columns = df.columns.str.strip()

    df['ORDER QTY'] = pd.to_numeric(
        df['ORDER QTY'],
        errors='coerce'
    ).fillna(0)

    filtered = df[
        df['PRIORITY']
        .astype(str)
        .str.lower()
        == level.lower()
    ]

    orders = filtered.to_dict(
        orient='records'
    )

    return render_template(
        'dashboard.html',
        orders=orders,
        title=level.upper() + ' Priority'
    )


# STATUS

@app.route('/status/<status>')
def status(status):

    df = pd.read_excel(
        FILE_PATH,
        engine='openpyxl'
    )

    df.columns = df.columns.str.strip()

    df['ORDER QTY'] = pd.to_numeric(
        df['ORDER QTY'],
        errors='coerce'
    ).fillna(0)

    filtered = df[
        df['STATUS']
        .astype(str)
        .str.lower()
        == status.lower()
    ]

    orders = filtered.to_dict(
        orient='records'
    )

    return render_template(
        'dashboard.html',
        orders=orders,
        title=status.capitalize() + ' Status'
    )


# RUN APP

if __name__ == '__main__':
    app.run(debug=True)