import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.ion()

plt.close('all')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# TRAINING PHASE

train = np.genfromtxt ('../data/hackdata_matrix.csv', delimiter=",").T
trainlabels = np.genfromtxt ('../data/hackdata_labels.csv', delimiter=",")


[n,m]   = np.shape(train)                   # number of pixels and number of training data
training= m / 3 * 2                         # first half used for training

testing = training + 1                      # index of first testing set instance (m-1 is the last)
eta     = 0.05                              # learning rate
winit   = 1                                 # parameter controlling magnitude of initial conditions

tmax    = 50000
classes = 6

Weights = winit * np.random.rand(classes,n) # Weight matrix (rows = output neurons, cols = input neurons)
normW   = np.sqrt(np.diag(Weights.dot(Weights.T)))
normW   = normW.reshape(classes,-1)         # reshape normW into a numpy 2d array
Weights = Weights / normW                   # normalise using numpy broadcasting -  http://docs.scipy.org/doc/numpy-1.10.1/user/basics.broadcasting.html

counter = np.zeros((1,classes))             # counter for the winner neurons
wCount  = np.ones((1,tmax+1)) * 0.25        # running avg of the weight change over time
alpha   = 0.999

fig_stats, axes_stats = plt.subplots(5,1)   # fig for the learning stats
fig_weights, axes_weights = plt.subplots(1,1)   # fig for the weights matrix

plt.show()
for t in range(1,tmax):
    i = math.ceil(training * np.random.rand())-1   # get a randomly generated index in the input range (training subset)
    train_instance = train[:,i]             # pick a training instance using the random index

    out_firing = Weights.dot(train_instance)                    # get output firing
    out_firing = out_firing.reshape((out_firing.shape[0], -1))  # reshape h into a numpy 2d array

    noise = np.random.rand(classes,1)  / 250

    # if not t % 1000:
    #     print 'Weights', Weights
    #     print 'out_firing', out_firing
    #     print 'noise', noise

    winner_index = np.argmax(out_firing+noise)              # get the index of the firing neuron

    counter[0,winner_index] += 1                            # increment counter for winner neuron

    dw = eta * (train_instance.T - Weights[winner_index,:])   # calculate the change in weights for the k-th output neuron
                                                            # get closer to the input (x - W)

    wCount[0,t] = wCount[0,t-1] * (alpha + dw.dot(dw.T)*(1-alpha)) # % weight change over time (running avg)

    Weights[winner_index,:] = Weights[winner_index,:] + dw         # weights for k-th output are updated

    # draw plots every 1000 iterations
    if not t % 1000:

        ###################### FIGURE 1
        #### (stats: output firing, train instance, recognised class, firing counter, weights change)
        axes_stats[0].clear()
        axes_stats[0].bar(np.arange(1,classes+1),out_firing,align='center')
        axes_stats[0].set_xticks(np.arange(1,classes+1))
        axes_stats[0].relim()
        axes_stats[0].autoscale_view(True,True,True)

        axes_stats[1].clear()
        #axes_stats[1].bar(np.arange(len(train_instance)),train_instance)
        axes_stats[1].imshow(np.asarray(train_instance).reshape(1,len(train_instance)),interpolation='nearest')
        axes_stats[1].get_xaxis().set_ticks([])
        axes_stats[1].get_yaxis().set_ticks([])

        axes_stats[2].clear()
        #axes_stats[2].bar(np.arange(len(Weights[winner_index,:])),Weights[winner_index,:])
        axes_stats[2].imshow(np.asarray(Weights[winner_index,:]).reshape(1,len(Weights[winner_index,:])),interpolation='nearest')
        axes_stats[2].get_xaxis().set_ticks([])
        axes_stats[2].get_yaxis().set_ticks([])

        axes_stats[3].clear()
        axes_stats[3].bar(np.arange(1,classes+1),counter.T,align='center')

        axes_stats[4].clear()
        axes_stats[4].plot(wCount[0,2:t+1],'-b', linewidth=2.0)
        axes_stats[4].set_ylim([-0.001, 0.255])

        plt.tight_layout()
        plt.draw()
        plt.pause(0.0001)

        ###################### FIGURE 2 (weights matrix)
        axes_weights.clear()
        im = axes_weights.imshow(Weights, interpolation='nearest')
        #axes_weights

        # Position the colorbars to the right of the images
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider1 = make_axes_locatable(axes_weights)
        cbar_ax1 = divider1.append_axes("right", "5%", pad="3%")
        cm1 = fig_weights.colorbar(im, cax=cbar_ax1)

        # Set the color range for the images and colorbars
        minX = 0
        maxX = 0.5
        im.set_clim(vmin=minX, vmax=maxX)
        cm1.set_clim(vmin=minX, vmax=maxX)

        plt.draw()
        plt.pause(0.0001)

# click anywhere on the stats plot to close both figures
plt.waitforbuttonpress()
plt.close('all')
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# TEST PHASE

fig_test, axes_test = plt.subplots(3,1)   # fig for the learning stats
plt.show()
for i in range(testing,m-1):

    test_instance = train[:,i]
    out_firing = Weights.dot(test_instance)                     # get output firing
    out_firing = out_firing.reshape((out_firing.shape[0], -1))  # reshape h into a numpy 2d array
    winner_index = np.argmax(out_firing)                        # get the index of the firing neuron

    # draw plots every 1000 iterations
    if not i % 100:

        axes_test[0].clear()
        axes_test[0].bar(np.arange(1,classes+1),out_firing,align='center')
        axes_test[0].set_xticks(np.arange(1,classes+1))
        axes_test[0].relim()
        axes_test[0].autoscale_view(True,True,True)

        axes_test[1].clear()
        axes_test[1].imshow(np.asarray(test_instance).reshape(1,len(test_instance)),interpolation='nearest')
        axes_test[1].get_xaxis().set_ticks([])
        axes_test[1].get_yaxis().set_ticks([])

        axes_test[2].clear()
        axes_test[2].imshow(np.asarray(Weights[winner_index,:]).reshape(1,len(Weights[winner_index,:])),interpolation='nearest')
        axes_test[2].get_xaxis().set_ticks([])
        axes_test[2].get_yaxis().set_ticks([])

        plt.tight_layout()
        plt.draw()
        plt.pause(0.001)

# click anywhere on the stats plot to close both figures
plt.waitforbuttonpress()