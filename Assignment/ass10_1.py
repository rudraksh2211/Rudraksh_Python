import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[6,  -8, 73, -110],
                [np.nan, -8, 0, 94],
                [34, -12, np.nan, 3]], dtype=float)

arr_filled = np.nan_to_num(arr, nan=0)        
arr_swapped = arr_filled[:3, :3].T            
arr_filled[:3, :3] = arr_swapped             

print("\nAfter NaN→0 and 3×3 swap:\n", arr_filled)

arr3d   = np.arange(24).reshape(2, 3, 4)      
moved   = np.moveaxis(arr3d, 0, -1)           
print("\n3‑D move‑axis demo:", arr3d.shape, "→", moved.shape)

arr_nan   = np.array([[2, np.nan, 7],
                      [4, 5,      np.nan],
                      [np.nan, 1, 9]], dtype=float)
col_mean  = np.nanmean(arr_nan, axis=0)
filled    = np.where(np.isnan(arr_nan), col_mean, arr_nan)
print("\nNaN→column‑mean:\n", filled)

arr_neg   = np.array([[-4, 3, -2],
                      [ 1,-7,  5]])
arr_clean = np.where(arr_neg < 0, 0, arr_neg)
print("\nNegatives→0:\n", arr_clean)

arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
print("\nAverage of arr1 & arr2:", (arr1 + arr2) / 2)

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[2,3,4],[5,6,7]])

def mode(a):
    vals, cnts = np.unique(a, return_counts=True)
    return vals[cnts.argmax()]

for name, M in [("A",A), ("B",B)]:
    print(f"\nArray {name}: mean={M.mean():.2f}, median={np.median(M):.2f}, mode={mode(M)}")

Acoef = np.array([[1,-2, 3],
                  [1, 3,-1],
                  [2,-5, 5]], dtype=float)
bvec  = np.array([9,-6,17], dtype=float)
x, y, z = np.linalg.solve(Acoef, bvec)
print(f"\nSolution →  x={x:.3f}, y={y:.3f}, z={z:.3f}")

subjects = ["C","C++","Python","Java","C#"]
sem1     = np.array([8.1, 7.2, 8.5, 6.9, 7.8])   
sem2     = np.array([8.4, 7.9, 8.7, 7.4, 8.1])

x = np.arange(len(subjects))
w = 0.35
plt.figure(figsize=(8,5))
plt.bar(x-w/2, sem1, width=w, label="Semester 1")
plt.bar(x+w/2, sem2, width=w, label="Semester 2")
plt.xticks(x, subjects)
plt.ylabel("SGPA / Marks")
plt.title("Semester Performance Comparison")
plt.legend()
plt.tight_layout()
plt.show()
