import timeit
import matplotlib.pyplot as plt

def fib_original(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_original(n-1) + fib_original(n-2)

def fib_optimized(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_optimized(n-1, memo) + fib_optimized(n-2, memo)
    return memo[n]

x = range(36)
y_original = [timeit.timeit(lambda: fib_original(i), number=1) for i in x]
y_optimized = [timeit.timeit(lambda: fib_optimized(i), number=1) for i in x]

plt.plot(x, y_original, label='Original code')
plt.plot(x, y_optimized, label='Optimized code')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Fibonacci computation time')
plt.legend()
plt.show()




