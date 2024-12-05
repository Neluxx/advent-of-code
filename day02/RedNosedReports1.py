from Reports import reports

safe_reports = 0

for levels in reports:
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    has_valid_differences = all(
        1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)
    )

    if (is_increasing or is_decreasing) and has_valid_differences:
        safe_reports += 1

print(safe_reports)
