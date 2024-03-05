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

    os.remove('temp_file.zip')

    # The `struct` modules provides `pack()` and `unpack()` functions for working with variable
    # length binary recorde formats. Pack codes `H` and `I` represent two and four byte
    # unsigned numbers respectively. The `<` indicates that they are standard size and in
    # litter-endian byte order.

    pass
