import pytest
from gasprombank.task_5 import get_new_words

PATH = 'tests/date/date_task_5.txt'
OPTIONS = [
    ('ласты', ['ластык', 'ластыковка']),
    ('кабала', ['кабаласты', 'кабаласт']),
    ('стыковка', ['стыковкабала', 'стыковкарась']),
]


@pytest.mark.parametrize('test_word, answer', OPTIONS)
def test_get_new_words(test_word, answer):
    assert get_new_words(PATH, test_word) == answer
