#!/usr/bin/env python3

from paperbasic import *

Entrez.email = "A.N.Other@example.com"
Entrez.tool  = "PaperLink"


def Link(pmid, link):	
	record = Entrez.read(Entrez.elink(dbfrom="pubmed", id=pmid))	
	if link == 'cited':
		IdList= [a['Id'] for i in record[0]["LinkSetDb"] if i['LinkName'] == 'pubmed_pubmed_citedin' for a in i['Link']]
	
	elif link == 'refs':
		IdList= [a['Id'] for i in record[0]["LinkSetDb"] if i['LinkName'] == 'pubmed_pubmed_refs' for a in i['Link']]
	
	print("\nWe found {} {} papers in the PubMed database".format(len(IdList), link))	
	return IdList

def fetch(pmid, link, prefix, wordcloud, download, IF_filter):
	
	idlist = Link(pmid, link) 
	df = entrez(idlist, prefix, IF_filter)
	
	### download pdf
	if download:
		Download(df, prefix)

	### WordCloud
	if wordcloud:
		Wordcloud(df, prefix)

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description="Searching for the cited papers or reference papers in Pubmed")

	parser.add_argument('-pmid', required=True, metavar='integer', help="Pubmed id of a specific paper") # 30992999
	parser.add_argument('-link', type=str, default = 'cited', choices=['cited','refs'], help = "the linked database (default: cited)")
	parser.add_argument('-prefix',type=str, metavar='string', default = 'Pubmed', help = "the prefix of output (default: Pubmed)")
	parser.add_argument('-cutoff', default=0, type=float, metavar='float', help = "Set the cut off of paper's journal impact factor (default: 0)")
	parser.add_argument('-wordcloud', action = 'store_true', help = "perform worldcloud plot for paper's abstract")
	parser.add_argument('-download', action = 'store_true', help = "download pdf files")
	
	args = parser.parse_args()

	fetch(args.pmid, args.link, args.prefix, args.wordcloud, args.download, args.cutoff)

