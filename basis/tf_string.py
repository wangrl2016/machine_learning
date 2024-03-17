import tensorflow as tf

if __name__ == '__main__':
    # Converts each entry in the given tensor to strings.
    print(tf.strings.as_string([3, 2]))
    print(tf.strings.as_string([3.1415926, 2.71828], precision=2).numpy())

    # bytes split
    print(tf.strings.bytes_split('hello').numpy())
    print(tf.strings.bytes_split(['hello', '123']))

    # format
    tensor = tf.range(5)
    print(tf.strings.format('tensor: {}, suffix', tensor))
    tensor_a = tf.range(2)
    tensor_b = tf.range(1, 4, 2)
    print(tf.strings.format('a: {}, b: {}, suffix', (tensor_a, tensor_b)))

    # join
    print(tf.strings.join(['abc', 'def']).numpy())
    print(tf.strings.join([['abc', '123'],
                           ['def', '456'],
                           ['ghi', '789']]).numpy())
    print(tf.strings.join([['abc', '123'],
                           ['def', '456']], separator=' ').numpy())

    print(tf.strings.lower('CamelCase string and ALL CAPS'))

    # Joins all strings into a single, or join along an axis.
    print(tf.strings.reduce_join([['abc', '123'],
                                  ['def', '456']]).numpy())
    print(tf.strings.reduce_join([['abc', '123'],
                                  ['def', '456']], axis=-1).numpy())
    
    # split
    print(tf.strings.split('hello world').numpy())
    print(tf.strings.split(['hello world', 'a b c']))

    # strip
    print(tf.strings.strip(['\nTensorFlow', '  The python library ']).numpy())

    # substr
    input = [b'Hello', b'World']
    position = 1
    length = 3
    print(tf.strings.substr(input, position, length))

    # upper
    print(tf.strings.upper('CamelCase string and ALL CAPS'))
