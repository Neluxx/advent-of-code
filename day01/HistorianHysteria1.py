from List1 import list1
from List2 import list2

list1.sort()
list2.sort()

distances = [abs(a - b) for a, b in zip(list1, list2)]

print(sum(distances))
