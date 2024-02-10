import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://www.copart.com/lot/79942243",
    ]

    def parse(self, response):
        for quote in response.css("form.prelimBidForm"):
            yield {
                "bid-price": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
