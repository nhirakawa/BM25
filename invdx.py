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

	def get_document_frequency(self, word, docid):
		if word in self.index:
			if docid in self.index[word]:
				return self.index[word][docid]
			else:
				raise LookupError('%s not in document %s' % (str(word), str(docid)))
		else:
			raise LookupError('%s not in index' % str(word))



class DocumentLengthTable:

	def __init__(self):
		self.table = dict()

	def add(self, docid, length):
		self.table[docid] = length

	def get_length(self, docid):
		if docid in self.table:
			return self.table[docid]
		else:
			raise LookupError('%s not found in table' % str(docid))