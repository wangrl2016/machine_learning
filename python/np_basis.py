import numpy as np

if __name__ == '__main__':
    # Seed for reproducibility.
    np.random.seed(0)

    # One-dimensional array
    x1 = np.random.randint(10, size=6)
    # Two-demensional array
    x2 = np.random.randint(10, size=(3, 4))
    # Three-dimensional array
    x3 = np.random.randint(10, size=(3, 4, 5))

    print('x3 ndim:', x3.ndim)
    print('x3 shape:', x3.shape)
    print('x3 size:', x3.size)

    print('dtype:', x3.dtype)
    print('itemsize:', x3.itemsize, 'bytes')
    print('nbytes:', x3.nbytes, 'bytes')

    print(x1)
    print(x1[0])
    print(x1[4])
    print(x1[-1])
    print(x1[-2])

    print(x2)
    print(x2[0][0])
    print(x2[2, 0])
    print(x2[2, -1])
    print(x2[0, 0])

    # This will be truncated.
    x1[0] = 3.14159
    print(x1)

    # If any of these are unspecified, they default to the value
    # start=0, stop=size of dimension, step=1.
    # x[start:stop:step]
    x = np.arange(10)
    print(x)
    # First five elements.
    print(x[:5])
    # Elements after index 5.
    print(x[5:])
    # Middle sub-array.
    print(x[4:7])
    # Every other element.
    print(x[::2])
    # Every other element, starting at index 1.
    print(x[1::2])
    # All elements, reversed.
    print(x[::-1])
    # Reversed every other from index 5.
    print(x[5::-2])

    # Multi-dimensional slices work in the same way, with multiple slices separated by commnas.
    print(x2)
    # Two rows, three columns.
    print(x2[:2, :3])

    # All rows, every other column.
    print(x2[:3, ::2])

    # reversed
    print(x2[::-1, ::-1])

    # first column of x2
    print(x2[:, 0])
    # first row of x2
    print(x2[0, :])

    # equivalent to x2[0, :]
    print(x2[0])

    # Subarrays as no-copy views.
    x2_sub = x2[:2, :2]
    print(x2_sub)

    x2_sub[0, 0] = 99
    print(x2_sub)

    print(x2)

    # Creating copies of arrays.
    x2_sub_copy = x2[:2, :2].copy()
    print(x2_sub_copy)

    x2_sub_copy[0, 0] = 42
    print(x2_sub_copy)

    print(x2)

    grid = np.arange(1, 10).reshape((3, 3))
    print(grid)

    x = np.array([1, 2, 3])
    # Row vector via reshape.
    print(x.reshape((1, 3)))

    # Row vector via newaxis.
    print(x[np.newaxis, :])

    # Column vector via reshape.
    print(x.reshape((3, 1)))

    # Column vector via newaxis.
    print(x[:, np.newaxis])

    x = np.array([1, 2, 3])
    y = np.array([3, 2, 1])
    print(np.concatenate([x, y]))

    z = [99, 99, 99]
    print(np.concatenate([x, y, z]))

    grid = np.array([[1, 2, 3],
                     [4, 5, 6]])
    print(np.concatenate([grid, grid]))

    # Concatenate along the second axis (zero-indexed).
    print(np.concatenate([grid, grid], axis=1))

    x = np.array([1, 2, 3])
    grid = np.array([[9, 8, 7],
                     [6, 5, 4]])
    # Vertically stack the arrays.
    np.vstack([x, grid])

    # Horizontally stack the arrays.
    y = np.array([[99],
                  [99]])
    print(np.hstack([grid, y]))

    # splitting of arrays.
    x = [1, 2, 3, 99, 99, 3, 2, 1]
    x1, x2, x3 = np.split(x, [3, 5])

    grid = np.arange(16).reshape((4, 4))
    print(grid)

    upper, lower = np.vsplit(grid, [2])
    print(upper)
    print(lower)

    left, right = np.hsplit(grid, [2])
    print(left)
    print(right)
