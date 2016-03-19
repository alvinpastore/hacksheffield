import csv      # imports the csv module
import datetime

def write_hackdata(d):

    data_file = '../data/hackdata_post.csv'

    activity    = 'activity'
    time_       = 'time'
    duration    = 'duration'
    steps       = 'steps'
    distance    = 'distance'
    speed       = 'speed'
    bearing     = 'bearing'

    header = ['index', activity, time_, duration, steps, distance, speed, bearing]
    outfile = open(data_file, 'wb') # opens the input csv file
    try:
        writer = csv.writer(outfile)
        writer.writerow(header)
        idx = 0
        for row in d:
            writer.writerow([idx, row[activity], row[time_], row[duration], row[steps], row[distance], row[speed], row[bearing]])
            idx += 1
    finally:
        outfile.close()




