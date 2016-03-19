from read_data import read_hackdata
import numpy as np
import matplotlib.pyplot as plt

# features
activity    = 'activity'
time        = 'time'
duration    = 'duration'
steps       = 'steps'
distance    = 'distance'
speed       = 'speed'
bearing     = 'bearing'

def print_data(d):

    for item in d:
        for feature,value in item.items():
            print feature + " " + str(value)

        print

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
    stats['variance'] = np.var(feature_data)
    stats['median']   = np.median(feature_data)
    stats['data']     = feature_data

    return stats

hackdata = read_hackdata()

walking_data    = filter_data(hackdata,(activity,'walking'))
still_data      = filter_data(hackdata,(activity,'still'))
unknown_data    = filter_data(hackdata,(activity,'unknown'))
in_vehicle_data = filter_data(hackdata,(activity,'in_vehicle'))
on_foot_data    = filter_data(hackdata,(activity,'on_foot_vehicle'))
on_bicycle_data = filter_data(hackdata,(activity,'on_bicycle'))
tilting_data    = filter_data(hackdata,(activity,'tilting'))

print "full  "       + str(len(hackdata))
print "on bicycle  " + str(len(on_bicycle_data))
print "on foot  "    + str(len(on_foot_data))
print "in vehicle  " + str(len(in_vehicle_data))
print "unknown  "    + str(len(unknown_data))
print "still  "      + str(len(still_data))
print "walking  "    + str(len(walking_data))
print "tilting  "    + str(len(tilting_data))

full_stats       = get_stats(hackdata,duration)
walking_stats    = get_stats(walking_data,duration)
still_stats      = get_stats(still_data,duration)
unknown_stats    = get_stats(unknown_data,duration)
in_vehicle_stats = get_stats(in_vehicle_data,duration)
on_bicycle_stats = get_stats(on_bicycle_data,duration)
tilting_stats    = get_stats(tilting_data,duration)

# print "full  "       + str(full_stats)
# print "on bicycle  " + str(on_bicycle_stats)
# print "in vehicle  " + str(in_vehicle_stats)
# print "unknown  "    + str(unknown_stats)
# print "still  "      + str(still_stats)
# print "walking  "    + str(walking_stats)
# print "tilting  "    + str(tilting_stats)

