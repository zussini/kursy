import numpy
numpy.__version__
%paste
Out
for k in sorted(Out):
    print(f"\nOut[{k}]:")
    print(Out[k])
%paste
%paste
%paste
Out
    np.abs(-1)
np.abs(-1)
np.abs(-10)
%paste
%paste
%xpaste
%paste
result
%paste
result
import array
L = list(range(10))
A = array.array('i', L)
A
%paste
%paste
np.array([1, 2, 3, 4], dtype='float32')
%paste
%paste
# nested lists result in multi-dimensional arrays
np.array([range(i, i + 3) for i in [2, 4, 6]])
np.zeros(10, dtype=int)
np.ones((3, 5), dtype=float)
np.full((3, 5), 3.14)
np.arange(0, 20, 2)
np.linspace(0, 1, 5)
np.random.random((3, 3))
np.random.normal(0, 1, (3, 3))
np.random.randint(0, 10, (3, 3))
np.eye(3)
np.empty(3)
np.zeros(10, dtype='int16')
np.zeros(10, dtype=np.int16)
%paste
import numpy as np
np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)
%paste
%paste
%cpaste
$paste
%paste
x1
x1[0]
x1[4]
x1[-1]
x2
x2[2,0
]
x2[2,-1]
x2[0,0] = 12
x2
x1[0] = 3.14159
x1
x = np.arange(10)
x
x[:5]
x[5:]
x[4:7]
x[::2]
x[1::2]
x[::-1]
x[5::-1]
x[5::-2]
x2
x2[:2,:3]
x2[:3,:2]
x2[::-1,::-1]
print(x2[:,0])
print(x2[0,:])
print(x2[1,:])
print(x2[2,:])
print(x2)
x2_sub = x2[:2,:2]
print(x2_sub)
x2_sub[0,0] = x2[:2,:2]
x2_sub = x2[:2,:2]
print(x2_sub)
x2_sub[0,0] = 99
print(x2_sub)
print(x2)
x2_sub_copy = x2[:2,:2].copy()
print(x2_sub_copy)
x2_sub_copy[0,0] = 42
print(x2_sub_copy)
print(x2)
grid = np.arange(1,10).reshape((3,3))
grid
x = np.array([1,2,3])
x.reshape((1,3))
x[np.newaxis,:]
x.reshape((3,1))
x[:,np.newaxis]
%paste
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])
z = [99, 99, 99]
print(np.concatenate([x, y, z]))
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
np.concatenate([grid, grid])
# concatenate along the second axis (zero-indexed)
np.concatenate([grid, grid], axis=1)
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])
# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)
grid = np.arange(16).reshape((4, 4))
grid
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)
left, right = np.hsplit(grid, [2])
print(left)
print(right)
!sqlite3 ~/.ipython/profile_default/history.sqlite \
  "select distinct session from history order by session;"
%history 771/1-1000 -f my_history.py
%history 768/1-1000 -f my_history.py
%history 766/1-1000 -f my_history.py
