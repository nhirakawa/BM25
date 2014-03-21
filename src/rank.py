__author__ = 'Nick Hirakawa'


from math import log

k1 = 1.2
k2 = 100
b = 0.75
R = 0.0


def score_BM25(n, f, qf, r, N, dl, avdl):
	K = compute_K(dl, avdl)
	first = log( ( (r + 0.5) / (R - r + 0.5) ) / ( (n - r + 0.5) / (N - n - R + r + 0.5)) )
	second = ((k1 + 1) * f) / (K + f)
	third = ((k2+1) * qf) / (k2 + qf)
	return first * second * third


def compute_K(dl, avdl):
	return k1 * ((1-b) + b * (float(dl)/float(avdl)) )