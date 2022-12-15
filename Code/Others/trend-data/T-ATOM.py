from pytrends.request import TrendReq
import datetime

# TZ = Timezone, and 360 is CST

# Numbers represent search interest relative to the highest point on the chart for the given region and time. 
# A value of 100 is the peak popularity for the term. 
# A value of 50 means that the term is half as popular. 
# A score of 0 means there was not enough data for this term.

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

    csvname = "trend-" + datetime.datetime.today().strftime('%Y-%m-%d') + ".csv"
    data.to_csv(csvname)
    
    return

trend()




