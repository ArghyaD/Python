# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 22:28:14 2018

@author: Soumik Saha
"""

from selenium import webdriver
import matplotlib.pyplot as plt
from selenium.webdriver.support.ui import Select
import numpy as np
import pandas as pd
import matplotlib.dates as date
import os
import glob


#driver = webdriver.Chrome(r"C:\Python27\Tools\chromedriver.exe")
url = r'https://wyniki.tge.pl/en/wyniki/archiwum/'

driver = webdriver.Chrome(r"chromedriver.exe")
driver.get(url)


market = Select(driver.find_element_by_id('id_market'))
market.select_by_value('rtee')
rof = Select(driver.find_element_by_id('id_data_scope'))
rof.select_by_value('contract')
tp = Select(driver.find_element_by_id('id_data_period'))
tp.select_by_value('1')
driver.find_element_by_xpath(r"//div[@class='submit']//input[@value='Next step »']").click()

field = Select(driver.find_element_by_id('id_fields'))
field.select_by_value('4')
driver.find_element_by_xpath(r"//div[@class='steps multiselect fields']//div[@class='center']//a[@class='left_to_right']").click()
contract = Select(driver.find_element_by_id('id_contracts'))
contract.select_by_value('4')
driver.find_element_by_xpath(r"//div[@class='steps multiselect contracts']//div[@class='center']//a[@class='left_to_right']").click()
driver.find_element_by_id(r'submit2').click()

default_download_path = r'C:\Users\Arghyadeep Choudhury\Downloads'
files_path = os.path.join(default_download_path, '*')
files = sorted(
    glob.iglob(files_path), key=os.path.getctime, reverse=True) 
dataset = pd.read_csv(files[0],sep=';|\s*',engine='python',skiprows=2)
BY19 = dataset.loc[dataset['Settlement'] == 'BASE_Y-19'].values

X = np.array(BY19[:,0])
Y = np.array(BY19[:,3])

plt.gca().xaxis.set_major_formatter(date.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(date.DayLocator())

fig = plt.figure()
fig.suptitle('Visualization')
plt.xlabel('Date')
plt.ylabel('Price')
plt.plot(X,Y)
plt.show()
plt.gcf().autofmt_xdate()
fig.savefig('VisualQ1.jpeg')