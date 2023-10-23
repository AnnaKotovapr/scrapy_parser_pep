# Проект асинхронный парсер PEP

## Автор
- Анна Котова
- E-mail: kotova.a.a.97@mail.ru
- Telegram: @annkotttt

##  Описание
Скрапер собирает данные обо всех PEP документах и формирует результат двух типов:
- pep_{datetime}.csv - список всех PEP (номер, название и статус)
- status_summary_{datetime}.csv - сколько найдено документов в каждом статусе (статус, количество)


## Технологии проекта
Scrapy — популярный фреймворк для парсинга веб сайтов


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:AnnaKotovapr/scrapy_parser_pep.git
cd scrapy_parser_pep
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

## Примеры команд
scrapy crawl pep - запуск парсера
