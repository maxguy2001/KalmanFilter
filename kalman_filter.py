import spoof_data as spoof
import numpy as np


class KalmanFilter:

    def __init__(self, initial_timestamp):
        self.state_vector = np.zeros(3)  # a, v, s
        self.state_covariance_matrix = np.zeros([3, 3])

        self.measurement_vector = np.zeros(3)

        # This seems important...
        self.measurement_covariance_matrix = (
            np.ones([3, 3]) - np.eye(3)) * 5000

        self.process_noise_covariance_matrix = np.eye(
            3) * 0.0001

        self.error_covariance_matrix = np.eye(3)
        self.system_noise_covariance_matrix = np.eye(3)  # *0.000002

        self.old_timestamp = initial_timestamp
        self.time_delta = 0

        self.new_state_estimate = np.zeros(3)

    # propagation functions

    def getStateTransitionMatrix(self):
        """
        get the state transition matrix which is the dynamic system function applied to the
        old state matrix
        """
        # TODO: consider more complex system models later
        mat = [1, 0, 0, self.time_delta, 1, 0,
               self.time_delta**2, self.time_delta, 1]
        return np.array(mat).reshape(3, 3)

    # measurement update functions

    def getErrorCovarianceMatrix(self):
        # propagate from start point
        state_transition_matrix = self.getStateTransitionMatrix()
        self.error_covariance_matrix = ((state_transition_matrix @ self.measurement_covariance_matrix)
                                        @ state_transition_matrix.T) + self.system_noise_covariance_matrix
        return None

    def getKalmanGain(self):
        mat1 = self.error_covariance_matrix @ self.error_covariance_matrix.T
        mat2 = self.error_covariance_matrix @ self.error_covariance_matrix @ self.error_covariance_matrix.T
        #print(mat1, mat2)
        kalman_gain = np.matmul(mat1, np.linalg.pinv(mat2))
        return kalman_gain

    def getStateEstimate(self, observed_state, kalman_gain):
        new_estimate = self.new_state_estimate + \
            (kalman_gain @ (observed_state - self.new_state_estimate))
        self.state_vector = new_estimate
        return None

    def getStateCovarianceMatrix(self, kalman_gain):
        self.state_covariance_matrix = self.state_covariance_matrix - \
            (kalman_gain @ self.state_covariance_matrix)
        return None

    def propagate(self, current_timestamp):

        self.time_delta = current_timestamp - self.old_timestamp

        state_transition_matrix = self.getStateTransitionMatrix()

        self.new_state_estimate = np.matmul(
            state_transition_matrix, self.state_vector)
        return None

    def measurementAndUpdate(self, observed_state):
        # get error covariance matrix
        # get kalman gain
        # get state estimate
        # get state covariance matrix

        self.getErrorCovarianceMatrix()
        kalman_gain = self.getKalmanGain()
        self.getStateEstimate(observed_state, kalman_gain)
        self.getStateCovarianceMatrix(kalman_gain)

    def estimate(self, current_timestamp, observed_state):
        self.propagate(current_timestamp)
        self.measurementAndUpdate(observed_state)
        return self.new_state_estimate
