# Scrapy settings for Klinecollective project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Klinecollective"

SPIDER_MODULES = ["Klinecollective.spiders"]
NEWSPIDER_MODULE = "Klinecollective.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
   "Accept-Language": "en",
   #"Cookie": "wmc_ip_info=eyJjb3VudHJ5IjoiUEsiLCJjdXJyZW5jeV9jb2RlIjoiUEtSIn0%3D; wmc_current_currency=USD; PHPSESSID=riuplf9uk4jh0u78f6fu7u6gcg; _gid=GA1.2.1260720491.1681843050; ln_or=eyI0NDc5NDgxIjoiZCJ9; __stripe_mid=e92bd83e-1757-4a21-b720-82799ab7379f7727d4; __insp_wid=1263964437; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9rbGluZWNvbGxlY3RpdmUuY29tL3Nob3Av; __insp_targlpt=SGFuZG1hZGUgUGFpbnRpbmdzIGZyb20gRW1lcmdpbmcgQXJ0aXN0cyB8IEtsaW5lIENvbGxlY3RpdmU%3D; __insp_sid=3236433288; __insp_uid=3424803832; yith_wrvp_products_list=%7B%221681845766%22%3A117819%2C%221681845771%22%3A148497%2C%221681845775%22%3A134452%2C%221681845997%22%3A149406%2C%221681846002%22%3A129829%2C%221681846311%22%3A148648%2C%221681846315%22%3A150617%2C%221681846322%22%3A150531%7D; _ga=GA1.1.1472648634.1681843050; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE2ODE4NDMwNTAsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8va2xpbmVjb2xsZWN0aXZlLmNvbS9zaG9wLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTY4MTg0ODA0OSwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly9rbGluZWNvbGxlY3RpdmUuY29tL3Nob3AvIn19; __insp_pad=13; __insp_slim=1681848056941; _ga_KMYKK0C8KC=GS1.1.1681850980.3.0.1681850980.0.0.0; _ga_V4WBTLZ9CS=GS1.1.1681850980.3.0.1681850980.60.0.0"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "Klinecollective.middlewares.KlinecollectiveSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "Klinecollective.middlewares.KlinecollectiveDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "Klinecollective.pipelines.KlinecollectivePipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)

# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
