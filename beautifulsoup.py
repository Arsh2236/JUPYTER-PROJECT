from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import csv

#initialize the chrome web driver
driver = webdriver.chrome()

page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401' 

#Fetching the web page
driver.get(page_url)

#wait for the table to load
driver.implicity_wait(10)

#Get the page sorce after JavaScript excution
page_source =  driver.page_source

#parse the html content 
soup = BeautifulSoup(page_source, 'html.parser')

#find the table element 
table = soup.find(id='simpleTable')

if table:
    #Extract the coloumn header
    headers = []

