# Web_scraping
Prueba de webscraping de salcobrand
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bs4 as bs
import urllib.request
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import requests
import time
from bs4 import BeautifulSoup
#ctrl c cerrar programa 
options=webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')#poner si no se quiere abrir la página
driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",chrome_options=options)
driver.get("https://salcobrand.cl/t/medicamentos/sistema-nervioso")
page_source=driver.page_source
driver.close()
soup=BeautifulSoup(page_source,'lxml')
nombre_productos=soup.find_all('span',class_='product-name truncate')
for producto in nombre_productos:
    print(producto.get_text())
#link=requests.get("https://analytics.google.com/analytics/web/#/report-home/a20386425w48307883p105301836")
#link
