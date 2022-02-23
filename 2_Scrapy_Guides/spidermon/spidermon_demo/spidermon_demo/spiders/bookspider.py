import scrapy
from spidermon_demo.items import BookItem

class BookSpider(scrapy.Spider):
	name = 'bookspider'
	start_urls = ["http://books.toscrape.com"]

	def parse(self, response):

		for article in response.css('article.product_pod'):
			book_item = BookItem(
				url = article.css("h3 > a::attr(href)").get(),
				title = article.css("h3 > a::attr(title)").extract_first(),
				price = article.css(".price_color::text").extract_first(),
			)
			yield book_item

		next_page_url = response.css("li.next > a::attr(href)").get()
		if next_page_url:
			yield response.follow(url=next_page_url, callback=self.parse)