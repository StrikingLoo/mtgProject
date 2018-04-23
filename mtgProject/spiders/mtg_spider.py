import scrapy 

class mtg_spider(scrapy.Spider):
    name="mtg"
    def start_requests(self):
        urls = ['http://mtgtop8.com/format?f=MO&meta=163']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    items = []
    def parse(self, response):
        
        xpath_s = '/html/body/div[3]/div/table'
        item = response.xpath(xpath_s)
        cont = str(item.extract())
        cont = cont.split('archetype?a=')
        archetypes = [arch[:3] for arch in cont[1:]]
        print(archetypes)
        with open('linklist.txt','w') as f:
            contents = '\n'.join(['http://mtgtop8.com/archetype?a='+a+'&meta=163&f=MO' for a in archetypes])
            f.write(contents)
