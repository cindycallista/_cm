import numpy as np

# 1. Recursive Determinant
def recursive_det(matrix):
    n = len(matrix)
    if n == 1: return matrix[0][0]
    if n == 2: return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    total = 0
    for j in range(n):
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        total += ((-1)**j) * matrix[0][j] * recursive_det(sub_matrix)
    return total

# 2. LU Decomposition Determinant
def lu_det(A):
    from scipy.linalg import lu
    p, l, u = lu(A)
    # det(A) = det(P) * det(L) * det(U)
    # det(P) is 1 or -1 based on row swaps
    det_p = np.linalg.det(p)
    return det_p * np.prod(np.diag(l)) * np.prod(np.diag(u))

# 3. Verification of Decompositions
def verify_decompositions():
    A = np.array([[4, 2, 1], [1, 3, 2], [1, 2, 5]], dtype=float)
    
    # LU
    from scipy.linalg import lu
    p, l, u = lu(A)
    print("LU Match:", np.allclose(p @ l @ u, A))
    
    # Eigen
    vals, vecs = np.linalg.eig(A)
    print("Eigen Match:", np.allclose(vecs @ np.diag(vals) @ np.linalg.inv(vecs), A))
    
    # SVD
    u_svd, s_svd, vh_svd = np.linalg.svd(A)
    print("SVD Match:", np.allclose(u_svd @ np.diag(s_svd) @ vh_svd, A))

# 4. SVD using Eigen Decomposition
def svd_via_eigen(A):
    # A^T A = V S^2 V^T
    vals, V = np.linalg.eigh(A.T @ A)
    # Sort descending
    idx = vals.argsort()[::-1]
    vals, V = vals[idx], V[:, idx]
    s = np.sqrt(np.abs(vals))
    # U = A V S^-1
    U = A @ V @ np.linalg.inv(np.diag(s))
    return U, s, V.T

# 5. PCA
def run_pca(data, components=2):
    # Centering
    mean_adj = data - np.mean(data, axis=0)
    # SVD on centered data
    u, s, vh = np.linalg.svd(mean_adj)
    # Project data
    return mean_adj @ vh.T[:, :components]

# Testing
A_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Note: det is 0 for this matrix
A_square = np.array([[3, 1], [1, 2]])

print(f"Recursive Det: {recursive_det(A_test)}")
print(f"LU Det: {lu_det(A_square)}")
verify_decompositions()

data_sample = np.random.rand(10, 3)
print("PCA Shape:", run_pca(data_sample, 2).shape)
