# Stepik selenium python course (Final Project)
Итоговый проект курса [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/)

Тестовый сайт: http://selenium1py.pythonanywhere.com

Реализованы следующие проверки (с использованием Page Object Model):
- добавление товара в корзину гостем
- переход на страницу логина/регистрации
- добавление товара в корзину зарегистрированным пользователем
- проверка корзины

Тестовое окружение:
- Windows 10
- Python 3.10.5
- Selenium 4.2.0
- PyTest 7.1.2
- браузер Chrome 103.0.5060.114
- браузер Firefox 102.0.1
- chromedriver 102.0.5005.61
- geckodriver 0.31.0

Для установки необходимых пакетов из файла requirements.txt используйте команду: 
```
pip install -r \path\to\requirements.txt
```
Тесты можно запускать в браузерах Chrome (по умолчанию) и Firefox с помощью дополнительного параметра `--browser_name`:
```
pytest --browser_name=chrome
pytest --browser_name=firefox
```
Также, тесты можно запускать для разных языков интерфейса (по умолчанию - en) с помощью дополнительного параметра `--language`:
```
pytest --language=fr
```
доступные языки: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans

Для запуска тестов с маркером @pytest.mark.need_review используйте команду:
```
pytest -v --tb=line --language=en -m need_review
```