from src.search import *
from src.plot import *

def main():
    author = input('Input Author:')
    print('processing numberOfpapers ...')
    dicOfpapers = numberOfpapers(author)
    barPlot(author,dicOfpapers)
    print('done')
    print('processing numberOfcoauthor ...')
    dicOfcoauthors = numberOfcoauthor(author)
    printNumberOfcoauthor(dicOfcoauthors)
    print('done')

if __name__ == "__main__":
    main()