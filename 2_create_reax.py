
import os
import random

import imageio


def group_emojis(emojis):

	categories = {}

	for e in emojis:

		if 'skin-tone' in e or 'emoji-modifier' in e or 'type' in e:
			print(e)

			category = e.replace('woman','person').replace('man','person')\
					.replace('female','').replace('male','')\
					.replace('boy','child').replace('girl','child')\
					.replace('women','people').replace('men','people')\
					.replace('-type-1-2','').replace('-type-3','')\
					.replace('-type-4','').replace('-type-5','').replace('-type-6','')\
					.replace('medium-light-','').replace('medium-dark-','')\
					.replace('dark-','').replace('light-','').replace('medium-','')\
					.replace('haired','hair')\
					.replace('red-hair','').replace('blond-hair','')\
					.replace('blonde','').replace('blond','')\
					.replace('black-hair','').replace('white-hair','')\
					.replace('dancing','dancer').replace('facepalming','facepalm')\
					.replace('biking','bicyclist')\
					.replace('person','').replace('child','')\
					.replace('-','').replace('skintone','')\
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


def create_gif_of_images(name,pngs):

	random.shuffle(pngs)

	images = []

	for png in pngs:
		path = f'emojis/{png}'
		images.append(imageio.imread(path))

	if 'gifs' not in os.listdir():
		os.mkdir('gifs')

	imageio.mimsave(f'gifs/{name}.gif', 3, images)


def main(abolish_the_police=True):

	emojis = os.listdir('emojis')
	groups = group_emojis(emojis)
	groups = filter_categories_to_minimum(groups)

	if abolish_the_police:
		groups = remove_categories_with_term(groups, 'police')

	for g in groups:
		create_gif_of_images(g,groups[g])
		



if __name__ == "__main__":
	main()