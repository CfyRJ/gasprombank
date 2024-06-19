import pytest
from gasprombank import task_2


DATE = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

OPTIONS = [
    [],
    [set(), set()],
]


def test_correct():
    assert task_2.get_count_number(DATE) == 14
    assert task_2.get_count_unique_number(DATE) == 13
    assert task_2.get_sum_all_num(DATE) == 264
    assert task_2.get_sum_all_unique_num(DATE) == 253
    assert task_2.get_midle_value(DATE) == 18.86
    assert task_2.get_sets_tuple(DATE) == (11, 3, 5, 32, 17, 2, 87,
                                           4, 44, 7, 8, 9, 11, 24)


@pytest.mark.parametrize("date", OPTIONS)
def test_empty(date):
    assert task_2.get_count_number(date) == 0
    assert task_2.get_count_unique_number(date) == 0
    assert task_2.get_sum_all_num(date) == 0
    assert task_2.get_sum_all_unique_num(date) == 0
    assert task_2.get_midle_value(date) == 0
    assert task_2.get_sets_tuple(date) == ()
