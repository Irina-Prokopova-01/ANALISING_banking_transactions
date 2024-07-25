import datetime

import pandas as pd

from src.reports import spent_by_category
from src.services import investment_bank
from src.utils import reading_excel
from src.views import views_file

if __name__ == "__main__":
    date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    data = reading_excel("../data/operations.xlsx")
    print(views_file(date, data))
    transactions_list = reading_excel("../data/operations.xlsx")
    print(investment_bank("2022-05", transactions_list, 2))
    transactions_df = pd.DataFrame(transactions_list)
    print((spent_by_category(transactions_df, "Фастфуд", "2022-05-25")).head())
