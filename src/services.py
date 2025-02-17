import datetime
import json
# import logging
from math import ceil, floor
from typing import Any, Dict, List, Union

# from config import SERVICES_LOGS
from src.utils import reading_excel


def limit_payment(limit: int, payment: Union[int, float]) -> int:
    """Функция принимает лимит округления (целое число) и сумму операции (вещественное число),
    возвращает сумму операции, округлённую в соответствии с переданным лимитом (целое число).
    """
    if payment < 0:
        payment_with_limit = floor(payment / limit) * limit
    elif payment > 0:
        payment_with_limit = ceil(payment / limit) * limit
    return payment_with_limit


def date_sorting(month: str, transactions: List[Dict[str, Any]]) -> List[Dict]:
    """Функция принимает месяц сортировки (строка) и список транзакций (словарей),
    возвращает отсортированный по переданному месяцу список транзакций (словарей)."""
    sorted_transactions_list = []
    month_of_sorting = datetime.datetime.strptime(month, "%Y-%m").month
    year_of_sorting = datetime.datetime.strptime(month, "%Y-%m").year
    for transaction in transactions:
        month_of_operation = datetime.datetime.strptime(
            transaction["Дата операции"], "%d.%m.%Y %H:%M:%S"
        ).month
        year_of_operation = datetime.datetime.strptime(
            transaction["Дата операции"], "%d.%m.%Y %H:%M:%S"
        ).year
        if (
            month_of_sorting == month_of_operation
            and year_of_sorting == year_of_operation
        ):
            sorted_transactions_list.append(transaction)
    return sorted_transactions_list


def investment_bank(
    month: str, transactions: List[Dict[str, Any]], limit: int
) -> float:
    """Функция принимает месяц (строка), список транзакций (словарей) и лимит округления (целое число),
    возвращает сумму (вещественное число), которую удалось бы отложить в Инвесткопилку
    за указанный месяц при учёте указанного лимита округления."""
    investment_result = 0
    sorted_transactions_by_month = date_sorting(month, transactions)
    for transaction in sorted_transactions_by_month:
        rounded_payment = limit_payment(limit, transaction["Сумма операции"])
        investment_result += abs(rounded_payment) - abs(transaction["Сумма операции"])
    result = round(float(investment_result), 2)
    result_json = json.dumps(result, ensure_ascii=False)
    # print(data_from_excel)
    return result_json


if __name__ == "__main__":
    data_from_excel = reading_excel("../data/operations.xlsx")
    print(data_from_excel)
    print(investment_bank("2021-10", data_from_excel, 2))
