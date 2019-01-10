"""formspider.py

This is a spider and in a scrapy project it would be saved in the 
`<ProjectName>/spiders` subdirectory of the project.

Execute the crawl by running scrapy with the crawl option and passing the
spider's name:
```
(venv) $ pwd
/Users/MyUser/MyProject
(venv) $ scrapy crawl horseForm
```
"""
from scrapy.http import FormRequest
from scrapy.spiders import Spider


class FormSpider(Spider):
    
    name = 'horseForm'
    start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

    # Helper Methods
    # ==============
    # These helper methods really belong in their own helper class/module
    # We'll figure out a sensible location later.
    def generate_page_outline(self, selector_objects):
        outline = ""
        hs = [selector_objects.css(f'{x}::text') 
                for x in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']]
        for i, level in enumerate(hs):
            for h in level:
                leading_spaces = " " * i
                outline += f'{leading_spaces}{h.extract()}\n'
        return outline

    def print_request_details(self, request):
        url = request.url
        headers = request.headers.to_unicode_dict()

        print(url)
        print("---- Headers ----")
        for key, value in headers.items():
            print(f'{key}: {value}')

        print("---- Body ----")
        # request doesn't seem to have an equivalent to response's `text`
        # method. So we're stuck with printing a bytestring here.
        print(request.body)

    def print_response_details(self, response):
        url_string = response.url

        # Note that it is possible to use the better but slower Beautiful
        # Soup library instead of scrapy's builtin decoder.
        # See:
        # https://doc.scrapy.org/en/latest/faq.html#can-i-use-scrapy-with-beautifulsoup

        # .headers is a Headers object, which is essentially a dict
        # of bytestrings. We could iterate through the ks and vs of headers
        # which would give us a bunch of bytestrings or use the provided
        # .to_unicode_dict() method which converts all the bytestrings to
        # regular unicode strings
        response_headers = response.headers.to_unicode_dict()

        # response.body is a bytestring. In this case we know we are using
        # a text-based response (a webpage) so we want to decode the bytestring
        # to unicode. `response` has a built-in .text method to decode to
        # unicode text
        response_text = response.text
        
        page_head = response.css('head')
        page_body = response.css('body')
        page_title = page_head.css('title::text').extract_first()
        page_body_text = page_body.extract_first()
        
        page_outline = self.generate_page_outline(page_body)


        print('---- http response ---')
        print(f'url: {url_string}')
        print('headers:')
        for key, value in response_headers.items():
            print(f'{key}: {value}')
        print('response body (showing first 500 characters):')
        print(response_text[:500])
        print('---- END http response ----')
        
        print("---- decoded HTML ----")
        print(f'Page Title: {page_title}')

        print("Page Outline:")
        print(page_outline)

        print('page body (showing first 500 characters):')
        print(page_body_text[:500])
        print("---- END decoded HTML")

    # Spider Methods
    # ==============
    def parse(self, response):
        # this is a zero-based index of the form on the page
        formnumber = 0

        # You can use the browser's development tools to look at the form
        # and get the field names ('name' attribute)
        formdata = {
            'firstname': 'alice',
            'lastname': 'robertson',
            'jobtitle': 'superspy'
        }

        print("==== PARSE ====")
        print("---- Initial response ----")
        print("This is the response (`HtmlResponse` object) from the initial GET request")
        self.print_response_details(response)
        
        print("---- Generate form request ----")
        print("Creating a form request from the response and the following form data:")
        print(formdata)
        print("==== END PARSE ====\n")


        # create a FormRequest object from the initial response (GET on the 
        # page with the form)
        # The FormSpider will perform this request when it is returned from 
        # this method
        # This chained request will itself call a callback (in this case
        # `after_post`) when a response is received.
        form_request = FormRequest.from_response(
            response, 
            formnumber=formnumber, 
            formdata=formdata,
            callback=self.after_post
        )

        print("==== PARSE (CONT'D) ====")
        print("Created form request object:")
        self.print_request_details(form_request)
        print("Now returning the form_request (to be performed)")
        print("==== END PARSE (CONT'D) ====\n")

        return form_request

    def after_post(self, response):
        # This is a callback function that will be called by the form request
        # (created in the parse callback). I.e., it will be called after the
        # form has been submitted
        print("==== AFTER_POST ====")
        self.print_response_details(response)
        print("==== END AFTER_POST ====\n")
