import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_REGEXP
from pep_parse import settings


class PepSpider(scrapy.Spider):
    name = settings.NAME
    allowed_domains = settings.ALLOWED_DOMAINS
    start_urls = settings.START_URLS

    def parse(self, response):
        peps = response.css('section#numerical-index td a::attr(href)')
        for pep_link in peps:
            pep_link = pep_link + '/'
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().replace('-', '')
        number, name = re.search(PEP_REGEXP, title).groups()
        status = (
            response.css('dt:contains("Status") + dd').css('abbr::text').get()
        )
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        # Передаём словарь с данными в конструктор класса item
        yield PepParseItem(data)
