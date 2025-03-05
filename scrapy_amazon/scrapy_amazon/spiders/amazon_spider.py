import json
from pathlib import Path

import scrapy


class EletrosSpider(scrapy.Spider):
    name = "eletros"

    def __init__(self):
        super().__init__()
        self.all_items = []

    def start_requests(self):
        urls = [
            "https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&promotion_type=lightning#deal_print_id=4c516e10-f9d5-11ef-b872-5747ac35524b&c_id=carousel&c_element_order=4&c_campaign=BOLOTA_MAIS-VENDIDOS&c_uid=4c516e10-f9d5-11ef-b872-5747ac35524b",
            "https://www.mercadolivre.com.br/ofertas?category=MLB1182&container_id=MLB779362-1#filter_applied=category&filter_position=3&origin=qcat",
        ]

        for url in urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                method="GET",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                },
            )

    def export_json(self, items):
        with open("items.json", "w") as f:
            json.dump(items, f)

    def parse(self, response: scrapy.http.Response):
        grid = response.xpath('//div[@class="poly-card__content"]').getall()

        items = []

        for item in grid:
            item_parsed = scrapy.Selector(text=item)
            title = item_parsed.css("a.poly-component__title::text").get()
            current_price_div = item_parsed.css("div.poly-price__current")

            amount = current_price_div.css(
                "span.andes-money-amount__fraction::text"
            ).get()

            cents = (
                current_price_div.css("span.andes-money-amount__cents::text").get()
                or "00"
            )
            price = f"{amount}.{cents}"

            items.append({"title": title, "price": price})

        self.all_items.extend(items)
        self.export_json(self.all_items)
        return items
