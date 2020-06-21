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


def download_emoji(url):

	filename = f'emojis/{url.split("/")[-1]}'

	print(f'downloading {filename}')

	r = requests.get(url,stream=True)

	with open(filename, 'wb') as f:
		# r.raw.decode_content = True
		f.write(r.content)


def download_emojis():

	if 'emojis' not in os.listdir():
		os.mkdir('emojis')

	emoji_urls = get_emoji_images_from_emojipedia()

	emojis_already_downloaded = os.listdir('emojis')

	print(emojis_already_downloaded)

	emoji_urls = [e for e in emoji_urls if (e.split('/')[-1] not in emojis_already_downloaded)]

	for url in emoji_urls:
		download_emoji(url)
		time.sleep(2)



if __name__ == "__main__":
	download_emojis()

