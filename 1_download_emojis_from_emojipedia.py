import os
import time
import shutil

import requests
from bs4 import BeautifulSoup

def get_emoji_images_from_emojipedia():

	url = "https://emojipedia.org/apple/ios-13.3/"

	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')

	image_elements = soup.find_all('img')
	image_urls = [i.get('data-src') for i in image_elements if i.get('data-src')]

	return image_urls

