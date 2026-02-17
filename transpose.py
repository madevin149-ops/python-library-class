# Define a 3x2 matrix
C = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Transpose the matrix (becomes 2x3)
C_transpose = C.T

# Define another matrix (3x2) for dot product compatibility
D = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Dot product: (2x3) dot (3x2) = (2x2)
dot_product = np.dot(C_transpose, D)

print("Transpose of C:")
print(C_transpose)

print("\nDot Product Result:")
print(dot_product)