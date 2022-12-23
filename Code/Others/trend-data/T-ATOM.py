from pytrends.request import TrendReq
import sqlalchemy as sq

# TZ = Timezone, and 360 is CST

# Numbers represent search interest relative to the highest point on the chart for the given region and time. 
# A value of 100 is the peak popularity for the term. 
# A value of 50 means that the term is half as popular. 
# A score of 0 means there was not enough data for this term.

# Database details to create a 'Database URL'
hostname = "#######"
dbname="#####"
uname="#####"
pwd="#####"


# Creating the engine/query method to the MySQL server
alch_db = sq.create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))


# Calling the google trends package, designating key words to search...
# ....Appending to my MySQL database
def trend():
    pytrends = TrendReq(hl='en_US', tz=360)

    keywords = ["Cosmos Ecosystem", "$ATOM", 
                "Cosmos ATOM", "Cosmos Network", 
                "Cosmos IBC"]

    pytrends.build_payload(kw_list = keywords, 
                        cat=0, 
                        timeframe='now 7-d', 
                        geo='', 
                        gprop='')

    data = pytrends.interest_over_time()

    data.to_sql('atom_trends', alch_db, if_exists='append')
    
    return print('All done :)')

trend()




