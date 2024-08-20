import numpy as np
import matplotlib.pyplot as plt
import seaborn

k1 = 11.875
k2 = 2.975
k3 = 0.125
k4 = 0.001

def get_vec(a, T, h):
    f = lambda x: k1 - k2 * x + k3 * x ** 2 - k4 * x ** 3
    X = [a]
    w1 = lambda x: f(x)
    w2 = lambda x: f(x + 0.5 * h * w1(x))
    w3 = lambda x: f(x + 0.5 * h * w2(x))
    w4 = lambda x: f(x + h * w3(x))

    for i in range(1, int(T / h)):
        X.append(X[i - 1] + h * (w1(X[i - 1]) + 2 * w2(X[i - 1]) + 2 * w3(X[i - 1]) + w4(X[i - 1])) / 6)
    
    return X


#seaborn.set_style("whitegrid")

h = 0.1
T = 7

t = np.linspace(0, T, int(T / h))

for i in range(250):
    plt.plot(t, get_vec(i * h, T, h), linewidth=2.0, color="red")

plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

T = 6

t = np.linspace(0, T, int(T / h))
for i in range(251, 1200):
    plt.plot(t, get_vec(i * h, T, h), linewidth=2.0, color="red")

plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

T = 7

t = np.linspace(0, T, int(T / h))

for i in range(1200):
    plt.plot(t, get_vec(i * h, T, h), linewidth=2.0, color="red")

plt.xlabel("t")
plt.ylabel("x(t)")
plt.show()

