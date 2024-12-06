from input import reports


def is_safe_report(levels):
    """Check if a report is safe."""
    is_increasing = all(levels[i] < levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] > levels[i + 1] for i in range(len(levels) - 1))
    has_valid_differences = all(
        1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(len(levels) - 1)
    )

    return (is_increasing or is_decreasing) and has_valid_differences


def is_safe_report_with_one_removal(levels):
    """Check if a report can be safe by removing one level."""
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1 :]
        if is_safe_report(modified_levels):
            return True
    return False


def get_safe_reports_count(reports, with_dampener):
    """Count how many reports are safe including Problem Dampener logic."""
    safe_count = 0
    for levels in reports:
        if with_dampener:
            if is_safe_report(levels) or is_safe_report_with_one_removal(levels):
                safe_count += 1
        else:
            if is_safe_report(levels):
                safe_count += 1
    return safe_count


print("Safe reports:", get_safe_reports_count(reports, False))
print("Safe reports with dampener:", get_safe_reports_count(reports, True))
