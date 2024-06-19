# Задание:
# 	1. Получить JSON из внешнего API
# 		ендпоинт: GET https://api.gazprombank.ru/very/important/
# docs?documents_date={"начало дня сегодня в виде таймстемп"}
# 	2. Валидировать входящий JSON используя модель pydantic
# 		(из ТЗ известно что поле "key1" имеет тип int,
# "key2"(datetime), "key3"(str))
# 	2. Представить данные "Columns" и "Rows" в виде
# плоского csv-подобного pandas.DataFrame
# 	3. В полученном DataFrame произвести переименование полей по след. маппингу
# 		"key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
# 	3. Полученный DataFrame обогатить доп. столбцом:
# 		"load_dt" -> значение "сейчас"(датавремя)

import requests
import json
import logging
from datetime import datetime
from pydantic import BaseModel, ValidationError, field_validator
from pandas import DataFrame


def get_beginner_today() -> int:
    now = datetime.now()
    start_of_today = datetime(now.year, now.month, now.day)

    return int(start_of_today.timestamp())


def get_time() -> int:
    return int(datetime.now().timestamp())


def get_json(documents_date: int) -> json:
    url = 'https://api.gazprombank.ru/very/important/docs'
    params = {
        'documents_date': documents_date
    }

    response = requests.get(url=url, params=params, timeout=30)

    return response.json()


class Document(BaseModel):
    Columns: list
    Description: str
    RowCount: int
    Rows: list[list]

    @field_validator('Rows')
    def value_rows(cls, rows):
        for row in rows:
            if not isinstance(row[0], int):
                logging.warning(f'{row[0]} is not integer')
                raise ValueError(f'{row[0]} is not integer')
            elif not isinstance(row[1], int) or len(str(row[1])) != 10:
                logging.warning(f'{row[1]} is not int and not lenght 10')
                raise ValueError(f'{row[1]} is not int and not lenght 10')
            elif not isinstance(row[2], str):
                logging.warning(f'{row[1]} is not string')
                raise ValueError(f'{row[1]} is not string')
        return rows


def make_documents(date: json) -> Document:
    try:
        docs = Document.model_validate_json(date)
        logging.info('Document has been made')
        return docs
    except NameError as e:
        logging.warning('No response was received from the URL.')
        raise SystemExit(e)
    except ValidationError as e:
        logging.warning(e.json())
        raise SystemExit(e)


def make_datefram(date: Document) -> DataFrame:
    values = zip(*date.Rows)
    result = DataFrame(dict(zip(date.Columns, values)))
    result = result.rename(columns={
        "key1": "document_id",
        "key2": "document_dt",
        "key3": "document_name"
        })
    return result


def add_load_dt(date: DataFrame) -> DataFrame:
    time = get_time()
    count_line_date = len(date)
    values = [time]*count_line_date
    date.insert(count_line_date, 'load_dt', values)
    return None


def main():
    today_timestamp = get_beginner_today()

    try:
        json_date = get_json(today_timestamp)
        logging.info('Response has been gotten')
    except requests.exceptions.Timeout as error:
        logging.warning(f'Connection timed out. {error}')
        raise SystemExit()

    documents = make_documents(json_date)

    result = make_datefram(documents)
    add_load_dt(result)
    return result


if __name__ == '__main__':
    print(main())
