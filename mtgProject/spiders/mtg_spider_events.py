import scrapy 

class mtg_spider(scrapy.Spider):
    name="mtg2"
    def start_requests(self):
        with open('mtgProject/linklist.txt','r') as links:
            urls = links.read().split('\n')[:-1] 
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    acum = ''
    count = 0
    def parse(self, response):
        
        xpath_s = '/html/body/div[3]/div/table'
        item = response.xpath(xpath_s)
        cont = str(item.extract())
        cont = '\n'.join(cont.split('  '))
        self.acum += cont
        self.count+= 1
        if self.count==(53):
            with open('events.txt','w') as f:
                f.write(self.acum)
          
        
