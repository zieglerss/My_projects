import time
import random

load = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.',]

print(''.join(load))

for i in range(0, 10):
    time.sleep(random.randint(0, 5))
    load[i] = '#'
    print(''.join(load))
