from sys import argv
#argv is the "argument variable" - "modules" - "libraries"
#This variable holds the arguments you pass to your Python script when you run it

script, first, second, third = argv
#^^"unpacks" argv so that, rather than holding all the arguments,
#it gets assigned to four variables you can work with: script, first, second, and third

print ("The script is called:", script)
print ("The first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

#to run python3.6 ex8.py first 2nd 3rd give the argv values


print (">>>> argv=", repr(argv))
