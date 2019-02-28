import nltk
from nltk.probability import LaplaceProbDist
from nltk.corpus import treebank, brown
from nltk.tag import hmm
import numpy as np
import cProfile
import io
import pstats

def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

@profile
def main():
    np.random.seed(1) #set a seed for reproducibility
    trainData = list(brown.tagged_sents())  #list of sentences, with each token assigned a tag
    np.random.shuffle(trainData) # shuffle the training data
    train_data = trainData[:int(0.7*len(trainData))] # 70% split of trainData is the training data
    test_data = trainData[int(0.7*len(trainData)):] # 30% split of trainData is the test data
    new_test = [y[0] for x in test_data for y in x] #extract each tag from lists of lists
    allStates2 = set()
    observationSymbols2 = set()  # Vocabulary in our case
    for t in train_data:
        for (word, tag) in t:
            allStates2.add(tag)
            observationSymbols2.add(word)
    allStates2 = list(allStates2) #add each tag to a set, then convert from set to list
    observationSymbols2 = list(observationSymbols2)#add each word to a set, then convert from set to list

    print("Total States (tags): ", len(allStates2)) #print how many unique tags
    print("Total Observation Symbols (Vocab): ", len(observationSymbols2))#print how many unique words
    print("Len of test data", len(test_data)) #how many items are in the test dataset

    smoothingFunction = lambda fdist, bins: LaplaceProbDist(fdist, bins) #Laplace was choosen as it appears to give better accuracy
    trainer = hmm.HiddenMarkovModelTrainer(states=allStates2,symbols=observationSymbols2) #use the training data to fit the model
    tagger = trainer.train_supervised(train_data, estimator=smoothingFunction)

    print("\n**** Test: Output of HMM tagger based on Viterbi algorithm ****")
    output = tagger.tag(new_test)
    test_data = [item for sublist in test_data for item in sublist]
    good = 0
    for x in range(len(output)):
        if output[x] == test_data[x]:
            good +=1
    print('The accuracy of this HMM Model versus the original tags is {:.1f}%.'.format(100*good/len(output)))

    print("\nComparsion with NLTK's trained tagger*****")
    nltk_output = nltk.pos_tag(new_test)
    nltk_good = 0
    for x in range(len(output)):
        if nltk_output[x] == test_data[x]:
            nltk_good +=1
    print('The accuracy of the NLTK Model versus the original tags is {:.1f}%.'.format(100 * nltk_good /len(nltk_output)))
main()

# answer to 3.4
# MaxEnt classifier is based off of Logistic Regression according to
# https://stackoverflow.com/questions/12389093/nltk-maximum-entropy-classifier-raw-score (The answer from the SKLearn contributer)
#
# The native POS_TAG function in NLTK is based off of a perceptron according to this
# https://stackoverflow.com/questions/32016545/how-does-nltk-pos-tag-work (accepted answer)
#
# According to https://stats.stackexchange.com/questions/162257/whats-the-difference-between-logistic-regression-and-perceptron
# "
# In some cases, the term perceptron is also used to refer to neural networks which use a logistic function as a transfer function (however, this is not in accordance with the original terminology). In that case, a logistic regression and a "perceptron" are exactly the same. Of course, with a perceptron it is possible to use multiple neurons all using a logistic transfer function, which becomes somewhat relatable to stacking of logistic regression (not the same, but similar)."
#
# A perceptron and logistic regression are extremely similar (if not the same) depending on the definition for what you mean by perceptron.
#
# This would explain the nearly identical results when comparing the POS_TAG function and the MaxEnt classifier
#
