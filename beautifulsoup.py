from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import csv

#initialize the chrome web driver
driver = webdriver.Chrome()

page_url = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401' 

#Fetching the web page
driver.get(page_url)

#wait for the table to load
driver.implicitly_wait(10)

#Get the page sorce after JavaScript excution
page_source =  driver.page_source

#parse the html content 
soup = BeautifulSoup(page_source, 'html.parser')

#find the table element 
table = soup.find('table', class_='pub-table')

if table:
    #Extract the column headers using list comprehension
    headers = [th.get_text().strip() for th in table.find_all('th')]

    #Exract the row data
    rows = []
    for tr in table.find_all('tr'):
       row = [td.get_text().strip() for td in tr.find_all('td')]
    if row:
        rows.append(row)


    #print column headers
    print("column headers:")
    print(headers)

    #print column headers
    print("\nRow Data:")
    print(rows)

    #new set of headers inside of tuple
    headers_tuple = (
        'All-items', 
        'Food5', 
        'Shelter6', 
        'Household operations, '
        'furnishings and equipment', 
        'Clothing and footwear', 
        'Transportation', 
        'Gasoline', 
        'Health and personal care', 
        'Recreation, education and reading', 
        'Alcoholic beverages, tobacco products and recreational cannabis', 
        'All-items excluding food and energy7', 
        'All-items excluding energy7', 
        'Energy7', 
        'Goods8', 
        'Services9'
    )
    
    #write the data to csv file
    with open('table_data.csv','w',newline="") as csvfile:
        write = csv.writer(csvfile)

        #insert the new oloumn as the first column in each row
        for i, row in enumerate(rows):
            rows[i] = [headers_tuple[i]] + row

    # write headers
    write.writerow(headers[2:8])

    #write row
    write.writerows(rows)

    print('Data has been successfully saved to table_data.csv!')
else:
    print('table not found')


    #close the webdriver
    driver.quit( )



