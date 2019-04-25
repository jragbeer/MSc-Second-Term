import pickle
from rouge import Rouge

rouge = Rouge()

# load in EU and CAN regulations
pickle_in1 = open("H:/true/Canada_Regulations.pickle", 'rb')
can_regs = pickle.load(pickle_in1)
pickle_in = open("EURegulations.pickle", 'rb')
eu_regs = pickle.load(pickle_in)

eu = {}
can = {}
eu_can = {}

with open('H:/true/EU_Regulations_10_epochs.txt', 'r') as file:
    data = file.read().replace('\n', '') # read in RNN output
    for x in list(eu_regs.keys()):
        try: # (gen, ref)
            scores = rouge.get_scores(data,eu_regs[x])#run rouge metrics
            eu[str(x)] = scores
        except:
            pass

with open('H:/true/CAN_Regulations_10_epochs.txt', 'r') as file:
    data = file.read().replace('\n', '') # read in RNN output
    for x in list(can_regs.keys()):
        try: # (gen, ref)
            scores = rouge.get_scores(data,can_regs[x]['content'])#run rouge metrics
            can[str(x)] = scores
        except:
            pass

with open('H:/true/EUandCAN_Regulations_10_epochs2.txt', 'r') as file:
    data = file.read().replace('\n', '') # read in RNN output
    i= 0 #document counter
    # all documents
    for x in [can_regs[y]['content'] for y in list(can_regs.keys())] + [eu_regs[y] for y in list(eu_regs.keys())]:
        try: # (gen, ref)
            scores = rouge.get_scores(data,x) #run rouge metrics
            i+=1
            eu_can[str(i)] = scores
        except:
            pass


# ROUGE-n recall=40% means that 40% of the n-grams in the reference summary are also present in the generated summary.
# ROUGE-n precision=40% means that 40% of the n-grams in the generated summary are also present in the reference summary.
# ROUGE-n F1-score=40% is more difficult to interpret, like any F1-score.
