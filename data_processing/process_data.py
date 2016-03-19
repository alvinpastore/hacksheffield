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


# removes rows with meaningless values (crazy-high [above 5 hours] or negative time)
def clean_durations(d):

    clean_data = []

    for row in d:
        if 0 <= row[duration] < SIX_HOURS:
            clean_data.append(row)

    return clean_data


# criterion is a tuple (feature, value)
def filter_data(data,criterion):

    filtered_data = []

    for row in data:
        if row[criterion[0]].lower() == criterion[1]:
            filtered_data.append(row)

    return filtered_data


def get_stats(data,feature):
    stats = {}

    # extract the values for the criterion
    feature_data = []
    for row in data:
        feature_data.append(int(row[feature]))

    stats['mean']     = np.mean(feature_data)
    stats['std']      = np.std(feature_data)
    stats['median']   = np.median(feature_data)
    stats['raw_data'] = feature_data

    return stats

hackdata = read_hackdata()
hackdata = clean_durations(hackdata)
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
