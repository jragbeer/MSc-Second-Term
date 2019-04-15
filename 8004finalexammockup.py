import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn import tree
np.random.seed(13)

def q2():
    thing = """
    The roars were loud and earth-shattering -- and not just on the course. There was Tida Woods, inside the Augusta National clubhouse, screaming at the television, nervous energy and anticipation consuming the room while her son was attempting to finish the most improbable of major championship victories.

    There were her grandchildren -- Tiger Woods' daughter, Sam, and son, Charlie -- waiting behind the 18th green, their first trip to one of the game's most historic sites about to be rewarded with a Masters triumph that few dreamed possible.

    Woods had a shot to spare on the final hole, tapping in for a bogey that wrapped a final-round 70 and a one-stroke victory over Brooks Koepka, Dustin Johnson and Xander Schauffele and produced a 15th major title -- 11 years after the previous one -- and a fifth green jacket.

    ADVERTISEMENT

    "Just unreal, to be honest with you,'' Woods said. "Just the whole tournament has meant so much to me over the years. Coming here in '95 for the first time, and being able to play as an amateur. Winning in '97 and then come full circle 22 years later, to be able to do it again. And just the way it all transpired today.

    "There were so many different scenarios that could have transpired on that back nine. There were so many guys who had a chance to win. Leaderboard was absolutely packed and everyone was playing well. You couldn't have had more drama than we all had out there, and now I know why I'm balding. This stuff is hard.
    "I think this is one of the best sports stories we've ever seen,'' said Trevor Immelman, who won the 2008 Masters -- when Woods finished second, the closest he had been to victory here since his previous win, in 2005.

    "When I was coming through the ranks and he was at the height of his game, you always got the feeling that he knew he was the best, you knew he was the best and that's just the way it is.

    "But a couple of years ago, after surgeries and everything else that happened, it was the first time I had ever seen him uncertain. It's a word that I would have never used for Tiger Woods is uncertain. To dig himself back from that moment to here is something that is just so special. Special for our game. This is awesome. For my mind, this goes down in the same vein as Jack in '86.''

    The stressful, emotional, exhausting day was made even more so for Woods with an early wake-up call due to impending storms that pushed up tee times more than five hours Sunday. With all of his back problems, Woods goes through a lengthy process to get ready to play any competitive round of golf.

    But it paled in comparison to the treacherous comeback Woods endured in recent years as he tried to recover from multiple surgeries.

    The most recent of those was almost exactly two years ago, just two weeks after Woods attended the annual Champions Dinner at Augusta National, needing a pain-killing shot just to make the trip.

    So frustrated with his situation was Woods that he confided in a few past champions that he thought his career was over, that he'd never play competitive golf again.

    "I had serious doubts after what transpired a couple years ago,'' he said. "I could barely walk. I couldn't sit. Couldn't lay down. I really couldn't do much of anything. Luckily, I had the procedure on my back, which gave me a chance of having a normal life. But then all of a sudden, I realized I could actually swing a golf club again.

    "To have the opportunity to come back like this, it is probably one of the biggest wins I've had for sure because of it.''
    """
    orig = [x.lower() for x in thing.split()]
    c = [list(x.lower()) for x in thing.split()]
    all_letters = list(set([w for i in c for w in i]))
    print(all_letters)

    pi = np.zeros(len(all_letters), dtype = np.float64)
    for i in range(len(c)):
        pi[all_letters.index(c[i][0])] +=1
    pi = pi/sum(pi)
    print(pi)

    A = np.zeros((len(all_letters), len(all_letters)))
    for i in orig:
        tt = list(i)
        qq = [(a,b) for a,b in zip(tt, tt[1:])]
        for y in qq:
            row = all_letters.index(y[0])
            col = all_letters.index(y[1])
            A[row, col] +=1

    print(A)
    rowSum = np.sum(A,1)
    B = (A.T/rowSum).T
    A = B
    print(A)

    def myfunc(k, PI, AA, data):
        i = np.random.choice(len(data), p=PI)
        first = data[i]
        for x in range(k-1):
            z = np.random.choice(len(data), p = AA[i,])
            print(z, AA[i,])
            first = first+str(data[z])


        print(first)

    myfunc(5, pi, A, all_letters)

def q4():
    N = 1500
    F = 15
    X, y = make_classification(N, n_features=F, flip_y=0.50)
    print(X.max())
    i = np.random.randint(N, size = 500)
    ii = np.random.randint(N, size = 500)
    iii = np.random.randint(N, size = 500)

    X1 = X[i, ]
    Y1 = y[i, ]
    X2 = X[ii,]
    Y2 = y[ii,]
    X3 = X[iii,]
    Y3 = y[iii,]

    clf = tree.DecisionTreeClassifier(min_samples_leaf=5)
    clf = clf.fit(X1, Y1)
    p = 0
    new = clf.predict(X1)
    retrain = []
    retrainy = []
    for t in range(len(X1)):
        if Y1[t] == new[t]:
            # print(Y1[t], new[t])
            p +=1
        else:
            retrain.append(X1[t,])
            retrainy.append(Y1[t,])
    print(p)
    print(p/len(new), (1-p/len(new)))
    print(len(retrain))
    print()
    print()
    new_X2 = np.concatenate((X2, retrain),0)
    new_Y2 = np.concatenate((Y2, retrainy),0)
    print(new_X2.shape)
    clf2 = tree.DecisionTreeClassifier(min_samples_leaf=5)
    clf2 = clf2.fit(new_X2, new_Y2)
    p2 = 0
    new2 = clf2.predict(new_X2)
    retrain2 = []
    retrainy2 = []
    for t in range(len(new_X2)):
        if new_Y2[t] == new2[t]:
            # print(new_Y2[t], new[t])
            p2 +=1
        else:
            retrain2.append(new_X2[t,])
            retrainy2.append(new_Y2[t,])
    print(p2)
    print(p2/len(new2), (1-p2/len(new2)))

    test_2 = clf.predict(X2)
    test_3 = clf.predict(X3)
    haha = 0
    for x in range(len(test_2)):
        if test_2[x] == test_3[x]:
            if test_2[x] == Y3[x]:
                haha +=1
        # print(test_3[x], test_2[x], Y3[x])
    print(haha/len(test_2))


    # print(i)

def q3():
    train_set_input = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    train_set_label = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361])

    # your code here to calculate w_ML
    try:
        wML = np.linalg.inv(np.dot(np.transpose(train_set_input), train_set_input))*np.dot(train_set_input.T, train_set_label)
    except:
        wML = np.dot(np.transpose(train_set_input), train_set_input) * np.dot(train_set_input.T, train_set_label)
    test_set_inpute = [20, 21, 22, 23, 24]
    test_set_label = [400, 441, 484, 529, 576]

    # your code here to calcluate test set error

    new = np.dot(wML.T, test_set_inpute)
    for i in range(len(new)):
        print(new[i], test_set_label[i])

    from sklearn.metrics import mean_squared_error
    print(mean_squared_error(test_set_label, new))
