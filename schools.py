from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import pprint as pprint 
import pymongo

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db