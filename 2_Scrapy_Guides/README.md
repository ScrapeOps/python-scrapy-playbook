# Scrapy Extensions


https://github.com/orgs/scrapy-plugins/repositories?type=all
https://github.com/croqaz/awesome-scrapy
https://github.com/AccordBox/awesome-scrapy
https://github.com/facert/awesome-spider
https://reposhub.com/python/web-crawling/BruceDone-awesome-crawler.html


---

https://github.com/holgerd77/django-dynamic-scraper


## Parsers

### Price Parser
https://github.com/scrapinghub/price-parser/

### Date Parser
[dateparser](https://github.com/scrapinghub/dateparser) is a great little library that allows you to easily parse human readable dates into Python datatimes. 

    >>> import dateparser

    >>> dateparser.parse('Fri, 12 Dec 2014 10:55:50')
    datetime.datetime(2014, 12, 12, 10, 55, 50)

    >>> dateparser.parse('1991-05-17')
    datetime.datetime(1991, 5, 17, 0, 0)

    >>> dateparser.parse('In two months')  # today is 1st Aug 2020
    datetime.datetime(2020, 10, 1, 11, 12, 27, 764201)

    >>> dateparser.parse('1484823450')  # timestamp
    datetime.datetime(2017, 1, 19, 10, 57, 30)

It supports almost every existing date format: absolute dates, relative dates (`"two weeks ago"` or `"tomorrow"`), timestamps, etc. from over 200 different languages.

### Number-Parser
[Number-Parser](https://github.com/scrapinghub/number-parser) is a simple library that converts numbers written in natural language into its numeric form. Examples:

    ## Parse Numbers in Place
    >>> from number_parser import parse
    >>> parse("I have two hats and thirty seven coats")
    'I have 2 hats and 37 coats'

    ## Parse Number
    from number_parser import parse_number
    >>> parse_number("two thousand and twenty")
    2020

    ## Parse Fraction
    >>> from number_parser import parse_fraction
    >>> parse_fraction("forty two divided by five hundred and six")
    '42/506'

It currently supports cardinal numbers in the following languages - English, Hindi, Spanish and Russian and ordinal numbers in English.


## Login


## Crawling Aids


### Autopager
[Autopager](https://github.com/TeamHG-Memex/autopager)


### Scrapy-Crawl-Once
[Scrapy-Crawl-Once](https://github.com/TeamHG-Memex/scrapy-crawl-once) is a Spider/Downloader middleware for Scrapy that ensures that your scrapers only ever crawl the content once. Everytime a page is crawled the Scrapy-Crawl-Once middleware stores a fingerprint of the request in a DB, then when a spider schedules a new request the Scrapy-Crawl-Once middleware checks if the fingerprint is in the DB and drops the request if it is.

This ensures that your scrapers won't scrape the same pages twice, even over numerous crawls. 

### Scrapy DeltaFetch
[Scrapy DeltaFetch](https://github.com/scrapy-plugins/scrapy-deltafetch), like [Scrapy-Crawl-Once](https://github.com/TeamHG-Memex/scrapy-crawl-once) is a Spider middleware that ensures your scrapers don't scrape pages it has already seen on previous crawls from the same spider. Creating a "delta crawl" which only crawls new content added to the website.

The difference between [Scrapy-Crawl-Once](https://github.com/TeamHG-Memex/scrapy-crawl-once) and [Scrapy DeltaFetch](https://github.com/scrapy-plugins/scrapy-deltafetch) is the fact that [Scrapy DeltaFetch](https://github.com/scrapy-plugins/scrapy-deltafetch) chooses whether to discard a request based on yielded items, whereas [Scrapy-Crawl-Once](https://github.com/TeamHG-Memex/scrapy-crawl-once) only discards requests where the `request.meta['crawl_once']` flag has been set.

---

## Headless Browsers

### Scrapy Selenium
[Scrapy Selenium](https://github.com/clemfromspace/scrapy-selenium)

### Better Scrapy Selenium Middleware
[Better Scrapy Selenium Middleware](https://github.com/dylanwalker/better-scrapy-selenium) is a fork of above.

### Playwright

### Puppeteer

### Splash


## Deployment

## Scrapy-Heroku
[scrapy-heroku](https://github.com/dmclain/scrapy-heroku)