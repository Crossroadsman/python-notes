"""horse.py

This is a spider and in a scrapy project it would be saved in the 
`<ProjectName>/spiders` subdirectory of the project.

Execute the crawl by running scrapy with the crawl option and passing the
spider's name:
```
(venv) $ pwd
/Users/MyUser/MyProject
(venv) $ scrapy crawl ike
```
"""
import scrapy


class HorseSpider(scrapy.Spider):
    
    # spider names must be unique within the project
    name = 'ike'

    # these are the first URLs to crawl
    start_urls = [
            'https://treehouse-projects.github.io/horse-land/index.html',
            'https://treehouse-projects.github.io/horse-land/mustang.html'
    ]

    # a scrapy spider class implements two methods:
    # `start_requests`,
    # `parse`
    def start_requests(self):
        """generates the initial requests to crawl the specified URLs and
        specifies the callback to be called when the response comes back
        from the requests

        It returns an iterable containing the initial Request objects
        for the crawler.
        """
        requests = [scrapy.Request(url=url, callback=self.parse)
                    for url in self.start_urls]

        return requests

    def parse(self, response):
        """This is the callback method for the requests. It describes how
        the response should be parsed, and what kind of objects should
        be returned.

        The return objects comprise scraped data and additional URLs to follow.

        Valid return types are iterable of Request and/or dicts or Item objects.
        """
        url = response.url
        page_name = url.split('/')[-1]
        filename = f'horses-{page_name}'
        print(f'URL: {url}')
        with open(filename, 'wb') as file:
            file.write(response.body)
        print(f'Saved file as: {filename}')
