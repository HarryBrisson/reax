
import os
import random

import imageio
from PIL import Image


def group_emojis(emojis):

	categories = {}

	for e in emojis:

		if 'skin-tone' in e or 'emoji-modifier' in e or 'type' in e:

			category = e.replace('woman','person').replace('man','person')\
					.replace('female','').replace('male','')\
					.replace('boy','child').replace('girl','child')\
					.replace('women','people').replace('men','people')\
					.replace('-type-1-2','').replace('-type-3','')\
					.replace('-type-4','').replace('-type-5','').replace('-type-6','')\
					.replace('medium-light-','').replace('medium-dark-','')\
					.replace('dark-','').replace('light-','').replace('medium-','')\
					.replace('haired','hair').replace('with','')\
					.replace('red-hair','').replace('blond-hair','')\
					.replace('blonde','').replace('blond','')\
					.replace('black-hair','').replace('white-hair','')\
					.replace('person','').replace('child','').replace('adult','')\
					.replace('-','').replace('skintone','')\
					.replace('dancing','dancer').replace('facepalming','facepalm')\
					.replace('biking','bicyclist').replace('running','runner')\
					.replace('shrugging','shrug').replace('golfing','golfer')\
					.replace('guards','guard').replace('gettinghaircut','haircut')\
					.replace('swimming','swimmer').replace("weightlifting","weightlifter")\
					.replace('princess','royal').replace('prince','royal')\
					.replace('sleuthorspy','sleuth').replace('white','')\
					.replace('informationdesk','tippinghand')\
					.replace('father','parent').replace('mother','parent')\
					.split('_')[0]

			category += "_all"

			if category in categories.keys():
				categories[category].append(e)
			else:
				categories[category] = [e]

	return categories

def filter_categories_to_minimum(categories,minimum=2):
	new_categories = {}
	for c in categories:
		if len(categories[c])>=minimum:
			new_categories[c] = categories[c]
	return new_categories

def remove_categories_with_term(categories, term):
	new_categories = {}
	for c in categories:
		if term not in c:
			new_categories[c] = categories[c]
	return new_categories


def gen_frame(path):
    im = Image.open(path)
    alpha = im.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

    # Paste the color of index 255 and use alpha as a mask
    im.paste(255, mask)

    # The transparency index is 255
    im.info['transparency'] = 255

    return im


def create_gif_of_images_alt(name,pngs):
	frames = [gen_frame(f'emojis/{png}') for png in pngs]  
	frames[0].save(f'gifs/{name}.gif', save_all=True, append_images=frames[1:], loop=0, disposal=2, duration=200)


def create_gif_of_images(name,pngs):

	random.shuffle(pngs)

	images = []

	for png in pngs:
		path = f'emojis/{png}'
		images.append(imageio.imread(path))

	if 'gifs' not in os.listdir():
		os.mkdir('gifs')

	imageio.mimsave(f'gifs/{name}.gif', images, duration=.2)


def main(abolish_the_police=True):

	emojis = os.listdir('emojis')
	groups = group_emojis(emojis)
	groups = filter_categories_to_minimum(groups)

	if abolish_the_police:
		groups = remove_categories_with_term(groups, 'police')

	for g in groups:
		(print(g))
		try:
			create_gif_of_images_alt(g,groups[g])
		except Exception as e:
			print(f'could not create for {g}: {e}')
		



if __name__ == "__main__":
	main()