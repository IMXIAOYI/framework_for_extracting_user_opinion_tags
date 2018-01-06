# framework_for_extracting_user_opinion_tags
my teammates and I created this framework to extract user opinion tags to conclude users' opinions on yelp restaurants</br>

* data source </br>
download yelp reviews directly as sql form. we extracted all the mcdonald's reviews
* obtain labels </br>
    + Part-of Speech(POS) Tagging
    + Build selection rules, for example conj+amod
    + extract labels based on rules
* remove duplication [simhash]
* topic modeling [lda]
* select labels
* we also tried to use word2vec+debscan+kmeans to do clustering and get labels

we wrote a report to represent our process in detail, check this link 
https://www.dropbox.com/s/spghyrzzoyo4dsi/final_report_final%20version.pdf?dl=0

this paper inspired us 
LI Piji1, MA Jun1, ZHANG Dongmei2, HAN Xiaohui1. Extraction and Ranking of Tags for User Opinions. , 2012, 26(5): 14-20.
