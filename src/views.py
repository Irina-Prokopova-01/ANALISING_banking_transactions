# Функция для страницы «Главная» расположена в модуле
# views.py
# Функция для страницы «Главная» принимает на вход
# DataFrame
# Вспомогательные функции, необходимые для работы функции страницы
# «Главная», расположены в модуле
# utils.py
# Основные функции для генерации JSON-ответов реализуйте в отдельном модуле
# views.py
# Валюты и акции для отображения на веб-страницах задаются в отдельном
# файле пользовательских настроек
# user_settings.json

# Реализуйте набор функций и главную функцию, принимающую
# на вход строку с датой и временем в формате
# YYYY-MM-DD HH:MM:SS
#  и возвращающую JSON-ответ со следующими данными:
#
# Приветствие в формате
# "???"
# , где
# ???
#  — «Доброе утро» / «Добрый день» / «Добрый вечер» / «Доброй ночи»
#  в зависимости от текущего времени.
# По каждой карте:
# последние 4 цифры карты;
# общая сумма расходов;
# кешбэк (1 рубль на каждые 100 рублей).
# Топ-5 транзакций по сумме платежа.
# Курс валют.
# Стоимость акций из S&P500.


import json

# from config import VIEWS_LOGS
from src.utils import (card_info, currency_rates, greetings,  # json_loader,
                       reading_excel, stock_rates, top_five_transactions)

# import logging



def views_file(date: str, transactions_df) -> str:
    """Функция принимает дату (строка) и DataFrame с данными по транзакциям.
    Возвращает ответ с приветствием, информацией по картам,
    топ-5 транзакций стоимость валюты и акций в виде json-строки."""
    try:
        # transactions = transactions_df.to_dict(orient="records")
        greeting = greetings(date)
        info_about_cards = card_info(transactions_df)
        five_transactions = top_five_transactions(transactions_df)
        # users_settings = json_loader()
        # currensy = currency_rates(users_settings[0])
        # stock = stock_rates(users_settings[1])
        result_dict = {
            "greeting": greeting,
            "cards": info_about_cards,
            "top_transactions": five_transactions,
            # "currency_rates": currensy,
            # "stock_prices": stock,
        }
        result_json = json.dumps(result_dict, ensure_ascii=False)
        return result_json
    except Exception:
        raise ValueError("При работе функции произошла ошибка.")


if __name__ == "__main__":
    data = reading_excel("../data/operations.xlsx")
    print(views_file("2024-07-06 10:42:30", data))
