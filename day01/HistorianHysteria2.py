from List1 import list1
from List2 import list2

similarity_score = 0

for value in list1:
    similarity_score += value * list2.count(value)

print(similarity_score)
