__author__ = 'Nick Hirakawa'

from invdx import build_data_structures
from rank import score_BM25


class QueryProcessor:
	def __init__(self, queries, corpus):
		self.queries = queries
		self.index, self.dlt = build_data_structures(corpus)

	def run(self):
		for query in self.queries:
			self.run_query(query)

	def run_query(self, query):
		for term in query:
			query_result = dict()
			if term in self.index:
				doc_dict = self.index[query]
				for docid, freq in doc_dict.iteritems():
					score = score_BM25(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
									   dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length())
					if docid in query_result:
						query_result[docid] += score
					else:
						query_result[docid] = score