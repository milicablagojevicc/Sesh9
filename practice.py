import random
from pstats import count_calls

s = 0
while s <= 800:
    s = 0
    for i in range(0,10):
       s = s + random.randint(1, 101)
       print(s)
print("Final sum exceeds 800:", s)