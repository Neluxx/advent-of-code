import re

from input import memory

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, memory)

results = []
for num1, num2 in matches:
    product = int(num1) * int(num2)
    results.append(product)

print("Result:", sum(results))
