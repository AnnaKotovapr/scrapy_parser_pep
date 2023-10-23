# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pep_parse (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


FEEDS = {
    # Имя файла для сохранения данных теперь указываем здесь,
    # а не при вызове паука из консоли.
    'results/pep_%(time)s.csv': {
        # Формат файла.
        'format': 'csv',
        # Поля, данные из которых будут выведены в файл, и их порядок.
        # Выведем в этот файл только два поля из трёх.
        'fields': ['number', 'name', 'status'],
        # Если файл с заданным именем уже существует, то
        # при значении False данные будут дописываться в существующий файл;
        # при значении True существующий файл будет перезаписан.
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
