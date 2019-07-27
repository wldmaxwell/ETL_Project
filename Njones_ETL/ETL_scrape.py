from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import pprint as pprint 

def init_browser():

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

Apt_and_Public_School_Info = {}

def scrape_apt_PublicSchool_info():
    try:
        browser = init_browser()

        schools_url = 'https://www.apartments.com/the-locks-tower-richmond-va/c58v4yf/'
        browser.visit(schools_url)

        schools_html = browser.html
        schools_soup = bs(schools_html, 'html.parser')

        schools = schools_soup.find_all('article', class_='diamond placard')
        
    
    Apt_and_Public_School_Info = []

        browser = init_browser
        link = PublicSchools.find('a')['href']
        
        browser.visit(link)
        school_link_html = browser.html
        
        school_link_soup = bs(school_link_html, 'html.parser')
        


for PublicSchools in apartments:
    
    school_Type = school_link_soup.find('p', class_='schoolType').text
    school_name = school_link_soup.find('p', class_='schoolName').text
    grade_levels = school_link_soup.find('p', class_='grades').text
    numb_of_students = school_link_soup.find('p', class_='numberOfStudents').text
    school_phone = school_link_soup.find('p', class_='schoolPhone').text
    RVA_PublicSchools_url.append({'Type': school_Type, 'School Name': school_name, 'Grade Levels': grade_levels, 'Student Count': numb_of_students, 'Phone': school_phone})

pprint.pprint(RVA_PublicSchools_url)
    