from sys import argv
from os.path import exists
#exists checks true/false if the file exists

script, from_file, to_file = argv

# print (f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()
# ^^ combine open and read shorten the code
# in_file = open(from_file)
# indata = in_file.read()

# print(">>>>>> in_file=", repr(in_file))
#
# print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

open(to_file, 'w').write(indata)
# ^^ combine open and write
# out_file = open(to_file, 'w')
# out_file.write(indata)

print("Alright, all done.")

# out_file.close() -- not needed but good practice for later
# in_file.close()  -- not needed but good practice for later

# to run python3.6 ex12.py ex10_sample.txt test.txt
