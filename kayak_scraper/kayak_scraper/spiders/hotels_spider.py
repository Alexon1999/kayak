from urllib.parse import quote, parse_qs, urlparse
import scrapy
import logging

top_cities = [
    "Mont Saint Michel",
    "St Malo",
    "Bayeux",
    "Le Havre",
    "Rouen",
    "Paris",
    "Amiens",
    "Lille",
    "Strasbourg",
    "Chateau du Haut Koenigsbourg",
    "Colmar",
    "Eguisheim",
    "Besancon",
    "Dijon",
    "Annecy",
    "Grenoble",
    "Lyon",
    "Gorges du Verdon",
    "Bormes les Mimosas",
    "Cassis",
    "Marseille",
    "Aix en Provence",
    "Avignon",
    "Uzes",
    "Nimes",
    "Aigues Mortes",
    "Saintes Maries de la mer",
    "Collioure",
    "Carcassonne",
    "Ariege",
    "Toulouse",
    "Montauban",
    "Biarritz",
    "Bayonne",
    "La Rochelle"
]


def check_exists_by_xpath(response, xpath):
    return len(response.xpath(xpath)) > 0


BASE_URL = 'https://www.booking.com/searchresults.html'


class HotelsSpiderSpider(scrapy.Spider):
    name = 'hotels_spider'
    allowed_domains = ['www.booking.com']
    start_urls = [BASE_URL + '?ss=' + quote(city) for city in top_cities]

    def parse(self, response, page_no=1):
        hotels = response.xpath(
            '//*[@id="search_results_table"]/div[2]/div/div/div/div[3]/div[@data-testid="property-card"]')

        parsed_url = urlparse(response.url)
        city = parse_qs(parsed_url.query)['ss'][0]

        for hotel in hotels:
            link = ''
            name = ''
            score = 0

            if check_exists_by_xpath(hotel, 'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a'):
                link = hotel.xpath(
                    'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a').attrib['href']
            if check_exists_by_xpath(hotel, 'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]'):
                name = hotel.xpath(
                    'div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a/div[1]/text()').get()
            if check_exists_by_xpath(hotel, 'div[1]/div[2]/div/div[1]/div[2]/div/a/span/div/div[1]'):
                score = float(hotel.xpath(
                    'div[1]/div[2]/div/div[1]/div[2]/div/a/span/div/div[1]/text()').get() or 0)
            hotel = {
                'name': name,
                'link': link,
                'score': score,
                'city': city,
            }
            try:
                hotel_detailed = response.follow(
                    link, callback=self.more_details, cb_kwargs={'hotel': hotel})
                yield hotel_detailed
            except:
                yield hotel

        # Check if it has the next page
        if check_exists_by_xpath(response, '//*[@id="search_results_table"]/div[2]/div/div/div/div[4]/div[2]/nav/div/div[3]/button[not(@disabled)]'):
            # Go to Next Page
            next_page = BASE_URL + '?ss=' + \
                quote(city) + '&offset=' + quote(str(25 * page_no))
            yield response.follow(next_page, callback=self.parse, cb_kwargs={'page_no': page_no+1})

    def more_details(self, response, hotel):
        lat, lng = response.xpath(
            '//*[@id="hotel_sidebar_static_map"]').attrib['data-atlas-latlng'].split(',')
        hotel['latitude'] = float(lat)
        hotel['longitude'] = float(lng)
        descriptions = response.xpath(
            '//*[@id="property_description_content"]/p/text()')[1:]
        all_description = ' '.join([desc.get() for desc in descriptions])
        hotel['description'] = all_description
        yield hotel
