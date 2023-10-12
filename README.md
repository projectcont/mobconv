# mobconv
Python приложение, показывающее курсы валют USD EUR за сегодня, вчера и позавчера

Python приложение по ссылке http://127.0.0.1:8000/
работает на Linux (Ununtu), c БД sqlite

По url  "http://95.183.13.132:5000/korp/update/" 
-сайт получает API на сегодня c  ресурcа https://www.cbr-xml-daily.ru/latest.js, 
- берет из него только нужные данные (курсы EUR, USD)
- сохраняет в БД 

Для периодического выполнение этой операции используется пакет django-apscheduler
# https://github.com/devchandansh/django-apscheduler/blob/master/example_project/example_project/urls.py
Его файлы расположены в каталоге excelsite/cron/
Так как функция (запрос внешнего API) выполняется один раз в сутки, 
и этот запрос короткий, то можно обойтись без CELERY

По кнопкам "КУРС НА СЕГОДНЯ"   "КУРС НА ВЧЕРА"  "КУРС НА ПОЗАВЧЕРА"
скрипт берет  из  БД строки (данные) за сегодня, вчера и позавчера и выводит в шаблон 

Логика расположена в каталоге excelsite/proc/

Разработка: Бограчев К.М., Django Framework
