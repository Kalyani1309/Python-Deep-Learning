import numpy as np

# Using NumPy create random vector of size 15 having only Integers in the range 1-20.
a = np.random.randint(1, 20, 15, int)
print("Randomized array: ", a)

# Reshape the array to 3 by 5
b = np.reshape(a, (3, 5))
# Print array shape
print("\nReshaped array of size 3*5: \n", b)

# Replace the max in each row by 0
print('\nPrint the matrix after replacing max in each row by 0: \n',
      np.where(b == np.max(b, axis=1).reshape((-1, 1)), 0, b))

# Extract a diagonal from the array, and save as .npy file format.
print("\nDiagonal elements: ", np.diagonal(b))
np.savetxt("output.npy", np.diagonal(b))
