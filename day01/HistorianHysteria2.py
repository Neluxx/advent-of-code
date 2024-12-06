from Lists import list1
from Lists import list2

similarity_score = sum(value * list2.count(value) for value in list1)

print(similarity_score)
