from collections import Counter
from itertools import combinations
from itertools import chain
import time

st = time.time()

cols = []
cols_fixed = []
nums = []
with open("retail.txt") as file:
    for line in file:
        cols.append(line.strip())
        for item in line.split():
            nums.append(item)

for i in range(0, len(cols)):
    cols_fixed.append(cols[i].split())

thres = round(0.01 * len(cols))
# print(len(cols))
item_support = Counter(nums)

freq_items = []
for num, freq in item_support.items():
    if (freq >= thres):
        freq_items.append(num)

lst = []

print('im here')

for col in cols_fixed:
    for item in col:
        lst.append(item)

# print(cols_fixed)
# print(freq_items)
# print(lst)

print('im done')

freq_pairs = list(combinations(lst, 2))

print('hi :0')

# print(freq_items)
# print(" ")
print(freq_pairs)

et = time.time()

execution_time = et - st
print('Execution time:', execution_time, 'seconds')