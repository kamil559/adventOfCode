import functools

from sourcecode.utils import get_sanitized_input


def get_ordered_zipped_elements(sanitized_input):
    sorted_left_side = sorted(map(lambda e: e[0], sanitized_input))
    sorted_right_side = sorted(map(lambda e: e[1], sanitized_input))
    return zip(sorted_left_side, sorted_right_side)


def _get_local_distance(accumulated_distance, items):
    left_item, right_item = items
    return accumulated_distance + abs(left_item - right_item)


def get_total_distance(zipped_elements):
    return functools.reduce(_get_local_distance, zipped_elements, 0)


if __name__ == '__main__':
    print(get_total_distance(get_ordered_zipped_elements(get_sanitized_input('day_1.txt'))))
