from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import pandas as pd
from pandas import read_sql
from sqlalchemy import create_engine, text

load_dotenv()  # Load environment variables from .env file

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

@app.route('/')
def mainpage():
    return render_template('index.html')

df = pd.read_csv('/home/helen_zheng/flask_e2e_project/data/cleaned_data.csv')
@app.route('/report')
def report(data=df):
    data = data.sample(50)
    return render_template('report.html', data=data)

#@app.route('/report')
#def report():
    # Establish a database connection
#    with engine.connect() as connection:
        # Execute an SQL query to fetch data (replace this with your query)
#        query1 = text('SELECT * FROM report')

#        result1 = connection.execute(query1)

        # Fetch all rows of data
#        db_data1 = result1.fetchall()

#    return render_template('report.html', data1=db_data1)

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)