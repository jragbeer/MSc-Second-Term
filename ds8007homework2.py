import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

style.use('ggplot')
def question1():
    headers = ['Class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols',
               'Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']

    df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header = None, names = headers, )

    sns.pairplot(df[headers[1:]])
    print('Question A')
    print("1) We can see that the 'Total phenols' variable and the 'Flavanoids' variable are highly correlated, as can be seen by their scatterplot (the points form a line from bottom left to top right).")
    print()
    print("2) It can be seen by the scatterplots that 'Color intensity' variable and the 'Flavanoids' variable have a non-linear relationship as the points form a sort of curve.")
    print()
    plt.figure()
    plt.scatter(df[df['Class']==1].Hue, df[df['Class']==1]['Color intensity'], label = 'Class 1')
    plt.scatter(df[df['Class']==2].Hue, df[df['Class']==2]['Color intensity'], label = 'Class 2')
    plt.scatter(df[df['Class']==3].Hue, df[df['Class']==3]['Color intensity'], label = 'Class 3')
    plt.xlabel('Hue')
    plt.ylabel('Color Intensity')
    plt.legend()
    print('3) From the scatterplot, it appears only Class 2 has datapoints with high hue and low color intensity. These points would lie in the bottom right of the chart.')
def question2():
    list_of_names = ['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base',
                     'length','width','height','curb-weight','engine-type','num-of-cylinders','engine-size','fuel-system','bore','stroke','compression-ratio',
                     'horsepower','peak-rpm','city-mpg','highway-mpg','price']
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data', header = None, names = list_of_names, na_values = '?')
    df.fillna(df.mean())
    plt.figure()
    for x in df['body-style'].unique():
        plt.scatter(df[df['body-style']==x]['make'],df[df['body-style']==x]['city-mpg'], label = x, alpha = 0.79)
    plt.xticks(rotation = 45)
    plt.xlabel('Make')
    plt.title('Make vs. City MPG vs. Body-Style')
    plt.ylabel('City MPG')
    plt.legend()
    print('Question B')
    print("1) There aren't certain combinations of make/body-style that have high city-mpg, but it be seen by the coloured scatterplot that sedans and hatchbacks consistently have the highest of all the cars, regardless of make.")
    print("Chevrolet, Honda and Nissan make the vehicles with the highest city-mpg.")
    plt.figure()
    plt.title('Price vs. Highway MPG vs.Fuel-Type')
    for x in df['fuel-type'].unique():
        plt.scatter(df[df['fuel-type']==x]['highway-mpg'],df[df['fuel-type']==x]['price'], label = x, alpha = 0.59)
    plt.xticks(rotation = 45)
    plt.xlabel('Highway MPG')
    plt.ylabel('Price')
    plt.legend()
    plt.figure()
    plt.title('Price vs. Highway MPG vs. Num-Of-Cylinders for vehicles with Diesel engine')
    plt.scatter(df[(df['fuel-type']=='diesel') & (df['num-of-cylinders']=="four")]['highway-mpg'], df[(df['fuel-type']=='diesel') & (df['num-of-cylinders']=="four")]['price'], label='Four', alpha=0.59, s= 30)
    plt.scatter(df[(df['fuel-type'] == 'diesel') & (df['num-of-cylinders'] == "five")]['highway-mpg'],
                df[(df['fuel-type'] == 'diesel') & (df['num-of-cylinders'] == "five")]['price'], label='Five',
                alpha=0.59, s = 60)
    plt.scatter(df[(df['fuel-type'] == 'diesel') & (df['num-of-cylinders'] == "six")]['highway-mpg'],
                df[(df['fuel-type'] == 'diesel') & (df['num-of-cylinders'] == "six")]['price'], label='Six',
                alpha=0.59, s = 90)
    plt.xlabel('Highway MPG')
    plt.ylabel('Price')
    plt.legend()
    print()
    print('2)Neither fuel-type really has cars with both high highway-mpg and high price. It can be seen by the scatter plot that Diesel cars would more satisfy that criteria however. All of the vehicles that meet that criteria are FOUR cylinder vehicles.')

question1()
question2()

plt.show()