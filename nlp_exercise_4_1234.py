def four_point_three():
    from sklearn.datasets import load_files
    import nltk
    import pandas as pd
    import numpy as np
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
    print([x for x in textTrain[0].decode('utf-8').split()])
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
        return ''.join(z)

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
    df = pd.DataFrame(xTrain.toarray(order = 'F'))

    def main(i, textTrain_):
        def stuff(news):
            path = "C:/Users/Julien/PycharmProjects/nlp/"
            with open(path + 'opinion-lexicon-English_positive-words.txt', 'r') as p:
                with open(path + "opinion-lexicon-English_negative-words.txt", 'r') as n:
                    pos = p.read().split()
                    neg = n.read().split()

                    posnum = len([x for x in pos if x in news])
                    negnum = len([x for x in neg if x in news])

                    return posnum, negnum
        b = [x for x in textTrain_[i].decode('utf-8').split()]
        positive, negative = stuff(b)
        return positive, negative
    poss = []
    negg = []
    for i in df.itertuples():
        pos_num, neg_num = main(i[0], textTrain)
        poss.append(pos_num)
        negg.append(neg_num)

    df=df.assign(e=pd.Series(poss).values)
    df=df.assign(f=pd.Series(negg).values)


    print (xTrain)

    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB(alpha=1.0)#alpha 1 for laplace smoothing(recall we add 1)
    clf.fit(df.as_matrix(), yTrain)

    print("Wait for me to finish...")
    xTest = vect.transform(textTest)
    df2 = pd.DataFrame(xTest.toarray(order = 'F'))

    poss2 = []
    negg2 = []
    for i in df2.itertuples():
        pos_num2, neg_num2 = main(i[0], textTrain)
        poss2.append(pos_num2)
        negg2.append(neg_num2)

    df2=df2.assign(e=pd.Series(poss2).values)
    df2=df2.assign(f=pd.Series(negg2).values)


    newdf = df2.values

    #clf.predict(X[2:3])

    for i in range(0,10):
        print('*'*14)
        # print(xTest[i])
        print("Prediction: ", clf.predict(newdf[i].reshape(1,-1)),
        ", Actual Label: ", yTest[i])


    print(clf.score(newdf,yTest))

    from sklearn.metrics import precision_recall_fscore_support

    yPred = clf.predict(newdf)

    precision, recall, fMeasure, support = \
        precision_recall_fscore_support(yTest, yPred, average='macro')

    print("Precision: ", precision)
    print("Recall: ", recall)
    print("F-measure: ", fMeasure)
    four_point_three()