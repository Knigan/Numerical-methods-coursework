import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn

def MC(N, T):
    k = [11.875, 2.975, 0.125, 0.001]

    eps = [0, 1, 2, 3]
    gamma = [1, 0, 3, 2]
    diff = [gamma[i] - eps[i] for i in range(4)]

    phi = lambda i, a: k[i] * math.factorial(a) / math.factorial(a - eps[i])

    m = 0
    t = [0]
    beta = [N]
    tau = [0, 0, 0, 0]

    while t[m] < T:
        for i in range(4):
            if beta[m] < eps[i]:
                tau[i] = np.inf
            else:
                r = np.random.uniform(0, 1)
                tau[i] = -np.log(1 - r) / phi(i, beta[m])
        
        taumin = min(tau)
        if taumin == np.inf:
            break

        t.append(t[m] + taumin)
        
        j = tau.index(taumin)
        beta.append(beta[m] + diff[j])
        
        m += 1
    
    return (t, beta, m)

results = MC(60, 10)

print("Число итераций:", results[2])

freq = [results[1].count(i) for i in range(100)]

relfreq = [freq[i] / (results[2] + 1) for i in range(100)]

print("Значения | Частоты  | Относительные частоты")

for i in range(100):
    print("%8d |" % (i), end = '')
    print(" %8d |" % freq[i], end = '')
    print(" %f" % relfreq[i])

seaborn.set_style("whitegrid")

plt.plot(results[0], results[1], linewidth=2.0, color="red")
plt.xlabel("t")
plt.ylabel("X")
plt.show()
