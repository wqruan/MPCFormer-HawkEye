import numpy as np
import matplotlib.pyplot as plt
epsilon1 = 1
epsilon2 = 1
epsilon_total = 1

# 满足1-差分隐私
def F1():
    return np.random.laplace(loc=0, scale=1/4/epsilon1)

# 满足1-差分隐私
def F2():
    return np.random.laplace(loc=0, scale=1/4/epsilon2)

# 满足2-差分隐私
def F3():
    return 4+np.random.laplace(loc=0, scale=1/8/epsilon_total)

# 根据串行组合性，满足2-差分隐私
def F_combined():
    return (F1() + F2()) / 2

# 绘制F1
plt.hist([F1() for i in range(1000)], bins=50, label='F1');
# plt.hist([F2() for i in range(1000)], bins=50, label='F2');

# 绘制F_combined（看起来应该比F1更"尖"）
plt.hist([F_combined() for i in range(1000)], bins=50, alpha=.7, label='F_combined');
# plt.hist([F3() for i in range(1000)], bins=50, alpha=.7, label='F3');

plt.legend();
plt.grid(color = 'r', linestyle = '--', linewidth = 0.5)
plt.savefig('2m4p.pdf')