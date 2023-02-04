import numpy as np
import matplotlib.pyplot as plt


def plotErrors(timestamps, errors):
    plt.plot(timestamps, errors)
    plt.xlabel("Time")
    plt.ylabel("Error")
    plt.show()
    return None


def plotFilter(true_vals, predicted_vals, noisy_data,  timestamps):
    plt.plot(timestamps, true_vals, label="True values")
    plt.plot(timestamps, predicted_vals, linestyle=":", label="Predicted vals")
    plt.plot(timestamps, noisy_data, marker=".",
             linestyle=" ", label="Raw data")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.show()
    return None


def meanAbsolueError(true_vals, predicted_vals):
    if len(true_vals) != len(predicted_vals):
        print("input array lengths do not match")
        return None

    total_abs_error = 0
    for i in range(len(true_vals)):
        total_abs_error += abs(true_vals[i] - predicted_vals[i])

    return total_abs_error/len(true_vals)


def modifiedLogError(true_vals, predicted_vals):
    if len(true_vals) != len(predicted_vals):
        print("input array lengths do not match")
        return None

    score = 0
    for i in range(len(true_vals)):
        if true_vals[i] != predicted_vals[i]:
            abs_diff = abs(true_vals[i] - predicted_vals[i])
            score += np.log(abs_diff + 1)

    return score
