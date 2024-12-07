import itertools
import operator

from utils import get_sanitized_input


def _get_paired_items(report_data) -> list[tuple[int]]:
    return itertools.pairwise(report_data)


def _check_is_data_increasing(paired_items) -> bool:
    return all(itertools.starmap(operator.lt, paired_items))


def _check_is_data_decreasing(paired_items) -> bool:
    return all(itertools.starmap(operator.gt, paired_items))


def _check_report_items_consistency(paired_items) -> bool:
    return all(itertools.starmap(lambda current_item, next_item: 1 <= abs(current_item - next_item) <= 3, paired_items))


def _check_report_data_consistency(report_data) -> bool:
    paired_items = list(_get_paired_items(report_data))
    return all([
        _check_is_data_decreasing(paired_items) or _check_is_data_increasing(paired_items),
        _check_report_items_consistency(paired_items)
    ])


def get_report_safety_score(sanitized_data) -> int:
    return sum((_check_report_data_consistency(report_data) for report_data in sanitized_data))


if __name__ == '__main__':
    print(get_report_safety_score(get_sanitized_input('day_2.txt')))
