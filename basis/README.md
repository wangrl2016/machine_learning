## Basic of Machine Learning

- [ ] Tensor

Tensors are multidimensional arrays with a uniform type (called a `dtype`). If you're
familiar with `NumPy`, tensors are (kind of) like `np.arrays`.

All tensors are immutable like Python numbers and strings: you can never update the contents
of the tensor, only create a new one.

Tensors have shapes. Some vocabulary:
* Shape: The length (number of elements) of each of the axes of a tensor.
* Rank: Number of tensor axes. A scalar has rank 0, a vector has rank 1, a matrix is rank 2.
* Axis or Dimension: A particular dimension of a tensor.
* Size: The total number of items in the tensor, the product of the shape vector's elements.

- [x] tf.version