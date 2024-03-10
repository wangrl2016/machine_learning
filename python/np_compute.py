import numpy as np
import timeit

if __name__ == '__main__':
    L = np.random.random(100)
    print(sum(L))
    print(np.sum(L))

    big_array = np.random.rand(100000)
    
    print(timeit.timeit('sum(big_array)',
                  number=10,
                  setup='from __main__ import big_array'))
    print(timeit.timeit('np.sum(big_array)',
                        number=10,
                        setup='from __main__ import big_array; import numpy as np'))
    
    print(min(big_array))
    print(max(big_array))
    print(np.min(big_array))
    print(np.max(big_array))

    print(timeit.timeit('min(big_array)',
                  number=10,
                  setup='from __main__ import big_array;'))
    print(timeit.timeit('np.min(big_array)',
                        number=10,
                        setup='from __main__ import big_array; import numpy as np'))
    
    print(big_array.min(), big_array.max(), big_array.sum())

    M = np.random.random((3, 4))
    print(M)

    print(M.sum())

    # Aggregation functions take an additional argument specifying the axis along which
    # the aggregate is computed.
    print(M.min(axis=0))

    print(M.max(axis=1))

    a = np.array([0, 1, 2])
    b = np.array([5, 5, 5])

    print(a + b)
    print(a + 5)

    M = np.ones((3, 3))
    print(M)
    print(M + a)

    a = np.arange(3)
    b = np.arange(3)[:, np.newaxis]
    print(a)
    print(b)
    print(a + b)
