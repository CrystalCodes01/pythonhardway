from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
#'w' is for write to file 'r' for read 'a' for append

print("Truncating the file. Goodbye!")
# target.truncate() <-- not needed as we are calling the 'w' write method

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")


lines=(line1, line2, line3)
target.write('\n'.join(lines))
target.write('\n')
# use .join and group all the lines together under var lines

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally we close it.")
target.close()

#to run python3.6 ex11.py ex10_sample.txt
