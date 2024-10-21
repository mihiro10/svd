import numpy as np

def svd_solve(A: np.array):
    """
    Singular Value Decomposition (SVD) on the input matrix A.

    Parameters:
        A (numpy.ndarray): The input matrix for which SVD is performed.

    Returns:
        U (numpy.ndarray): Left singular vectors matrix.
        Sigma (numpy.ndarray): Diagonal matrix of singular values.
        V_T (numpy.ndarray): Transposed right singular vectors matrix.
        cond_number (float): Condition number of the matrix.
        inv_A (numpy.ndarray): Inverse of the input matrix A.

    Raises:
        ValueError: If at least one of the singular values is 0, indicating that the inverse of the matrix does not exist.
    """

    tolerance = 1e-5

    # Compute A * A^T and A^T * A
    A_AT = np.dot(A, A.T)
    AT_A = np.dot(A.T, A)
    
    # Compute eigenvalues and eigenvectors for A * A^T
    eigenvalues_U, eigenvectors_U = np.linalg.eig(A_AT)
    # Compute eigenvalues and eigenvectors for A^T * A
    eigenvalues_V, eigenvectors_V = np.linalg.eig(AT_A)
    
    # Sort eigenvalues and corresponding eigenvectors in descending order
    sorted_indices_U = np.argsort(eigenvalues_U)[::-1]
    sorted_indices_V = np.argsort(eigenvalues_V)[::-1]
    
    eigenvalues_U = eigenvalues_U[sorted_indices_U]
    eigenvectors_U = eigenvectors_U[:, sorted_indices_U]
    
    eigenvalues_V = eigenvalues_V[sorted_indices_V]
    eigenvectors_V = eigenvectors_V[:, sorted_indices_V]

    # Left singular vectors
    U = eigenvectors_U
    # Right singular vectors
    V = eigenvectors_V

    # Construct Sigma matrix with singular values
    Sigma = np.zeros_like(A, dtype=float)
    for i in range(len(eigenvalues_U)):
        Sigma[i, i] = np.sqrt(eigenvalues_U[i])

    # Adjust sign for consistency
    sign_correction = np.sign((A @ V)[0] * (U @ Sigma)[0])
    V = V * sign_correction
    
    # Check singular values close to zero
    for val in np.diag(Sigma):
        if np.abs(val) < tolerance:
            raise ValueError("At least one of the singular values is 0. This means the inverse of the matrix does not exist.")
        
    # Condition number
    min_singular_value = np.min(np.diag(Sigma))
    max_singular_value = np.max(np.diag(Sigma))
    cond_number = max_singular_value / min_singular_value

    # Inverse of Sigma
    Sigma_inv = np.linalg.inv(Sigma)
    # Inverse of A
    inv_A = V @ Sigma_inv @ U.T

    # Transpose V to get V_T
    V_T = V.T

    return U, Sigma, V_T, cond_number, inv_A
