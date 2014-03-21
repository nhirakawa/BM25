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
			text = x.split()
			docid = text.pop(0)

	def get_corpus(self):
		pass


class QueryParser:

	def __init__(self, filename):
		self.filename = filename
		with open(filename) as f:
			lines = ''.join(f.readlines())
		self.queries = [x.rstrip() for x in lines.split('\n')[:-1]]

	def get_queries(self):
		return self.queries


if __name__ == '__main__':
	qp = QueryParser('text/queries.txt')
	print qp.get_queries()