import os
import struct
import zipfile

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

    os.remove('temp_file.zip')



