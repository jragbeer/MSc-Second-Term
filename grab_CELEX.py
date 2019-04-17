import bs4 as bs
import pandas as pd
import numpy as np
import urllib.request
import re
import pickle

def love(id):
    url = "https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1555086040753&uri=CELEX:{}".format(id)
    a = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(a, 'xml')  # top peaks of the year
    c = soup.find_all('div', {"id" : "document1"})
    try:
        return c[0].text
    except Exception as e:
        print(str(e))
        return c
pickle_in0 = open("all_docsbb.pickle","rb")
wowpp = pickle.load(pickle_in0)
# print(wowpp[0].keys())
# wowww = [w.split(':')[1] for cool in wowpp for i in cool for w in i]
# # print(len(wowpp))
# print(len(set(wowww)))
#
# pickle_in = open("all_documents.pickle","rb")
# wow = pickle.load(pickle_in)
# print(len(set(wow)))
pickle_in1 = open("abc.pickle","rb")
thing = pickle.load(pickle_in1)
qq =list(thing.keys())
print(thing[qq[0]])
# pp = 0
# print(thing.keys())
# for y in thing.keys():
#     if 'where' in thing[y]:
#         pp+=1
# print(pp, len(list(thing.keys())))
# pp = [x for x in set(wowww) if x not in qq]

# for x in pp:
#     # print(x)
#     if list(x)[-1] == 'R':
#         x = x[:-1]
#     if x not in qq:
#         # if len(thing[x]) == 0:
#         #     print(x)
#         try:
#             thing[str(x)] = love(x)
#             print(thing[str(x)])
#             pickle_out = open("abc.pickle", "wb")
#             pickle.dump(thing, pickle_out)
#             pickle_out.close()
#         except Exception as e:
#             print('error',x)
#             print(str(e))
#             pass


import pprint
# print(thing("32015R0758"))

# for i in set(wow):
#     if list(i)[-1] == 'R':
#         i = i[:-1]
#     try:
#         print(i)
#         alls[str(i)] = thing(i)
#         print(alls[str(i)])
#         pickle_out = open("def.pickle", "wb")
#         pickle.dump(alls, pickle_out)
#         pickle_out.close()
#     except:
#         pickle_out = open("def.pickle", "wb")
#         pickle.dump(alls, pickle_out)
#         pickle_out.close()
#         pass


