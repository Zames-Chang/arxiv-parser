import matplotlib.pyplot as plt
import numpy as np

def barPlot(author,dic):
    x = dic.keys()
    y = []
    y_pos = np.arange(len(x))
    for key in dic.keys():
        y.append(dic[key])
    plt.bar(y_pos, y, align='center', alpha=0.5)
    plt.xticks(y_pos, x)
    plt.ylabel('number of papers')
    plt.title(author)
    plt.savefig('numberOfpapers.png')