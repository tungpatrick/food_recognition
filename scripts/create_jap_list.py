import pandas as pd
import numpy as np
import requests
import json
from bs4 import BeautifulSoup
import csv
import os

def get_japanese_food(url):
    """
    This function is made specifically to collect a list of Japanese food items
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    names = []

    for i in range(2, 8):
        names.extend([" ".join(i.text.split()[1:]) for i in soup.findAll("h2", attrs={"class": "redLink"})])

        response = requests.get(url+"-part"+str(i))
        soup = BeautifulSoup(response.text, "lxml")

    return names

# get list of japanese foods from this link
jap_food = get_japanese_food("https://www.japan-talk.com/jt/new/japanese-food-list")

# create folder structure
for i in jap_food:
    os.mkdir(os.path.join("..", "images","train",i))
    os.mkdir(os.path.join("..", "images","valid",i))
    os.mkdir(os.path.join("..", "images","test",i))

# export list of japanese food
with open(os.path.join("..", "food_list", "jap_list.csv"), "w") as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(jap_food)
