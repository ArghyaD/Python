# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 15:11:23 2018

@author: Soumik Saha
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
from selenium.webdriver.support.ui import Select
import numpy as np
import matplotlib.dates as date
import datetime as dt

driver = webdriver.Chrome(r"chromedriver.exe")
url = r'http://markets.businessinsider.com/commodities/historical-prices/co2-emissionsrechte/euro'
driver.get(url)


ref_calendar = {'January':1,'February':2,'March':3,'April':4,
                'May':5,'June':6,'July':7,
                'August':8,'September':9,'October':10,'November':11,
                'December':12}

start_month = Select(driver.find_element_by_id('historic-prices-start-month'))
start_year = Select(driver.find_element_by_id('historic-prices-start-year'))


year = start_year.first_selected_option.text
year = int(year)


month = start_month.first_selected_option.text
month = ref_calendar[month]
month -= 2

if month <= 0:
    month = 12 + month
    year -= 1
    year = str(year)
    start_year.select_by_value(year)
start_month.select_by_value(str(month))
driver.find_element_by_id('request-historic-price').click()
    
html = driver.page_source
soup = BeautifulSoup(html, "html5lib")
table_lst = []

for tag in soup.find_all('table',class_='table instruments'):
    table_lst.append(tag.text)
f_table = re.sub('\s\s+','K',table_lst[0])

temp = re.sub('KDaily HighKDaily Low','',f_table)
temp = re.split('K',temp)
temp = temp[4:-1]
date_lst = []
open_lst = []
close_lst = []

size = len(temp)
i=0
while(i<size):
    if(i%3) == 0:
        date_lst.append(temp[i])
    elif i%3 == 1:
        close_lst.append(temp[i])
    else:
        open_lst.append(temp[i])
    i+=1

X = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in date_lst]
Y = np.array(close_lst)
plt.gca().xaxis.set_major_formatter(date.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(date.DayLocator())
fig = plt.figure()
fig.suptitle('Visualization')

plt.plot(X,Y)
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.yticks(np.arange(7,15,3))
plt.show()
plt.gcf().autofmt_xdate()
fig.savefig('VisualQ2.jpeg')

