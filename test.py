from matplotlib import pyplot as plt
import helpers

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]

bias_sq = [256, 128, 64, 32, 16, 8, 4, 2, 1]

error = [x + y for x, y in zip(variance, bias_sq)]

xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')

plt.plot(xs, bias_sq, 'r-.', label='bias^2')

plt.plot(xs, error, 'b:', label='total error')

plt.legend(loc=9)

plt.xlabel('model complexity')

plt.title('the bias variance tradeoff')
