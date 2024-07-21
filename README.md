# Приложение для банковских операций.

## Описание и использование:

В проекте разработана новая фича для личного кабинета клиента банка.
Разработано приложение для анализа транзакций, которые находятся в Excel-файле. 
Приложение будет генерировать JSON-данные для веб-страниц, формировать Excel-отчеты, 
а также предоставлять другие сервисы в прпоцессе дальнейшей разработки.

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
* src/main.py Модуль отвечающий за работу с пользователем
* src/views.py Модуль отвечающий за основные функции для генерации JSON-ответов.
* src/reports.py Модуль функции отчетов, записывающей результат в файл.
* src/services.py Модуль-сервис позволяет проанализировать, какие категории были наиболее выгодными 
для выбора в качестве категорий повышенного кешбэка. Реализация инвест-копилки.

## Папка data:

* В папке размещен файл о финансовых транзакциях. Поддерживаемое расширение файла: .xlsx.

## Установка:

* Для создания виртуального окружения и установки зависимостей используйте Poetry.

* Ссылка для добавления проекта https://github.com/Irina-Prokopova-01/ANALISING_banking_transactions.

* Модуль utils.py использует сервис https://apilayer.com и https://www.alphavantage.

* Создайте .env из .env.template и добавьте токен API в .env как описано в шаблоне.

    
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
