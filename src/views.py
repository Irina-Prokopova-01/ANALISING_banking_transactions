import json
import logging

from src.utils import (
    card_info,
    currency_rates,
    greetings,
    json_loader,
    reading_excel,
    stock_rates,
    top_five_transactions,
)

logger = logging.getLogger("views")
file_handler = logging.FileHandler("../logs/views.log", encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def views_file(date: str, transactions_df) -> str:
    """Функция принимает дату (строка) и DataFrame с данными по транзакциям.
    Возвращает ответ с приветствием, информацией по картам,
    топ-5 транзакций стоимость валюты и акций в виде json-строки."""
    try:
        logger.info(
            "Функция начинает работу, собирает результаты работ своих подфункций."
        )
        # transactions = transactions_df.to_dict(orient="records")
        greeting = greetings(date)
        logger.info("Функция приветствия завершила свою работу.")
        info_about_cards = card_info(transactions_df)
        logger.info("Функция по сбору информации по картам завершила свою работу.")
        five_transactions = top_five_transactions(transactions_df)
        logger.info("Функция топ-5 транзакций завершила свою работу.")
        users_settings = json_loader()
        currency = currency_rates(users_settings[0])
        logger.info("Функция курса валют завершила свою работу.")
        stock = stock_rates(users_settings[1])
        logger.info("Функция котировок акций завершила свою работу.")
        logger.info("Функция формирует общий результат результат.")
        result_dict = {
            "greeting": greeting,
            "cards": info_about_cards,
            "top_transactions": five_transactions,
            "currency_rates": currency,
            "stock_prices": stock,
        }
        result_json = json.dumps(
            result_dict, ensure_ascii=False, indent=2, separators=(",", ": ")
        )
        logger.info("Функция успешно завершила свою работу.")
        return result_json
    except Exception:
        logger.error("При работе функции произошла ошибка.")
        raise ValueError("При работе функции произошла ошибка.")


if __name__ == "__main__":
    data = reading_excel("../data/operations.xlsx")
    print(views_file("2024-07-06 10:42:30", data))
