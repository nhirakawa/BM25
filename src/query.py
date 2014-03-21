__author__ = 'Nick Hirakawa'


from invdx import build_data_structures


class QueryProcessor:

	def __init__(self, queries, corpus):
		self.queries = queries
		self.index, self.dlt = build_data_structures(corpus)