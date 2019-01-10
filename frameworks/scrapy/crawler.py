"""crawler.py

This is a spider and in a scrapy project it would be saved in the 
`<ProjectName>/spiders` subdirectory of the project.

Execute the crawl by running scrapy with the crawl option and passing the
spider's name:
```
(venv) $ pwd
/Users/MyUser/MyProject
(venv) $ scrapy crawl whirlaway
```
"""
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HorseSpider(CrawlSpider):
    """CrawlSpider is a generic Spider subclass used for common crawling
    tasks.

    https://doc.scrapy.org/en/latest/topics/spiders.html#crawlspider
    """
    name = 'whirlaway'
    allowed_domains = ['treehouse-projects.github.io']
    start_urls = ['https://treehouse-projects.github.io/horse-land']

    # A LinkExtractor defines how links should be extracted from web pages 
    # (strictly, `scrapy.http.response` objects), using a regex pattern.
    # It returns a list of links (strictly, `scrapy.link.link` objects)
    link_pattern = r'.*'
    link_extractor = LinkExtractor(allow=link_pattern)
    
    # A Rule takes a LinkExtractor and a callback parsing function. The callback
    # will be called for every link exctracted by the LinkExtractor
    horse_rule = Rule(link_extractor, callback='parse_horses', follow=True)

    rules = [horse_rule]

    def parse_horses(self, response):
        """Parsers will be used as callbacks. They take a response object and
        return a list containing Item and/or Request objects.
        """
        url = response.url

        # The `css` method lets us use CSS selectors to select page elements
        # It returns a list of SelectorObjects (these make it easier to
        # progressively refine selectors). You can call extract() on a 
        # Selector or extract_first on a list of Selectors
        # Use pseudo selectors to get the text or attributes of an HTML
        # element instead of the HTML itself.
        # See:
        # https://doc.scrapy.org/en/latest/topics/selectors.html#id1
        title = response.css('title::text').extract_first()
        print("==== CRAWLING URL ====")
        print(f'{title} ({url})')
        print("==== END URL ====")
