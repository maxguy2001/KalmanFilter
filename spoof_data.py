import numpy as np
import random
#from collections import namedtuple

class FakeData:
    def __init__(self):
        self.cumulative_time_ = 0
        self.num_datapoints_ = 100
        self.avg_time_delta_micros_ = 1000
        self.max_variation_time_delta_ = 100
        self.num_axis_ = 3
        self.active_axis_ = 1
        
    def oneDimensionAcceleration(self, trajectory_function):
        
        self.cumulative_time_ = 0
        time_points = np.zeros(self.num_datapoints_)
        acc_vals = np.zeros(self.num_datapoints_)
        
        for i in range(self.num_datapoints_):
            
            #make noisy intervals for data collection
            time_delta_noise = random.randint(-self.max_variation_time_delta_, self.max_variation_time_delta_)
            time_delta = self.avg_time_delta_micros_ + time_delta_noise
            self.cumulative_time_ += time_delta
            
            #update timepoints and acceleration values
            time_points[i] = self.cumulative_time_
            acc_vals[i] = self.trajectory_function(self.cumulative_time_)
        
        return time_points, acc_vals
    
    
    def oneDimensionFullRun(self, acceleration_function, deceleration_function):
        pass
    
    def threeDimensionalAcceleration(self, acceleration_function):
        self.cumulative_time_ = 0
        time_points = np.zeros(self.num_datapoints_)
        acc_vals = np.zeros([self.num_datapoints_, self.num_axis_])
        
        for i in range(self.num_datapoints_):
            
            #make noisy intervals for data collection
            time_delta_noise = random.randint(-self.max_variation_time_delta_, self.max_variation_time_delta_)
            time_delta = self.avg_time_delta_micros_ + time_delta_noise
            self.cumulative_time_ += time_delta
            
            #update timepoints and acceleration values
            time_points[i] = self.cumulative_time_
            for j in range(self.num_axis_):
                if j == self.active_axis_:  
                    #add acc val
                    acc_vals[i, j] = self.trajectory_function(self.cumulative_time_)
                else:
                    #add noise
                    acc_vals[i, j] = self.accelerometerNoise(mu=0, sigma=0.2)
                    
        return time_points, acc_vals
    
    
    def threeDimensionalFullRun(self, acceleration_function, deceleration_function):
        pass
    
    def linearAcceleration(timepoint):
        #return arbitrary linear function of timepoint.
        return (0.5*timepoint) + 0.325
    
    def linearDeceleration(timepoint):
        #return arbitrary linear function of timepoint.
        return (-0.75*timepoint) + 0.496
    
    def exponentialAcceleration(timepoint):
        #arbitrary exponential acceleration function 
        return 0.25*np.exp(timepoint)
    
    def inverseDeceleration(timepoint):
        #inverse deceleration function modified to avoid division by 0 errors
        return (1/(timepoint+0.2))
    
    def accelerometerNoise(mu=0, sigma=0.2):
        #returns random gaussian noise for accelerometer non-useful axis
        return random.gauss(mu=mu, sigma=sigma)

    def polynomialAcceleration(timepoint):
        #return arbitrary polynomial function of timepoint
        return (0.1*timepoint - 2)**3 + 2*(0.1*timepoint - 2)**2


