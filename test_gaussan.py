import numpy as np
import matplotlib.pyplot as plt
epsilon = 1
vals_laplace = [np.random.laplace(loc=0, scale=100/epsilon) for x in range(1000)]
delta = 10e-5
sigma = np.sqrt(2 * np.log(1.25 / delta)) * 10 / epsilon
vals_gauss = [np.random.normal(loc=0, scale=sigma) for x in range(1000)]

plt.hist(vals_laplace, bins=50, label='Laplace')
plt.hist(vals_gauss, bins=50, alpha=.7, label='Gaussian');
plt.legend();
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
plt.grid()
# plt.figure(facecolor='blue')
plt.savefig('gaussian.pdf')
