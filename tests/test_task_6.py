from pandas import DataFrame
from gasprombank.task_6 import Document, make_documents, make_datefram
from pandas.testing import assert_frame_equal


def test_empty_rows():
    with open('tests/date/task_6_Rows_empty.json') as f:
        json_date = f.read()
    doc_check = Document.model_validate_json(json_date)
    doc = make_documents(json_date)
    assert doc_check == doc


def test_work():
    check_dataframe = DataFrame({
        'document_id': [1, 2, 3],
        'document_dt': [1718226111, 1718226222, 1718226333],
        'document_name': ['Alex_1', 'Alex_2', 'Alex_3'],
    })
    with open('tests/date/task_6.json') as f:
        json_date = f.read()
    data = make_documents(json_date)
    data_frame = make_datefram(data)
    assert_frame_equal(check_dataframe, data_frame)
