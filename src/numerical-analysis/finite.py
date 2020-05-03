import numpy as np
import matplotlib.pyplot as plt

x = 0.1
dt = 0.1

f = lambda x: 0.1 * x ** 5 - 0.2 * x ** 3 + 0.1 * x - 0.2
df = lambda x: 0.5*x**4 - 0.6*x**2 + 0.1

d1_analytic = 0.09405
d2_analytic = -0.118

print(f"\t f'(x)\t\t err\t\t f''(x)\t\t err")
# forward
d1 = (f(x + dt) - f(x)) / dt
d2 = (f(x + 2 * dt) - 2 * f(x + dt) + f(x)) / dt ** 2
print(f"FFD\t {d1: .5f}\t {d1 - d1_analytic: .5f}\t {d2: .5f}\t {d2 - d2_analytic: .5f}")

# backward
d1 = (f(x) - f(x - dt)) / dt
d2 = (f(x) - 2 * f(x - dt) + f(x - 2 * dt)) / dt ** 2
print(f"FFD\t {d1: .5f}\t {d1 - d1_analytic: .5f}\t {d2: .5f}\t {d2 - d2_analytic: .5f}")

# central
d1 = (f(x + dt) - f(x - dt)) / (2 * dt)
d2 = (f(x + dt) - 2 * f(x) + f(x - dt)) / dt ** 2
print(f"FFD\t {d1: .5f}\t {d1 - d1_analytic: .5f}\t {d2: .5f}\t {d2 - d2_analytic: .5f}")

x = np.linspace(-1, 1)
d1 = (f(x + dt) - f(x)) / dt
d2 = (f(x + dt) - 2 * f(x) + f(x - dt)) / dt ** 2

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle("Finite Difference Methods")
ax1.plot(x, f(x))
ax1.set_title("f(x)")
ax2.plot(x, d1)
ax2.plot(x, df(x), '--k')
ax2.set_title("f'(x)")
ax3.plot(x, d2)
ax3.set_title("f''(x)")

plt.tight_layout()
plt.show()
