from input import list1
from input import list2

list1.sort()
list2.sort()

distances = [abs(a - b) for a, b in zip(list1, list2)]
similarity_score = sum(value * list2.count(value) for value in list1)

print("Distances:", sum(distances))
print("Similarity Score:", similarity_score)
