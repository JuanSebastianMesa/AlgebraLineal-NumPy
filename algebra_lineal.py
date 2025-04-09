# algebra_lineal.py
import numpy as np

def multiplicar_matrices(A, B):
    return np.dot(A, B)

def determinante(matriz):
    return np.linalg.det(matriz)

def resolver_sistema(A, b):
    return np.linalg.solve(A, b)

if __name__ == "__main__":
    A = np.array([[2, 3], [1, 2]])
    B = np.array([[1, 0], [4, 5]])
    b = np.array([5, 3])

    print("A * B =\n", multiplicar_matrices(A, B))
    print("Determinante de A:", determinante(A))
    print("Solución del sistema Ax = b:", resolver_sistema(A, b))