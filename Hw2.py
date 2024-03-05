import random
from collections import Counter

def find_duplicates(arr):
    counts=Counter(arr)
    duplicate=[num for num,count in counts.items() if count > 1]
    return duplicate

random.seed(400121055)
rand_numbers=[random.randint(1,21) for _ in range(1000)]
result=find_duplicates(rand_numbers)
print(result)

