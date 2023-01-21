from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("C:/Users/rizho/OneDrive/Desktop/STEP TO FUTURE/PYTHON SPECIAL/SCRAPING PART1/chromedriver.exe")
page = requests.get(START_URL)
soup = bs(page.text, 'html.parser')
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')
headers = ["name","distance","mass","radius"]
Star_Data = []


def scrap():

    for td_tag in soup.find_all("td", attrs={"class", "wikitable sortable jquery-tablesorter"}):

        li_tags = td_tag.find_all("td")
        temp_list = []

        temp_list.append(li_tags)

        for index, li_tag in enumerate(li_tags):

            if index == 0:

                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:

                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")

        Star_Data.append(temp_list)




        
       



scrap()
headers = ["name","distance","mass","radius"]
# Define pandas DataFrame 
planet_df_1 = pd.DataFrame(Star_Data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('updated_scraped_data.csv',index=True, index_label="id")