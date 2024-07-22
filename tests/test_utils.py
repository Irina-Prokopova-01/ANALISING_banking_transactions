import os
from unittest.mock import patch

import pytest

from src.utils import (
    card_info,
    currency_rates,
    greetings,  # reading_excel,
    json_loader,
    stock_rates,
    top_five_transactions,
)


@pytest.fixture
def greeting_fix():
    return "2025-12-06 19:42:30"


def test_greetings_with_fixture(greeting_fix):
    assert greetings(greeting_fix) == "Добрый вечер!"


@pytest.mark.parametrize(
    "date, expected",
    [("2024-07-06 14:42:30", "Добрый день!"), ("2044-12-06 04:42:30", "Доброй ночи!")],
)
def test_greetings(date, expected):
    assert greetings(date) == expected


def test_greetings_with_wrong_date():
    with pytest.raises(ValueError) as exc_info:
        greetings("abcd")
        assert str(exc_info.value) == "Введены некорректные данные!"


# @patch("pandas.read_excel")
# def test_reading_excel(mock_read_excel):
#     mock_read_excel.return_value = pd.DataFrame(
#         [
#             {
#                 "id": 650703.0,
#                 "state": "EXECUTED",
#                 "date": "2023-09-05T11:30:32Z",
#                 "amount": 16210.0,
#                 "currency_name": "Sol",
#             }
#         ]
#     )
#     result = reading_excel("../tests/test_file.xlsx")
#     assert result == [
#                 {
#                     "id": 650703.0,
#                     "state": "EXECUTED",
#                     "date": "2023-09-05T11:30:32Z",
#                     "amount": 16210.0,
#                     "currency_name": "Sol",
#                 }
#             ]
#


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {
                    "Дата операции": "28.03.2018 09:24:15",
                    "Дата платежа": "29.03.2018",
                    "Номер карты": "*7197",
                    "Статус": "OK",
                    "Сумма операции": -150.0,
                    "Валюта операции": "RUB",
                    "Сумма платежа": -150.0,
                    "Валюта платежа": "RUB",
                    "Кэшбэк": "nan",
                    "Категория": "Связь",
                    "MCC": 4814.0,
                    "Описание": "МТС",
                    "Бонусы (включая кэшбэк)": 3,
                    "Округление на инвесткопилку": 0,
                    "Сумма операции с округлением": 150.0,
                },
                {
                    "Дата операции": "28.03.2018 08:23:56",
                    "Дата платежа": "30.03.2018",
                    "Номер карты": "*7197",
                    "Статус": "OK",
                    "Сумма операции": -197.7,
                    "Валюта операции": "RUB",
                    "Сумма платежа": -197.7,
                    "Валюта платежа": "RUB",
                    "Кэшбэк": "nan",
                    "Категория": "Супермаркеты",
                    "MCC": 5411.0,
                    "Описание": "Billa",
                    "Бонусы (включая кэшбэк)": 3,
                    "Округление на инвесткопилку": 0,
                    "Сумма операции с округлением": 197.7,
                },
            ],
            [{"last_digits": "7197", "total_spent": -347.7, "cashback": -3.48}],
        )
    ],
)
def test_card_info(transactions, expected):
    assert card_info(transactions) == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {"Сумма операции": 1},
                {"Сумма операции": 9},
                {"Сумма операции": 4},
                {"Сумма операции": 31},
                {"Сумма операции": 11},
                {"Сумма операции": -17},
                {"Сумма операции": -100},
                {"Сумма операции": 5},
            ],
            [
                {"Сумма операции": 9},
                {"Сумма операции": 11},
                {"Сумма операции": -17},
                {"Сумма операции": 31},
                {"Сумма операции": -100},
            ],
        )
    ],
)
def test_top_five_transactions(transactions, expected):
    assert top_five_transactions(transactions) == expected


users_settings = {"user_currencies": "USD"}


@patch("json.load")
def test_json_loader(mock_json_load):
    mock_json_load.return_value = {"user_currencies": ["USD"], "user_stocks": ["AAPL"]}
    assert json_loader() == (["USD"], ["AAPL"])


def test_json_loader_with_wrong_file_name():
    with pytest.raises(ValueError) as exc_info:
        json_loader("abcd.json")
        assert (
            str(exc_info.value)
            == "Возникла ошибка при обработке файла пользовательских настроек!"
        )


request_to_return_currency = {
    "query": {"amount": 1, "from": "USD", "to": "RUB"},
    "result": 90.00,
    "success": True,
}


@patch("requests.get")
@patch.dict(os.environ, {"API_KEY_2": "my_api_key"})
def test_currency_rates(mock_request):
    mock_request.return_value.json.return_value = request_to_return_currency
    assert currency_rates(["USD"]) == [{"currency": "USD", "rate": 90.0}]
    mock_request.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1",
        headers={"apikey": "my_api_key"},
        timeout=5,
        allow_redirects=False,
    )


def test_currency_rates_with_wrong_data():
    with pytest.raises(Exception) as exc_info:
        currency_rates("ABC")
        assert str(exc_info.value) == "При работе функции произошла ошибка!"


request_to_return_stock = {"Global Quote": {"01. symbol": "IBM", "05. price": 10.00}}


@patch("requests.get")
@patch.dict(os.environ, {"API_KEY_STOCK": "my_api_key"})
def test_stock_rates(mock_request):
    mock_request.return_value.json.return_value = request_to_return_stock
    assert stock_rates(["IBM"]) == [{"price": 10.0, "stock": "IBM"}]
    # mock_request.assert_called_once_with(
    #     "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=my_api_key",
    #     timeout=5,
    #     allow_redirects=False,
    # )


def test_stock_rates_with_wrong_data():
    with pytest.raises(Exception) as exc_info:
        stock_rates("ABC")
        assert str(exc_info.value) == "При работе функции произошла ошибка!"
