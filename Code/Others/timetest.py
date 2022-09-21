import datetime
import pendulum

def prev():
    global start
    global stop
    tdy = datetime.date.today()
    t_year = (tdy.year)
    t_ph = (tdy.month)
    t_month = t_ph - 1
    t_day = 1
    t_hour = 23
    t_min = 59


    index = pendulum.datetime(t_year, t_month, t_day, t_hour, t_min)
    table = index.end_of('month')
    s_table = index.timestamp()
    start = s_table + 25259
    t_table = table.timestamp()
    stop = t_table + 25199.000001
    print(start, 'First Timestamp Loaded')
    print(stop, 'Last Timestamp Loaded')
    return

prev()

