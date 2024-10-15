import sys
import random

for line in sys.stdin:
    if line == "Hi\n":
        print('Hi')
    if line == "GetRandom\n":
        print(random.randint(-1000, 1000))
    if line == "Shutdown\n":
        break
    sys.stdout.flush()
