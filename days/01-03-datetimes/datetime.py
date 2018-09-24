'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime, timedelta

import os
#import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
'''
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)
'''
logfile = 'logfile.txt'
with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    date_time_string = (line.split(' ')[1])
    dt = datetime.strptime(date_time_string, '%Y-%m-%dT%H:%M:%S')
    return dt

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    test_string = "Shutdown initiated"
    time_list = []
    for string_lines in loglines:
        if test_string in string_lines:
            time_list.append(convert_to_datetime(string_lines))
    period = str(time_list[1] - time_list[0]).split(':')
    period_int = [int(num) for num in period]
    t_delta = timedelta(hours = period_int[0], minutes= period_int[1], seconds = period_int[2])
    return t_delta

print(type(time_between_shutdowns(loglines)))