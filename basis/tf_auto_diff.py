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

    [dl_dw, dl_db] = tape.gradient(loss, [w,  b])
    print(w.shape)
    print(dl_dw.shape)

    my_vars = {
        'w': w,
        'b': b
    }
    grad = tape.gradient(loss, my_vars)
    print(grad['b'])

    # A trainable variable.
    x0 = tf.Variable(3.0, name='x0')
    # Not trainable.
    x1 = tf.Variable(3.0, name='x1', trainable=False)
    # Not a Variable: A variable + tensor returns a tensor.
    x2 = tf.Variable(2.0, name='x2') + 1.0
    # Not a variable.
    x3 = tf.constant(3.0, name='x3')

    with tf.GradientTape() as tape:
        y = (x0**2) + (x1**2) +(x2**2)
    
    grad = tape.gradient(y, [x0, x1, x2, x3])
    for g in grad:
        print(g)
    
    print(var.name for var in tape.watched_variables())

    x = tf.constant(3.0)
    with tf.GradientTape() as tape:
        tape.watch(x)
        y = x**2
    
    # dy = 2x * dx
    dy_dx = tape.gradient(y, x)
    print(dy_dx.numpy())

    x0 = tf.Variable(0.0)
    x1 = tf.Variable(10.0)

    with tf.GradientTape(watch_accessed_variables=False) as tape:
        tape.watch(x1)
        y0 = tf.math.sin(x0)
        y1 = tf.nn.softplus(x1)
        y = y0 + y1
        ys = tf.reduce_sum(y)

    # dys/dx1 = exp(x1) / (1 + exp(x1)) = sigmoid(x1)
    grad = tape.gradient(ys, {'x0': x0, 'x1': x1})
    print('dy/dx0:', grad['x0'])
    print('dy/dx1:', grad['x1'].numpy())

    x = tf.constant(3.0)
    with tf.GradientTape() as tape:
        tape.watch(x)
        y = x * x
        z = y * y
    
    # Use the tape to compute the gradient of z with respect to the
    # intermediate value y.
    # dz_dy = 2 * y and y = x**2 = 9
    print(tape.gradient(z, y).numpy())

    x = tf.constant([1, 3.0])
    with tf.GradientTape(persistent=True) as tape:
        tape.watch(x)
        y = x * x
        z = y * y

    # [4.0, 108.0] (4 * x**3 at x = [1.0, 3.0])
    print(tape.gradient(z, x).numpy())
    # [2.0, 6.0] (2 * x at x = [1.0, 3.0])
    print(tape.gradient(y, x).numpy())

    x = tf.Variable(2.0)
    with tf.GradientTape(persistent=True) as tape:
        y0 = x**2
        y1 = 1 / x
    
    print(tape.gradient(y0, x).numpy())
    print(tape.gradient(y1, x).numpy())

    x = tf.Variable(2.)
    with tf.GradientTape() as tape:
        y = x * [3., 4.]
    print(tape.gradient(y, x).numpy())

