import itertools
import operator
import re
from functools import reduce
from typing import Iterable

from utils import get_input_data


def _extract_method_args(args: str) -> list[int]:
    extracted_args = re.findall(r'(\d+,\d+)', args)[0].split(',')
    return list(map(int, extracted_args))


def _remove_noise_from_method_calls(method_calls: list[tuple[str]]) -> Iterable[list[str]]:
    return map(lambda t: [i for i in t if i], method_calls)


def _extract_pattern_from_string(lines: list[str], pattern: str) -> list[tuple]:
    return itertools.chain.from_iterable([re.findall(pattern, line) for line in lines])


def _get_valid_method_calls(lines: list[str]) -> Iterable[list[str]]:
    return _remove_noise_from_method_calls(
        _extract_pattern_from_string(lines, r'(mul)(\(\d+,\d+\))|(do\(\))|(don\'t\(\))')
    )


def _evaluate_single_call(fn_str: str, args_str: str) -> int:
    fn, args = getattr(operator, fn_str, None), _extract_method_args(args_str)
    return fn(*args) if fn else 0


def calculate_all_method_calls(lines: list[str]) -> int:
    return reduce(
        operator.add,
        (
            _evaluate_single_call(fn_str, args_str) for fn_str, args_str in
            _extract_pattern_from_string(lines, r'(mul)(\(\d+,\d+\))')
        ),
        0
    )


def get_accumulative_state(state: tuple, method_with_args: list) -> tuple:
    accumulator, toggle_value = state
    toggle_flags = {'don\'t()': False, 'do()': True}
    needs_calculation = method_with_args[0] not in toggle_flags.keys() and toggle_value
    new_toggle_value = toggle_flags.get(method_with_args[0], None)
    toggle_value = new_toggle_value if new_toggle_value is not None else toggle_value
    calculated_single_call = _evaluate_single_call(*method_with_args) if needs_calculation else 0
    return accumulator + calculated_single_call, toggle_value


def calculate_valid_method_calls(lines: list[str]) -> int:
    valid_method_calls = _get_valid_method_calls(lines)
    return reduce(get_accumulative_state, valid_method_calls, (0, True))[0]


if __name__ == '__main__':
    print(f'calculate_all_method_calls: {calculate_all_method_calls(get_input_data("day_3.txt"))}')
    print(f'calculate_only_valid_method_calls: {calculate_valid_method_calls(get_input_data("day_3.txt"))}')
