from read_data import read_hackdata
import write_data
import numpy as np
import matplotlib.pyplot as plt

# features
activity    = 'activity'
time_       = 'time'
duration    = 'duration'
steps       = 'steps'
distance    = 'distance'
speed       = 'speed'
bearing     = 'bearing'

UNKNOWN = 'unknown'
TILTING = 'tilting'

FIVE_HOURS = 18000
SIX_HOURS  = 21600

def print_data(d):

    for item in d:
        for feature,value in item.items():
            print feature + " " + str(value)

        print


# removes rows with meaningless
# duration  (above 5/6 hours or negative durations)
# steps     (above 60k steps or negative steps)
# distance  (above 500km or negative distance)
# speed     (above 130km/h or negative speed)
def clean_data(d):
    clean_d = []

    for row in d:
        if 0 <= row[duration] < SIX_HOURS \
                and 0 <= row[steps] < 60000\
                and 0 <= row[distance] < 500\
                and 0 <= row[speed] < 130:
            clean_d.append(row)

    return clean_d


# criterion is a tuple (feature, value)
def filter_data(d,criterion):
    filtered_data = []

    for row in d:
        if row[criterion[0]].lower() == criterion[1]:
            filtered_data.append(row)

    return filtered_data


# won't work for activity or time_
def get_stats(d,feature):
    s = {}
    feature_data = []
    for row in d:
        feature_data.append(float(row[feature]))

    s['mean']     = np.mean(feature_data)
    s['std']      = np.std(feature_data)
    s['median']   = np.median(feature_data)
    s['raw_data'] = feature_data

    return s


def translate_undecided(d):
    translate_amount = 0

    for i in range(1,len(d)-1):
        undecided = d[i][activity] == UNKNOWN or d[i][activity] == TILTING
        # if the previous and next activities are the same
        if d[i-1][activity] == d[i+1][activity] and d[i][activity] != d[i+1][activity] and undecided:
            translate_amount += 1
            d[i][activity] = d[i-1][activity]
        # if the previous and next activities are not the same use the time difference to translate unknown
        elif  d[i-1][activity] != d[i+1][activity] and d[i][activity] != d[i+1][activity] and undecided:
            translate_amount += 1
            t_prev = d[i-1][time_]
            t_next = d[i+1][time_]
            if d[i][time_] - t_prev > t_next - d[i][time_]:
                d[i][activity] = d[i+1][activity]
            else:
                d[i][activity] = d[i-1][activity]

    print "translated " + str(translate_amount) + " rows"
    return d, translate_amount


def collapse_undecided(d):
    collapsed_data = []
    collapse_amount = 0

    i = 0
    while i < len(d):
        if d[i][activity] == UNKNOWN or d[i][activity] == TILTING:
            j = i+1
            while j < len(d):
                if d[j][activity] == d[i][activity]:
                    d[i][duration] = d[i][duration] + d[j][duration]
                    d[i][steps] = d[i][steps] + d[j][steps]
                    d[i][distance] = d[i][distance] + d[j][distance]
                    d[i][speed] = d[i][speed] + d[j][speed]
                    j += 1
                    collapse_amount += 1
                else:
                    collapsed_data.append(d[i])
                    i = j
                    break

        else:
            collapsed_data.append(d[i])
        i += 1
    print "collapsed " + str(collapse_amount) + " rows"
    return collapsed_data, collapse_amount

# step 1 read the data
hackdata = read_hackdata()
original_data_amount = len(hackdata)

# step 2 clean the data from unrealistic values
hackdata = clean_data(hackdata)
clean_data_amount = len(hackdata)

collapsed = 1
translated = 1
while collapsed > 0 or translated > 0:

    # step 3 translate undecided (unknown and tilting) to activity
    hackdata,translated = translate_undecided(hackdata)

    # step 4 collapse consecutive undecided
    hackdata,collapsed = collapse_undecided(hackdata)


#distance_stats = get_stats(hackdata,distance)
#print 'distance stats \n' \
#      'mean: {0},  median: {1} std: {2} max: {3}'.\
#    format(distance_stats['mean'],distance_stats['median'],distance_stats['std'],max(distance_stats['raw_data']))

#plt.hist(distance_stats['raw_data'], bins=100)
#plt.show()

#write_data.write_hackdata(hackdata)
write_data.write_hackdata_matrix(hackdata)