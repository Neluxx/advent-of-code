import re

from input import memory

# Define patterns for mul, do, and don't instructions
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Split the memory into a list of instructions
instructions = re.split(r"(\bdo\(\)|\bdon't\(\))", memory)

# Initialize state and results
is_enabled = True
results = []

# Process each instruction or chunk
for instruction in instructions:
    # Check for do() and don't() instructions
    if re.match(do_pattern, instruction):
        is_enabled = True
    elif re.match(dont_pattern, instruction):
        is_enabled = False
    else:
        # Process mul instructions if enabled
        matches = re.findall(mul_pattern, instruction)
        if is_enabled:
            for num1, num2 in matches:
                product = int(num1) * int(num2)
                results.append(product)

# Calculate the final result
print("Result:", sum(results))
