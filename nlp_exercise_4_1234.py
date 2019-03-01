from sklearn.datasets import load_files
import nltk
# Read training files
path = 'C:/Users/Julien/PycharmProjects/nlp/'
reviewsTrain = load_files(path + "abc/train/")
# Lets get training reviews and training labels in sepearate lists
textTrain, yTrain = reviewsTrain.data, reviewsTrain.target

# Let's understand the two lists: reviews (text_train) and their labels (y_train)
print("Type of text train: ",type(textTrain))
print("Length of texttrain: ",len(textTrain))
print("Text at index 6:\n ", textTrain[6])
print("Label of the review at Index 6: ",yTrain[6])
# 0 for negative and 1 for positive

# Here we are searching  br tags and replacing them by a
# space in each review
textTrain = [review.replace(b"<br />", b" ") for review in textTrain]
print ("Clean data:\n", textTrain[25])

def no(a):
    z = nltk.word_tokenize(a.decode('utf-8'))
    nots = ["n't","not","no","never"]
    negatives = [x for x in range(len(z)) if z[x] in nots]
    punc = [',', '.', '!', '?', ':', ';']
    for q in negatives:
        for i in range(1,100):
            try:
                if z[q+i] not in punc:
                    z[q+i] = 'NOT_'+str(z[q+i])
                else:
                    break
            except:
                pass
    return z
print(no(textTrain[25]))
# textTrain = [no(x) for x in textTrain]

reviewsTest = load_files(path + "abc/test/")
textTest, yTest = reviewsTest.data, reviewsTest.target
print("Number of documents in test data: ", len(textTest))

textTest = [review.replace(b"<br />", b" ") for review in textTest]
print ("Review at 1st index \n", textTest[0])
print ("Class at 1st index (0 for neg, 1 for pos):", yTest[0])

import nltk
import string
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer

#Custom function for toeknization
def myTokenizer(textData):
    stemmer = PorterStemmer()
    stemmedWords=[stemmer.stem(w) for w in nltk.word_tokenize(textData)]
     # uncomment following, if you wanna see stems but beware, it will print for 2000 reviews
    #print ("First 2 stemmed words: ", stemmedWords[:2])
    return  stemmedWords

#we are going to filter out only punctation symbols as stop words
# Stop words list
punctuationList=list(string.punctuation)
print ("Punctuations: " ,punctuationList)
# Initialize Count Vectorizer object
print ("Please wait.....")
vect=CountVectorizer(tokenizer=myTokenizer, stop_words=punctuationList)
vect.fit(textTrain)
print ("Total vocabulary: ",len(vect.vocabulary_))

# If you wanna see words and their frequencies, uncomment the following code
print ((vect.vocabulary_))

print ("Wait for me to finish......")
xTrain = vect.transform(textTrain)
print (repr(xTrain))

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB(alpha=1.0)#alpha 1 for laplace smoothing(recall we add 1)
clf.fit(xTrain, yTrain)

print("Wait for me to finish...")
xTest = vect.transform(textTest)

print(repr(xTest))
#clf.predict(X[2:3])

for i in range(0,10):
    print("Prediction: ", clf.predict(xTest[i]),
          ", Actual Label: ", yTest[i])


print(clf.score(xTest,yTest))