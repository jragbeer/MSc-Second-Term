import pickle
from rouge import Rouge
import datetime
import pandas as pd

rouge = Rouge()
path = "C:/Users/Julien/PycharmProjects/webscraping/tensorflow-rnn-shakespeare-master/"
# load in EU and CAN regulations
pickle_in1 = open(path + "Canada_Regulations2.pickle", 'rb')
can_regs = pickle.load(pickle_in1)
pickle_in = open(path + "EURegulations.pickle", 'rb')
eu_regs = pickle.load(pickle_in)

timee = datetime.datetime.now()
print(timee)
print(len(list(can_regs.keys())))

eu = {}
can = {}
eu_can = {}

print(timee)
with open(path + 'EU_Regulations_10_epochs.txt', 'r') as file:
    data = file.read().replace('\n', '') # read in RNN output
    for x in list(eu_regs.keys()):
        try: # (gen, ref)
            scores = rouge.get_scores(data,eu_regs[x])#run rouge metrics
            eu[str(x)] = scores
        except:
            pass
pickle_out = open("eu_rouge.pickle","wb")
pickle.dump(eu, pickle_out)
pickle_out.close()
i= 0
# print('done', datetime.datetime.now()-timee)

with open(path + 'CAN_Regulations_10_epochs.txt', 'r') as file:
    data = file.read().replace('\n', '') # read in RNN output
    for x in list(can_regs.keys()):
        try: # (gen, ref)
            scores = rouge.get_scores(data,can_regs[x]['content'])#run rouge metrics
            i += 1
            print(i)
            can[str(x)] = scores
        except:
            pass
pickle_out = open("can_rouge.pickle","wb")
pickle.dump(can, pickle_out)
pickle_out.close()
print('done', datetime.datetime.now()-timee)
with open(path + '/EUandCAN_Regulations_10_epochs2.txt', 'r') as file:
    data = file.read().replace('\n', '') # read in RNN output
    i= 0 #document counter
    # all documents
    for x in [can_regs[y]['content'] for y in list(can_regs.keys())] + [eu_regs[y] for y in list(eu_regs.keys())]:
        try: # (gen, ref)
            scores = rouge.get_scores(data,x) #run rouge metrics
            i+=1
            print(i)
            eu_can[str(i)] = scores
        except:
            pass
print('done', datetime.datetime.now()-timee)
pickle_out = open("can_eu_rouge.pickle","wb")
pickle.dump(eu_can, pickle_out)
pickle_out.close()
print('done', datetime.datetime.now()-timee)

pickle_out = open("can_eu_rouge.pickle","rb")
eu = pickle.load(pickle_out)
new = []
new2 = []
for x in list(eu.keys()):
    new.append(eu[x][0]['rouge-1']['p'])
    new2.append(eu[x][0]['rouge-2']['p'])
print(pd.Series(new).describe())
print(pd.Series(new2).describe())

# ROUGE-n recall=40% means that 40% of the n-grams in the reference summary are also present in the generated summary.
# ROUGE-n precision=40% means that 40% of the n-grams in the generated summary are also present in the reference summary.
# ROUGE-n F1-score=40% is more difficult to interpret, like any F1-score.