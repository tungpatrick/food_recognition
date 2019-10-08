import pandas as pd
import numpy as np
import requests
import json
from bs4 import BeautifulSoup
import os

# In order to collect better quality images of the food, I manually created a json
# file that translated the jap_list.csv foods into Japanese. This is so that I can
# get better results on a search engine.

# read translated food items
with open("../food_list/jap_translate.json", "r", encoding="utf8") as f:
    jap_translate = json.load(f)

# download images to train dir
NUM_IMAGES = 500
images_per_group = NUM_IMAGES

for food in jap_translate.keys():
    # check number of files in directory
    for r, d, files in os.walk(os.path.join("..", "images", "train", food)):
        files_in_directory = len(files)

    if files_in_directory < images_per_group:
        print("Collecting image urls for {}.".format(food))

        jap_name = jap_translate[food]
        page = 1
        image_urls = []
        while len(set(image_urls)) <= images_per_group:
            # download images from Yahoo Japan
            yahoo_url = "https://search.yahoo.co.jp/image/search?p="+jap_name+"&ei=UTF-8&b="+str(page)
            response = requests.get(yahoo_url)
            soup = BeautifulSoup(response.text, "lxml")

            image_urls.extend([i["src"] for i in soup.findAll("img")[:-1]])
            page += 20

        print("Downloading images for {}.".format(food))
        for index, img_url in enumerate(set(image_urls)):
            img_data = requests.get(img_url).content
            with open(os.path.join("..", "images", "train", food, food+"_"+str(index)+".jpg"), "wb") as handler:
                handler.write(img_data)
    else:
        print("Images for {} is already downloaded.".format(food))
