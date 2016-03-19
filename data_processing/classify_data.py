import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.ion()

plt.close('all')

train = np.genfromtxt ('../data/hackdata_matrix.csv', delimiter=",").T
trainlabels = np.genfromtxt ('../data/hackdata_labels.csv', delimiter=",")

print train
print train.shape
raw_input()
print trainlabels
print trainlabels.shape
raw_input()

[n,m]   = np.shape(train)                   # number of pixels and number of training data
eta     = 0.05                              # learning rate
winit   = 1                                 # parameter controlling magnitude of initial conditions

tmax    = 60000
classes = 6

Weights = winit * np.random.rand(classes,n) # Weight matrix (rows = output neurons, cols = input neurons)
normW   = np.sqrt(np.diag(Weights.dot(Weights.T)))
normW   = normW.reshape(classes,-1)         # reshape normW into a numpy 2d array
Weights = Weights / normW                   # normalise using numpy broadcasting -  http://docs.scipy.org/doc/numpy-1.10.1/user/basics.broadcasting.html

counter = np.zeros((1,classes))             # counter for the winner neurons
wCount  = np.ones((1,tmax+1)) * 0.25        # running avg of the weight change over time
alpha   = 0.999

fig_stats, axes_stats = plt.subplots(5,1)   # fig for the learning stats
plt.show()
for t in range(1,tmax):
    i = math.ceil(m * np.random.rand())-1   # get a randomly generated index in the input range
    train_instance = train[:,i]             # pick a training instance using the random index

    out_firing = Weights.dot(train_instance)                    # get output firing
    out_firing = out_firing.reshape((out_firing.shape[0], -1))  # reshape h into a numpy 2d array

    noise = np.random.rand(classes,1) / 10
    winner = np.max(out_firing+noise)                       # get the max in the output firing vector + noise
    winner_index = np.argmax(out_firing+noise)              # get the index of the firing neuron

    counter[0,winner_index] += 1                            # increment counter for winner neuron

    dw = eta * (winner_index.T - Weights[winner_index,:])   # calculate the change in weights for the k-th output neuron
                                                            # get closer to the input (x - W)

    wCount[0,t] = wCount[0,t-1] * (alpha + dw.dot(dw.T)*(1-alpha)) # % weight change over time (running avg)

    Weights[winner_index,:] = Weights[winner_index,:] + dw         # weights for k-th output are updated

    # draw plots for the first timestep and then every 300 iterations
    if not t % 1000:
        # plot stats
        axes_stats[0].clear()
        axes_stats[0].bar(np.arange(1,classes+1),out_firing,align='center')
        axes_stats[0].set_xticks(np.arange(1,classes+1))
        axes_stats[0].relim()
        axes_stats[0].autoscale_view(True,True,True)

        axes_stats[1].clear()
        axes_stats[1].bar(np.arange(len(train_instance)),train_instance)
        axes_stats[1].get_xaxis().set_ticks([])
        axes_stats[1].get_yaxis().set_ticks([])

        axes_stats[2].clear()
        axes_stats[2].bar(np.arange(len(Weights[winner_index,:])),Weights[winner_index,:])
        axes_stats[2].get_xaxis().set_ticks([])
        axes_stats[2].get_yaxis().set_ticks([])

        axes_stats[3].clear()
        axes_stats[3].plot(wCount[0,2:t+1],'-b', linewidth=2.0)
        axes_stats[3].set_ylim([-0.001, 0.255])

        axes_stats[4].clear()
        axes_stats[4].bar(np.arange(1,classes+1),counter.T,align='center')

        plt.tight_layout()
        plt.draw()
        plt.pause(0.0001)

# click anywhere on the stats plot to close both figures
plt.waitforbuttonpress()