from selectorlib import Extractor
import requests
class temp:
    #to represent temp value from timeanddata.com/weather page
    ''' headers = {

        "pragma": "no-cache",

        'cache-control': "no-cache",

    'upgrade - insecure - requests' : '1',

    'user-agent' : 'Mozilla/5.0 (X11; Cros x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+exml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

   'accept - Language': "en-GB, en-US;q=0.9,en;q=0.8",
    }'''
    base_url = 'http://www.timeanddate.com/weather/'
    yaml_path = 'temp.yaml'

    def __init__(self,country,city):
        self.country=country.replace(" ","-")
        self.city=city.replace(" ","-")

    def _build_url(self):
        url = self.base_url + self.country + "/" + self.city
        return url
    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yaml_path) #extractor is object
        r = requests.get(url)
        content = r.text
        raw = extractor.extract(content)
        return raw


    def get(self):
        scraped = self._scrape()
        res = float(scraped['tem'].replace("°C",""))
        return res


if __name__=="__main__":
    country = input("country: ")
    city = input("city: ")
    temperature = temp(country,city).get()
    print(temperature)


