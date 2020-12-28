#!/usr/bin/env python3

from paperbasic import *

Entrez.email = "A.N.Other@example.com"
Entrez.tool  = "PaperFetch"

def fetch(term, prefix, wordcloud, download, IF_filter, retmax):
	
	esearch = Entrez.esearch(db="pubmed", term=term, RetMax=retmax)
	read_esearch = Entrez.read(esearch)
	print("Total items: ", read_esearch["Count"])
	print("We only return first %d items" % min(retmax, int(read_esearch["Count"])))
	
	idlist = read_esearch["IdList"]
	df = entrez(idlist, prefix, IF_filter)
	
	### download pdf
	if download:
		Download(df, prefix)

	### WordCloud
	if wordcloud:
		Wordcloud(df, prefix)
	
	### Time Series plot

if __name__ == '__main__':
	
	#parser = argparse.ArgumentParser(description="A tool for fetch academic papers from Pubmed", usage="./Paperlink.py -pmid 30992999 -link refs -prefix test -cutoff 20 -download -wordcloud")
	parser = argparse.ArgumentParser(description="A tool for fetch academic papers from Pubmed")

	parser.add_argument('-t', '--term', type=str, metavar='string', required=True, help="the search term, Entrez text query")
	parser.add_argument('-p', '--prefix',type=str, metavar='string', default = 'Pubmed', help = "the prefix of output (default: Pubmed)")
	parser.add_argument('-cutoff', default=0, type=float, metavar='float', help = "Set the cut off of paper's journal impact factor (default: 0)")
	parser.add_argument('-RetMax', default=1000, type=int, metavar='integer', help = "return max number of papers (default: 1000)")
	parser.add_argument('-wordcloud', action = 'store_true', help = "perform worldcloud plot for paper's abstract")
	parser.add_argument('-download', action = 'store_true', help = "download pdf files")
	
	args = parser.parse_args()

	fetch(args.term, args.prefix, args.wordcloud, args.download, args.cutoff, args.RetMax)

