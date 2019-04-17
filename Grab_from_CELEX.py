import bs4 as bs
import pandas as pd
import numpy as np
import urllib.request
import re
import pickle

def thing(year, page= None):
    if page == None:
        url = 'https://eur-lex.europa.eu/search.html?qid=1555083986081&type=named&DD_YEAR={}&name=browse-by:eu-parliament-regulations'.format(year)
    else:
        url = 'https://eur-lex.europa.eu/search.html?qid=1555083986081&type=named&DD_YEAR={}&name=browse-by:eu-parliament-regulations&page={}'.format(year, page)
    a = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(a, 'xml')  # top peaks of the year

    c = soup.find_all('div', {"class" : "col-sm-6"})
    reg = r'CELEX:\w{1,}'
    celex = []
    for x in c:
        try:
            celex.append(re.findall(reg, str(x)))
        except:
            pass
    return celex

alls = []

for x in range(1994, 2020):
    alls.append(thing(x))
    # if x < 1999:
    #     continue
    for z in range(2,21):
        alls.append(thing(x,z))
    print(x, len(alls),len(set([w.split(':')[1] for cool in alls for i in cool for w in i])))


bb = set([w.split(':')[1] for cool in alls for i in cool for w in i])
pickle_out = open("all_docsbb.pickle","wb")
pickle.dump(bb, pickle_out)
pickle_out.close()