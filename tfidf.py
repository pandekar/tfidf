import math

def tf(n_terms, total_terms):
	tf = n_terms / total_terms
	return tf

def idf(total_doc, total_doc_with_terms):
	idf = math.log10(total_doc/total_doc_with_terms)
	return idf

