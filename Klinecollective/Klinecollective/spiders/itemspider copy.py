import scrapy
import json
import csv
from slugify import slugify

class ItemspiderSpider(scrapy.Spider):
    name = "c_itemspider"
    allowed_domains = ["klinecollective.com"]
    start_urls = ["https://klinecollective.com/product/reality/"]


    def parse(self, response):
        data = {}
        title = response.xpath("//h1/text()").get()

        variations = response.xpath("//form[@class='variations_form cart']/@data-product_variations").get()
        variations = json.loads(variations)
        
        i = 0
        tmp = 1
        for i in range(len(variations)-1):
            option1Name = ""
            option1Value = []
            option2Name = []
            option2Value = []
            option3Name = []
            option3Value = []
            option4Name = []
            option4Value = []

            keys = variations[i]['attributes']
            for key in keys:
                tmpKey = key
                tmpKey = tmpKey.split("attribute_pa_")
                varName = tmpKey[1]
                varVal = str(variations[i]['attributes'][key])
                text = list(variations[i]['attributes'])
                
                if(len(text) > 0 and text[0] == variations[i]['attributes'][key]):
                    option1Name = varName
                    option1Value.insert(varVal)
                if(len(text) > 1 and text[1] == variations[i]['attributes'][key]):
                    option2Name = varName
                    option2Value.insert(varVal)
                if(len(text) > 2 and text[2] == variations[i]['attributes'][key]):
                    option3Name = varName
                    option3Value.insert(varVal)
                if(len(text) > 3 and text[3] == variations[i]['attributes'][key]):
                    option4Name = varName
                    option4Value.insert(varVal)
            print(option1Name)
            data["handle"] = slugify(title)
            data["title"] = title
            data["desc"] = response.xpath("//div[@class='woocommerce-product-details__short-description']").get()
            data["Option1Name"] =  option1Name
            data["Option2Name"] =  option2Name     
            data["Option3Name"] =  option3Name     
            data["Option4Name"] =  option4Name     
            data["salePrice"] = variations[i]['display_price']
            data["price"] = variations[i]['display_regular_price']
            data["sku"] = variations[i]['sku']
            data["img"]= variations[i]['image']['url']

            i += 1
        yield data

    
