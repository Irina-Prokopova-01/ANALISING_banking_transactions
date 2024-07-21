# Новый виджет для банковских операций.

## Описание и использование:

В проекте разработана новая фича для личного кабинета клиента банка.
Это виджет для удобства визуализации и сохранности данных пользователя, который показывает 
несколько банковских операций клиента с картами и счетами, таких как обработка транзакций, 
маскировка данных и логирование операций.
Точкой запуска программы является модуль main.py - запустите его и отвечайте на вопросы программы.

## Структура проекта

├── src
│ ├── __init__.py
│ ├── utils.py
│ ├── main.py
│ ├── views.py
│ ├── reports.py
│ └── services.py
├── data
│ ├── operations.xlsx
├── tests
│ ├── __init__.py
│ ├── test_utils.py
│ ├── test_views.py
│ ├── test_reports.py
│ └── test_services.py
├── user_settings.json
├── .venv/
├── .env
├── .env_template
├── .git/
├── .idea/
├── .flake8
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md


* src/utils.py модуль с вспомогательными функциями для модуля views.py, 
реализующими приветствие, сортировку транзакций по сумме платежа, cashback, widget номера карты, запросы к 
внешним API
* src/main.py модуль отвечающий за кодировку счета/карты 
* src/views.py модуль отвечающий за основные функции для генерации JSON-ответов.
* src/reports.py модуль отвечающий за фильтрацию словарей по дате/ключу
* src/services.py модуль для генерации различных данных, используемых в виджете.

## Модуль utils:

Функция, которая принимает на вход путь до файла и возвращает список словарей с данными 
о финансовых транзакциях. Поддерживаемые расширения файлов:  
* .xlsx.

## Установка:

* для создания виртуального окружения и установки зависимостей используйте Poetry

* ссылка для добавления проекта https://github.com/Irina-Prokopova-01/ANALISING_banking_transactions

* модуль utils.py использует сервис https://apilayer.com и https://www.alphavantage.

* создайте .env из .env.template и добавьте токен API в .env как описано в шаблоне.
* 
    
## Установите зависимости:


Для создания виртуального окружения и установки зависимостей используйте Poetry

Модуль utils.py использует сервис https://apilayer.com и https://www.alphavantage. Создайте 
.env из .env.example и добавьте токен API в .env как описано в шаблоне.

## Получение API ключа для конвертации валют и получения цен на акции S&P500

Exchange Rates Data API: https://apilayer.com/exchangerates_data-api
API S&P500: https://www.alphavantage.co/query

## Примеры использования кода:

```def investment_bank(
    month: str, transactions: List[Dict[str, Any]], limit: int
) -> float:
    investment_result = 0
    sorted_transactions_by_month = date_sorting(month, transactions)
    for transaction in sorted_transactions_by_month:
        rounded_payment = limit_payment(limit, transaction["Сумма операции"])
        investment_result += abs(rounded_payment) - abs(transaction["Сумма операции"])
    result = round(float(investment_result), 2)
    result_json = json.dumps(result, ensure_ascii=False)
    # print(data_from_excel)
    return result_json
```

## Тестирование

* запуск тестов c pytest
* запуск тестов с покрытием pytest --cov

## Логирование

В проект добавлены логгеры. 
Логи записываются в папку 'logs' в файлы services.log, reports.log, views.log, utils.log соответственно. 
Логи включают метку времени, название модуля, уровень серьезности и сообщение,
описывающее событие или ошибку, которые произошли.

## Документация

## Лицензия

## Конфиденциальные данные
Конфиденциальные данные должны находиться в файле .env. Пример данных для работы хранятся в файле .env_template
