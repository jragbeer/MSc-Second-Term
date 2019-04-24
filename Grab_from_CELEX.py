import bs4 as bs
import pandas as pd
import numpy as np
import urllib.request
import re
import pickle

def grab_celex_function(year, page= None):
    # if a page number is supplied, use it;
    # else go to the first page of the year for EU Parliament
    if page == None:
        url = 'https://eur-lex.europa.eu/search.html?qid=1555083986081&type=named&DD_YEAR={}&name=browse-by:eu-parliament-regulations'.format(year)
    else:
        url = 'https://eur-lex.europa.eu/search.html?qid=1555083986081&type=named&DD_YEAR={}&name=browse-by:eu-parliament-regulations&page={}'.format(year, page)
    response = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(response, 'lxml')  # use BS to parse response
    all_data = soup.find_all('div', {"class" : "col-sm-6"}) #class in the html that data is in
    reg = r'CELEX:\w{1,}' #regex to capture celex (needs to be split later)
    celex = []
    for x in all_data:
        try:
            celex.append(re.findall(reg, str(x)))
        except:
            pass
    return celex

alls = [] #list to put all celex in

# create list of lists for all celex. Each list will have celex from that URL (year/page)
for x in range(1994, 2020):
    alls.append(grab_celex_function(x)) # grabs celex from first page of year
    for z in range(2,21):
        alls.append(grab_celex_function(x,z)) # grabs celex from second+ page of year

# create a set with all of the celex for all of the EU Parliament Regulations
# output list as a pickle for next part of data pipeline
ouptut = set([w.split(':')[1] for cool in alls for i in cool for w in i])
pickle_out = open("all_eu_celex.pickle","wb")
pickle.dump(ouptut, pickle_out)
pickle_out.close()