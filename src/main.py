import datetime

import pandas as pd

from src.reports import spent_by_category
from src.services import investment_bank
from src.utils import reading_excel
from src.views import views_file

if __name__ == "__main__":
    date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    print(views_file(date, transactions_df))
    print("\n###################\n")
    transactions_list = reading_excel("../data/operations.xlsx")
    print(investment_bank("2021-10", transactions_list.to_dict(orient="records"), 2))
    print("\n###################\n")
    transactions_df = pd.DataFrame(transactions_list)
    print((spent_by_category(transactions_df, "Фастфуд", "2021-10-25")).head())
