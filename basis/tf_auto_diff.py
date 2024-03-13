import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    x = tf.Variable(3.0)

    with tf.GradientTape() as tape:
        y = x**2
    
    # dy = 2x * dx
    dy_dx = tape.gradient(y, x)
    print(dy_dx.numpy())

    w = tf.Variable(tf.random.normal((3, 2)), name='w')
    b = tf.Variable(tf.zeros(2, dtype=tf.float32), name='b')
    x = [[1., 2., 3.]]

    with tf.GradientTape(persistent=True) as tape:
        y = x @ w + b
        loss = tf.reduce_mean(y**2)
