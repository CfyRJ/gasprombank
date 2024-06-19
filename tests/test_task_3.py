import pytest
from gasprombank.task_3 import make_dicts_from_lists


OPTIONS = [
    (
        [[1, 'ku', [1, 'ku', ()]], [4, 5, 6]],
        [{'k1': 1, 'k2': 'ku', 'k3': [1, 'ku', ()]},
         {'k1': 4, 'k2': 5, 'k3': 6}],
         ),
    ([], []),
    ([[], []], [{}, {}]),

]


@pytest.mark.parametrize('date, answer', OPTIONS)
def test_make_dicts_from_lists(date, answer):
    assert make_dicts_from_lists(date) == answer
