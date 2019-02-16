import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc

# HW Assignment 3 - DS 8007 

def image1():
    under45 = [79, 16]
    over45 = [69, 22]
    over65 = [44, 39]
    men = [65, 25]
    women = [72, 20]
    b = 0

    plt.bar(0, under45[0], width=0.2, color='k', align='center')
    plt.bar(0.4, under45[1], width=0.2, color='k', align='center', alpha=0.5)

    plt.bar(1, over45[0], width=0.2, color='k', align='center')
    plt.bar(1.4, over45[1], width=0.2, color='k', align='center', alpha=0.5)

    plt.bar(2, over65[0], width=0.2, color='k', align='center')
    plt.bar(2.4, over65[1], width=0.2, color='k', align='center', alpha=0.5)

    plt.bar(3, men[0], width=0.2, color='b', align='center')
    plt.bar(3.4, men[1], width=0.2, color='b', align='center', alpha=0.5)

    plt.bar(4, women[0], width=0.2, color='g', align='center')
    plt.bar(4.4, women[1], width=0.2, color='g', align='center', alpha=0.5)

    plt.xticks([x + 0.2 for x in range(5)], ['Under 45', '45-65', 'Over 65', 'Men', "Women"])
    plt.ylabel(
        'Percentage of respondents who say that it\'s likely there will be a female president in their lifetime (%)')
    plt.title('DARKER = "YES", LIGHER = "NO"')
    plt.ylim([0, 105])
    plt.suptitle('MRS. PRESIDENT')
    ax = plt.gca()
    ax.grid(which='major', axis='y', linestyle='--', alpha=0.3)
    plt.show()
image1()

def image4():
    paid = {'Professional':42, 'Clerical':25, 'Other': 33}
    unpaid = {'Professional':30, 'Clerical':31, 'Other': 39}

    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar([0], paid['Professional'], width, color = 'darkgreen', alpha = 0.75)
    p2 = plt.bar([0], paid['Clerical'], width, bottom=paid['Professional'], color = 'darkgreen', alpha = 0.3)
    p3 = plt.bar([0], paid['Other'], width, bottom=paid['Professional']+paid['Clerical'], color = 'silver', alpha = 0.4)
    p4 = plt.bar([1], unpaid['Professional'], width, color = 'darkviolet', alpha = 0.75)
    p5 = plt.bar([1], unpaid['Clerical'], width, bottom=unpaid['Professional'], color = 'darkviolet', alpha = 0.3)
    p6 = plt.bar([1], unpaid['Other'], width, bottom=unpaid['Professional']+unpaid['Clerical'], color = 'silver', alpha = 0.4)

    x = plt.annotate(s = str(paid['Professional'])+ '%', xy=(0, paid['Professional']/2), fontsize = 'x-large')
    xx = plt.annotate(s = str(paid['Clerical'])+ '%', xy=(0, paid['Professional'] + (paid['Clerical']/2)), fontsize = 'x-large')
    xxx = plt.annotate(s = str(paid['Other'])+ '%', xy=(0, paid['Professional'] + paid['Clerical'] + (paid['Other']/2)), fontsize = 'x-large')

    y = plt.annotate(s = str(unpaid['Professional'])+ '%', xy=(1, unpaid['Professional']/2), fontsize = 'x-large')
    yy = plt.annotate(s = str(unpaid['Clerical'])+ '%', xy=(1, unpaid['Professional'] + (unpaid['Clerical']/2)), fontsize = 'x-large')
    yyy = plt.annotate(s = str(unpaid['Other'])+ '%', xy=(1, unpaid['Professional'] + unpaid['Clerical'] + (unpaid['Other']/2)), fontsize = 'x-large')



    plt.ylabel('Percentage of time spent on task'.upper())
    plt.title('Darker: Professional Tasks | Lighter: Clerical and Non-Essential Tasks | Silver: Other'.upper())
    plt.xticks([0,1],['Paid'.upper(), 'Unpaid'.upper()])
    plt.show()
image4()

def image3():
    jobs = {
        'Lead Software Engineer Contractor': [221, 239],
        'Product Management Director': [203, 218],
        'Directors': [172, 231],
        'Engineering Director': [184, 198],
        'Human Resources Director': [183, 199],
        'Senior Partner Technology Manager': [180, 195],
        'Staff User Experience Designer': [167, 197],
        'Marketing Director': [165, 179],
        'Group Product Manager': [157, 172],
        'Senior Managers': [143, 192]}
    b = 0
    ax = plt.gca()
    ax.grid(which='both', axis='y', linestyle='--', alpha=0.3)
    for x in jobs.keys():
        plt.bar(b, jobs[x][1] - jobs[x][0], bottom=jobs[x][0], width=0.4)
        b += 1
    plt.ylabel('Salary ($ 1000\'s)')
    plt.title('TOP 10 SALARIES AT GOOGLE')
    plt.xticks([x for x in range(len(list(jobs.keys())))], [x for x in list(jobs.keys())], rotation=10)
    plt.ylim([130, 250])
    plt.show()
image3()

