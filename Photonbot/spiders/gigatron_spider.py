import scrapy


class GigatronSpider(scrapy.Spider):
    name = "gigatron"

    def start_requests(self):
        urls = ["https://www.gigatron.rs/"]

        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
