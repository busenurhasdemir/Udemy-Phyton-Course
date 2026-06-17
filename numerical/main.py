"""
import numpy as np
import matplotlib.pyplot as plt
import math

try:
    plt.style.use('seaborn-v0_8-poster')
except OSError:
    plt.style.use('ggplot')

x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))

labels = ['First Order', 'Third Order', 'Fifth Order', 'Seventh Order']

plt.figure(figsize=(10, 8))

for n, label in zip(range(4), labels):
    y = y + ((-1)**n * (x**(2*n+1))) / math.factorial(2*n+1)
    plt.plot(x, y, label=label)

plt.plot(x, np.sin(x), 'k', label='Analytic')
plt.grid(True)
plt.title('Taylor Series Approximations of Various Orders')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
"""
"""
import numpy as np
import pandas as pd

# ==========================================================
# Jacobi Iterative Method
# ==========================================================
def jacobi_method(A, b, x0=None, tol=1e-8, max_iter=500):
    
    Jacobi Iterative Method

    This function solves the linear system Ax = b using the Jacobi method.

    Idea:
    -----
    Each component of x^(k+1) is computed ONLY using values from x^(k).
    That is, all updates are done simultaneously (no immediate reuse).

    Mathematical formula:
    ---------------------
    x_i^(k+1) = (1 / a_ii) * ( b_i - sum_{j != i} a_ij * x_j^(k) )

    Parameters:
    -----------
    A : matrix (n x n)
        Coefficient matrix
    b : vector (n)
        Right-hand side
    x0 : initial guess (optional)
    tol : tolerance for stopping criterion
    max_iter : maximum number of iterations

    Returns:
    --------
    x : approximate solution
    iteration : number of iterations used
    history : list of iteration data (for tables/analysis)
    

    # Convert inputs to numpy arrays
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)

    # Initial guess: if not provided, use zero vector
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)

    # Extract diagonal matrix D and remainder matrix R = A - D
    D = np.diag(np.diag(A))
    R = A - D

    # Precompute inverse of diagonal (cheap operation)
    D_inv = np.diag(1 / np.diag(A))

    history = []

    # Iterative process
    for k in range(1, max_iter + 1):

        # Jacobi update (vectorized form)
        x_new = D_inv @ (b - R @ x)

        # Compute error (difference between successive iterates)
        error = np.linalg.norm(x_new - x, ord=np.inf)

        # Compute residual ||b - Ax||
        residual = np.linalg.norm(b - A @ x_new, ord=np.inf)

        # Store iteration information
        history.append({
            "Iteration": k,
            "Approximation": x_new.copy(),
            "Error (inf-norm)": error,
            "Residual (inf-norm)": residual
        })

        # Stopping criterion
        if error < tol:
            return x_new, k, history

        # Update solution
        x = x_new

    return x, max_iter, history


# ==========================================================
# Gauss-Seidel Iterative Method
# ==========================================================
def gauss_seidel_method(A, b, x0=None, tol=1e-8, max_iter=500):
    
    Gauss-Seidel Iterative Method

    This function solves Ax = b using the Gauss-Seidel method.

    Idea:
    -----
    Unlike Jacobi, Gauss-Seidel uses newly computed values immediately.
    This typically leads to faster convergence.

    Mathematical formula:
    ---------------------
    x_i^(k+1) = (1 / a_ii) * ( b_i
                    - sum_{j<i} a_ij * x_j^(k+1)
                    - sum_{j>i} a_ij * x_j^(k) )

    Key difference:
    ---------------
    - Lower part (j < i): uses updated values
    - Upper part (j > i): uses old values

    Parameters and Returns are same as Jacobi.
    

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)

    history = []

    # Iteration loop
    for k in range(1, max_iter + 1):

        x_old = x.copy()

        # Update each variable sequentially
        for i in range(n):

            # Sum using already updated values
            sum1 = np.dot(A[i, :i], x[:i])

            # Sum using old values
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])

            # Update x_i
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        # Compute error
        error = np.linalg.norm(x - x_old, ord=np.inf)

        # Compute residual
        residual = np.linalg.norm(b - A @ x, ord=np.inf)

        # Store iteration data
        history.append({
            "Iteration": k,
            "Approximation": x.copy(),
            "Error (inf-norm)": error,
            "Residual (inf-norm)": residual
        })

        # Stopping condition
        if error < tol:
            return x, k, history

    return x, max_iter, history


# ==========================================================
# Function to display results and comparisons
# ==========================================================
def display_results(example_name, A, b, x0=None, tol=1e-8, max_iter=500):
    
    This function runs both methods and prints:

    - Exact solution
    - Approximate solutions
    - Number of iterations
    - Comparison table
    - First few iteration values
    

    print("=" * 70)
    print(example_name)
    print("=" * 70)

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Compute exact solution using direct solver
    exact_solution = np.linalg.solve(A, b)

    # Run Jacobi
    x_jacobi, iter_jacobi, hist_jacobi = jacobi_method(A, b, x0, tol, max_iter)

    # Run Gauss-Seidel
    x_gs, iter_gs, hist_gs = gauss_seidel_method(A, b, x0, tol, max_iter)

    print("\nExact solution:")
    print(exact_solution)

    print("\nJacobi solution:")
    print(x_jacobi)
    print("Jacobi iterations:", iter_jacobi)

    print("\nGauss-Seidel solution:")
    print(x_gs)
    print("Gauss-Seidel iterations:", iter_gs)

    # Create comparison table
    comparison_table = pd.DataFrame({
        "Method": ["Jacobi", "Gauss-Seidel"],
        "Iterations": [iter_jacobi, iter_gs],
        "Final Residual": [
            hist_jacobi[-1]["Residual (inf-norm)"],
            hist_gs[-1]["Residual (inf-norm)"]
        ],
        "Approximate Solution": [x_jacobi, x_gs]
    })

    print("\nComparison Table:")
    print(comparison_table)


# ==========================================================
# Example 1 (Diagonally dominant system)
# ==========================================================
A1 = [
    [10, -1,  2,  0],
    [-1, 11, -1,  3],
    [ 2, -1, 10, -1],
    [ 0,  3, -1,  8]
]
b1 = [6, 25, -11, 15]

# ==========================================================
# Example 2 (Another stable system)
# ==========================================================
A2 = [
    [4,  1,  1],
    [2,  7,  1],
    [1, -3, 12]
]
b2 = [7, -1, 12]

# Initial guesses
x0_1 = [0, 0, 0, 0]
x0_2 = [0, 0, 0]

# Run both examples
display_results("Example 1", A1, b1, x0=x0_1)
display_results("Example 2", A2, b2, x0=x0_2)
"""
"""
import numpy as np

def sor(A, b, x0=None, omega=1.25, tol=1e-8, max_iter=100):
    """  """
    Solves Ax = b using the Successive Over-Relaxation (SOR) method.

    Parameters
    ----------
    A : numpy.ndarray
        Coefficient matrix
    b : numpy.ndarray
        Right-hand side vector
    x0 : numpy.ndarray, optional
        Initial guess
    omega : float
        Relaxation parameter (0 < omega < 2)
        omega = 1 gives Gauss-Seidel
    tol : float
        Tolerance for stopping criterion
    max_iter : int
        Maximum number of iterations

    Returns
    -------
    x : numpy.ndarray
        Approximate solution
    iterations : int
        Number of iterations used
    history : list
        List of iterates for convergence tracking
  
    n = len(b)

    if x0 is None:
        x = np.zeros(n, dtype=float)
    else:
        x = x0.astype(float)

    history = [x.copy()]

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            # Sum using the newest available values
            sigma1 = np.dot(A[i, :i], x[:i])

            # Sum using the old values for the remaining entries
            sigma2 = np.dot(A[i, i+1:], x_old[i+1:])

            # SOR update formula
            x[i] = (1 - omega) * x_old[i] + (omega / A[i, i]) * (b[i] - sigma1 - sigma2)

        history.append(x.copy())

        # Stop if infinity norm of difference is small enough
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x, k + 1, history

    return x, max_iter, history


# ---------------------------------------------------
# Example 1
# ---------------------------------------------------
# A diagonally dominant system

A1 = np.array([
    [4, 1, 2],
    [3, 5, 1],
    [1, 1, 3]
], dtype=float)

b1 = np.array([4, 7, 3], dtype=float)

x1, iter1, hist1 = sor(A1, b1, omega=1.1, tol=1e-10, max_iter=100)

print("=" * 60)
print("Example 1")
print("Matrix A:")
print(A1)
print("Vector b:")
print(b1)
print("Approximate solution by SOR:")
print(x1)
print("Number of iterations:", iter1)

# Compare with exact solution from NumPy
x1_exact = np.linalg.solve(A1, b1)
print("Exact solution:")
print(x1_exact)
print("Infinity norm of error:", np.linalg.norm(x1 - x1_exact, ord=np.inf))


# ---------------------------------------------------
# Example 2
# ---------------------------------------------------
# Another linear system

A2 = np.array([
    [10, -1, 2, 0],
    [-1, 11, -1, 3],
    [2, -1, 10, -1],
    [0, 3, -1, 8]
], dtype=float)

b2 = np.array([6, 25, -11, 15], dtype=float)

x2, iter2, hist2 = sor(A2, b2, omega=1.2, tol=1e-10, max_iter=200)

print("=" * 60)
print("Example 2")
print("Matrix A:")
print(A2)
print("Vector b:")
print(b2)
print("Approximate solution by SOR:")
print(x2)
print("Number of iterations:", iter2)

# Compare with exact solution from NumPy
x2_exact = np.linalg.solve(A2, b2)
print("Exact solution:")
print(x2_exact)
print("Infinity norm of error:", np.linalg.norm(x2 - x2_exact, ord=np.inf))
print("=" * 60)
"""


