def loop():
    x = 0
    for i in range(1000000):
        x = x + i
    return x

def vectorized():
    import numpy as np
    x = np.arange(1000000)
    return np.sum(x)

print("Loop result:", loop())
print("Vectorized result:", vectorized())

# Benchmarking the performance of the loop and vectorized implementations
import time

# Time the loop implementation
start = time.time()
loop_result = loop()
end = time.time()
loop_time = end - start

# Time the vectorized implementation
start = time.time()
vectorized_result = vectorized()
end = time.time()
vectorized_time = end - start

print("Loop time:", loop_time)
print("Vectorized time:", vectorized_time)
print("Speedup:", loop_time / vectorized_time)