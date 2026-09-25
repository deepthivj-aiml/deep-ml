import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_array=np.array(X)
	# Transpose it to 3x2
	X_T = X_array.T
	# Calculate the inverse
	A_inv = np.linalg.inv(np.dot(X_T,X_array))
	theta=np.dot(np.dot(A_inv, X_array.T),y)
	# A vector with many decimals
	result = np.array(theta)

	# Round to 4 decimal places
	rounded = np.round(result, 4)

	return rounded