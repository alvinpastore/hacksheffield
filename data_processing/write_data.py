import csv      # imports the csv module
import datetime

activity    = 'activity'
time_       = 'time'
duration    = 'duration'
steps       = 'steps'
distance    = 'distance'
speed       = 'speed'
bearing     = 'bearing'

def write_hackdata(d):

    data_file = '../data/hackdata_post.csv'

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

def map_activity(act):
    if act == 'in_vehicle':
        return 0
    if act == 'on_bicycle':
        return 1
    if act == 'still':
        return 2
    if act == 'unknown':
        return 3
    if act == 'tilting':
        return 4
    if act == 'walking':
        return 5
    if act == 'running':
        return 6


def write_hackdata_matrix(d):

    outfile_matrix = open('../data/hackdata_matrix.csv', 'wb')
    outfile_labels = open('../data/hackdata_labels.csv', 'wb')

    try:
        writer_matrix = csv.writer(outfile_matrix)
        writer_labels = csv.writer(outfile_labels)
        for row in d:
            writer_matrix.writerow([row[time_].time().hour, row[duration], row[steps], row[distance], row[speed], row[bearing]])
            writer_labels.writerow([map_activity(row[activity])])
    finally:
        outfile_matrix.close()
        outfile_labels.close()