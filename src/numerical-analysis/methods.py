import numpy as np

# Newton - Raphson root finding

error = 1e-15
iterations = 100


def f(x):
    return x ** 2 - 2


def f_hat(x):
    return 2 * x


x = 10

for i in range(iterations):
    x_new = x - f(x) / f_hat(x)
    if abs(x - x_new < error):
        break
    x = x_new

print(x)
print(np.sqrt(2))
