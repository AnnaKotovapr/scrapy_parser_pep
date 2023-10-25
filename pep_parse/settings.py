BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
VALUE = 300

PEP_REGEXP = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'
NAME = 'pep'
ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']
ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}


ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': VALUE,
}
