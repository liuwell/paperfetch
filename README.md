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
  
#####  2.2 Search the references
  
  
```bash
paperlink.py -pmid 29570994 -link refs
```
  
##  Acknowledge
  
  
Thanks for [Biopython's Entrez module](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec139 ) and [Sci-Hub API](https://github.com/zaytoun/scihub.py ).
  
