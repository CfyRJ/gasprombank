import pytest
from gasprombank.task_1 import analyz_date


PATH_FILE = 'tests/date/file.csv'
PATH_FILE_EMPTY = 'tests/date/file_empty.csv'
PATH_FILE_JUST_NAME_COLUMN = 'tests/date/file_just_name_column.csv'
CHECK_DATE_CORRECT = {
    'unique_id':
    [['Фамилия2', 'Имя2', 'Отчество2', '11.01.1972', '457865234-3431'],
     ['Фамилия54', 'Имя54', 'Отчество54', '25.04.1986', '457865234-3454'],
     ['Фамилия0', 'Имя0', 'Отчество0', '10.01.1992', '457865234-3500'],
     ['Фамилия10', 'Имя10', 'Отчество10', '10.10.2010', '457865234-3501'],
     ['Фамилия12', 'Имя12', 'Отчество12', '12.12.2012', '457865234-3502']],
    'identical_id':
    [['Фамилия1', 'Имя1', 'Отчество1', '21.11.1998', '312040348-3048'],
     ['Фамилия3', 'Имя3', 'Отчество3', '20.08.1978', '312040348-3048']]
     }
CHECK_DATE_EMPTY = {}
CHECK_DATE_JUST_NAME = {'unique_id': [], 'identical_id': []}

OPTIONS = [
    (PATH_FILE, CHECK_DATE_CORRECT),
    (PATH_FILE_EMPTY, CHECK_DATE_EMPTY),
    (PATH_FILE_JUST_NAME_COLUMN, CHECK_DATE_JUST_NAME)
    ]


@pytest.mark.parametrize("path_file, check_date", OPTIONS)
def test_analyz_date(path_file, check_date):
    assert analyz_date(path_file) == check_date
