import csv, time
from utility import simple_get, get_names, get_hits_on_name
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from requests_html import HTML, HTMLSession

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'property_type', 'bedroom_count', 'bathroom_count'])

properties = [
    'https://www.airbnb.co.uk/rooms/14531512?guests=1&adults=1&sl_alternate_dates_exclusion=true&source_impression_id=p3_1558628674_R6YuSMmaRax0zqfF',
    'https://www.airbnb.co.uk/rooms/19278160?guests=1&adults=1&sl_alternate_dates_exclusion=true&source_impression_id=p3_1558628675_grYph0qY3hsdrmrR',
    'https://www.airbnb.co.uk/rooms/1939240?guests=1&adults=1&sl_alternate_dates_exclusion=true&source_impression_id=p3_1558628677_uQAnPPsNNPFSteuW',
]

for property in properties:



    raw_html = simple_get(property)
    html = BeautifulSoup(raw_html, 'html.parser')

    name = html.select('span._18hrqvin')[0].text
    property_type = html.select('div._1p3joamp')[0].text
    bedroom_count = html.select('#room div._hgs47m div._n5lh69r div._36rlri div')[1].text # nr of bedrooms
    bathroom_count = html.select('#room div._hgs47m div._n5lh69r div._36rlri div')[3].text # nr of bathrooms



    driver = webdriver.Chrome(executable_path='/Users/josdyr/Downloads/chromedriver')
    driver.get(property)
    # button = driver.find_element_by_css_selector('div#amenities div._1p3joamp button._1dv8bs9v')
    accept_cookie = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/button')
    accept_cookie.click()
    time.sleep(1) # don't think this is needed
    button = driver.find_element_by_xpath('//*[@id="amenities"]/div/div/div/div/section/div[3]/div/button')
    button.click()
    # import ipdb; ipdb.set_trace()


    # amenities = html.select('body > div:nth-child(35) > div > div > div > div > div > div > section > div > section > div:nth-child(1) > section > div > div:nth-child(2) > div:nth-child(1) > div')

    import ipdb; ipdb.set_trace()
    csv.writer.writerow([name, property_type, bedroom_count, bathroom_count])

    print("name: {},\nproperty_type: {},\nbedroom_count: {},\nbathroom_count: {}".format(name, property_type, bedroom_count, bathroom_count))

csv_file.close()
