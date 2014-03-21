#invdx.py
# An inverted index
__author__ = 'Nick Hirakawa'


class InvertedIndex:

	def __init__(self):
		self.index = dict()

	def add(self, word, doc):
		if word in self.index:
			d = self.index[word]
			d[doc] += 1
		else:
			d = dict()
			d[doc] = 1
			self.index[word] = d


class DocumentLengthTable:

	def __init__(self):
		self.table = dict()

	def add(self, docid, length):
		self.table[docid] = length

	def get_length(self, docid):
		return self.table[docid]