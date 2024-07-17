
# Вспомогательные функции, необходимые для работы функции страницы
# «Главная», расположены в модуле
# utils.py

# Вспомогательные функции, необходимые для работы функции страницы
# «Главная», используют библиотеку
# json

# Вспомогательные функции, необходимые для работы функции
# страницы «Главная», используют API.


# Вспомогательные функции, необходимые для работы функции страницы
# «Главная», используют библиотеку
# datetime

# Вспомогательные функции, необходимые для работы функции страницы
# «Главная», используют библиотеку
# logging


# Вспомогательные функции, необходимые для работы функции страницы
# «Главная», используют библиотеку
# pandas

import os
import datetime
import pandas as pd
import openpyxl
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(currency: str, amount: float) -> float:
    """Обращение к внешнему API для получения текущего курса валют"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": os.getenv("API_KEY")}
    params = {"to": "RUB", "from": currency, "amount": amount}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    return round(data["result"], 2)
# def get_transactions_xlsx_file(path: str) -> list[dict]:
#     """Функция, которая принимает на вход путь до файла с расширением xlsx и
#     возвращает список словарей с данными о фин. транзакциях."""
#     if not os.path.exists(path):
#         return []
#         if ".xlsx" in path:
#             xlsx_file_transactions = pd.read_excel(path)
#             return xlsx_file_transactions.to_dict(orient="records")


def user_greeting() -> str:
    """Функция приветствия в зависимости от текущего времени «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи»."""
    now = datetime.datetime.now()
    if now.hour >= 4 and now.hour <= 12:
        greet = 'Доброе утро!'
    elif now.hour >= 12 and now.hour <= 16:
        greet = 'Добрый день!'
    elif now.hour >= 16 and now.hour <= 0:
        greet = 'Добрый вечер!'
    else:
        greet = 'Доброй ночи!'
    return greet


def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскирующая номер карты"""
    if type(card_number) is not str:
        raise TypeError
    if card_number.isdigit() and len(card_number) == 16:
        masked_number = f"*{card_number[12:]}"
        return masked_number
    return None

def total_expenses(path: str, date_start: str, date_end: str) -> int:
    """Функция которая считает сумму расходов за период"""
    df = pd.read_excel(path)
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], dayfirst=True)
    filtered_df = df[(df['Дата операции'] >= date_start) & (df['Дата операции'] <= date_end)]
    sum_expenses = round(sum(filtered_df.loc[:, 'Сумма операции с округлением']))
    return sum_expenses


def cashback(df: list[dict]) -> int:
    """Функция считающая сумму cashback за период"""
    pass

def top_five_transactions(df: list[dict]) -> list[dict]:
    """Топ 5 транзакций по сумме платежа"""
    df = pd.read_excel(path)
    sort_df = df.sort_values('Сумма операции с округлением', ascending=False)
    return sort_df.head(5)


if __name__ == '__main__':
    card_number = '7000792289606361'
    path = "../data/operations.xlsx"



    # transactions = get_transactions_xlsx_file("../data/operations.json")
    # if transactions:
    #     print("Список транзакций:")
    #     for transaction in transactions:
    #         print(transaction)
    # else:
    #     print("Файл не найден, пустой или содержит некорректный формат.")

    print(get_mask_card_number(card_number))
    print(user_greeting())
    print(total_expenses(path, '28.12.2021', '29.12.2021'))
    print(top_five_transactions(path))
    print(convert_to_rubles('USD', '1'))

