__author__ = 'Nick Hirakawa'

import re


class CorpusParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')

	def parse(self):
		with open(self.filename) as f:
			s = ''.join(f.readlines())
		blobs = s.split('#')[1:]
		for x in blobs:
			split = x.split()
			docid = split.pop(0)


if __name__ == '__main__':
	cp = CorpusParser('text/tccorpus.txt')
	cp.parse()