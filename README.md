#  paperfetch
  
**paperfetch** can search papers from Pubmed and download papers from Sci-Hub, it also can get the reference and cited papers from a given article
  
##  Requirements
  
  
Required python version
  
* python >= 3.6
  
Several python packages are requied for paperfetch
  
* biopython  
* matplotlib  
* pandas  
* wordcloud  
* beautifulsoup4  
* requests  
* retrying  
* pysocks  
  
##  Installation
  
  
```{bash}
# Clone remote repository
git clone https://github.com/liuwell/paperfetch.git
  
# Install required python pacakge
cd paperfetch
pip install -r requirements.txt
  
# Add execution path
# The path of current dir can get by shell command "pwd"
echo "export PATH=$PATH:current_dir/paperfetch" >> ~/.bashrc
source ~/.bashrc
```
  
##  Usage
  
  
**paperfetch** have two modules to fetch paper's information.
  
####  1. paperfetch
  
  
```bash{code_chunk_offset=0,
paperfetch.py -h
```

```
usage: paperfetch.py [-h] -t string [-p string] [-cutoff float]
                     [-RetMax integer] [-wordcloud] [-download]

A tool for fetch academic papers from Pubmed

optional arguments:
  -h, --help            show this help message and exit
  -t string, --term string
                        the search term, Entrez text query
  -p string, --prefix string
                        the prefix of output (default: Pubmed)
  -cutoff float         Set the cut off of paper's journal impact factor
                        (default: 0)
  -RetMax integer       return max number of papers (default: 1000)
  -wordcloud            perform worldcloud plot for paper's abstract
  -download             download pdf files
```

  
#####  1.1 Search academic papers according a given term
  
  
```bash
# generate a txt file with search result
paperfetch.py -t "small RNA[title]" -p smallRNA
```
  
#####  1.2 Filter papers according to impact factor
  
  
```bash
paperfetch.py -t "small RNA[title]" -p smallRNA -cutoff 3
```
  
#####  1.3 Download papers' pdf files from Sci-Hub
  
  
```bash
paperfetch.py -t "small RNA[title]" -p smallRNA -cutoff 3 -download
```
  
#####  1.4 Perform a wordcloud plot for searched papers' abstract
  
  
```bash
paperfetch.py -t "small RNA[title]" -p smallRNA -cutoff 3 -wordcloud
```
  
####  2. paperlink
  
  
```bash{code_chunk_offset=1,
paperlink.py -h
```

```
usage: paperlink.py [-h] -pmid integer [-link {cited,refs}] [-prefix string]
                    [-cutoff float] [-wordcloud] [-download]

Searching for the cited papers or reference papers in Pubmed

optional arguments:
  -h, --help          show this help message and exit
  -pmid integer       Pubmed id of a specific paper
  -link {cited,refs}  the linked database (default: cited)
  -prefix string      the prefix of output (default: Pubmed)
  -cutoff float       Set the cut off of paper's journal impact factor
                      (default: 0)
  -wordcloud          perform worldcloud plot for paper's abstract
  -download           download pdf files
```

  
#####  2.1 Search the cited papers
  
  
```bash
paperlink.py -pmid 29570994 -link cited
```
```
We found 552 cited papers in the PubMed database

The cut off of IF is 0, remained papers: 552
      ID      PMID PublishDate                  Journal      IF                                              Title                                           Abstract
	  0      1  33632232    2021 Feb      J Nanobiotechnology   6.518  A paclitaxel and microRNA-124 coloaded stepped...  BACKGROUND: Triple negative breast cancer (TNB...
	  1      2  33628737    2021 Feb              Front Oncol   4.848  The Paradoxical Behavior of microRNA-211 in Me...  Cancer initiation, progression, and metastasis...
	  2      3  33614707    2021 Jan         Front Mol Biosci   4.188  Intercellular Communication by Vascular Endoth...  Respiratory diseases and their comorbidities, ...
	  3      4  33613718    2021 Mar               Oncol Lett   2.311  Association between microRNA-527 and glypican-...  The present study aimed to identify the specif...
	  4      5  33603718    2021 Jan          Front Microbiol   4.235  Probiotics and MicroRNA: Their Roles in the Ho...  Probiotics are widely accepted to be beneficia...
	  ..   ...       ...         ...                      ...     ...                                                ...                                                ...
	  547  548  29795674    2018 May                 PLoS One   2.740  Human microRNAs preferentially target genes wi...  MicroRNAs (miRNAs) are short, endogenous RNAs ...
	  548  549  29725042    2018 May                  Sci Rep   3.998  Reduced Autophagy by a microRNA-mediated Signa...  Autophagy plays a key role in the pathogenesis...
	  549  550  29702599    2018 Apr            Int J Mol Sci   4.556   Noncoding RNA:RNA Regulatory Networks in Cancer.  Noncoding RNAs (ncRNAs) constitute the majorit...
	  550  551  29692333    2018 Oct  Trends Endocrinol Metab  11.641                     miR-33: A Metabolic Conundrum.  The miR-33 microRNAs (miRNAs) are crucial regu...
	  551  552  29601548    2018 Mar             Biomedicines   4.717  Roles of NF-kappaB Signaling in the Regulation...  The NF-kappaB family of transcription factors ...

[552 rows x 7 columns]
```
#####  2.2 Search the references
  
  
```bash
paperlink.py -pmid 29570994 -link refs
```
```
We found 402 refs papers in the PubMed database

The cut off of IF is 0, remained papers: 402
      ID      PMID PublishDate              Journal      IF                                              Title                                           Abstract
	  0      1  29887379    2018 Jul                 Cell  38.637  A Network of Noncoding Regulatory RNAs Acts in...  Noncoding RNAs (ncRNAs) play increasingly appr...
	  1      2  29483647    2018 Mar  Nat Struct Mol Biol  11.980  MicroRNA degradation by a conserved target RNA...  microRNAs (miRNAs) repress target transcripts ...
	  2      3  29351846    2018 Jan             Mol Cell  15.584  Dual Strategies for Argonaute2-Mediated Biogen...  While Slicer activity of Argonaute is central ...
	  3      4  29298863    2018 May              FASEB J   4.966  Dual regulation of HMGB1 by combined JNK1/2-AT...  In the context of diabetes, obesity, and metab...
	  4      5  29288704    2018 Mar          Exp Hematol   2.820  The mirn23a and mirn23b microrna clusters are ...  Mice deficient for microRNA (miRNA) cluster mi...
	  ..   ...       ...         ...                  ...     ...                                                ...                                                ...
	  397  398  10706289    2000 Feb               Nature  42.778  The 21-nucleotide let-7 RNA regulates developm...  The C. elegans heterochronic gene pathway cons...
	  398  399  10642801    1999 Dec             Dev Biol   2.895  The lin-4 regulatory RNA controls developmenta...  lin-4 encodes a small RNA that is complementar...
	  399  400   9054503    1997 Mar                 Cell  38.637  The cold shock domain protein LIN-28 controls ...  Mutations in the heterochronic gene lin-28 of ...
	  400  401   8252622    1993 Dec                 Cell  38.637  Posttranscriptional regulation of the heteroch...  During C. elegans development, the temporal pa...
	  401  402   8252621    1993 Dec                 Cell  38.637  The C. elegans heterochronic gene lin-4 encode...  lin-4 is essential for the normal temporal con...

[402 rows x 7 columns]

```
##  Acknowledge
  
  
Thanks for [Biopython's Entrez module](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec139 ) and [Sci-Hub API](https://github.com/zaytoun/scihub.py ).
  
