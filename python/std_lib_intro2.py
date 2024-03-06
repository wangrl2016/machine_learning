import array
import bisect
import collections
import decimal
import heapq
import os
import struct
import threading
import weakref, gc
import zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

class AValue:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return str(self.value)

if __name__ == '__main__':
    msg = 'This data dit not exist in a file before being added to the ZIP file.'
    zf = zipfile.ZipFile('temp_file.zip',
                         mode='w',
                         compression=zipfile.ZIP_DEFLATED)
    try:
        # temp_file.zip is zip name, from_string.txt is file name.
        zf.writestr('from_string.txt', msg)
    finally:
        zf.close()

    zf = zipfile.ZipFile('temp_file.zip', 'r')
    print(zf.read('from_string.txt'))
    zf.close()

    # The `struct` modules provides `pack()` and `unpack()` functions for working with variable
    # length binary recorde formats. Pack codes `H` and `I` represent two and four byte
    # unsigned numbers respectively. The `<` indicates that they are standard size and in
    # litter-endian byte order.
    with open('temp_file.zip', 'rb') as f:
        data = f.read()

    start = 0
    # Show the first file headers.
    for i in range(1):
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start+16])
        crc32, comp_size, uncomp_size, filename_size, extra_size = fields
        start += 16
        filename = data[start:start + filename_size]
        start += filename_size
        extra = data[start: start + extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size)
        start += extra_size + comp_size

    f = open('my_data.txt', 'a')
    f.write('Now the file has more content!')
    f.close

    background = AsyncZip('my_data.txt', 'my_archive.zip')
    background.start()

    print('The main program continues to run in foreground.')
    background.join()
    print('Main program waited until background was done.')

    # The `weakref` module provides tools for tracking objects without creating a reference.
    # When the object is no longer needed, it is automatically removed from a weakref
    # table and a callback is triggered for weakref objects.
    # Create a reference.
    a = AValue(10)
    # Does not create a reference.
    d = weakref.WeakValueDictionary()
    d['primary'] = a
    # Fetch the object if it is still alive.
    print(d['primary'])

    # Remove the one reference.
    del a
    gc.collect()

    # Entry was automatically removed.
    # d['primary']

    # Two byte unsigned binary numbers (typecode `H`) rather than the usual 16 bytes
    # per entry for regular lists of Python int objects.
    a = array.array('H', [4000, 10, 700, 22222])
    print(sum(a))
    print(a[1:3])

    d = collections.deque(['task1', 'task2', 'task3'])
    d.append('task4')
    print('Handling', d.popleft())

    scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
    bisect.insort(scores, (300, 'ruby'))
    print(scores)

    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    # Rearrange the list into heap order.
    heapq.heapify(data)
    # Add a new entry.
    heapq.heappush(data, -5)
    # Fetch the three smallest entries.
    print([heapq.heappop(data) for i in range(3)])

    print(round(decimal.Decimal('0.70') * decimal.Decimal('1.05'), 2))
    print(round(0.70 * 1.05, 2))

    print(decimal.Decimal('1.00') % decimal.Decimal('.10'))
    print(1.00 % 0.10)

    print(sum([decimal.Decimal('0.1')]*10) == decimal.Decimal('1.0'))
    print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0)

    decimal.getcontext().prec = 36
    print(decimal.Decimal(1) / decimal.Decimal(7))

    os.remove('temp_file.zip')
    os.remove('my_data.txt')
    os.remove('my_archive.zip')


