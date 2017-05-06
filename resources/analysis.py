#David Yelsey
import codecs
from collections import defaultdict, Counter
from operator import itemgetter
import sys

def add_pound(word):
	return '#'+word.rstrip()+'#'

def make_histogram(name):
	f = codecs.open(name, encoding='utf-8')
	stop_words = [u'\n']

	histogram = defaultdict(int)
	for line in f:
		for i in line:
			i = i.lower()
			if i not in stop_words:
				histogram[i] += 1
	f.close()
	return histogram

def print_hist(histogram):
	result = sorted(histogram.items(), key=itemgetter(1), reverse=True)
	for i, item in enumerate(result):
		if i > 30:
			break
		print item[0]," : ",item[1]


def make_trie(name):
	f = codecs.open(name, encoding='utf-8')
	trie = defaultdict(lambda: defaultdict(int))
	for line in f:
		words = line.split()
		for word in words:
			word = word.lower()
			for letter in range(len(word)):
				if letter+1 == len(word):
					trie[word[letter]]['#'] += 1
				else:
					trie[word[letter]][word[letter+1]] += 1
	return trie


def find_max(trie):
	max_count = {}
	for i, item in enumerate(trie):
		max_l = u''
		max_c = 0
		for i in trie[item].keys():
			if trie[item][i] > max_c:
				max_l = trie[item].keys()[0]
				max_c = trie[item][i]
		max_count[item] = (u' '.join(max_l), max_c)
	return max_count

def add_to(data):
	histogram = {}
	for data_set in data:
		for letter in data_set.keys():
			if letter in histogram.keys():
				if histogram[letter][1] < data_set[letter][1]:
					histogram[letter] = data_set[letter]
			else:
				histogram[letter] = data_set[letter]
	return histogram

def print_trie(trie):
	print "\nMost likely succeeding letters\n============================="
	for i in trie.keys():
		print i, " ==> ", trie[i][0] 

if sys.argv[1] == '-h':
	poems = make_histogram('jdt.poems.2017-02-01.txt')
	reviews = make_histogram('jdt.reviews.2017-01-31.txt')
	stories = make_histogram('jdt.stories.2017-01-31.txt')
	stories1 = make_histogram('jdt.stories.2017-02-01.txt')
	histogram = Counter(stories) + Counter(poems) + Counter(reviews) + Counter(stories1)
	print_hist(histogram)

elif sys.argv[1] == '-b':
	histogram = []
	histogram.append(find_max(make_trie('jdt.poems.2017-02-01.txt')))
	histogram.append(find_max(make_trie('jdt.reviews.2017-01-31.txt')))
	histogram.append(find_max(make_trie('jdt.stories.2017-01-31.txt')))
	histogram.append(find_max(make_trie('jdt.stories.2017-02-01.txt')))
	histogram = add_to(histogram)
	print_trie(histogram)

else:
	print "Usage: analysis.py -h [historgram] or -b [bigram]"

