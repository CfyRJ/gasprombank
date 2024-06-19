# в наличии список множеств. внутри множества целые числа
# m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
# Задание: посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все множества в один кортеж
# *написать решения в одну строку


def get_count_number(date: list[set]) -> int:
    return sum(map(len, date))


def get_sum_all_num(date: list[set]) -> int:
    return sum(map(sum, date))


def get_midle_value(date: list[set], round_num=2) -> int:
    try:
        return round(
            get_sum_all_num(date) / get_count_number(date),
            round_num
            )
    except ZeroDivisionError:
        return 0


def get_sets_tuple(date: list[set]) -> int:
    return tuple([num for element in date for num in element])


def get_combined_set(date: list[set]) -> set:
    result = set()
    for element in date:
        result.update(element)
    return result


def get_count_unique_number(date: list[set]) -> int:
    return len(get_combined_set(date))


def get_sum_all_unique_num(date: list[set]) -> int:
    return sum(get_combined_set(date))


if __name__ == '__main__':
    date = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
    print(get_count_number(date))
    print(get_count_unique_number(date))
    print(get_sum_all_num(date))
    print(get_sum_all_unique_num(date))
    print(get_midle_value(date))
    print(get_sets_tuple(date))
    date = [set(), set()]
    date = []
    print(get_count_number(date))
    print(get_count_unique_number(date))
    print(get_sum_all_num(date))
    print(get_sum_all_unique_num(date))
    print(get_midle_value(date))
    print(get_sets_tuple(date))
