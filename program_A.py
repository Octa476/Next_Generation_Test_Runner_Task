# Pseudo-Random Number Generator
import sys
import random

# The pseudo-random integer is in the [-LIMIT, LIMIT] interval.
LIMIT = 1000

# For every new line written to stdin execute the instructions.
for line in sys.stdin:
    # "Hi" command which writes to stdout "Hi".
    if line == "Hi\n":
        print('Hi')
    # "GetRandom" command which writes to stdout a pseudo-random integer.
    if line == "GetRandom\n":
        print(random.randint(-LIMIT, LIMIT))
    # "Shutdown" command which ends the loop(terminates the process gracefully).
    if line == "Shutdown\n":
        break
    # It pushes the output made by "print" to the stdout.
    sys.stdout.flush()
