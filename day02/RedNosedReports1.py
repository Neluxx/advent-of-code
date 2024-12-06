from Reports import reports


def is_safe_report(levels):
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    has_valid_differences = all(
        1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)
    )

    return (is_increasing or is_decreasing) and has_valid_differences


def get_safe_reports_count(reports):
    return sum(1 for levels in reports if is_safe_report(levels))


print(get_safe_reports_count(reports))
