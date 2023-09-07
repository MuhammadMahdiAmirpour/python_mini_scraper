import scrapy

class SiteSpider(scrapy.Spider):
    name = "site_scraper"
    start_urls = [
            "https://www.scrapethissite.com/pages/simple/"
            ]

#     def start_requests(self):
#         return [
#                 scrapy.Request(url = "https://www.scrapethissite.com", callback = self.parse)
#                 ]

    def parse(self, response, **kwargs):
        country_names = [country_name for country_name in [str.strip(country_name) for country_name in response.css("h3.country-name::text").getall()] if country_name != '']
        country_capitals = response.css("div.country-info span.country-capital::text").getall()
        country_populations = response.css("div.country-info span.country-population::text").getall()
        country_areas = response.css("div.country-info span.country-area::text").getall()
        countries =  [
                {
                    "name": name,
                    "capital": capital,
                    "population": population,
                    "area": area,
                    }
                for name, capital, population, area in zip(country_names, country_capitals, country_populations, country_areas)
                ]
        for country in countries:
            yield {
                    "name": country["name"],
                    "capital": country["capital"],
                    "population": country["population"],
                    "area": country["area"]
                    }

