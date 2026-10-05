"""
Problem: Numerical Computing with NumPy
Author: Bhavishya Dewangan
"""
try:
    import numpy as np

    def numpy_demo():
        # 1D array operations
        arr = np.array([10, 20, 30, 40, 50], dtype=np.float32)
        print("Array:", arr)
        print("Mean:", np.mean(arr), "| Std Dev:", np.std(arr))

        # 2D Matrix multiplication
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        C = np.dot(A, B)
        print("Matrix Product (A dot B):\n", C)

    if __name__ == "__main__":
        numpy_demo()
except ImportError:
    print("NumPy not installed. Install via: pip install numpy")
