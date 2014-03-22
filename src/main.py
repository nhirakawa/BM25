__author__ = 'Nick Hirakawa'


from parse import *
from query import QueryProcessor
import operator


def main():
	qp = QueryParser(filename='../text/queries.txt')
	cp = CorpusParser(filename='../text/corpus.txt')
	qp.parse()
	queries = qp.get_queries()
	cp.parse()
	corpus = cp.get_corpus()
	proc = QueryProcessor(queries, corpus)
	results = proc.run()
	for result in results:
		sorted_x = sorted(result.iteritems(), key=operator.itemgetter(1))
		sorted_x.reverse()
		print len(sorted_x)


if __name__ == '__main__':
	main()