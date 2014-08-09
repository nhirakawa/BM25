BM25
====

A Python implementation of the BM25 ranking function.

Implementation
=============

There are 4 main modules of the program: parser, query processor, ranking function, and data structures. The parser module parses the query file and the corpus file to produce a list and a dictionary, respectively. The query processor takes each query in the query list and scores the documents based on the terms. The ranking function is an implementation of the BM25 ranking function; it uses the natural logarithm in its calculations. Finally, the data structures module contains an inverted index and a document length table. The inverted index use a dictionary to map each word to a dictionary; this secondary dictionary maps each document id to the word frequency in the outer dictionary. The document length table contains the length of each document, and also has a function to calculate the average document length of the collection.

How To Run
----------

To run, simply run `$ python main.py` in the src folder. 
