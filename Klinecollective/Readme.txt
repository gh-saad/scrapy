Url = https://klinecollective.com/shop/
Product Listing Page:
    Next Page Xpath:
        //nav/a[@class="next page-numbers"]/@href

    Products listing Xpath:
        //div[3]/ul[@class="products columns-3"]

    Products Card Xpath:
        //div[3]/ul/li[1]

    Product link Xpath:
        //div[3]/ul/li[1]/div/a/@href

Single Product Page:
    Product Title Xpath: Title
    //h1

    Product Short Desc Xpath: Body (HTML)
    //div[@class="woocommerce-product-details__short-description"]

    Product Variation Xpath:
    //form[@class="variations_form cart"]/@data-product_variations
    
    Product Images
    //*[@id="qodef-woo-page"]/div/div[1]/div/div/div/div/figure/div[2]/div[1]/a/@href 

    Product Tags:
    //span[3]/span[2]/a[1]/text()