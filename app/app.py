from flask import Flask, render_template, request, url_for, redirect, session
import os
from dotenv import load_dotenv
import pandas as pd
from pandas import read_sql
from sqlalchemy import create_engine, text
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from db_functions import update_or_create_user

load_dotenv()  # Load environment variables from .env file

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}

connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(
        connection_string,
        connect_args=connect_args,

)

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)

@app.route('/')
def mainpage():
    return render_template('index.html')

@app.route('/auth')
def auth():
    return render_template('auth.html')

df = pd.read_csv('/home/helen_zheng/flask_e2e_project/data/cleaned_data.csv')
@app.route('/hiv')
def hiv(data=df):
    data = data.sample(50)
    return render_template('hiv.html', data=data)

@app.route('/aids')
def aids(data=df):
    data = data.sample(50)
    return render_template('aids.html', data=data)

@app.route('/death')
def death(data=df):
    data = data.sample(50)
    return render_template('death.html', data=data)

@app.route('/report')
def report():
    # establish a database connection
    with engine.connect() as connection:
        # execute an SQL query to fetch data
        query1 = text('SELECT * FROM report')

        result1 = connection.execute(query1)

        # fetch all rows of data
        db_data1 = result1.fetchall()

    return render_template('report.html', data1=db_data1)

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')



@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    # note, if running locally on a non-google shell, do not need to override redirect_uri and can just use url_for as below
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    # if running in google shell, need to override redirect_uri to the external web address of the shell, e.g.,
    redirect_uri = 'https://5000-cs-806611175101-default.cs-us-east1-vpcf.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)