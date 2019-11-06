import sys
import math


print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    test = "test"
    greeting = 'Hello {}'.format(who_to_greet)
    return greeting

print (greet('swakin'))
print (greet('world'))