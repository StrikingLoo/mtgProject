import scrapy 

class mtg_spider(scrapy.Spider):
    name="mtg3"
    def start_requests(self):
        
        with open('mtgProject/decks.txt','r') as links:
            urls = links.read().split('\n')[:self.n]
            urls = ['http://mtgtop8.com/'+deck for deck in urls]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    n = 777
    count = 0
    def parse(self, response):
        
	    # xpath of deck:
        #/html/body/div[3]/div/table/tbody/tr/td[2]/table[2]/tbody/tr/td/table/tbody/tr
        deck_xpath = '/html/body/div[3]/div/table/tr/td[2]/table[2]/tr/td/table/tr'
        xpath_s =deck_xpath
        item = response.xpath(xpath_s)
        cont = str(item.extract())[3:-2]
        print(cont)
        self.count+= 1

        with open('./decks/deck_table'+str(self.count)+'.html','w') as f:
            f.write(cont)
          
        
