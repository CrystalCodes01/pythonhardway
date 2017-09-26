def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# better way of doing the same thing
def print_two_agian(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#no arguments
def print_none():
    print("I got nothin")


print_two("Crystal", "Maria")
print_two_agian("Crystal", "Maria")
print_one("First!")
print_none()
