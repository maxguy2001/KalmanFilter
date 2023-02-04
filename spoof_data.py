import numpy as np
import matplotlib.pyplot as plt
import random


class SpoofData:
    def __init__(self):
        pass

    def plotRun(run):
        data, noisy_data, timestamps = run()
        plt.plot(timestamps, data)
        plt.plot(timestamps, noisy_data)
        plt.show()
        return None

    def run1(self):
        timestamps = np.linspace(0, 100, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        func1 = lambda x: -0.03*x**2 + 3*x
        func1Deriv = lambda x: -0.06*x + 3
        func1DDeriv = lambda x: -0.06

        data[:,2] = func1(timestamps)
        data[:,1] = func1Deriv(timestamps)
        data[:,0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run2(self):
        timestamps = np.linspace(0, 100, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        func1 = lambda x: np.log(x)
        func1Deriv = lambda x: 1/x
        func1DDeriv = lambda x: -1/(x**2)

        data[:,2] = func1(timestamps)
        data[:,1] = func1Deriv(timestamps)
        data[:,0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run3(self):
        timestamps = np.linspace(0, 100, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        func1 = lambda x: (0.1*x - 2)**3 + 2*(0.1*x - 2)**2
        func1Deriv = lambda x: 0.3 * (0.1*x - 2)**2 + 0.4 * (0.1*x - 2)
        func1DDeriv = lambda x: 3/25 * (0.1 * x - 2) + 2/25

        data[:,2] = func1(timestamps)
        data[:,1] = func1Deriv(timestamps)
        data[:,0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 5)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 5)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 5)
        return data, noisy_data, timestamps

    def run4(self):
        timestamps = np.linspace(0, 8, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        func1 = lambda x: np.exp(-x) * np.sin(x)
        func1Deriv = lambda x: np.cos(x) * np.exp(-x) - np.sin(x) * np.exp(-x)
        func1DDeriv = lambda x: -2 * np.exp(-x) * np.cos(x)

        data[:,2] = func1(timestamps)
        data[:,1] = func1Deriv(timestamps)
        data[:,0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run5(self):
        timestamps = np.linspace(0, 8, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        func1 = lambda x: 0.1*np.exp(x) + 2*x
        func1Deriv = lambda x: 0.1*np.exp(x) + 2
        func1DDeriv = lambda x: 0.1*np.exp(x)

        data[:,2] = func1(timestamps)
        data[:,1] = func1Deriv(timestamps)
        data[:,0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run6(self):
        timestamps = np.linspace(0, 12, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        func1 = lambda x: 5*np.sin(x)
        func1Deriv = lambda x: 5*np.cos(x)
        func1DDeriv = lambda x: -5*np.sin(x)

        data[:,2] = func1(timestamps)
        data[:,1] = func1Deriv(timestamps)
        data[:,0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run7(self):
        timestamps = np.linspace(0, 15, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        func1 = lambda x: 5*x
        func1Deriv = lambda x: 5

        data[:,2] = func1(timestamps)
        data[:,1] = func1Deriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = random.gauss(0, 0.2)
        return data, noisy_data, timestamps