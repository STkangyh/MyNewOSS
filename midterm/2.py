import numpy as np
import time

test_sizes = [100, 200, 300, 400, 500]

for size in test_sizes:
    # Create a random matrix of given size
    matrix = np.random.uniform(0, 1, size=(size, size))

    # Measure execution time for pinv calculation
    start_time = time.time()
    pinv_result = np.linalg.pinv(matrix)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Matrix size: {size}x{size}, Execution Time: {execution_time:.6f} seconds")
# 측정 결과
'''
Matrix size: 100x100, Execution Time: 0.007983 seconds
Matrix size: 200x200, Execution Time: 0.026705 seconds
Matrix size: 300x300, Execution Time: 0.057830 seconds
Matrix size: 400x400, Execution Time: 0.090463 seconds
Matrix size: 500x500, Execution Time: 0.162094 seconds
'''