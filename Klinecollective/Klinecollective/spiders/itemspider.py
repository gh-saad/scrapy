import scrapy
import json
import csv
from slugify import slugify

class ItemspiderSpider(scrapy.Spider):
    name = "itemspider"
    allowed_domains = ["klinecollective.com"]
    start_urls = ["https://klinecollective.com/product/reality/"]


    def parse(self, response):
        fixedData = {
            "Title": response.xpath("//h1/text()").get(),
            "Body": response.xpath("//div[@class='woocommerce-product-details__short-description']").get()
        }
        images = []
        tags = []

        for loop in range(1,50):
            image = response.xpath("//figure/div/div["+str(loop)+"]/a/@href").get()
            if image:
                images.append(image)
            else:
                break

        for loop in range(1,500):
            tag = response.xpath("//span[3]/span[2]/a["+str(loop)+"]/text()").get()
            if tag:
                tags.append(tag)
            else:
                break

        variations = response.xpath("//form[@class='variations_form cart']/@data-product_variations").get()
        variations = json.loads(variations)
        # print(len(variations)) # 30
        
        i = 0
        optionNames = []
        optionValues = []

        for i in range(len(variations)):
            keys = variations[i]['attributes']
            optionName = []
            optionValue = []
            for key in keys:
                tmpKey = key
                tmpKey = tmpKey.split("attribute_pa_")
                varName = tmpKey[1]
                varVal = str(variations[i]['attributes'][key])
                # print(varName)
                # print(varVal)
                if varName not in optionName:
                    optionName.append(varName)
                optionValue.append(varVal)
            if optionName not in optionNames:
                optionNames.append(optionName)
            optionValues.append(optionValue)
            i += 1

        data = {}
        for col in range(len(optionNames[0])-1):
            # print(optionNames[0][col])
            csvLine = 1
            if len(images) > len(optionValues):
                length = len(images)
            else:
                length = len(optionValues)

            for row in range(length):
                # print(optionValues[row][col])
                data["handle"] = slugify(fixedData["Title"])
                if csvLine == 1:
                    data["URL"] = response.request.url
                    data["title"] = fixedData["Title"]
                    data["desc"] = fixedData["Body"]
                    data["Option_1_Name"] = optionNames[0][col]
                    data["Option_1_Value"] = optionValues[row][col]
                    data["Option_2_Name"] = optionNames[0][col+1]
                    data["Option_2_Value"] = optionValues[row][col+1]
                    data["Tags"] = ",".join(tags)
                    data["sku"] = response.xpath("//div/div/span[1]/span[2]/text()").get().strip()
                    data["salePrice"] = variations[csvLine-1]['display_price']
                    data["price"] = variations[csvLine-1]['display_regular_price']
                    if csvLine-1 < len(images):
                        data["img"]= images[csvLine-1]
                        data["position"]= csvLine
                    else:
                        data["img"] = ""
                        data["position"]= ""    
                else:
                    data["URL"] = "" 
                    data["title"] = ""
                    data["desc"] = ""
                    data["Option_1_Name"] = ""
                    if row < len(optionValues) and col < len(optionNames[0]):
                        data["Option_1_Value"] = optionValues[row][col]
                    else:
                        data["Option_1_Value"] = ""
                    data["Option_2_Name"] = ""
                    if row < len(optionValues) and col+1 < len(optionNames[0]):
                        data["Option_2_Value"] = optionValues[row][col+1]
                    else:
                        data["Option_2_Value"] = ""
                    data["Tags"] = ""
                    data["sku"] = ""
                    if csvLine-1 < len(variations):
                        data["salePrice"] = variations[csvLine-1]['display_price']
                        data["price"] = variations[csvLine-1]['display_regular_price']
                    else:
                        data["salePrice"] = ""
                        data["price"] = ""
                    if csvLine-1 < len(images):
                        data["img"]= images[csvLine-1]
                        data["position"]= csvLine
                    else:
                        data["img"] = ""
                        data["position"]= ""
                csvLine +=1
                yield data

        with open('download/links.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for line in reader:
                yield response.follow(line[0], callback=self.parse)
    
