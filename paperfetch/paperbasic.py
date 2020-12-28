#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from Bio import Entrez
from Bio import Medline

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import argparse
import re
import pandas as pd
import os
import sys

from scihub import SciHub

### get paper's impact factor
def get_IF():
	dIF={}
	realpath = sys.path[0]
	with open('%s/../data/Journal_Abbr_IF.txt' % realpath) as f:
		for line in f:
			line=line.split('\t')
			dIF[line[1]]=float(line[2])
	return dIF

### fetch papers
def entrez(idlist, prefix, IF_filter):
	efetch = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
	parse_medline = Medline.parse(efetch)
	dIF = get_IF()
	lineList=[]
	for i, article in enumerate(list(parse_medline)):
		try:
			# Abstract
			abstract = str(article.get('AB', '?'))
			# Source
			source = str(article.get('SO', '?'))
			# DOI, title
			doi = source.split('doi: ')[-1].split()[0][:-1]
			title = str(article.get('TI', '?'))
			if '/' in title:
				title = title.replace('/', '-')
			pdfname = str(i+1) + '-' + title[:-1] + '.pdf'

			# journal, IF
			journal = source.split('.')[0]
			IF = dIF.get(journal)
			if IF == None:
				IF = 0

			# publish date
			pubdate = source.split('.')[1][1:9]
			pubdate = pubdate.split(';')[0]

			line = [i+1, article['PMID'], pubdate, journal, IF, article['TI'], abstract, doi, pdfname]
			lineList.append(line)
		except Exception as e:
			#print(i+1, ', ', "Key Error")
			print(e)

	df = pd.DataFrame(lineList, columns=['ID', 'PMID', 'PublishDate', 'Journal', 'IF', 'Title', 'Abstract', 'DOI', 'pdfname'])
	df = df[df['IF']>=IF_filter]
	#df = df.sort_values(by='IF', ascending=False)
	print("\nThe cut off of IF is %d, remained papers: %s" % (IF_filter, df.shape[0]))
	
	dfout = df.iloc[:, 0:7]
	print(dfout)
	fout = prefix + "_papers.txt"
	dfout.to_csv(fout, index=False, sep='\t')
	return df

### download pdf
def Download(df, prefix):
	df2 = df.iloc[:, 7:9].T
	df2 = df2.to_dict()
	
	sh = SciHub()
	print('\nDownlaoding pdf files ...')

	# make directory
	directory = prefix + '_pdf'
	if not os.path.exists(directory):
		try:
			os.makedirs(directory)
		except Exception as e:
			print("make directory error!")
	
	# download
	for a in df2:
		doi = df2[a]['DOI']
		pdfname = df2[a]['pdfname']
		pdfname2 = os.path.join(directory, pdfname)
		result = sh.download(doi, path=pdfname2)
		print('+++ Downloaded sucessful, %s' % pdfname)

### WordCloud
def Wordcloud(df, prefix):

	print("\nPerforming wordcloud plot ... ")
	Abstract = ' '.join(df['Abstract'].to_numpy())
	cnt = Counter(Abstract.split())
	most_occur = cnt.most_common(10)
	print("Most 10 Frequent word:",most_occur)

	wordcloud = WordCloud().generate(Abstract)
	plt.figure(figsize=(10,20))
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	figout=prefix+"_wordcloud.png"
	plt.savefig(figout, dpi=300, bbox_inches='tight')


