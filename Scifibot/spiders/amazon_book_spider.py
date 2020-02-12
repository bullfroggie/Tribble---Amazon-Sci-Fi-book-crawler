# -*- coding: utf-8 -*-
import scrapy


class AmazonBookSpider(scrapy.Spider):
    name = "amazon_spider"

    pages = 2

    start_urls = [
        "https://www.amazon.com/s?rh=n%3A16272%2Cp_72%3A4-&pf_rd_i=16272&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3237dbf3-c1bb-5c72-8ce7-e082992624f7&pf_rd_r=P45DS9NK334QDQCFXPHG&pf_rd_s=merchandised-search-10&pf_rd_t=101&ref=Oct_TopRatedC_16272_SAll",
    ]

    def parse(self, response):
        books = response.css(".s-include-content-margin")

        for book in books:
            yield {
                "title": book.css(".a-color-base.a-text-normal::text").extract_first(),
                "author": book.css(".a-color-secondary .a-size-base:nth-child(2)")
                .css("::text")
                .extract_first()
                .strip(),
                "image": book.css("img.s-image::attr(src)").extract_first(),
                "price": float(
                    f"{book.css('.sg-col-inner .sg-row .a-spacing-top-small .a-price span span').css('::text').extract()[1]}.{book.css('.sg-col-inner .sg-row .a-spacing-top-small .a-price span span').css('::text').extract()[4]}"
                ),
                "url": f"https://www.amazon.com/{book.css('a.a-link-normal::attr(href)').extract_first()}",
            }

        next_page = f"https://www.amazon.com/s?i=stripbooks&bbn=16272&rh=n%3A16272%2Cp_72%3A1250221011%2Cp_n_feature_browse-bin%3A2656022011&dc&page={AmazonBookSpider.pages}&pf_rd_i=16272&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=3237dbf3-c1bb-5c72-8ce7-e082992624f7&pf_rd_r=P45DS9NK334QDQCFXPHG&pf_rd_s=merchandised-search-10&pf_rd_t=101&qid=1581470763&rnid=618072011&"

        if AmazonBookSpider.pages <= 70:
            AmazonBookSpider.pages += 1
            yield response.follow(next_page, callback=self.parse)
