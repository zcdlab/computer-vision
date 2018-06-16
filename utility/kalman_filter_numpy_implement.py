# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 15:55:00 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

# intial parameters
n_iter = 200
# truth value (typo in example at top of p. 13 calls this z)
x = 0.1
# observations (normal about x, sigma=0.1)
z = np.random.normal(x, 0.1, size=(n_iter,))
# noise variance
Q = 1e-5

xhat = np.zeros(n_iter,)      # a posteri estimate of x
P = np.zeros(n_iter,)         # a posteri error estimate
xhatminus = np.zeros(n_iter,) # a priori estimate of x
Pminus = np.zeros(n_iter,)    # a priori error estimate
K = np.zeros(n_iter,)         # gain or blending factor (kalman factor)

R = 0.1 ** 2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = 0.0
P[0] = 1.0

for k in range(1, n_iter):
    # time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1] + Q

    # measurement update
    K[k] = Pminus[k] / (Pminus[k] + R)
    xhat[k] = xhatminus[k] + K[k] * (z[k] - xhatminus[k])
    P[k] = (1 - K[k]) * Pminus[k]

plt.figure()
plt.plot(z,'k+',label='noisy measurements')
plt.plot(xhat,'b-',label='a posteri estimate')
plt.axhline(x,color='g',label='truth value')
plt.legend()
plt.title('Estimate vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('Voltage')

plt.figure()
valid_iter = range(1,n_iter) # Pminus not valid at step 0
plt.plot(valid_iter,Pminus[valid_iter],label='a priori error estimate')
plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
plt.xlabel('Iteration')
plt.ylabel('$(Voltage)^2$')
plt.setp(plt.gca(),'ylim',[0,.01])
plt.show()
