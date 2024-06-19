# имеется текстовый файл file.csv, в котром
# разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные
# 3 строки, включая строку заголовков полей)
# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют
# разные данные - собрать отдельно такие записи


import csv


def read_date_csv(path: str) -> iter:
    with open(path, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            yield row


def get_identical_id(date: list[list], id: str, index_id: int) -> int:
    '''
    Is there a duplicate identifier in the list
    index_id: position identifier in the list

    return:
    index: position duplicate identifier in the list
    -1: duplicate identifier not found
    '''
    for index, line in enumerate(date):
        if line[index_id] == id:
            return index
    return -1


def analyz_date(path_file: str) -> dict:
    """
    return:
    {
    unique_id: unique data
    identical_id: unique data with the same identifier
    }
    """
    date = read_date_csv(path_file)

    try:
        field_names = date.__next__()
    except StopIteration:
        return {}

    index_field_id = field_names.index('id')
    unique_id_date = []
    identical_id_unique_date = []
    for line in date:
        identical_index = get_identical_id(
            unique_id_date,
            line[index_field_id],
            index_field_id
        )
        if identical_index == -1:
            unique_id_date.append(line)
        elif unique_id_date[identical_index] != line:
            identical_id_unique_date.append(unique_id_date.pop(identical_index))
            identical_id_unique_date.append(line)

    return {'unique_id': unique_id_date,
            'identical_id': identical_id_unique_date}


if __name__ == '__main__':
    path = 'test-task-work/gasprombank/tests/date/file.csv'
    res = analyz_date(path)
    print(res)

    print('unique_id')
    for line in res['unique_id']:
        print(line)

    print('identical_id')
    for line in res['identical_id']:
        print(line)

    path = 'test-task-work/gasprombank/tests/date/file_empty.csv'
    res = analyz_date(path)
    print(res)

    path = 'test-task-work/gasprombank/tests/date/file_just_name_column.csv'
    res = analyz_date(path)
    print(res)
