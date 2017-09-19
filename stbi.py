#import fungsi dari file tfidf
from tfidf import tf, idf

#variable
n_terms = 3
total_terms = 100
total_doc_with_terms = 1000
total_doc = 10000000

#memanggil fungsi tf untuk menghitung term frequency
#variable tf_value akan menampung file dari hasil komputasi fungsi tf
tf_value = tf(n_terms, total_terms)

idf_value = idf(total_doc, total_doc_with_terms)

#print tf_value
print("Term frequency: {0}".format(tf_value))

print("inverse doc frequency: {0}".format(idf_value))

tfidf_value = tf_value*idf_value

print("tf * idf: {0}".format(tfidf_value))