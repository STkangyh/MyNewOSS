import numpy as np
import matplotlib.pyplot as plt

# Given data
test_size = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
comp_time = np.array([0.040322303771972656, 0.14821386337280273, 0.18218684196472168, 0.34340929985046387, 0.568464994430542, 0.8692693710327148, 1.214226245880127, 1.415954828262329, 1.8326914310455322, 2.249859571456909])

# Linear model: y = ax + b
linear_coefficients = np.polyfit(test_size, comp_time, 1)
linear_model = np.poly1d(linear_coefficients)

# Quadratic model: y = ax^2 + b
quadratic_coefficients = np.polyfit(test_size, comp_time, 2)
quadratic_model = np.poly1d(quadratic_coefficients)

# Cubic model: y = ax^3 + b
cubic_coefficients = np.polyfit(test_size, comp_time, 3)
cubic_model = np.poly1d(cubic_coefficients)

# Calculate RMSE for linear model
linear_predicted = linear_model(test_size)
linear_rmse = np.sqrt(np.mean((comp_time - linear_predicted) ** 2) / len(linear_predicted))

# Calculate RMSE for quadratic model
quadratic_predicted = quadratic_model(test_size)
quadratic_rmse = np.sqrt(np.mean((comp_time - quadratic_predicted) ** 2) / len(quadratic_predicted))

# Calculate RMSE for cubic model
cubic_predicted = cubic_model(test_size)
cubic_rmse = np.sqrt(np.mean((comp_time - cubic_predicted) ** 2) / len(cubic_predicted))

# Visualization
plt.scatter(test_size, comp_time, label='Data')
plt.plot(test_size, linear_model(test_size), label='O(N)')
plt.plot(test_size, quadratic_model(test_size), label='O(N^2)')
plt.plot(test_size, cubic_model(test_size), label='O(N^3)')
plt.xlabel('Matrix Size(N)')
plt.ylabel('Computing Time[sec]')
plt.legend()
plt.show()

# Print RMSE results
"""
RMSE for Linear Model: {0.0510868990250786}
RMSE for Quadratic Model: {0.012843737777663781}
RMSE for Cubic Model: {0.011858798837734573}
"""