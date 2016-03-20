from __future__ import division
import csv      # imports the csv module
import datetime



def read_hackdata():

    hackdata = []
    data_file = '../data/hackdata.csv'

    activity    = 'activity'
    time_       = 'time'
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
            event_time = datetime.datetime.fromtimestamp(float(row[2])/1000.0)

            # create a dictionary entry with the details of the row (except index...)
            event = {activity: row[1].strip().lower(), time_: event_time, duration: int(row[3]),
                    steps: int(row[4]), distance: int(row[5]), speed: int(row[6]), bearing: int(row[7])}

            # append event row to list (...index is now the index in the list)
            hackdata.append(event)

    finally:
        infile.close()

    return hackdata



