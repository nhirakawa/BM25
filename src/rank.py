__author__ = 'Nick Hirakawa'


from math import log

k1 = 1.2
k2 = 100
b = 0.75
R = 0.0


def rank_BM25(n_i, f_i, qf_i, r_i, N, dl, avdl):
	K = compute_K(dl, avdl)
	first = log( ( (r_i + 0.5) / (R - r_i + 0.5) ) / ( (n_i - r_i + 0.5) / (N - n_i - R + r_i + 0.5)) )
	second = ((k1 + 1) * f_i) / (K + f_i)
	third = ((k2+1) * qf_i) / (k2 + qf_i)
	return first * second * third


def compute_K(dl, avdl):
	return k1 * ((1-b) + b * (float(dl)/float(avdl)) )