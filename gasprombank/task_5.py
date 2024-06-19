# В наличии текстовый файл с набором русских
# слов(имена существительные, им.падеж)
# Одна строка файла содержит одно слово.
# Задание:
# Написать программу которая выводит список слов, 
# каждый элемент списка которого - это новое слово,
# которое состоит из двух сцепленных в одно,
# которые имеются в текстовом файле.
# Порядок вывода слов НЕ имеет значения


def get_date_file(path: str) -> list[str]:
    try:
        with open(path) as file:
            date = file.read().lower().split()
    except IOError:
        raise f'Error opening file.'
    return date


def input_word() -> str:
    '''
    Returns the guaranteed one word entered by the user.
    '''
    while True:
        word = input('Enter one word. ').split()
        if len(word) == 1:
            return word[0]


def get_new_words(path: str, user_word: str) -> list[str]:
    '''
    The function mixes words from the path with
    the user_word. Returns a list of new words.

    path: path to the file with the original words
    user_word: the word the user enters
    '''

    date = get_date_file(path)
    result = []

    for i in range(len(user_word)-1, -1, -1):
        prefix = user_word[i:]
        for word in date:
            if user_word == word:
                continue
            if word.startswith(prefix):
                result.append(user_word[:i]+word)
    return result


def main(path: str):
    user_word = input_word().lower()
    return get_new_words(path, user_word)


if __name__ == '__main__':
    path = 'test-task-work/gasprombank/tests/date/date_task_5.txt'
    # date = get_date_file(path)
    # print(date, type(date))
    # print(input_word())
    print(*main(path), sep='\n')
