from io import *

tsize = 1059+5

f = open("ab.bin","rb")
old_file_position = f.tell()
f.seek(0, SEEK_END)
size = f.tell()
f.seek(old_file_position, SEEK_SET)

fn = open("ab2.bin","wb")

data = f.read(size-tsize)
fn.write(data)

f.close()
fn.close()
