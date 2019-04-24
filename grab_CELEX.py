import bs4 as bs
import pandas as pd
import numpy as np
import urllib.request
import re
import pickle

# celex == document ID / document number

def grab_function(id):
    # URL to grab data from
    url = "https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1555086040753&uri=CELEX:{}".format(id)
    response = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(response, 'xml')  # use BS to parse data
    info = soup.find_all('div', {"id" : "document1"}) # find the text of the document on the page
    try:
        return info[0].text #return the text of the document
    except Exception as e:
        print(str(e))
        return info
pickle_in0 = open("all_eu_celex.pickle","rb")
all_celex_list = pickle.load(pickle_in0)
data = {}
for x in all_celex_list:
    # some celex have a trailing R that shouldn't be used, remove if that's the case
    if list(x)[-1] == 'R':
        x = x[:-1]
    # grab data using url and celex number, if fail, move on
    try:
        data[str(x)] = grab_function(x)
        # save to file after each data pull, to ensure time saved if process is shut down early
        pickle_out = open("eu_data.pickle", "wb")
        pickle.dump(data, pickle_out)
        pickle_out.close()
    except Exception as e:
        # print which celex number caused an error and the error
        print('error',x)
        print(str(e))
        pass


