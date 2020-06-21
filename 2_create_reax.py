
import os

emojis = os.listdir('emojis')
print(emojis)

def group_emojis(emojis):
	categories = {}
	for e in emojis:
		category = emoji.replace('man','person').replace('woman','person')\
				.replace('boy','child').replace('girl','child')\
				.replace('-type-1-2','').replace('-type-3','')\
				.replace('-type-4','').replace('type-5','').replace('type-6','')\
				.replace('medium-light-','').replace('medium-dark-','')\
				.replace('dark-','').replace('light-','').replace('medium-','')\