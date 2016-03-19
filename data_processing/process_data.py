from read_data import read_hackdata
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

FIVE_HOURS = 18000
SIX_HOURS  = 21600

def print_data(d):

    for item in d:
        for feature,value in item.items():
            print feature + " " + str(value)

        print


# removes rows with meaningless duration values (above 5/6 hours or negative durations)
# removes rows with meaningless steps values (above 60k steps or negative steps)
# removes rows with meaningless distance values (above 500km or negative distance)
# removes rows with meaningless speed values (above 130km/h or negative speed)
def clean_durations(d):

    clean_data = []

    for row in d:
        if 0 <= row[duration] < SIX_HOURS \
                and 0 <= row[steps] < 60000\
                and 0 <= row[distance] < 500\
                and 0 <= row[speed] < 130:
            clean_data.append(row)

    return clean_data


# criterion is a tuple (feature, value)
def filter_data(d,criterion):

    filtered_data = []

    for row in d:
        if row[criterion[0]].lower() == criterion[1]:
            filtered_data.append(row)

    return filtered_data


def get_stats(d,feature):
    stats = {}

    # extract the values for the criterion
    feature_data = []
    for row in d:
        feature_data.append(int(row[feature]))

    stats['mean']     = np.mean(feature_data)
    stats['std']      = np.std(feature_data)
    stats['median']   = np.median(feature_data)
    stats['raw_data'] = feature_data

    return stats


def translate_unknown(d):

    for i in range(2,len(d)-2):
        # previous two entries are the same of next two but the middle one is different
        previous_match = d[i-2][activity] == d[i-1][activity]
        next_match = d[i+1][activity] == d[i+2][activity]
        jump_match = d[i-1][activity] == d[i+1][activity] and next_match and previous_match
        d[i][activity] == ''
        if d[i][activity] != jump_match:
            print d[i-2]
            print d[i-1]
            print d[i]
            print d[i+1]
            print d[i+2]

            d[i][activity] = d[i-1][activity]


    return d

hackdata = read_hackdata()
original_data_amount = len(hackdata)
hackdata = clean_durations(hackdata)
print "pruned " + str(original_data_amount - len(hackdata)) + " rows"

stats = get_stats(hackdata,duration)

print stats['mean']
print stats['median']
print stats['std']

plt.hist(stats['raw_data'], bins=100)
plt.show()


#
# walking_data    = filter_data(hackdata,(activity,'walking'))
# still_data      = filter_data(hackdata,(activity,'still'))
# unknown_data    = filter_data(hackdata,(activity,'unknown'))
# in_vehicle_data = filter_data(hackdata,(activity,'in_vehicle'))
# on_foot_data    = filter_data(hackdata,(activity,'on_foot_vehicle'))
# on_bicycle_data = filter_data(hackdata,(activity,'on_bicycle'))
# tilting_data    = filter_data(hackdata,(activity,'tilting'))
#
#
# full_stats       = get_stats(hackdata,duration)
# walking_stats    = get_stats(walking_data,duration)
# still_stats      = get_stats(still_data,duration)
# unknown_stats    = get_stats(unknown_data,duration)
# in_vehicle_stats = get_stats(in_vehicle_data,duration)
# on_bicycle_stats = get_stats(on_bicycle_data,duration)
# tilting_stats    = get_stats(tilting_data,duration)
