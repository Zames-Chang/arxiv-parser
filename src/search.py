import urllib.request as request
import re

def search(author):
    url = f"https://arxiv.org/search/?query={author}&searchtype=author"
    content = request.urlopen(url)
    res = content.read().decode('utf-8')
    return res
def nextPage(url):
    content = request.urlopen(url)
    res = content.read().decode('utf-8')
    return res
def numberOfpapers(author):
    dic = {}
    res = search(author)
    pattern = "has-text-black-bis has-text-weight-semibold\">originally announced</span>[\s\S]*?</p>"
    result = re.findall(pattern, res)
    year = '[0-9][0-9][0-9][0-9]'
    for r in result:
        date = re.search(year,r).group()
        if(date in dic):
            dic[date] += 1
        else:
            dic[date] = 1
    return dic
        