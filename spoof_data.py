import numpy as np
import matplotlib.pyplot as plt
import random


class FakeData:
    def __init__(self):
        pass

    def plotRun(run):
        data, noisy_data, timestamps = run()
        plt.plot(timestamps, data)
        plt.plot(timestamps, noisy_data)
        plt.show()
        return None

    def run1():
        timestamps = np.linspace(0, 100, 1000)
        data = np.zeros(len(timestamps))
        noisy_data = np.zeros(len(timestamps))

        for i in range(len(timestamps)):
            data[i] = -0.03*timestamps[i]**2 + 3*timestamps[i]
            noisy_data[i] = data[i] + random.gauss(mu=0, sigma=0.5)
        return data, noisy_data, timestamps

    def run2():
        timestamps = np.linspace(1, 100, 1000)
        data = np.zeros(len(timestamps))
        noisy_data = np.zeros(len(timestamps))

        for i in range(len(timestamps)):
            data[i] = np.log(timestamps[i])
            noisy_data[i] = data[i] + random.gauss(0, 0.05)
        return data, noisy_data, timestamps

    def run3():
        timestamps = np.linspace(0, 100, 1000)
        data = np.zeros(len(timestamps))
        noisy_data = np.zeros(len(timestamps))

        for i in range(len(timestamps)):
            data[i] = (0.1*timestamps[i] - 2)**3 + 2*(0.1*timestamps[i] - 2)**2
            noisy_data[i] = data[i] + random.gauss(0, 0.05)
        return data, noisy_data, timestamps

    def run4():
        timestamps = np.linspace(0, 8, 1000)
        data = np.zeros(len(timestamps))
        noisy_data = np.zeros(len(timestamps))

        for i in range(len(timestamps)):
            data[i] = np.exp(-timestamps[i]) * np.sin(timestamps[i])
            noisy_data[i] = data[i] + random.gauss(0, 0.005)
        return data, noisy_data, timestamps

    def run5():
        timestamps = np.linspace(0, 8, 1000)
        data = np.zeros(len(timestamps))
        noisy_data = np.zeros(len(timestamps))

        for i in range(len(timestamps)):
            data[i] = 0.1*np.exp(timestamps[i]) + 2*timestamps[i]
            noisy_data[i] = data[i] + random.gauss(0, 0.5)
        return data, noisy_data, timestamps

    def run6():
        timestamps = np.linspace(0, 12, 1000)
        data = np.zeros(len(timestamps))
        noisy_data = np.zeros(len(timestamps))

        for i in range(len(timestamps)):
            data[i] = 5*np.sin(timestamps[i])
            noisy_data[i] = data[i] + random.gauss(0, 0.15)
        return data, noisy_data, timestamps

    def run7():
        timestamps = np.linspace(0, 15, 1000)
        data = np.zeros(len(timestamps))
        noisy_data = np.zeros(len(timestamps))

        for i in range(len(timestamps)):
            data[i] = 5*timestamps[i]
            noisy_data[i] = data[i] + random.gauss(0, 0.35)
        return data, noisy_data, timestamps
