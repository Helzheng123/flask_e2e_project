from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from faker import Faker
from azure import Report
import os
import random 
from dotenv import load_dotenv

load_dotenv()

## Database credentials 
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string and creating the engine 
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = (f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
                    f"?charset={DB_CHARSET}")

engine = create_engine(
        connection_string,
        connect_args=connect_args)

# Creating a session to populate the data
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

boroughs = ['Brooklyn', 'Queens', 'Bronx', 'Manhattan', 'Staten Island', 'ALL']

uhfs = ['All', 'Bayside - Little Neck', 'Bedford Stuyvesant - Crown Heights', 'Bensonhurst - Bay Ridge', 'Borough Park', 'Canarsie - Flatlands', 
                    'Central Harlem - Morningside Heights', 'Chelsea - Clinton', 'Coney Island - Sheepshead Bay', 'Crotona - Tremont', 'Downtown - Heights - Park Slope', 
                    'East Flatbush - Flatbush', 'East Harlem', 'East New York', 'Flushing - Clearview', 'Fordham - Bronx Park', 'Fresh Meadows', 'Gramercy Park - Murray Hill',
                    'Greenpoint', 'Greenwich Village - Soho', 'High Bridge - Morrisania', 'Hunts Point - Mott Haven', 'Jamaica', 'Kingsbridge - Riverdale', 'Long Island City - Astoria',
                    'Lower Manhattan', 'Northeast Bronx', 'Pelham - Throgs Neck', 'Port Richmond', 'Ridgewood - Forest Hills', 'Rockaway', 'South Beach - Tottenville',
                    'Southeast Queens', 'Southwest Queens', 'Stapleton - St. George', 'Sunset Park', 'Union Square - Lower East Side', 'Upper East Side', 'Upper West Side', 
                    'Washington Heights - Inwood', 'West Queens', 'Williamsburg - Bushwick', 'Willowbrook']

# populate Report table
for _ in range(10):
    reports = Report(
        year=fake.random_int(min=2011, max=2021),
        borough = fake.random_element(elements=boroughs),
        uhf=fake.random_element(elements=uhfs)
    )
    session.add(reports)

# Commit the changes to the database
session.commit()

# Close the session
session.close()