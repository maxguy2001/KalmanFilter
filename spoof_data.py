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

        def func1(x): return -0.03*x**2 + 3*x
        def func1Deriv(x): return -0.06*x + 3
        def func1DDeriv(x): return -0.06

        data[:, 2] = func1(timestamps)
        data[:, 1] = func1Deriv(timestamps)
        data[:, 0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.00002)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.00002)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.00002)
        return data, noisy_data, timestamps

    def run2(self):
        timestamps = np.linspace(0, 100, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        def func1(x): return np.log(x)
        def func1Deriv(x): return 1/x
        def func1DDeriv(x): return -1/(x**2)

        data[:, 2] = func1(timestamps)
        data[:, 1] = func1Deriv(timestamps)
        data[:, 0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run3(self):
        timestamps = np.linspace(0, 100, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        def func1(x): return (0.1*x - 2)**3 + 2*(0.1*x - 2)**2
        def func1Deriv(x): return 0.3 * (0.1*x - 2)**2 + 0.4 * (0.1*x - 2)
        def func1DDeriv(x): return 3/25 * (0.1 * x - 2) + 2/25

        data[:, 2] = func1(timestamps)
        data[:, 1] = func1Deriv(timestamps)
        data[:, 0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 5)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 5)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 5)
        return data, noisy_data, timestamps

    def run4(self):
        timestamps = np.linspace(0, 8, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        def func1(x): return np.exp(-x) * np.sin(x)
        def func1Deriv(x): return np.cos(
            x) * np.exp(-x) - np.sin(x) * np.exp(-x)

        def func1DDeriv(x): return -2 * np.exp(-x) * np.cos(x)

        data[:, 2] = func1(timestamps)
        data[:, 1] = func1Deriv(timestamps)
        data[:, 0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run5(self):
        timestamps = np.linspace(0, 8, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        def func1(x): return 0.1*np.exp(x) + 2*x
        def func1Deriv(x): return 0.1*np.exp(x) + 2
        def func1DDeriv(x): return 0.1*np.exp(x)

        data[:, 2] = func1(timestamps)
        data[:, 1] = func1Deriv(timestamps)
        data[:, 0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run6(self):
        timestamps = np.linspace(0, 12, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        def func1(x): return 5*np.sin(x)
        def func1Deriv(x): return 5*np.cos(x)
        def func1DDeriv(x): return -5*np.sin(x)

        data[:, 2] = func1(timestamps)
        data[:, 1] = func1Deriv(timestamps)
        data[:, 0] = func1DDeriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = data[i, 0] + random.gauss(0, 0.2)
        return data, noisy_data, timestamps

    def run7(self):
        timestamps = np.linspace(0, 15, 1000)
        data = np.zeros([len(timestamps), 3])
        noisy_data = np.zeros([len(timestamps), 3])

        def func1(x): return 5*x
        def func1Deriv(x): return 5

        data[:, 2] = func1(timestamps)
        data[:, 1] = func1Deriv(timestamps)

        for i in range(len(timestamps)):
            noisy_data[i, 2] = data[i, 2] + random.gauss(0, 0.2)
            noisy_data[i, 1] = data[i, 1] + random.gauss(0, 0.2)
            noisy_data[i, 0] = random.gauss(0, 0.2)
        return data, noisy_data, timestamps
