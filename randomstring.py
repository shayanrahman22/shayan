import random as rd
import string 
import time 
from collections import Counter

random_list = []

while True:
    random=''.join(rd.choices(string.ascii_lowercase,k=3))
    
    random_list.append(random)
    print(random)
    if random == 'cat':
        print("found")
        break

count = Counter(random_list)
for str,freq in count.items():
    if freq >1:
        print(str,"=",freq)
