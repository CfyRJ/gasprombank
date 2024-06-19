# имеется список списков
# a = [[1,2,3], [4,5,6]]
# Задание:
# сделать список словарей
# b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]


def make_dicts_from_lists(date: list[list]) -> list[dict]:
    return [
        {f'k{i+1}': element[i] for i in range(len(element))}
        for element in date
        ]


if __name__ == '__main__':
    date = [[1, 2, 3], [4, 5, 6]]
    print(make_dicts_from_lists(date))
    date = []
    print(make_dicts_from_lists(date))
    date = [[], []]
    print(make_dicts_from_lists(date))
    date = [[1, 'ku', [1, 'ku', ()]], [4, 5, 6]]
    print(make_dicts_from_lists(date))
