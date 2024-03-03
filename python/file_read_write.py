import json
import os

if __name__ == '__main__':
    f = open('temp_file', 'w', encoding='utf-8')
    f.close()

    # if you're not using the `with` keyword, then you should call `f.close()` to close the file and immediately
    # free up any system resources used by it.
    with open('temp_file', encoding='utf-8') as f:
        read_data = f.read()

    with open('temp_file', 'w', encoding='utf-8') as f:
        f.write('This is a test\n')
        value = ('the answer', 42)
        f.write(str(value))

    with open('temp_file', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)

    f = open('temp_file', 'wb+')
    f.write(b'0123456789abcdef')
    f.seek(5)
    print(f.read(1))
    # The position is computed from adding offset to a reference point; the reference point is
    # selected by the `whence` argument. A whence value of 0 meansure from the begining of the
    # file, 1 uses the current file position, and 2 uses the end of the file as the reference
    # point.
    print(f.seek(-3, 2))
    print(f.read(1))

    # Saving structured data with json.
    x = [1, 'simple', 'list']
    print(json.dumps(x))

    f = open('temp_file', 'w+')
    json.dump(x, f)
    f = open('temp_file', 'r')
    x = json.load(f)
    print(x)

    os.remove('temp_file')
