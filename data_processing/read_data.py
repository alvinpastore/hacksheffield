from __future__ import division
import csv      # imports the csv module
import datetime

import sys      # imports the sys module

data_file = '../data/hackdata.csv'

hackdata_structure = []

activity    = 'activity'
time        = 'time'
duration    = 'duration'
steps       = 'steps'
distance    = 'distance'
speed       = 'speed'
bearing     = 'bearing'


infile = open(data_file, 'rb') # opens the input csv file
try:
    reader = csv.reader(infile)
    next(reader, None)  # skip the headers

    for row in reader:

        # translate ms from 1.1.1970 to datetime format of the event
        event_time = datetime.datetime.fromtimestamp(float(event[time])/1000.0)

        # create a dictionary entry with the details of the row (except index...)
        event = {activity: row[1], time: event_time, duration: row[3],
                steps: row[4], distance: row[5], speed: row[6], bearing: row[7]}

        # append event row to list (...index is now the index in the list)
        hackdata_structure.append(event)

finally:
    infile.close()


