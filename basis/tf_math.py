import numpy as np
import tensorflow as tf

if __name__ == '__main__':
    # Computes the absolute value of a tensor.
    x = tf.constant([-2.25, 3.25])
    print(tf.abs(x))

    # complex number
    x = tf.constant([[-2.25 + 4.75j], [-3.25 + 5.75j]])

    # Computes acos of x element-wise.
    x = tf.constant([1.0, -0.5, 3.4, 0.2, 0.0, -2], dtype=tf.float32)
    print(tf.math.acos(x))

    x = [1, 2, 3, 4, 5]
    y = 1
    print(tf.add(x, y))

    x = tf.convert_to_tensor([1, 2, 3, 4, 5])
    y = tf.convert_to_tensor(1)
    print(x + y)

    x = [1, 2, 3, 4, 5]
    y = tf.constant([1, 2, 3, 4, 5])
    print(tf.add(x, y))

    x = tf.constant([1, 2], dtype=tf.int8)
    y = [2**7 + 1, 2**7 + 2]
    print(tf.add(x, y))

    x = np.ones(6).reshape(1, 2, 1, 3)
    y = np.ones(6).reshape(2, 1, 3, 1)
    print(tf.add(x, y).shape.as_list())

    # Returns the index with the largest value across axes of a tensor.
    A = tf.constant([2, 20, 30, 3, 6])
    print(tf.math.argmax(A))

    # Returns the index with the smallest value across axes of a tensor.
    a = [1, 10, 26.9, 2.8, 166.32, 62.3]
    print(tf.math.argmin(input=a))

    # Return the ceiling of the input, element-wise.
    print(tf.math.ceil([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0]))

    # cos
    x = tf.constant([-float("inf"), -9, -0.5, 1, 1.2, 200, 10000, float("inf")])
    print(tf.math.cos(x))

    # divide
    x = tf.constant([16, 12, 11])
    y = tf.constant([4, 6, 2])
    print(tf.divide(x, y))

    # Returns the truth value of (x == y) element-wise.
    x = tf.constant([2, 4])
    y = tf.constant(2)
    print(tf.math.equal(x, y))




