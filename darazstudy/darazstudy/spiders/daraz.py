# -*- coding: utf-8 -*-

from darazstudy.common import *

BaseURL     = "https://www.daraz.pk"
TargetURLS  = [
    f"{BaseURL}/smartphones/",
    f"{BaseURL}/laptops/",
]

MHeaderz    = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
}

class DarazSpider(Spider):
    name = 'daraz'
    start_urls = [ x for x in TargetURLS ]
    custom_settings = {
        'ITEM_PIPELINES' : {
            'darazstudy.pipelines.DarazstudyExcelPipeline': 300
        },
        'SPIDER_MIDDLEWARES': {
            # 'darazstudy.middlewares.DarazstudySpiderMiddleware': 543
        },
        'DOWNLOADER_MIDDLEWARES' : {
            # 'darazstudy.middlewares.DarazstudyDownloaderMiddleware': 543
        },
        'FEED_EXPORT_ENCODING'              :   'utf-8',
        'LOG_ENABLED'                       :   True,
        'ROBOTSTXT_OBEY'                    :   False,
        'COOKIES_ENABLED'                   :   False,
        'TELNETCONSOLE_ENABLED'             :   False,
        'HTTPCACHE_ENABLED'                 :   True,
        'COMPRESSION_ENABLED'               :   True,
        'HTTPCACHE_GZIP'                    :   True,
        'HTTPCACHE_EXPIRATION_SECS'         :   0,
        'DOWNLOAD_TIMEOUT'                  :   30,
        'RETRY_TIMES'                       :   30,
        'DOWNLOAD_DELAY'                    :   0,
        'CONCURRENT_REQUESTS'               :   4,
        'CONCURRENT_REQUESTS_PER_DOMAIN'    :   2,
        'CONCURRENT_REQUESTS_PER_IP'        :   2,
        'ROTATING_PROXY_PAGE_RETRY_TIMES'   :   120,
        # 'HTTPCACHE_STORAGE'                 :   'scrapy.extensions.httpcache.DbmCacheStorage',
        'HTTPCACHE_STORAGE'                 :   'scrapy.extensions.httpcache.FilesystemCacheStorage',
        # 'HTTPCACHE_POLICY'                  :   'scrapy.extensions.httpcache.RFC2616Policy',
        'HTTPCACHE_POLICY'                  :   'scrapy.extensions.httpcache.DummyPolicy',
        'STATSMAILER_RCPTS'                 :   ['myupdates@mailinator.com'],
        'ROTATING_PROXY_LIST_PATH'          :   'proxylist.txt',
        'DOWNLOAD_HANDLERS'                 :   {'s3': None}
    }

    def parse(self, resp):
        script = resp.xpath("//script[contains(.,'window.pageData=')]/text()").get()
        if script != None:
            script = sub( r"window.pageData=", "", script)
            jdata = loads(script)
            if jdata:
                jdata = jdata['mods']['listItems']
                for p in jdata:
                # for p in jdata[:2]:
                    p_href = p.get('productUrl')
                    p_nid = p.get('nid')
                    p_price = p.get('price')
                    p_type = p.get('tItemType')
                    p_sku = p.get('sku')
                    p_sellerid = p.get('sellerId')
                    p_sellername = p.get('sellerName')
                    p_categories = p.get('categories')
                    p_rating = p.get('ratingScore')
                    p_reviews = p.get('review')
                    p_brandid = p.get('brandId')
                    p_brandname = p.get('brandName')

                    ## fixes
                    p_href = resp.urljoin(p_href)
                    if "?" in p_href:
                        p_href = p_href.split("?")[0]

                    resp.meta['p_href'] = p_href
                    resp.meta['p_nid'] = p_nid
                    resp.meta['p_price'] = p_price
                    resp.meta['p_type'] = p_type
                    resp.meta['p_sku'] = p_sku
                    resp.meta['p_sellerid'] = p_sellerid
                    resp.meta['p_sellername'] = p_sellername
                    resp.meta['p_categories'] = p_categories
                    resp.meta['p_rating'] = p_rating
                    resp.meta['p_reviews'] = p_reviews
                    resp.meta['p_brandid'] = p_brandid
                    resp.meta['p_brandname'] = p_brandname

                    yield Request( p_href, callback=self.productpg, meta=resp.meta, headers=MHeaderz )
    
    def productpg(self, resp):
        script = resp.xpath("//script[contains(.,'app.run')]/text()").get()
        if script:
            script = script.strip().split("app.run(")[1][:-8]
            jdata = loads(script)
            if isinstance(jdata, dict):
                p_sold = jdata.get('data',None).get('root', None).get('fields', None).get('review', None).get('ratings', None).get('soldCount', None)
                resp.meta['p_sold'] = p_sold
                yield resp.meta
