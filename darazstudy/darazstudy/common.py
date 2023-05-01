# -*- coding: utf-8 -*-

from re import M
import logging, re, requests
from re import escape
from random import randint
import xlsxwriter, mimetypes, csv
import base64, requests, json
from ast import literal_eval
from requests import get, post
from darazstudy.settings import *
from itertools import product
from copy import copy, deepcopy
from unidecode import unidecode
from mysql.connector import connect
from re import sub, search, findall
from bs4 import BeautifulSoup as bs
from lxml.html import tostring, fromstring
from scrapy.exceptions import IgnoreRequest
from itemadapter import is_item, ItemAdapter
from json import dumps, loads, detect_encoding
from scrapy.utils.response import open_in_browser
from requests_futures.sessions import FuturesSession
from scrapy import Spider, Request, FormRequest, signals
from urllib.parse import quote, quote_plus, unquote, urlencode
