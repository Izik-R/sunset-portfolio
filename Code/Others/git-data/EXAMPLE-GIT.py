import san
from datetime import datetime as dt
from datetime import timedelta
import sqlalchemy as sq

# Database cred's to connect
hostname = "#####"
dbname="####"
uname="####"
pwd="#####"

# Initializing server connection
db = sq.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))


def commits():
    
    # Gathering todays date, and also the beginning of 'this' week
    today = dt.now()
    week = today - timedelta(days=6)

    # API Key to access data
    san.ApiConfig.api_key = '######' #type: ignore

    # GraphQL arg's to gather data requested
    df = san.get(
    "dev_activity",
    slug="bitcoin",
    from_date=week,
    to_date=today,
    interval='1d'
    )

    # Naming the columns something other than 'value' thats returned
    df.columns = ['git_commits'] #type: ignore
    df.to_sql('test_table', db, if_exists='append') #type: ignore
    
    return(print('Commits gathered'))

commits()

