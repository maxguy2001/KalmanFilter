import spoof_data as spoof
import numpy as np

class KalmanFilter:

  def __init__():
    self.state_vector = np.zeros(3) #a, v, s
    self.state_covariance_matrix = np.zeros([3, 3])
    self.kalman_gain = np.zeros([3,3])
    self.measurement_vector = np.zeros(3)
    self.measurement_covariance_matrix = np.zeros([3,3])
    self.process_noise_covariance_matrix = np.zeros([3,3])
    self.old_timestamp = 0
    self.time_delta = 0
    self.state_estimate = np.zeros(3)
  
  def estimate(self, current_timestamp, observed_state):
    propagate(current_timestamp)
    measurementAndUpdate(observed_state)
    return self.state_estimate

  def propagate(self, current_timestamp):

    self.time_delta = current_timestamp - self.old_timestamp

    state_transition_matrix = getStateTransitionMatrix(self)
    self.state_estimate = np.matmul(state_transition_matrix, self.state_vector)
    return None

  def measurementAndUpdate(self, observed_state):
    # get measurement covariance
    # get process noise covaraince
    # get kalman gain
    # get state estimate
    # get state covariance matric
    pass

  #propagation functions
  def getStateTransitionMatrix(self):
    """
    get the state transition matrix which is the dynamic system function applied to the
    old state matrix
    """
    #TODO: consider more complex system models later
    return np.array([[1,0,0],[self.time_delta, 1, 0],[self.time_delta**2, self.time_delta, 1]])

  #measurement update functions
  def getMeasurementCovariance():
    pass

  def getProcessNoiseCovariance():
    pass

  def getKalmanGain():
    pass

  def getStateEstimate():
    pass

  def getStateEstimateCovariance():
    pass