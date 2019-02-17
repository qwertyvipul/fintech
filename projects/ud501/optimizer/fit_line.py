import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def error(line, data):
    # err = sum((actual - predicted) ^ 2)
    # predicted = Ci0 + Ci1*Xi
    err = np.sum((data[:, 1] - (line[0] + line[1] * data[:, 0]))**2)
    return err


def fit_line(data, err_func):
    # Generate initial guess for the line model
    l = np.float32([0, np.mean(data[:,1])])
    
    # Plot initial guess (optional)
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] + l[1]*x_ends, 'm--', linewidth=2.0, label="Initial Guess")
    
    # Call optimizer to minimize error function
    result = spo.minimize(err_func, l, args = (data,), method="SLSQP", options={"disp":True})
    return result.x


# Original Line
l_orig = np.float32([2, 4])
print("Original Line: C0={}, C1={}".format(l_orig[0], l_orig[1]))
X_orig = np.linspace(0, 10, 21)
Y_orig = l_orig[0] + l_orig[1] * X_orig

noise_sigma = 3.0
noise = np.random.normal(0, noise_sigma, Y_orig.shape)
data = np.asarray([X_orig, Y_orig + noise]).T

plt.plot(X_orig, Y_orig, 'b--', linewidth=2.0, label="Original Line")
plt.plot(data[:,0], data[:,1], "go", label="Data Points")

l_fit = fit_line(data, error)
Y_fit = l_fit[0] + l_fit[1] * X_orig

print("Original Line: C0={}, C1={}".format(l_fit[0], l_fit[1]))

plt.plot(X_orig, Y_fit, 'r--', linewidth=2.0, label="Fitting Line")
plt.show()