import sys
import random
from textblob import TextBlob as tb

#full = tb(sys.stdin.read())
para = tb("""The term "Aryan" has to do with linguistic and not at all with physical characteristics, and it would seem reasonably clear that mere resemblance in language, indicating a common linguistic root buried in remotely ancient soil, is altogether inadequate to prove common racial origin. There is, and can be, no assurance that the so-called Aryan language was not spoken by a variety of races living in proximity to one another. Our own history has witnessed the adoption of the English tongue by millions of Negroes, whose descendants can never be classified racially with the descendants of white persons notwithstanding both may speak a common root language.

The word "Caucasian" is in scarcely better repute. It is at best a conventional term, with an altogether fortuitous origin, which, under scientific manipulation, has come to include far more than the unscientific mind suspects. According to Keane, for example, it includes not only the Hindu but some of the Polynesians, (that is the Maori, Tahitians, Samoans, Hawaiians and others), the Hamites of Africa, upon the ground of the Caucasic cast of their features, though in color they range from brown to black. We venture to think that the average well informed white American would learn with some degree of astonishment that the race to which he belongs is made up of such heterogeneous elements.""")

def recdef(sent):
	use = tb(sent)
	final = list()

	for word in use.words:
		if word.definitions != []:
			final.append(random.choice(word.definitions))

	return ' '.join(final)


# print recdef(str(random.choice(para.sentences)))

wewant = list()

for i in range(10):
	for word in recdef(str(random.choice(para.sentences))).split():
		if random.randint(1, 8) == 1:
			wewant.append('\n')
		wewant.append(word)

print " ".join(wewant)
