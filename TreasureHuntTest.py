import random
from collections import deque

def bin(num):
    arr = []
    for i in range(3, -1, -1):
        arr.append((1 << i) & num != 0)
    arr = [1 if el else 0 for el in arr]
    return arr

num = random.randint(0, 15)
seq = [8, 10, 12, 10, 14, 10, 10, 12, 10]
print (num)

for el in seq:
    num ^= el  
    num = 0

    arr = deque(bin(num))
    arr.rotate(random.randint(0, 3))
    for i in range(4):
        if arr[i]:
            num += (1 << i)

    num ^= 15
    if num == 0:
        print ("good")
        break
    num ^= 15
    if num == 0:
        print ("good")
        break
